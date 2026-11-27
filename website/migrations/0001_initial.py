from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(name="HomePageContent", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("site_name", models.CharField(default="DUKE VADIS", max_length=120)),
            ("hero_title", models.CharField(default="DUKE VADIS", max_length=200)),
            ("hero_subtitle", models.TextField(default="Welcome to the official home of Duke Vadis.")),
            ("about_text", models.TextField(default="Duke Vadis is driven by faith, creativity and the power of music to inspire.")),
            ("updated_at", models.DateTimeField(auto_now=True)),
        ]),
        migrations.CreateModel(name="Service", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("name", models.CharField(max_length=140)), ("description", models.TextField()),
            ("active", models.BooleanField(default=True)), ("sort_order", models.PositiveIntegerField(default=0)),
        ], options={"ordering": ["sort_order", "name"]}),
        migrations.CreateModel(name="Souvenir", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("name", models.CharField(max_length=140)), ("description", models.TextField(blank=True)),
            ("price", models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
            ("image_url", models.URLField(blank=True)), ("active", models.BooleanField(default=True)),
        ]),
        migrations.CreateModel(name="Booking", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("name", models.CharField(max_length=140)), ("email", models.EmailField(max_length=254)),
            ("phone", models.CharField(blank=True, max_length=40)),
            ("event_date", models.DateField(blank=True, null=True)),
            ("event_type", models.CharField(blank=True, max_length=140)), ("details", models.TextField()),
            ("status", models.CharField(choices=[("new","New"),("contacted","Contacted"),("confirmed","Confirmed"),("declined","Declined")], default="new", max_length=20)),
            ("created_at", models.DateTimeField(auto_now_add=True)),
        ]),
        migrations.CreateModel(name="ContactMessage", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("name", models.CharField(max_length=140)), ("email", models.EmailField(max_length=254)),
            ("message", models.TextField()), ("created_at", models.DateTimeField(auto_now_add=True)),
            ("handled", models.BooleanField(default=False)),
        ]),
    ]
