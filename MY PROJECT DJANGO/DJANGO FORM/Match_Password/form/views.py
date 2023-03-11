from django.shortcuts import render
from .forms import StudentRegistration
from django.http import HttpResponseRedirect
# Create your views here.


def thankyou(request):
    return render(request, 'form/success.html')


def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        # print('\nPOST REQUEST\n')
        # # print(fm)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            rpassword = fm.cleaned_data['rpassword']
            print(fm.cleaned_data)
            print(name)
            print(email)
            print(password)
            print(rpassword)
            return HttpResponseRedirect('success/')
            # return render(request, 'form/success.html', {'name': name})

    else:
        fm = StudentRegistration()
        print('\nGET REQUEST\n')
    return render(request, 'form/userregistration.html', {'form': fm})
