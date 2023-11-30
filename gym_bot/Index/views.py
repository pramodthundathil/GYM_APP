from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from Members.models import Subscription_Period, Subscription, Batch_DB
from Members.forms import Subscription_PeriodForm, BatchForm


def Home(request):
    return render(request,"index.html")

def Setting_Module(request):
    form = BatchForm()
    sub_form = Subscription_PeriodForm()
    batch = Batch_DB.objects.all()
    speriod = Subscription_Period.objects.all()
    context = {
        "form":form,
        "sub_form":sub_form,
        "batch":batch,
        "speriod":speriod
    }
    return  render(request, "settings.html",context)

def BatchSave(request):
    if request.method == "POST":
        form = BatchForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Batch Data Saved")
            return redirect("Setting_Module")
        else:
            messages.error(request,"Something Went wrong")
            return redirect("Setting_Module")
    return redirect("Setting_Module")

def Batch_Delete(request,pk):
    batch = Batch_DB.objects.get(id = pk).delete()
    messages.success(request,"Batch Data Deleted")
    return redirect("Setting_Module")


def SubscriptionPeriodSave(request):
    if request.method == "POST":
        form = Subscription_PeriodForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Subscription Period Saved")
            return redirect("Setting_Module")
        else:
            messages.error(request,"Something Went wrong")
            return redirect("Setting_Module")
    return redirect("Setting_Module")

def SubScriptionPeriod_Delete(request,pk):
    batch = Subscription_Period.objects.get(id = pk).delete()
    messages.success(request,"Subscription period Data Deleted")
    return redirect("Setting_Module")

    
    


def SignIn(request):
    if request.method == "POST":
        uname = request.POST['uname']
        pswd = request.POST['pswd']
        user = authenticate(request, username=uname, password = pswd)
        if user is not None:
            login(request, user)
            return redirect("Home")
        else:
            messages.error(request, "User Name or Password Incorrect")
            return redirect("SignIn")
    return render(request,"login.html")

def SignOut(request):
    logout(request)
    return redirect(SignIn)
