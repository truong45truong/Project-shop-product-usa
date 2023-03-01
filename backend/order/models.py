from django.db import models
from product.models import Product
from login.models import User
import uuid 
# Create your models here.

class Transport(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.CharField(null=False,max_length=50)
    name = models.CharField(max_length=50)
    logo = models.ImageField(null=True)
    price = models.FloatField(null=True)

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    datetime = models.DateTimeField()
    receiver = models.CharField(max_length=50,null=True)
    address_receiver = models.CharField(max_length=200,null=True)
    phone_receiver = models.CharField(max_length=10,null=True)
    status = models.BooleanField()
    note = models.CharField(max_length=50,null=True)
    logs = models.TextField(null=True)
    total_price = models.FloatField(null=True)
    cancel = models.BooleanField(null = False)
    request_cancel = models.BooleanField(null = False)
    transport_id = models.ForeignKey(Transport, on_delete=models.SET_NULL, null=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
class DetailOrder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.BooleanField()
    quantity = models.IntegerField()
    order_id = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True,related_name='detail_orders')
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)