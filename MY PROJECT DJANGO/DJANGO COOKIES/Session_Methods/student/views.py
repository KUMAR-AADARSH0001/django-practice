from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.


def setsessioncookie(request):
    request.session['fname'] = 'Aadarsh'
    request.session['lname'] = 'Kumar'
    return render(request, 'student/setsessioncookie.html', )


def getsessioncookie(request):
    fname = request.session.get('fname', default='No Data')
    lname = request.session.get('lname', default='No Data')
    keys = request.session.keys()
    items = request.session.items()
    # this method is set or get both
    age = request.session.setdefault('age', 20)
    return render(request, 'student/getsessioncookie.html', context={'fname': fname, 'lname': lname, 'keys': keys, 'items': items})


def delsessioncookie(request):
    request.session.flush()
    return render(request, 'student/delsessioncookie.html', )
