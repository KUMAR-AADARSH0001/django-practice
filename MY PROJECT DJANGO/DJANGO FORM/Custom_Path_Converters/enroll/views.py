from django.shortcuts import render

# Create your views here.


def show_details(request, year):
    context = {'yr': year}
    return render(request, 'enroll/show.html', context)
