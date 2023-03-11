from django.urls import path
from . import views

urlpatterns = [
    path('set/', views.setcookie),
    path('get/', views.getcookie),
    path('del/', views.delcookie),
]
