from django.shortcuts import render
from .models import MusicRelease
def home(request):
 return render(request,"home.html",{"releases":MusicRelease.objects.filter(is_published=True)})
