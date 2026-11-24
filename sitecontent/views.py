from django.contrib import messages
from django.shortcuts import redirect, render
from .models import BookingEnquiry, MediaItem, SiteSettings, Song
def home(request):
    return render(request, "home.html", {"site": SiteSettings.objects.first(), "songs": Song.objects.all(), "media_items": MediaItem.objects.all()[:8]})
def booking(request):
    if request.method == "POST":
        BookingEnquiry.objects.create(name=request.POST.get("name", "").strip(), email=request.POST.get("email", "").strip(), phone=request.POST.get("phone", "").strip(), organisation=request.POST.get("organisation", "").strip(), event_date=request.POST.get("event_date") or None, event_location=request.POST.get("event_location", "").strip(), message=request.POST.get("message", "").strip())
        messages.success(request, "Thank you. Your booking enquiry has been received.")
        return redirect("booking")
    return render(request, "booking.html")
