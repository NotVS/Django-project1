from django.shortcuts import loader, redirect
from django.http import HttpResponse
from .models import User
from datetime import date

# Create your views here.

def registration(request):
    template = loader.get_template('registration2.html') 

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        second
    
def login(request):
    template = loader.get_template('login2.html')

def new_crop(request):
    pass