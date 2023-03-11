from django.urls import path
from . import views

urlpatterns = [
    # path('student/<my_id>/', views.show_details,
    #      name='detail'),  # this is used for str
    path('', views.home, name='home'),
    path('student/<int:my_id>/', views.show_details,
         name='detail'),  # this is used for int
    path('student/<int:my_id>/<int:my_subid>/', views.show_subdetails,
         name='subdetail'),  # this is used for int

]
