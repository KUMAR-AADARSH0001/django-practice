from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.


def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        # print('\nPOST REQUEST\n')
        # # print(fm)
        if fm.is_valid():
            print(fm.cleaned_data)
            print(fm.cleaned_data['name'])
            print(fm.cleaned_data['age'])
            print(fm.cleaned_data['password'])
            fm = StudentRegistration()

    else:
        fm = StudentRegistration()
        print('\nGET REQUEST\n')
    return render(request, 'form/userregistration.html', {'form': fm})
