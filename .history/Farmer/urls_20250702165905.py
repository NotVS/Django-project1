from django.urls import path
from . import views

urlpatterns = [
    path('login2', views.login)]