from django.urls import path     
from . import views
urlpatterns = [
    path('', views.create),	   
    path('shows/create',views.create_show),
    path('shows/edit/<int:uid>',views.UpdateShow),
    path('shows', views.mainshows),
    path('delete/<int:uid>', views.delete_show),
    path('shows/<int:uid>',views.show_information),
    path('edit/<int:uid>',views.editShow),
]