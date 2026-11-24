from django.contrib import admin
from .models import BookingEnquiry, MediaItem, SiteSettings, Song
@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("artist_name", "contact_email", "contact_phone")
    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ("title", "is_featured", "release_date")
    list_filter = ("is_featured",)
    search_fields = ("title", "description")
@admin.register(MediaItem)
class MediaItemAdmin(admin.ModelAdmin):
    list_display = ("title", "kind", "created_at")
    list_filter = ("kind",)
    search_fields = ("title", "caption")
@admin.register(BookingEnquiry)
class BookingEnquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "event_date", "created_at")
    search_fields = ("name", "email", "organisation")
    readonly_fields = ("created_at",)
