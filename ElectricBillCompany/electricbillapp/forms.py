from django import forms
from .models import *

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name','email','phone','comments']

class RegisterYourHouseForm(forms.ModelForm):
    class Meta:
        model = RegisterYourHouse
        fields = ['name', 'address', 'phonenumber', 'postalcode']

class GenerateBillForm(forms.Form):
    primarykey = forms.IntegerField()
    units = forms.IntegerField()

class BackEndPortalForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
