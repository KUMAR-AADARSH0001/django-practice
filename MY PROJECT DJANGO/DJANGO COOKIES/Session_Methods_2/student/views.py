from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.


def setsessioncookie(request):
    request.session['fname'] = 'Aadarsh'
    request.session.set_expiry(600)
    return render(request, 'student/setsessioncookie.html', )


def getsessioncookie(request):
    fname = request.session.get('fname', default='No Data')
    return render(request, 'student/getsessioncookie.html', context={'fname': fname})


def delsessioncookie(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'student/delsessioncookie.html', )
