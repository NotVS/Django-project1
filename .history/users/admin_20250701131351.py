from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name"date_joined", "phone")

admin.site.register(User, UserAdmin)
