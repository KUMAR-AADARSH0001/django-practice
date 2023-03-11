from django.shortcuts import render
from .forms import SignupForm
from django.contrib import messages
# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Account created Successfully!!!!')
            fm = SignupForm()
    else:
        fm = SignupForm()
    return render(request, 'enroll/signup.html', {'form': fm})
