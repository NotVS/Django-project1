from django.db import models

# Create your models here.
class User(models.Model): # describes model (for database)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    username = models.CharField(max_length)