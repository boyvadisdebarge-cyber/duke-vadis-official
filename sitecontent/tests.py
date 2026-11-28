import shutil
import tempfile
from pathlib import Path

from django.test import TestCase, override_settings

from .views import HERO_SLIDES

PLAIN = {
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {"BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"},
}


class HeroCarouselTests(TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        (self.tmp / "images" / "hero").mkdir(parents=True)
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def get(self):
        with override_settings(STATICFILES_DIRS=[self.tmp], STORAGES=PLAIN):
            return self.client.get("/")

    def test_six_slides_planned(self):
        self.assertEqual(len(HERO_SLIDES), 6)
        self.assertTrue(all(alt for _, alt, _ in HERO_SLIDES))

    def test_no_images_keeps_hero_and_no_controls(self):
        r = self.get()
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, "Created to<br>")
        self.assertContains(r, "TO SERVE MY FATHER")
        self.assertNotContains(r, 'id="carousel-prev"')
        self.assertNotContains(r, "carousel-photo")

    def test_present_images_become_slides_with_controls(self):
        for path, _, _ in HERO_SLIDES:
            (self.tmp / path).write_bytes(b"x")
        r = self.get()
        self.assertContains(r, 'class="carousel-slide carousel-photo"', count=6)
        self.assertContains(r, 'aria-label="Previous slide"')
        self.assertContains(r, 'aria-label="Next slide"')
        self.assertContains(r, 'aria-label="Pause slideshow"')
        self.assertContains(r, "prefers-reduced-motion")
        self.assertContains(r, "Created to<br>")  # original hero retained as first slide
        self.assertContains(r, "worship-1-white-suit-choir.jpg")

    def test_partial_images_only_include_existing(self):
        (self.tmp / HERO_SLIDES[5][0]).write_bytes(b"x")
        r = self.get()
        self.assertContains(r, 'class="carousel-slide carousel-photo"', count=1)
        self.assertContains(r, "wildlife-6-african-sunset.jpg")
