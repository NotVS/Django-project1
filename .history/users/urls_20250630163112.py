from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.users, name= 'users')
]