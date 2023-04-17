from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE,serialize=id)
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True,blank=True)
    email = models.CharField(max_length=200,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __self__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=200,null=True)

    def __self__(self):
        return self.name
        

class Product(models.Model):
    CATEGORY = (('Indoor','Indoor'),('Outdoor','Outdoor'))
    tag = models.ManyToManyField(Tag)
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200,null=True,choices=CATEGORY)
    description = models.CharField(max_length=200,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __self__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),('Out for Delivery','Out for Delivery'),('Delivered','Delivered')
    )
    cust = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL,serialize=id)  # Many(order) to One(customer) relationship : One Customer can have Multiple orders.
    prod = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL,serialize=id)   # Many(order) to One(product) Relationship : One Product can be ordered Multiple times.
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200,null=True,choices=STATUS)   



