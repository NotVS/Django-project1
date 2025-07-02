from django.urls import path
from . import views

urlpatterns = [
    path()
    path('users/', views.users, name= 'users'),
    path('users/details/<int:id>/', views.details, name = 'details'),
]

