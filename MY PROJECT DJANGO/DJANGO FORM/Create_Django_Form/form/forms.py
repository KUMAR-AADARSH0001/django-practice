from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    email = forms.EmailField()
    password = forms.PasswordInput()
