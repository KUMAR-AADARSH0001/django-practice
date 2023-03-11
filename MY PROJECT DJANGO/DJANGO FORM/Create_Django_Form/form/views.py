from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.


def showformdata(request):
    fm = StudentRegistration
    return render(request, 'form/userregistration.html', {'form': fm})
