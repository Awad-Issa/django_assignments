from django.db import models

class dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.TextField(max_length=2)

class ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(dojo, related_name="ninjas", on_delete=models.CASCADE) 

def get_all_dojos():
    return dojo.objects.all()    


def get_all_ninja():
    return ninja.objects.all() 

def add_ninja(request):
    first_name = request.POST['first_name']
    last_name =  request.POST['last_name']
    dojo_id = request.POST['dojo_id']
    new_ninja_awad=ninja.objects.create(first_name=first_name,last_name=last_name,dojo_id=dojo_id)
    return new_ninja_awad

def add_dojo(request):
    name = request.POST['name']
    city = request.POST['city']
    state = request.POST['state']
    new_dojo_awad=dojo.objects.create(name=name,city=city,state=state)
    return new_dojo_awad


