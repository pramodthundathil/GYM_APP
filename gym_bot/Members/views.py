from django.shortcuts import render, redirect
from .forms import MemberAddForm, SubscriptionAddForm, PaymentForm
from .models import MemberData, Subscription, Payment
from django.contrib import messages


# member configarations and subscription add on same method 
# one forign key field is prent in subscription Meber forign key, priod forign key, Batch forgin key
#
def Member(request):
    form = MemberAddForm()
    sub_form = SubscriptionAddForm()
    Trainee = MemberData.objects.all()[:8][::-1]
    subscribers = Subscription.objects.all()[:8][::-1]

    if request.method == "POST":
        form = MemberAddForm(request.POST,request.FILES)
        sub_form = SubscriptionAddForm(request.POST)
        if form.is_valid():
            member = form.save()
            member.save()
        else:
            messages.error(request,"Entered Personal Data is Not Validated Please try agine")
            return redirect("Member")
        if sub_form.is_valid():
            sub_data = sub_form.save()
            sub_data.save()
            sub_data.Member = member
            sub_data.save()
            messages.success(request,"New Member Was Added Successfully Please Make Payent details..")
            return redirect("Member")  
        else:    
            messages.error(request,"Entered Subscription Data is Not Validated Please try agine")
            return redirect("Member")   

    context = {

        "form":form,
        "sub_form":sub_form,
        "Trainee":Trainee,
        "subscribers":subscribers

        }
    return render(request,"members.html",context)

def MembersSingleView(request,pk):
    member = MemberData.objects.get(id = pk)
    subscription = Subscription.objects.get(Member = member)

    context = {
        "member":member,
        "subscription":subscription,

    }
    return render(request,"memberssingleview.html",context)

def DeleteMember(request,pk):
    member = MemberData.objects.get(id=pk)
    member.Photo.delete()
    member.delete()
    messages.error(request,"Member Data Deleted Success")
    return redirect("Member")

def MemberAccess(request):
    return render(request,"memberaccess.html")

def Payments(request):
    form = PaymentForm()
    pay = Payment.objects.all()[::-1]
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save()
            sub = Subscription.objects.get(Member = payment.Member)
            payment.Subscription_ID = sub
            payment.Amount = sub.Amount
            payment.Payment_Status = True 
            payment.Access_status = True
            payment.save()
            sub.Payment_Status = True
            sub.save()
            user = payment.Member
            user.Access_status = True
            user.save()
            messages.info(request,"Payment Updated for member {}".format(user))
            return redirect("Payments")
        else:
            messages.info(request,"Payment Not Updated")
            return redirect("Payments")


    context = {
        "form":form,
        "pay":pay
    }
    return render(request, "payments.html",context)

def DeletePayment(request,pk):
    Pay = Payment.objects.get(id = pk).delete()
    messages.info(request,"Payment Deleted")
    return redirect("Payments")


