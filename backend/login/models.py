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
    phone    = models.CharField(max_length=12,blank=True)
    token_permission_infor_user = models.UUIDField(default=uuid.uuid4 , unique=True)
    USERNAME_FIELD = 'username'
    
    def __str__(self):
        return  self.email

    def __unicode__(self):
        return self
    # def save(self, *args , **kwargs):
    #     def handleImageUpload(file_upload):
    #         nameFile = str(uuid4()) + '.' + file_upload.split('.')[-1]
    #         print("handle",file_upload,nameFile)
    #         old_name = path_root + '/user/' + file_upload
    #         new_name = path_root + '/user/' +  nameFile
    #         os.rename(old_name, new_name)
    #         return nameFile
    #     print("create user running",self.photo)
    #     try :
    #         if self.photo == None:
    #            self.photo = settings.DOMAIN + "media/photos/user/avt.png"
    #         else:
    #             print(self.photo)
    #             self.photo = settings.DOMAIN + "media/photos/user/" + str(self.photo)
    #             print(self.photo)
    #     except Exception as e:
    #         print(e)

    #     return super().save(*args,**kwargs)
class Address(models.Model):
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address_content =models.CharField(max_length=500,null=False)
    status = models.BooleanField(null = False)
    user_id=models.ForeignKey(User, on_delete=models.SET_NULL, null=True , related_name='address')
class PhoneUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    user_id=models.ForeignKey(User, on_delete=models.SET_NULL, null=True , related_name='phones')