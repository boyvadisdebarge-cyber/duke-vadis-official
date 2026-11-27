from django.db import models

class HomePageContent(models.Model):
    site_name = models.CharField(max_length=120, default="DUKE VADIS")
    hero_title = models.CharField(max_length=200, default="DUKE VADIS")
    hero_subtitle = models.TextField(default="Welcome to the official home of Duke Vadis.")
    about_text = models.TextField(default="Duke Vadis is driven by faith, creativity and the power of music to inspire.")
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self): return "Homepage content"

class Service(models.Model):
    name=models.CharField(max_length=140)
    description=models.TextField()
    active=models.BooleanField(default=True)
    sort_order=models.PositiveIntegerField(default=0)
    def __str__(self): return self.name
    class Meta: ordering=["sort_order","name"]

class Souvenir(models.Model):
    name=models.CharField(max_length=140)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=9,decimal_places=2,null=True,blank=True)
    image_url=models.URLField(blank=True)
    active=models.BooleanField(default=True)
    def __str__(self): return self.name

class Booking(models.Model):
    name=models.CharField(max_length=140)
    email=models.EmailField()
    phone=models.CharField(max_length=40,blank=True)
    event_date=models.DateField(null=True,blank=True)
    event_type=models.CharField(max_length=140,blank=True)
    details=models.TextField()
    status=models.CharField(max_length=20,choices=[("new","New"),("contacted","Contacted"),("confirmed","Confirmed"),("declined","Declined")],default="new")
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.name} — {self.created_at:%Y-%m-%d}"

class ContactMessage(models.Model):
    name=models.CharField(max_length=140)
    email=models.EmailField()
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    handled=models.BooleanField(default=False)
    def __str__(self): return f"Message from {self.name}"
