from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        valname = self.cleaned_data['name']
        valemail = self.cleaned_data['email']
        valpassword = self.cleaned_data['password']
        if len(valname) < 4:
            raise forms.ValidationError('Name should be more then 3 words')

        if len(valemail) < 10:
            raise forms.ValidationError('Email should be more then 10 words')

        if len(valpassword) < 8:
            raise forms.ValidationError(
                'Password should be more and equal then 8 words')
