from django.db import models
from product.models import Product
import uuid
# Create your models here.
class New (models.Model):
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.CharField(null=False,max_length=50)
    name=models.CharField(max_length=50,null=False)
    description=models.TextField(null=True)
    product_id = models.ForeignKey(Product, on_delete= models.SET_NULL, null = True, blank= True, related_name='news')
    
    def __str__(self) -> str:
        return str(self.slug)
class Photo_new(models.Model):
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data=models.ImageField(upload_to='media/photos/')
    new_id = models.ForeignKey(New, on_delete=models.SET_NULL, null=True,blank=True,related_name='photo_news')

    fields = ['data']