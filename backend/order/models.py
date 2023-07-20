from django.db import models
from product.models import Product
from flashSaleProduct.models import Voucher
from login.models import User
import uuid 
from PIL import Image,Image,ImageDraw
from django.core.files import File
from io import BytesIO
import secrets
import os
import qrcode

# Create your models here.
class Qrcode(models.Model):
    id = models.BigAutoField(primary_key=True)
    qrcode  = models.ImageField(null=False,blank=True,upload_to='static/qrcode')
    name=models.CharField(max_length=2000)
    token = models.CharField(max_length=100,null=False,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    feedback = models.CharField(max_length=1000)
    def __str__(self):
      return self.name
    def save(self, *args , **kwargs):
      token = secrets.token_hex(16)
      url = "127.0.0.1/order/qrcode/"+token
      self.token = token
      qr_image = qrcode.make(url)
      qr_offset = Image.new('RGB',(415,415),'white')
      qr_offset.paste(qr_image)
      files_name = f'media/photos/qr_code/{self.name}-{self.id}qr.png'
      stream = BytesIO()
      qr_offset.save(stream,'PNG')
      self.qrcode.save(files_name,File(stream),save=False)
      qr_offset.close()
      super().save(*args,**kwargs)
class Transport(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.CharField(null=False,max_length=50)
    name = models.CharField(max_length=50)
    logo = models.ImageField(null=True)
    price = models.FloatField(null=True)

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=500)
    datetime = models.DateTimeField()
    receiver = models.CharField(max_length=50,null=True)
    address_receiver = models.CharField(max_length=200,null=True)
    phone_receiver = models.CharField(max_length=10,null=True)
    status = models.BooleanField(default = False)
    is_payment = models.BooleanField()
    note = models.CharField(max_length=50,null=True)
    logs = models.TextField(null=True)
    total_price = models.FloatField(null=True)
    cancel = models.BooleanField(null = False)
    request_cancel = models.BooleanField(null = False)
    transport_id = models.ForeignKey(Transport, on_delete=models.SET_NULL, null=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    voucher_id = models.ForeignKey(Voucher, on_delete=models.SET_NULL, null=True)
    confirm = models.BooleanField(null = False, default = False)
    qr_code_id = models.ForeignKey(Qrcode, on_delete=models.SET_NULL, null=True)
class DetailOrder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.BooleanField()
    quantity = models.IntegerField()
    order_id = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True,related_name='detail_orders')
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.BooleanField()
    order_id = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True,related_name='payments')
    total_price = models.FloatField(null=True)
    cod = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
