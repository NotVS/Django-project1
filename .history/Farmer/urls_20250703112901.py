from django.urls import path
from . import views

urlpatterns = [
    path('login2/', views.login, name = 'login2'),
    path('registration2/', views.registration, name = 'registration2'),
    path('main2/')]