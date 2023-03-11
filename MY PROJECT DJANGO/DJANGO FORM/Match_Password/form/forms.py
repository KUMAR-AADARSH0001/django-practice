from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(
        label='Password(again)', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        valpswd = cleaned_data['password']
        valrpswd = cleaned_data['rpassword']

        if valpswd != valrpswd:
            raise forms.ValidationError('Password does not match')
