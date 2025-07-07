from django.shortcuts import loader, redirect
from django.http import HttpResponse
from .models import User
from datetime import date

# Create your views here.

def registration(request):
    template = loader.get_template('registration2.html') 

def login(request):
    pass

def new_crop(request):
    pass