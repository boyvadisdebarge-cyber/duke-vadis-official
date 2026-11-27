from django.contrib import admin
from .models import HomePageContent

@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Header", {"fields": ("site_name", "tagline", "main_heading")}),
        ("Welcome section", {"fields": ("welcome_heading", "welcome_text")}),
        ("Music section", {"fields": ("song_heading", "song_text", "release_text")}),
        ("Links and footer", {"fields": ("youtube_url", "footer_text")}),
    )
    readonly_fields = ("updated_at",)
