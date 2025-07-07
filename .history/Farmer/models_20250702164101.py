from django.db import models

# Create your models here.
class Farmer(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField()
    password = models.CharField()   
    phone_no = models.CharField(null = True, max_length = 15)
    
    service = models.CharField(max_length = 30)

class Crop(models.Model):
    farmer = models.ForeignKey(Farmer)
    crop_type = models.CharField(max_length = 50)
    location = models.CharField(max_length = 20)