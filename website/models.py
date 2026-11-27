from django.db import models

class HomePageContent(models.Model):
    site_name = models.CharField(max_length=120, default="DUKE VADIS")
    tagline = models.CharField(max_length=200, default="Gospel Music Artist")
    main_heading = models.CharField(max_length=200, default="CREATED TO PRAISE YOU")
    welcome_heading = models.CharField(max_length=200, default="Welcome")
    welcome_text = models.TextField(default="Welcome to the official website of Duke Vadis.\nMusic filled with faith, hope, gratitude and heartfelt praise.")
    song_heading = models.CharField(max_length=200, default="Created to Praise You")
    song_text = models.TextField(default="A new gospel song celebrating our love for God and the power of praise.")
    release_text = models.CharField(max_length=200, default="Release date coming soon!")
    youtube_url = models.URLField(default="https://www.youtube.com/results?search_query=Duke+Vadis+Movies")
    footer_text = models.CharField(max_length=200, default="© 2026 Duke Vadis. All rights reserved.")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Homepage content"
        verbose_name_plural = "Homepage content"

    def __str__(self):
        return "Duke Vadis homepage"
