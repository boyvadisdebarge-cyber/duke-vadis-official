import json
import os
import subprocess
import sys
from pathlib import Path

from django.core.files.storage import FileSystemStorage
from django.test import SimpleTestCase, TestCase, override_settings

from core.checks import cloudinary_config
from core.storage import video_storage

BASE = Path(__file__).resolve().parent.parent
CLD_VARS = ["CLOUDINARY_URL", "CLOUDINARY_CLOUD_NAME", "CLOUDINARY_API_KEY", "CLOUDINARY_API_SECRET"]


def settings_with(env):
    """Import config.settings in a clean subprocess with the given Cloudinary env (fake values only)."""
    clean = {k: v for k, v in os.environ.items() if k not in CLD_VARS}
    clean.update(env)
    code = ("import json,django.conf as c,os;os.environ['DJANGO_SETTINGS_MODULE']='config.settings';"
            "from django.conf import settings as s;"
            "print(json.dumps({'use':s.USE_CLOUDINARY,'partial':s.CLOUDINARY_PARTIAL,"
            "'backend':s.STORAGES['default']['BACKEND'],'apps':[a for a in s.INSTALLED_APPS if 'cloudinary' in a]}))")
    out = subprocess.run([sys.executable, "-c", code], cwd=BASE, env=clean, capture_output=True, text=True, check=True)
    return json.loads(out.stdout.strip().splitlines()[-1])


class CloudinarySettingsTests(SimpleTestCase):
    def test_absent_credentials_fall_back_to_local_disk(self):
        r = settings_with({})
        self.assertFalse(r["use"]); self.assertFalse(r["partial"])
        self.assertEqual(r["backend"], "django.core.files.storage.FileSystemStorage")
        self.assertEqual(r["apps"], [])

    def test_cloudinary_url_enables_cloudinary(self):
        r = settings_with({"CLOUDINARY_URL": "cloudinary://key:secret@demo"})
        self.assertTrue(r["use"])
        self.assertEqual(r["backend"], "cloudinary_storage.storage.MediaCloudinaryStorage")

    def test_three_part_variables_enable_cloudinary(self):
        r = settings_with({"CLOUDINARY_CLOUD_NAME": "demo", "CLOUDINARY_API_KEY": "k", "CLOUDINARY_API_SECRET": "s"})
        self.assertTrue(r["use"]); self.assertFalse(r["partial"])

    def test_partial_configuration_is_flagged_not_crashing(self):
        r = settings_with({"CLOUDINARY_CLOUD_NAME": "demo"})
        self.assertFalse(r["use"]); self.assertTrue(r["partial"])
        r = settings_with({"CLOUDINARY_URL": "not-a-cloudinary-url"})
        self.assertFalse(r["use"]); self.assertTrue(r["partial"])


class CloudinaryStorageAndChecksTests(SimpleTestCase):
    @override_settings(USE_CLOUDINARY=False)
    def test_video_storage_without_credentials_is_local(self):
        self.assertIsInstance(video_storage(), FileSystemStorage)

    def test_video_storage_with_credentials_uses_video_resource_type(self):
        env = {k: v for k, v in os.environ.items() if k not in CLD_VARS}
        env.update({"CLOUDINARY_URL": "cloudinary://key:secret@demo", "DJANGO_SETTINGS_MODULE": "config.settings"})
        code = ("import django;django.setup();from core.storage import video_storage;"
                "print(type(video_storage()).__name__)")
        out = subprocess.run([sys.executable, "-c", code], cwd=BASE, env=env, capture_output=True, text=True, check=True)
        self.assertEqual(out.stdout.strip(), "VideoMediaCloudinaryStorage")

    @override_settings(USE_CLOUDINARY=False, CLOUDINARY_PARTIAL=True)
    def test_check_errors_on_partial_config(self):
        self.assertEqual([m.id for m in cloudinary_config(None)], ["core.E001"])

    @override_settings(USE_CLOUDINARY=False, CLOUDINARY_PARTIAL=False, DEBUG=False)
    def test_check_warns_without_credentials_in_production_mode(self):
        self.assertEqual([m.id for m in cloudinary_config(None)], ["core.W001"])

    @override_settings(USE_CLOUDINARY=True, CLOUDINARY_PARTIAL=False)
    def test_check_silent_when_configured(self):
        self.assertEqual(cloudinary_config(None), [])


@override_settings(STORAGES={"default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
                             "staticfiles": {"BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"}})
class HomeRendersTests(TestCase):
    def test_home_renders_with_youtube_embed_without_cloudinary(self):
        r = self.client.get("/")
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, "youtube-nocookie.com/embed/h5NE0YTWqMw")
