from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [("core", "0001_initial")]
    operations = [
        migrations.CreateModel(
            name="SiteProfile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("about_heading", models.CharField(default="A life shaped by faith and music", max_length=180)),
                ("about_text", models.TextField(default="Duke Vadis shares a message of faith, hope and praise through gospel music, creative experiences and meaningful connections.")),
                ("contact_email", models.EmailField(blank=True, max_length=254)),
                ("contact_phone", models.CharField(blank=True, max_length=40)),
                ("location", models.CharField(blank=True, max_length=180)),
            ],
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=140)),
                ("description", models.TextField()),
                ("is_published", models.BooleanField(default=True)),
                ("display_order", models.PositiveIntegerField(default=0)),
            ],
            options={"ordering": ["display_order", "title"]},
        ),
        migrations.CreateModel(
            name="Souvenir",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=140)),
                ("description", models.TextField(blank=True)),
                ("image", models.ImageField(blank=True, upload_to="souvenirs/")),
                ("price_label", models.CharField(blank=True, help_text="Optional display text; no online checkout is enabled.", max_length=60)),
                ("is_available", models.BooleanField(default=True)),
                ("display_order", models.PositiveIntegerField(default=0)),
            ],
            options={"ordering": ["display_order", "name"]},
        ),
        migrations.CreateModel(
            name="BookingRequest",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=140)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(blank=True, max_length=40)),
                ("event_type", models.CharField(max_length=120)),
                ("event_date", models.DateField(blank=True, null=True)),
                ("message", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("status", models.CharField(choices=[("new","New"),("contacted","Contacted"),("confirmed","Confirmed"),("closed","Closed")], default="new", max_length=20)),
            ],
            options={"ordering": ["-created_at"]},
        ),
        migrations.CreateModel(
            name="ContactMessage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=140)),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField(blank=True, max_length=180)),
                ("message", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("is_read", models.BooleanField(default=False)),
            ],
            options={"ordering": ["-created_at"]},
        ),
    ]
