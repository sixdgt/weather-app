from dataclasses import field, fields
from django import forms

from weatherapp.models import AppUser

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        # to generate form with all fields/attributes form
        # fields = "__all__"
        # to generate form with limited/custom field
        fields = ('email', 'password')
        model = AppUser

class ProfileUploadForm(forms.ModelForm):
    class Meta:
        fields = ('profile_pic',)
        model = AppUser

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        fields = ('first_name', 'middle_name', 'last_name',\
            'email', 'contact', 'dob', 'password', 'address', 'lat', 'long')

        model = AppUser