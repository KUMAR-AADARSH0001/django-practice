from .forms import TeacherForm
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import StudentForm, TeacherForm
# Create your views here.


def student_form(request):
    if request.method == 'POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = StudentForm()
        print('\nGET REQUEST\n')
    return render(request, 'enroll/student.html', {'form': fm})


def teacher_form(request):
    if request.method == 'POST':
        fm = TeacherForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = TeacherForm()
        print('\nGET REQUEST\n')
    return render(request, 'enroll/teacher.html', {'form': fm})
