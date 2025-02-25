from django.db import models

# Create your models here.
class categoryDB(models.Model):
    cat_name = models.CharField(max_length=100,null=True,blank=True)
    cat_des = models.CharField(max_length=100, null=True, blank=True)
    cat_image = models.ImageField(upload_to="Category_Image", null=True, blank=True)
class productDB(models.Model):
    cat_name = models.CharField(max_length=100,null=True,blank=True)
    pro_name = models.CharField(max_length=100, null=True, blank=True)
    pro_price = models.IntegerField(null=True, blank=True)
    pro_des = models.CharField(max_length=100, null=True, blank=True)
    pro_quantity = models.CharField(max_length=100, null=True, blank=True)
    pro_image = models.ImageField(upload_to="Product_Image", null=True, blank=True)

