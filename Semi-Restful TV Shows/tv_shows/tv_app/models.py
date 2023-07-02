from django.db import models

# Create your models here.
class account(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)

class create_account(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    account.objects.create(first_name=first_name,last_name=last_name)

