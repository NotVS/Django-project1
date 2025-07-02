from django.shortcuts import loader
from django.http import HttpResponse
from .models import User

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
    best_player = User.objects.filter(last_name = 'Sanogo', id = 5)
    context = {
        'diddy_bluds' : ['six-seven', '69', '420'],
        'ohio_bluds' : ['mustard', 'diddenbludden', 'drake'],
    'my_users' : my_data,
    
    }
    
    return HttpResponse(template.render(context, request))


