from django.urls import path
from . import views

urlpatterns = [
    path('set/', views.setsessioncookie),
    path('get/', views.getsessioncookie),
    path('del/', views.delsessioncookie),
]
