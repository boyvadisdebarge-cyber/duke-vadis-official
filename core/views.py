from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import BookingRequestForm, ContactMessageForm
from .models import MusicRelease, PromoBanner, Service, SiteProfile, SongButton, Souvenir

def home(request):
    booking_form = BookingRequestForm(prefix="booking")
    contact_form = ContactMessageForm(prefix="contact")
    if request.method == "POST":
        form_type = request.POST.get("form_type")
        if form_type == "booking":
            booking_form = BookingRequestForm(request.POST, prefix="booking")
            if booking_form.is_valid():
                booking_form.save()
                messages.success(request, "Thank you. Your booking request has been received. We will contact you to discuss the details.")
                return redirect("home")
        elif form_type == "contact":
            contact_form = ContactMessageForm(request.POST, prefix="contact")
            if contact_form.is_valid():
                contact_form.save()
                messages.success(request, "Thank you for contacting Duke Vadis. Your message has been received.")
                return redirect("home")
    profile = SiteProfile.objects.first()
    context = {
        "profile": profile,
        "promo_banners": PromoBanner.objects.filter(is_active=True),
        "releases": MusicRelease.objects.filter(is_published=True),
        "song_buttons": SongButton.objects.filter(is_active=True),
        "services": Service.objects.filter(is_published=True),
        "souvenirs": Souvenir.objects.filter(is_available=True),
        "booking_form": booking_form,
        "contact_form": contact_form,
    }
    return render(request, "home.html", context)
