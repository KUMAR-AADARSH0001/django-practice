from django.shortcuts import render
from .forms import UserRegistration
from django.contrib import messages
# Create your views here.


def show(request):
    if request.method == 'POST':
        fm = UserRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            # messages.add_message(request, messages.INFO,
            #                      'Your Account Created Successfully !!!!!')
            messages.success(
                request, 'Your Account Created Successfully !!!!!')
            messages.info(request, '\nNow You Can Login !!!!!')
    else:
        fm = UserRegistration()
    return render(request, 'msgfm/userregistration.html', {'form': fm})
