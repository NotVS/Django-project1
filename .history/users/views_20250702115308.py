from django.shortcuts import loader, redirect
from django.http import HttpResponse
from .models import User
from django.contrib.auth.forms import UserCreationForm

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
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("users/testing")
        
        else:
            form = 
        
    form = UserCreationForm()
    context = {"form" : form}
    return HttpResponse(template.render(context, request))
    