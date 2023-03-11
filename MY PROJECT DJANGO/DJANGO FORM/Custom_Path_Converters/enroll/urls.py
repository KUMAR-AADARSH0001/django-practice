from django.urls import path, register_converter
from . import views, convertors

register_converter(convertors.FourDigitYearConvertor, 'yyyy')

urlpatterns = [

    path('student/session/<yyyy:year>/', views.show_details,
         name='subdetail'),  # this is used for int

]
