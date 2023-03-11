from django.urls import path
from vldtr_cstm import views

urlpatterns = [
    path('reg/', views.showformdata),
]
