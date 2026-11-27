# Generated for the song feature video content model.
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_songbutton"),
    ]

    operations = [
        migrations.CreateModel(
            name="SongFeatureVideo",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(default="Behind the Song", max_length=180)),
                ("description", models.TextField(blank=True, help_text="A short introduction to the song or video.")),
                ("video", models.FileField(blank=True, help_text="Upload an MP4 or other browser-supported video.", upload_to="song-feature-videos/")),
                ("poster_image", models.ImageField(blank=True, help_text="Optional cover image shown before the video plays.", upload_to="song-feature-posters/")),
                ("is_active", models.BooleanField(default=True)),
                ("display_order", models.PositiveIntegerField(default=0)),
            ],
            options={
                "verbose_name": "Song feature video",
                "verbose_name_plural": "Song feature videos",
                "ordering": ["display_order", "-id"],
            },
        ),
    ]
