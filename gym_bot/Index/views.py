from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from Members.models import Subscription_Period, Subscription, Batch_DB, TypeSubsription,MemberData,Payment
from Members.forms import Subscription_PeriodForm, BatchForm, TypeSubsriptionForm
from datetime import datetime, timedelta
from django.utils import timezone

this_month = timezone.now().month
end_date = timezone.now()
start_date = end_date + timedelta(days=-5)


def Home(request):
    subscribers = Subscription.objects.all()[:8][::-1]
    members = MemberData.objects.all()
    month = datetime.now().strftime('%B')
    notification_payments = Payment.objects.filter(Payment_Date__gte = start_date,Payment_Date__lte = end_date )

    
    collected_amount = 0

    payment = Payment.objects.filter(Payment_Date__month = this_month)
    for i in payment:
        collected_amount += i.Amount
    
    context = {
        "subscribers":subscribers,
        "membercount":members.count(),
        "feepending":Subscription.objects.filter(Payment_Status = False).count(),
        "month":month,
        "collected_amount":collected_amount,
        "notification_payments":notification_payments,
        "notificationcount":notification_payments.count()
    }

    return render(request,"index.html",context)

def Setting_Module(request):

    form = BatchForm()
    sub_form = Subscription_PeriodForm()
    typesub_form = TypeSubsriptionForm()

    batch = Batch_DB.objects.all()
    speriod = Subscription_Period.objects.all()
    Sub_type = TypeSubsription.objects.all()

    context = {
        "form":form,
        "sub_form":sub_form,
        "batch":batch,
        "speriod":speriod,
        "typesub_form":typesub_form,
        "Sub_type":Sub_type
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

def SubscriptionTypeSave(request):
    if request.method == "POST":
        form = TypeSubsriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Subscription Type Saved")
            return redirect("Setting_Module")
        else:
            messages.error(request,"Something Went wrong")
            return redirect("Setting_Module")
    return redirect("Setting_Module")

def SubScriptionType_Delete(request,pk):
    batch = TypeSubsription.objects.get(id = pk).delete()
    messages.success(request,"Subscription Type Deleted")
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
