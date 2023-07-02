from django.shortcuts import render, redirect
from . import models
from .models import shows
# from django.db import models
from django.contrib import messages


def create(request):
    return render(request,'create.html')

def create_show(request):
    errors = shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/') 
    show_title = request.POST['show_title']
    show_network = request.POST['show_network']
    show_date = request.POST['show_date']
    show_desc = request.POST['show_desc']
    shows.objects.create(show_title = show_title,
                         show_network = show_network, 
                         show_desc=show_desc, 
                         show_date=show_date ) 
    return redirect('/')

def UpdateShow(request,uid):
    show_to_update = models.shows.objects.get(id=uid) 
    if request.POST:
        show_to_update.show_title= request.POST['show_title']
        show_to_update.show_network= request.POST['show_network']
        show_to_update.show_date= request.POST['show_date']
        show_to_update.show_desc= request.POST['show_desc']
        show_to_update.save()
        return redirect('/shows')

def mainshows(request):
    context = {
        "shows_information": shows.objects.all()
    }
    return render (request,'read.html',context)

def delete_show(request,uid):
    show_to_delete = models.shows.objects.get(id= uid)
    show_to_delete.delete()
    return redirect ('/shows')

def show_information(request,uid):

    context = {
        "shows_information1": models.shows.objects.get(id=uid)
    }
    return render (request,'shows_id.html',context)

def editShow(request,uid):
    data = {
        'show' : models.shows.objects.get(id=uid) 
    }
    return render(request,"edit.html",data)     