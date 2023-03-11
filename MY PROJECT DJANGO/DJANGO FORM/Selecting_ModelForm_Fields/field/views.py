from django.shortcuts import render
from .forms import UserForm

# Create your views here.


def show(request):
    fm = UserForm
    return render(request, 'field/userform.html', {'form': fm})
