from django.contrib import admin
from .models import HomePageContent, Service, Souvenir, Booking, ContactMessage

@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    list_display=("site_name","updated_at")

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display=("name","active","sort_order")
    list_editable=("active","sort_order")
    search_fields=("name","description")

@admin.register(Souvenir)
class SouvenirAdmin(admin.ModelAdmin):
    list_display=("name","price","active")
    list_editable=("active",)
    search_fields=("name","description")

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display=("name","email","event_date","event_type","status","created_at")
    list_filter=("status","event_date")
    search_fields=("name","email","phone")
    list_editable=("status",)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display=("name","email","handled","created_at")
    list_filter=("handled","created_at")
    list_editable=("handled",)
    search_fields=("name","email","message")
