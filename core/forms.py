from django import forms
from .models import BookingRequest, ContactMessage

class BookingRequestForm(forms.ModelForm):
    class Meta:
        model = BookingRequest
        fields = ["name", "email", "phone", "event_type", "event_date", "message"]
        widgets = {
            "event_date": forms.DateInput(attrs={"type": "date"}),
            "message": forms.Textarea(attrs={"rows": 4}),
        }

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]
        widgets = {"message": forms.Textarea(attrs={"rows": 5})}
