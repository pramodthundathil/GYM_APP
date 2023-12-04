from django.urls import path 
from .import views 

urlpatterns = [
    path("Member",views.Member,name="Member"),
    path("Payments",views.Payments,name="Payments"),
    path("MembersSingleView/<int:pk>",views.MembersSingleView,name="MembersSingleView"),
    path("MemberAccess",views.MemberAccess,name="MemberAccess"),
    path("DeletePayment/<int:pk>",views.DeletePayment,name="DeletePayment"),
    path("DeleteMember/<int:pk>",views.DeleteMember,name="DeleteMember"),


    
      
]
