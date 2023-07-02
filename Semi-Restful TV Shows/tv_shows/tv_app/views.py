from django.shortcuts import render, HttpResponse,redirect
from . import models
def index(request):
    context = {
        "shows_information":models.get_all_shows()
    }
    return render(request,'read.html',context)

def showsform(request):
    return render(request,"create.html")

def create_show(request):
    models.add_show(request)
    return redirect('/shows/new')


