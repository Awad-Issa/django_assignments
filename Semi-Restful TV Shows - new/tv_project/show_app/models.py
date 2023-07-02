from django.db import models

class showManager(models.Manager):
    def basic_validator(self,postdata):
        errors = {}
        if len(postdata['show_title']) < 2 :
            errors ['show_title'] = "title name should be at least 2 characters"
        if len(postdata['show_network']) < 3 :
            errors ['show_network'] = "network name should be at least 3 characters"
        if len(postdata['show_desc']) < 10 :
            errors ['show_desc']  = "Description should be at least 10 characters"        
        return errors       

class shows(models.Model):
    show_title = models.CharField(max_length=255)
    show_network = models.CharField(max_length=255)
    show_desc = models.CharField(max_length=255)
    show_date = models.DateField(default=None)
    created_at = models.DateTimeField(auto_now=True )
    updated_at = models.DateTimeField(auto_now=True)
    objects = showManager()

def delete_show(request):
    shows.objects.get(id)
