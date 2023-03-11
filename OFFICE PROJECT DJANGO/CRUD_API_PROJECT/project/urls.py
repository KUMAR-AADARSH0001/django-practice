from django.urls import path
from . import views


urlpatterns = [
    path('create_stu/',views.student_create),
    path('one_stu/<int:pk>/',views.student_info_one),
    path('all_stu/',views.student_info_all),
]