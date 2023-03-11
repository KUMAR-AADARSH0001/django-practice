from django.shortcuts import render
from .forms import UserRegistration
from django.contrib import messages
# Create your views here.


def show(request):
    messages.info(request,'Now you can Login')
    messages.success(request, 'Account Updated')
    messages.warning(request, 'This is warning')
    messages.error(request, 'This is an error')
    fm = UserRegistration()
    return render(request, 'msgfm/userregistration.html', {'form': fm})
