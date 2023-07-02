from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	
    path('shows',views.index),
    path('showsform',views.showsform),
    path('shows/new',views.create_show),
]




