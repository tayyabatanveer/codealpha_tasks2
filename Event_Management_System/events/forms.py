# events/forms.py
from django import forms
from .models import Registration

class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = []  
