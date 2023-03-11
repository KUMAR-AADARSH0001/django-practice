from django.urls import path
from enroll import views

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
]
