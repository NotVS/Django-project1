from django.shortcuts import loader
from django.http import HttpResponse

def users(request):
    template = loader.get_template('all_.html')
    return HttpResponse(template.render())