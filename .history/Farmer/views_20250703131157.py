from django.shortcuts import loader, redirect
from django.http import HttpResponse
from .models import Farmer
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
        service = request.POST.get('service')
        
        if not (first_name and last_name and email and password and phone_no):
            context = {'error' : 'fill out all details'}
            
            return HttpResponse(template.render(context, request))
        
        
        new_farmer = Farmer(first_name = first_name,
                            last_name = last_name,
                            email = email,
                            password = password,
                            phone_no = phone_no,
                            service = service)
        
        new_farmer.save()
        
        return redirect('/main2/')
    
    return HttpResponse(template.render({}, request))
    
def login(request):
    template = loader.get_template('login2.html')
    
    if request.method == "POST":
        mail = request.POST.get('email')
        pwd = request.POST.get('password')
        
        try:
            x = Farmer.objects.get(email = mail)
            if pwd == x.password:
                return redirect('/main2/')
            
            else:
                context = {'error' : 'incorrect password'}
                return HttpResponse(template.render(context, request))
            
        except Farmer.DoesNotExist:
            context = {'error': 'no such user found'}
            return HttpResponse(template.render(context, request))
    
    return HttpResponse(template.render({}, request))
        

def main(request):
    template = loader.get_template("main2.html")
    
    return HttpResponse(template.render({}, request))



def new_crop(request):
    request.session['farmer_id'] = Farmer.id
    template = loader.get_template("new_crop.html")
    farmers = Farmer.objects.all()
    context = {'farmers' : farmers}
    
    return HttpResponse(template.render(context, request))