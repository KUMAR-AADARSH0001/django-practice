from django.shortcuts import render, HttpResponse
from datetime import datetime, timedelta
# Create your views here.


def setsessioncookie(request):
    request.session['name'] = 'Aadarsh'
    return render(request, 'student/setsessioncookie.html', )


def getsessioncookie(request):
    if 'name' in request.session:
        name = request.session['name']
        return render(request, 'student/getsessioncookie.html', context={'name': name})
    else:
        return HttpResponse('<h1>Your Session Has Expired  !.!.!.!.!.</h2>')


def delsessioncookie(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'student/delsessioncookie.html', )
