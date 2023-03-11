from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField(min_length=5, max_length=30, label_suffix='', strip=False, error_messages={
                           'required': 'Enter your name'})
    roll = forms.IntegerField()
    price = forms.DecimalField(
        min_value=5, max_value=40, max_digits=5, decimal_places=1)
    rate = forms.FloatField(min_value=5, max_value=40)
    comment = forms.SlugField()
    email = forms.EmailField(min_length=5, max_length=50)
    password = forms.CharField(
        min_length=5, max_length=50, widget=forms.PasswordInput)
    website = forms.URLField()
    description = forms.CharField(widget=forms.Textarea)
    feedback = forms.CharField(min_length=5, max_length=100, widget=forms.TextInput(
        attrs={'class': 'somecss1 somecss2', 'id': 'uniqueid'}))
    notes = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 4, 'cols': 100}))
    agree = forms.BooleanField(label_suffix='', label='I Agree')
