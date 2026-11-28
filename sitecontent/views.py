from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.staticfiles import finders
from django.contrib.staticfiles.storage import staticfiles_storage
from .models import BookingEnquiry, MediaItem, SiteSettings, Song
HERO_SLIDES = [
    ("images/hero/worship-1-white-suit-choir.jpg", "Worship leader in a white suit singing in front of a choir under stage lights", "50% 30%"),
    ("images/hero/worship-2-wide-stage.jpg", "Wide view of the worship stage with the leader in white, the choir and stage lights", "50% 40%"),
    ("images/hero/worship-3-colorful-lights.jpg", "Choir and worship leader on stage lit by colorful stage lights", "50% 35%"),
    ("images/hero/worship-4-sanctuary-choir.jpg", "Worship leader with the choir inside a church sanctuary", "50% 30%"),
    ("images/hero/worship-5-sunset-waterfall.jpg", "Portrait of the worship leader before a waterfall landscape at sunset", "50% 40%"),
    ("images/hero/wildlife-6-african-sunset.jpg", "African wildlife silhouetted against a sunset", "50% 60%"),
]
def hero_slides():
    """Photo slides whose image file is present. Missing files are skipped so the page never errors."""
    slides = []
    for path, alt, pos in HERO_SLIDES:
        try:
            if staticfiles_storage.exists(path) or finders.find(path):
                slides.append({"src": staticfiles_storage.url(path), "alt": alt, "pos": pos})
        except Exception:
            continue
    return slides
def home(request):
    return render(request, "home.html", {"site": SiteSettings.objects.first(), "songs": Song.objects.all(), "media_items": MediaItem.objects.all()[:8], "hero_slides": hero_slides()})
def booking(request):
    if request.method == "POST":
        BookingEnquiry.objects.create(name=request.POST.get("name", "").strip(), email=request.POST.get("email", "").strip(), phone=request.POST.get("phone", "").strip(), organisation=request.POST.get("organisation", "").strip(), event_date=request.POST.get("event_date") or None, event_location=request.POST.get("event_location", "").strip(), message=request.POST.get("message", "").strip())
        messages.success(request, "Thank you. Your booking enquiry has been received.")
        return redirect("booking")
    return render(request, "booking.html")
