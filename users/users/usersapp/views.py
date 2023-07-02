from django.shortcuts import render, HttpResponse, redirect
from . import models
def index(request):
    context = {
        "users_information": models.get_all_users()
    }
    return render(request,"index.html", context)

def add_user(request):
    models.add_user(request)
    return redirect('/')