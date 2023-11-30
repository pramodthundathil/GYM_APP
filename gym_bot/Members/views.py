from django.shortcuts import render, redirect
from .forms import MemberAddForm, SubscriptionAddForm

def Member(request):
    form = MemberAddForm()
    sub_form = SubscriptionAddForm()


    context = {"form":form,"sub_form":sub_form}
    return render(request,"members.html",context)

def Payments(request):
    return render(request, "payments.html")
