from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    # path('hi/<int:num>',views.routing)

]
