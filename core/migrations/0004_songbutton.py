from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("core", "0003_promobanner")]

    operations = [
        migrations.CreateModel(
            name="SongButton",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("slot_number", models.PositiveSmallIntegerField(help_text="Number shown on the music button (1–10).", unique=True)),
                ("title", models.CharField(blank=True, help_text="Optional song title. Leave blank to show Song 01, Song 02, etc.", max_length=160)),
                ("listen_url", models.URLField(blank=True, help_text="Paste the song's public audio or streaming link when ready.", max_length=500)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={"ordering": ["slot_number"]},
        ),
        migrations.RunPython(
            lambda apps, schema_editor: [
                apps.get_model("core", "SongButton").objects.get_or_create(slot_number=n)
                for n in range(1, 11)
            ],
            migrations.RunPython.noop,
        ),
    ]
