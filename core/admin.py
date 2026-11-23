from django.contrib import admin
from .models import MusicRelease
@admin.register(MusicRelease)
class MusicReleaseAdmin(admin.ModelAdmin):
 list_display=("title","release_date","is_featured","is_published")
 list_filter=("is_featured","is_published")
 search_fields=("title","description")
