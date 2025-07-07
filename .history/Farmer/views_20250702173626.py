from django.shortcuts import loader, redirect
from django.http import HttpResponse
from .models import User
from datetime import date

# Create your views here.

def registration(request):
    template = loader.get_template('registration2.html') 

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_no = request.POST.get('phone_no')
        
        if not (first_name and last_name and email and password and phone_no):
            context = {}
    
def login(request):
    template = loader.get_template('login2.html')

def new_crop(request):
    pass