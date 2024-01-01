from django import forms
from .models import Contact, Subscriber


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'message']


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']