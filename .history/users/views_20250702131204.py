from django.shortcuts import loader, redirect
from django.http import HttpResponse
from .models import User
from datetime import date

def users(request):
    myusers = User.objects.all().values()
    template = loader.get_template('all_users.html')
    context = {
        'myusers' : myusers
    }
    
    return HttpResponse(template.render(context, request))


def details(request, id):
    myuser = User.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'myuser' : myuser,
    }
    
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request):
    template = loader.get_template('template.html')
    my_data = User.objects.all() #querying data
    best_player = User.objects.filter(last_name = 'Sanogo', id = 5).values() | User.objects.filter(id = 2).values()
    context = {
        'diddy_bluds' : ['six-seven', '69', '420'],
        'ohio_bluds' : ['mustard', 'diddenbludden', 'drake'],
    'my_users' : my_data,
    'sangolo' : best_player
    }
    
    return HttpResponse(template.render(context, request))


def registration(request):
    template = loader.get_template("registration.html")
    
    if request.method == "POST":
        firstname = request.POST.get("first_name")
        lastname = request.POST.get("last_name")
        usname = request.POST.get("username")
        pwd = request.POST.get("password")
        phone_number = request.POST.get("phone")
        
        if not(firstname and lastname and usname and pwd and phone_number):
            context = {
                "error" : "please fill out all fields"
            }  
        
            return HttpResponse(template.render(context, request)) 
        
        new_user = User(first_name = firstname,
                        last_name = lastname,
                        username = usname,
                        password = pwd,
                        phone = phone_number,
                        date_joined = date.today())
        
        new_user.save()
        
        return redirect("testing")


    return HttpResponse(template.render({}, request))
    
    
    def login(request):
        template = loader.get_template('login.html')
        
        if request.method == "GET":
            for x in User:
                if x[2] == request.method.GET('username'):
                    if x[3] == request.method.GET
                
        
        
        return HttpResponse(template.render({}, request))