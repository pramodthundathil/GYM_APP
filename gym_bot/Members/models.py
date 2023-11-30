from django.db import models


# Setting classess 

class Batch_DB(models.Model):
    Batch_Name = models.CharField(max_length=255,choices=(("Morning","Morning"),("Evening","Evening"),("Stoped","Stoped")))
    Batch_Status = models.BooleanField(default=True)
    Batch_Time = models.TimeField(auto_now_add=False)

    def __str__(self):
        return (str(self.Batch_Name) + " " + str(self.Batch_Time))



class Subscription_Period(models.Model):
    Period = models.PositiveIntegerField()
    Category = models.CharField(max_length=255, choices=(("Month","Month"),("Year","Year")))

    def __str__(self):
        return (str(self.Period) + " " +str(self.Category))
    

class MemberData(models.Model):
    First_Name = models.CharField(max_length=255)
    Last_Name = models.CharField(max_length=255)
    Date_Of_Birth = models.DateField(auto_now_add=False)
    Gender = models.CharField(max_length=255,choices=(("Male","Male"),("Female","Female"),("Other","Other")))
    Mobile_Number = models.IntegerField()
    Email = models.EmailField()
    Address = models.TextField(max_length=200)
    Medical_History = models.TextField(max_length=2000,null=True,blank=True)
    Registration_Date = models.DateField(auto_now_add=False)
    Photo = models.FileField(upload_to='member_photo')
    Active_status = models.BooleanField(default=True)
    Access_status = models.BooleanField(default=False)

    def __str__(self):
        return self.First_Name + self.Last_Name

class Subscription(models.Model):
    Member = models.ForeignKey(MemberData, on_delete=models.CASCADE,null=True, blank=True)
    Type_Of_Subscription = models.CharField(max_length=255)
    Period_Of_Subscription = models.ForeignKey(Subscription_Period, on_delete=models.SET_NULL,null=True, blank=True)
    Amount = models.IntegerField()
    Subscribed_Date = models.DateField(auto_now_add=False)
    Batch = models.ForeignKey(Batch_DB, on_delete=models.SET_NULL,null=True, blank=True)
    Batch_Status = models.BooleanField(default=True)
    Payment_Status = models.BooleanField(default=False)

class Payment(models.Model):
    Member = models.ForeignKey(MemberData, on_delete=models.CASCADE)
    Subscription_ID = models.ForeignKey(Subscription, on_delete=models.SET_NULL,null=True,blank=True)
    Amount = models.IntegerField()
    Payment_Status = models.BooleanField(default=True)
    Access_status = models.BooleanField(default=False)




