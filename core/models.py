from django.db import models

class MusicRelease(models.Model):
    title = models.CharField(max_length=180)
    description = models.TextField(blank=True)
    release_date = models.DateField(null=True, blank=True)
    artwork = models.ImageField(upload_to="releases/", blank=True)
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-is_featured", "-release_date", "-created_at"]
    def __str__(self):
        return self.title

class SiteProfile(models.Model):
    about_heading = models.CharField(max_length=180, default="A life shaped by faith and music")
    about_text = models.TextField(default="Duke Vadis shares a message of faith, hope and praise through gospel music, creative experiences and meaningful connections.")
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=40, blank=True)
    location = models.CharField(max_length=180, blank=True)
    def __str__(self):
        return "Duke Vadis website profile"

class Service(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
    is_published = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)
    class Meta:
        ordering = ["display_order", "title"]
    def __str__(self):
        return self.title

class Souvenir(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="souvenirs/", blank=True)
    price_label = models.CharField(max_length=60, blank=True, help_text="Optional display text; no online checkout is enabled.")
    is_available = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)
    class Meta:
        ordering = ["display_order", "name"]
    def __str__(self):
        return self.name

class BookingRequest(models.Model):
    name = models.CharField(max_length=140)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    event_type = models.CharField(max_length=120)
    event_date = models.DateField(null=True, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="new", choices=[("new","New"),("contacted","Contacted"),("confirmed","Confirmed"),("closed","Closed")])
    class Meta:
        ordering = ["-created_at"]
    def __str__(self):
        return f"{self.name} — {self.event_type}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=140)
    email = models.EmailField()
    subject = models.CharField(max_length=180, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    class Meta:
        ordering = ["-created_at"]
    def __str__(self):
        return f"{self.name}: {self.subject or 'Website enquiry'}"
