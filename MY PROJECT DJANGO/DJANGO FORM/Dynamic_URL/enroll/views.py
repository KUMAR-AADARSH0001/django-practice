from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'enroll/home.html')


# def show_details(request, my_id):
#     context = {'id': my_id}
#     return render(request, 'enroll/show.html', context)


def show_details(request, my_id):
    if my_id == 1:
        context = {'id': my_id, 'name': 'Aman'}
    if my_id == 2:
        context = {'id': my_id, 'name': 'Aashish'}
    if my_id == 3:
        context = {'id': my_id, 'name': 'Aadarsh'}
    if my_id == 4:
        context = {'id': my_id, 'name': 'Dheeraj'}
    if my_id == 5:
        context = {'id': my_id, 'name': 'Rohit'}
    return render(request, 'enroll/show.html', context)


def show_subdetails(request, my_id, my_subid):
    if my_id == 1 and my_subid == 1:
        context = {'id': my_id, 'name': 'Aman', 'info': 'Sub_details'}
    if my_id == 2 and my_subid == 2:
        context = {'id': my_id, 'name': 'Aashish', 'info': 'Sub_details'}
    if my_id == 3 and my_subid == 3:
        context = {'id': my_id, 'name': 'Aadarsh', 'info': 'Sub_details'}
    if my_id == 4 and my_subid == 4:
        context = {'id': my_id, 'name': 'Dheeraj', 'info': 'Sub_details'}
    if my_id == 5 and my_subid == 5:
        context = {'id': my_id, 'name': 'Rohit', 'info': 'Sub_details'}
    return render(request, 'enroll/show.html', context)
