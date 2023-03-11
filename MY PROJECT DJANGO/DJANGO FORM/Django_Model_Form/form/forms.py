from django.core import validators
from django import forms
from .models import User


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        labels = {'name': 'Enter Your Name',
                  'email': 'Enter Your Email',
                  'password': 'Enter Your Password'}
        error_messages = {
            'name': {'required': 'Please enter your name'},
            'email': {'required': 'Please enter your email'},
            'password': {'required': 'Please enter your password'},
        }
        widgets = {
            'password': forms.PasswordInput
        }
