from django.urls import path 
from .import views 

urlpatterns = [
    path("Member",views.Member,name="Member"),
    path("Payments",views.Payments,name="Payments"),
      
]
