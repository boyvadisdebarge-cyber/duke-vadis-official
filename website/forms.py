from django import forms
from .models import Booking, ContactMessage

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields=["name","email","phone","event_date","event_type","details"]
        widgets={"event_date":forms.DateInput(attrs={"type":"date"})}

class ContactForm(forms.ModelForm):
    class Meta:
        model=ContactMessage
        fields=["name","email","message"]
