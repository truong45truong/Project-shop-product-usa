from django.db import models
import uuid
from mptt.models import MPTTModel, TreeForeignKey
from login.models import User
# Create your models here.

class Category(MPTTModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.CharField(null=False,max_length=50,unique=True)
    name=models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name
    
class Product(models.Model):
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.CharField(null=False,max_length=50)
    name=models.CharField(max_length=50,null=False)
    sex = models.IntegerField(null=True)
    description=models.TextField(null=True)
    category_id=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Price(models.Model):
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price=models.FloatField(null=True)
    sale=models.FloatField(null=True)
    status=models.BooleanField(null=True)
    datetime_create=models.DateTimeField(null=True)
    price_total=models.FloatField(null=True)
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True,blank=True,related_name='prices')

    def __str__(self):
        return self.product_id.name
class Photo_product(models.Model):
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data=models.ImageField(upload_to='media/photos/')
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True,blank=True,related_name='photo_products')

    fields = ['data']
class Heart( models.Model):
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True,related_name='hearts')
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True,blank=True,related_name='hearts')
    
