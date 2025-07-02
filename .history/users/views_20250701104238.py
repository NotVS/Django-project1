from django.shortcuts import loader
from django.http import HttpResponse
from .models import User

def users(request):
    myusers = User.objects.all().values()
    template = loader.get_template('all_users.html')
    
    return HttpResponse(template.render())