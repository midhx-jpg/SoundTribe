from django.db import models

# Create your models here.
class registerdb(models.Model):
    First_name=models.CharField(max_length=50,null=True,blank=True)
    Last_name=models.CharField(max_length=50,null=True,blank=True)
    Email=models.EmailField(max_length=50,null=True,blank=True)
    Username=models.CharField(max_length=50,null=True,blank=True)
    Password=models.CharField(max_length=50,null=True,blank=True)
    Password2=models.CharField(max_length=50,null=True,blank=True)

class contactdb(models.Model):
    Name=models.CharField(max_length=50,null=True,blank=True)
    Email=models.CharField(max_length=100,null=True,blank=True)
    Subject=models.CharField(max_length=200,null=True,blank=True)
    Message=models.CharField(max_length=500,null=True)


class checkoutdb(models.Model):
    Username=models.CharField(max_length=50,null=True,blank=True)
    Eventname=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Mobile=models.IntegerField(null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    TotalPrice=models.IntegerField(null=True,blank=True)