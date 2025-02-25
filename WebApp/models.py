from django.db import models

# Create your models here.
class contactDB(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    phone = models.IntegerField(null=True, blank=True)
    subject = models.CharField(max_length=600, null=True, blank=True)
    message = models.CharField(max_length=500, null=True, blank=True)
class registerDB(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    pwd = models.CharField(max_length=100, null=True, blank=True)
    confirmpwd = models.CharField(max_length=100, null=True, blank=True)

class cartDB(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    pro_name=models.CharField(max_length=100,null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    total_price=models.IntegerField(null=True,blank=True)
    pro_image=models.ImageField(upload_to="cart_images",null=True,blank=True)

class orderDB(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email= models.EmailField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    state=models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    pincode = models.IntegerField(null=True, blank=True)
    message = models.CharField(max_length=500, null=True, blank=True)
    total_price = models.IntegerField(null=True, blank=True)

