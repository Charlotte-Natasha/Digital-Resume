import email
from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True, widget= forms.TextInput(attrs={ 'placeholder':'*Full Name..', 'class': 'form-control'}))
    email = forms.EmailField(max_length=200, required=True, widget= forms.TextInput(attrs={ 'placeholder':'*Email..', 'class': 'form-control'}))
    subject = forms.CharField(max_length=100, required=True, widget= forms.TextInput(attrs={ 'placeholder':'*Subject..', 'rows': '2'}))
    message = forms.CharField(max_length=500, required=True, widget= forms.Textarea(attrs={ 'placeholder':'*Your message here..', 'rows': '6'}))

    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')

