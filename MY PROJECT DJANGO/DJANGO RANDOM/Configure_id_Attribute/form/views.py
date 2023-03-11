from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.


def showformdata(request):
    # fm = StudentRegistration(auto_id='some_%s')   if you wnat to id in string
    fm = StudentRegistration(auto_id=True)
    return render(request, 'form/userregistration.html', {'form': fm})
