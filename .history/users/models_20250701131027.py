from django.db import models
from datetime import date

# Create your models here.
class User(models.Model): # describes model (for database)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    username = models.CharField(null = True, max_length = 20)
    password = models.CharField(null = True, max_length = 20)
    
    phone = models.IntegerField(null = True)
    date_joined = models.DateField(auto_now = True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"