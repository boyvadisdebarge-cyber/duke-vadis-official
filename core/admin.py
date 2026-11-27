from django.contrib import admin
from .models import BookingRequest, ContactMessage, MusicRelease, PromoBanner, Service, SiteProfile, Souvenir

@admin.register(PromoBanner)
class PromoBannerAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "display_order", "created_at")
    list_filter = ("is_active",)
    list_editable = ("is_active", "display_order")
    search_fields = ("title", "subtitle")
    fields = ("title", "subtitle", "image", "button_text", "button_url", "is_active", "display_order")

@admin.register(MusicRelease)
class MusicReleaseAdmin(admin.ModelAdmin):
    list_display = ("title", "release_date", "is_featured", "is_published")
    list_filter = ("is_featured", "is_published")
    search_fields = ("title", "description")

@admin.register(SiteProfile)
class SiteProfileAdmin(admin.ModelAdmin):
    list_display = ("about_heading", "contact_email", "contact_phone")

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "display_order")
    list_editable = ("is_published", "display_order")
    search_fields = ("title", "description")

@admin.register(Souvenir)
class SouvenirAdmin(admin.ModelAdmin):
    list_display = ("name", "price_label", "is_available", "display_order")
    list_editable = ("is_available", "display_order")
    search_fields = ("name", "description")

@admin.register(BookingRequest)
class BookingRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "event_type", "event_date", "status", "created_at")
    list_filter = ("status", "event_type", "created_at")
    search_fields = ("name", "email", "phone")
    readonly_fields = ("created_at",)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "is_read", "created_at")
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "email", "subject", "message")
    readonly_fields = ("created_at",)
