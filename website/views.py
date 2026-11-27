from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import HomePageContent, Service, Souvenir, Booking, ContactMessage

def home(request):
    content=HomePageContent.objects.first() or HomePageContent()
    return render(request,"website/home.html",{"content":content,"services":Service.objects.filter(active=True),"souvenirs":Souvenir.objects.filter(active=True)})

@require_POST
def booking(request):
    Booking.objects.create(name=request.POST.get("name","").strip(),email=request.POST.get("email","").strip(),phone=request.POST.get("phone","").strip(),event_date=request.POST.get("event_date") or None,event_type=request.POST.get("event_type","").strip(),details=request.POST.get("details","").strip())
    messages.success(request,"Thank you. Your booking request has been received.")
    return redirect("/#booking")

@require_POST
def contact(request):
    ContactMessage.objects.create(name=request.POST.get("name","").strip(),email=request.POST.get("email","").strip(),message=request.POST.get("message","").strip())
    messages.success(request,"Thank you. Your message has been received.")
    return redirect("/#contact")
