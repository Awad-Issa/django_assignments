from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email_address = models.EmailField(max_length=245)
    age = models.IntegerField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

def get_all_users():
    return Users.objects.all()

def add_user(request):
    first_name = request.POST['first_name']
    last_name =  request.POST['last_name']
    email_address =  request.POST['email']
    age =  request.POST['age']
    Users.objects.create(first_name=first_name,last_name=last_name,email_address=email_address,age=age)












