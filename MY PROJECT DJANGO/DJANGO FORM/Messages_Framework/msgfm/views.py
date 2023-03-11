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
            print(messages.set_level(request))
            messages.debug(request, '\nThis is debug')
            print(messages.get_level(request))
            messages.debug(request, '\nThis is debug')
    else:
        fm = UserRegistration()
    return render(request, 'msgfm/userregistration.html', {'form': fm})
