from django.shortcuts import render
from .forms import StudentRegistration
from django.http import HttpResponseRedirect
from .models import User
# Create your views here.


def thankyou(request):
    return render(request, 'form/success.html')


def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        # print('\nPOST REQUEST\n')
        # # print(fm)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pd = fm.cleaned_data['password']
            # if you want to update the value then give id before the name in next line
            reg = User(name=nm, email=em, password=pd)
            reg.save()

            return HttpResponseRedirect('success/')
            # return render(request, 'form/success.html', {'name': name})

    else:
        fm = StudentRegistration()
        print('\nGET REQUEST\n')
    return render(request, 'form/userregistration.html', {'form': fm})
