from django.shortcuts import render
from django.http import HttpResponse

def users(request):
    template = loader.get_template('myfirst.html')
    