from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [("core", "0002_siteprofile_service_souvenir_bookingrequest_contactmessage")]
    operations = [
        migrations.CreateModel(
            name="PromoBanner",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(help_text="Main headline shown over the banner", max_length=180)),
                ("subtitle", models.CharField(blank=True, help_text="Short supporting line, e.g. NEW SINGLE • OUT NOW", max_length=240)),
                ("image", models.ImageField(upload_to="promo-banners/")),
                ("button_text", models.CharField(blank=True, default="Discover the music", max_length=60)),
                ("button_url", models.CharField(blank=True, default="#music", max_length=300)),
                ("is_active", models.BooleanField(default=True)),
                ("display_order", models.PositiveIntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["display_order", "-created_at"]},
        ),
    ]
