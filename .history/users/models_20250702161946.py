from django.db import models
from datetime import date

# Create your models here.
class User(models.Model): # describes model (for database)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    username = models.CharField(null = True, max_length = 15)
    password = models.CharField(null = True, max_length = 20)
    
    phone = models.CharField(null = True, max_length = 15)
    date_joined = models.DateField(auto_now = True)
    

class Farmer(models.model):
    
    