from django.forms import ModelForm
from django import forms
from .models import *

class ContactForm(forms.Form):

    name=forms.CharField(
        label='Enter your name',
        required=True,
        widget=forms.TextInput(attrs={'class':'nameclass'}))

    email=forms.EmailField(
        label='Enter your Email',
        required=True,
        widget=forms.TextInput(attrs={'class':'emailclass'}))



    phone=forms.IntegerField(
        label='Enter your Mobile',
        required=True,
        widget=forms.TextInput(attrs={'class':'phoneclass','type':'phone'}))

    subject=forms.CharField(
        label='Enter your subject',
        required=True,
        widget=forms.TextInput(attrs={'class':'messageclass'}))

    message=forms.CharField(
        label='Enter your Message',
        required=True,
        widget=forms.Textarea(attrs={'class':'messageclass'}))



    

      
