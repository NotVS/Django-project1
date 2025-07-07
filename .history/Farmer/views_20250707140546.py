from django.shortcuts import loader, redirect
from django.http import HttpResponse
from .models import Farmer, Crop
from datetime import date
import matplotlib.pyplot as plt

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
    template = loader.get_template("view_crops.html")
    farmer_id = request.session.get("farmer_id")
    
    farmers = Farmer.objects.all()
    for farmer in farmers:
        crops = Crop.objects.filter(farmer = farmer)
        
    
    
    
    if not farmer_id:
        context = {'error' : 'not logged in'}
        return HttpResponse(template.render(context, request))
    
    my_crops = Crop.objects.filter(farmer_id = farmer_id)
    
    context = {'my_crops': my_crops}
    return HttpResponse(template.render(context, request))



def crop_chart(request):
    template = loader.get_template("crop_chart.html")
    farmer_id = request.session.get("farmer_id")
    
    if not farmer_id:
        context = {'error' : 'farmer not logged in'}
        return HttpResponse(template.render(context, request))
    
    crops = Crop.objects.filter(farmer_id = farmer_id)
    
    for x in Farmer.objects.all():
        if x.id == farmer_id:
            farmer = x.first_name 
            break
        
      
    crop_types = [crop.crop_type for crop in crops]
    areas = [crop.area for crop in crops]
    prices = [crop.price_per_m2 for crop in crops]
        
        
    fig, axs = plt.subplots(1, 2, figsize = (12, 6))
    
    # bar chart - crop areas
    axs[0].bar(crop_types, areas, color = 'green')
    axs[0].set_title(f"{farmer}'s Crop Areas")
    axs[0].set_ylabel('Area (m²)')
    axs[0].tick_params(axis = 'x', rotation = 45)
    
    # bar chart - crop prices
    
    axs[1].bar(crop_types, prices, color = 'blue')
    axs[1].set_title(f"{farmer}'s Crop Prices")
    axs[1].set_ylabel('Price per m²')
    axs[1].tick_params(axis = 'x')
        