# Django-project1
Working on mastering django

Login system

template (login.html):
- Extends master.html, uses block content to put the login form.
- Has username and password inputs, submit button, csrf token for security measures
  
urls.py:
- path('login/', views.login, name='login') links to login view.
  
views.py (def login):
- Checks if request is POST.
- Gets username and password from request.POST.
- Checks if user exists in User model.
- Redirects to another page if login works, else shows error.

models.py:
- User model has username, password, and other fields defind in a class. Used to check login.


Registration system

template (registration.html):
- Extends master.html, uses block content for the form.
- Fields: first name, last name, username, password, phone.
- Uses csrf token.

urls.py:
- path('registration/', views.registration, name='registration').

views.py (def registration):
- Checks if request is POST.
- Gets data from request.POST.
- Makes sure all fields are filled.
- Creates User object, saves to database.
- Redirects after save.

models.py:
- Same User model. New user data gets saved to it.


Shell commands
Go to project folder, activate venv (e.g in anaconda prompt), run server:

STARTING WEBSITE
1. cd (path to project folder)
2. folder_name\Scripts\activate
3. python manage.py runserver

ACCESSING DATABASE (python shell):
1. cd (path to project folder)
2. folder_name\Scripts\activate
3. python manage.py shell
4. from appname.models import (e.g user)
5. User.objects.all().values() will display all values in SQL

MAKING DATABASE CHANGES (python shell)
- user = User.objects.create(...)
- user.save()

MAKING MODEL CHANGES (models.py) - go to Anaconda Prompt
1. python manage.py makemigrations users
2. python manage.py migrate

Django admin
Make superuser: python manage.py createsuperuser
Access: http://127.0.0.1:8000/admin/

Login with superuser.
You can view, edit, or delete users and see all records.
