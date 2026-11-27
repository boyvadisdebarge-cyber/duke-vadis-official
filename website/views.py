from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import HomePageContent, Service, Souvenir
from .forms import BookingForm, ContactForm

def home(request):
    content=HomePageContent.objects.first() or HomePageContent()
    return render(request,"website/home.html",{"content":content,"services":Service.objects.filter(active=True),"souvenirs":Souvenir.objects.filter(active=True),"booking_form":BookingForm(),"contact_form":ContactForm()})

@require_POST
def booking(request):
    form=BookingForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,"Thank you. Your booking request has been received.")
    else:
        messages.error(request,"Please check the booking details and try again.")
    return redirect("/#booking")

@require_POST
def contact(request):
    form=ContactForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,"Thank you. Your message has been received.")
    else:
        messages.error(request,"Please check your contact details and try again.")
    return redirect("/#contact")
