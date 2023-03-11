from django.urls import path
from vldtr_bltn import views

urlpatterns = [
    path('reg/', views.showformdata),
]
