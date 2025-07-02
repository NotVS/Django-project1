from django.db import models
from datetime import date

# Create your models here.
class User(models.Model): # describes model (for database)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    
    phone = models.IntegerField()
    date_joined = models.DateField(date.toda)