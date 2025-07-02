from django.shortcuts import loader
from django.http import HttpResponse

def users(request):
    myusers = User.objects.all()
    template = loader.get_template('all_users.html')
    return HttpResponse(template.render())