from django.shortcuts import render, HttpResponse, redirect
from . import models


# This function will do ....
# Date:
# Created by:
# Input Parameter:
# output Paraemeter 
def index(request):
    context = {
        "dojo_information": models.get_all_dojos(),
        "ninja_information" :models.get_all_ninja()
      }
    return render(request,'index.html',context)

def add_dojo(request):
    models.add_dojo(request)
    return redirect('/')
    

def add_ninja(request):
    models.add_ninja(request)
    return redirect('/')    