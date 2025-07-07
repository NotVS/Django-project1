from django.urls import path
from . import views

urlpatterns = [
    path('login2/', views.login, name = 'login2'),
    path('registration2/', views.registration, name = 'registration2'),
    path('main2/', views.main, name = 'main2'),
    path('main2/new_crop/', views.new_crop, name = 'new_crop')]