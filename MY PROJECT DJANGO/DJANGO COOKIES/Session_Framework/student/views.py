from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.


def setsessioncookie(request):
    request.session['fname'] = 'Aadarsh'
    request.session['lname'] = 'Kumar'
    return render(request, 'student/setsessioncookie.html', )


def getsessioncookie(request):
    # fname = request.session['fname']
    fname = request.session.get('fname', default='No Data')
    lname = request.session.get('lname', default='No Data')
    return render(request, 'student/getsessioncookie.html', context={'fname': fname, 'lname': lname})


def delsessioncookie(request):
    if 'fname' in request.session:
        del request.session['fname']
    return render(request, 'student/delsessioncookie.html', )
