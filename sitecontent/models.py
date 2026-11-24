from django.db import models
class SiteSettings(models.Model):
    artist_name = models.CharField(max_length=120, default="Duke Vadis")
    tagline = models.CharField(max_length=180, default="Gospel Music Artist")
    about_text = models.TextField(blank=True)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=40, blank=True)
    youtube_channel = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    tiktok_url = models.URLField(blank=True)
    featured_song_title = models.CharField(max_length=180, default="Created to Praise You")
    announcement = models.CharField(max_length=240, default="A new gospel song coming soon")
    class Meta:
        verbose_name = "Site settings"
        verbose_name_plural = "Site settings"
    def __str__(self):
        return self.artist_name
class Song(models.Model):
    title = models.CharField(max_length=180)
    description = models.TextField(blank=True)
    youtube_url = models.URLField(blank=True)
    artwork = models.ImageField(upload_to="songs/", blank=True)
    release_date = models.DateField(null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-is_featured", "-created_at"]
    def __str__(self):
        return self.title
class MediaItem(models.Model):
    class Kind(models.TextChoices):
        PHOTO = "photo", "Photo"
        VIDEO = "video", "Video"
    title = models.CharField(max_length=180)
    kind = models.CharField(max_length=10, choices=Kind.choices, default=Kind.PHOTO)
    image = models.ImageField(upload_to="gallery/", blank=True)
    video_url = models.URLField(blank=True)
    caption = models.CharField(max_length=240, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-created_at"]
    def __str__(self):
        return self.title
class BookingEnquiry(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    organisation = models.CharField(max_length=160, blank=True)
    event_date = models.DateField(null=True, blank=True)
    event_location = models.CharField(max_length=180, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-created_at"]
    def __str__(self):
        return f"{self.name} – {self.created_at:%Y-%m-%d}"
