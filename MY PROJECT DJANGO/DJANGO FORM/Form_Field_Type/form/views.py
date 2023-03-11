from django.shortcuts import render
from .forms import StudentRegistration
from django.http import HttpResponseRedirect
# Create your views here.


def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        # print('\nPOST REQUEST\n')
        # # print(fm)
        if fm.is_valid():
            print(fm.cleaned_data)

    else:
        fm = StudentRegistration()
        print('\nGET REQUEST\n')
    return render(request, 'form/userregistration.html', {'form': fm})
