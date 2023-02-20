from django.db import models
from product.models import Product
import uuid
# Create your models here.
class FlashSale(models.Model):
    id = models.UUIDField(primary_key = True , default = uuid.uuid4 , editable=False )
    name = models.CharField(max_length= 200 , blank = True)
    note = models.TextField()
    
class DetailFlashSale(models.Model):
    id = models.UUIDField(primary_key = True , default = uuid.uuid4 , editable=False )
    flash_sale_id = models.ForeignKey(FlashSale, on_delete=models.SET_NULL, null=True , related_name='detail_flash_sale')
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True , related_name='detail_flash_sale')
    datetime_created = models.DateTimeField(auto_now = True, auto_now_add=False,blank = True, null = False)
    datetime_finished = models.DateTimeField(blank = True,null = False)
    status = models.BooleanField(blank = True, null = False)