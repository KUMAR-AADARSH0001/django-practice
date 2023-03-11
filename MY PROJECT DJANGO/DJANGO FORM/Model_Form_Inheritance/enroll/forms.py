from django import forms
from .models import User


class StudentForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['student_name', 'email', 'password']


class TeacherForm(forms.ModelForm):
    class Meta(StudentForm.Meta):
        fields = ['teacher_name', 'email', 'password']
