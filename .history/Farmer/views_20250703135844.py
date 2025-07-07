from django.shortcuts import loader, redirect
from django.http import HttpResponse
from .models import Farmer, Crop
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
                request.session['farmer_id'] = x.id
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
    template = loader.get_template("new_crop.html")
    farmer_id = request.session.get("farmer_id")
    
    if not farmer_id:
        context = {'error' : 'farmer not logged in'}
        return HttpResponse(template.render(context, request))
    
    farmer = Farmer.objects.get(id = farmer_id)
    
    if request.method == "POST":
        crop_type = request.POST.get("crop_type")
        location = request.POST.get("location")
        area = request.POST.get("area")
        price_per_m2 = request.POST.get("price_per_m2")
        
        planting_date = request.POST.get("planting_date")
        harvest_date = request.POST.get("harvest_date")
        
        add_crop = Crop(farmer = farmer
                        ,crop_type = crop_type,
                        location = location,
                        area = area,
                        price_per_m2 = price_per_m2,
                        planting_date = planting_date,
                        harvest_date = harvest_date)
        
        add_crop.save()
        
        return redirect('/main2/view_crops/')
        
        
    farmers = Farmer.objects.all()
    context = {'farmers' : farmers}
    
    return HttpResponse(template.render(context, request))





def view_crops(request):
    template = loader.get_template("master2.html")
    
    return HttpResponse(template.render({}, request))
