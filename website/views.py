from django.shortcuts import render
from .models import HomePageContent

def home(request):
    content = HomePageContent.objects.first()
    if content is None:
        content = HomePageContent.objects.create()
    return render(request, "website/home.html", {"content": content})
