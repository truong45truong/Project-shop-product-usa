from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
from django.conf import settings
import shutil
import os
import uuid
path_root = str(settings.BASE_DIR)+"/media/photos"

# Create your models here.
class User(AbstractUser):
    id       = uuid4()
    photo    = models.ImageField(upload_to =  'media/photos/user', height_field = None, width_field = None, max_length = None)
    name     = models.CharField( max_length=200 )
    password = models.CharField( max_length = 200)
    email    = models.EmailField(max_length = 254)
    token_permission_infor_user = models.UUIDField(default=uuid.uuid4 , unique=True)
    USERNAME_FIELD = 'username'
    
    def __str__(self):
        return  self.email

    def __unicode__(self):
        return self

class Address(models.Model):
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address_content =models.CharField(max_length=500,null=False)
    status = models.BooleanField(null = False)
    user_id=models.ForeignKey(User, on_delete=models.SET_NULL, null=True , related_name='address')
class PhoneUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    status = models.BooleanField(null = False)
    user_id=models.ForeignKey(User, on_delete=models.SET_NULL, null=True , related_name='phones')