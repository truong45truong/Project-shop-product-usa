from venv import create
from django.db import models
from uuid import uuid4
from mptt.models import MPTTModel,TreeForeignKey
from login.models import User
from django.conf import settings
from PIL import Image
import os 
import uuid
from io import BytesIO
from product.models import Product
path_upload_image = str(settings.BASE_DIR)+"/media/photos"
path_upload_video = str(settings.BASE_DIR)+"/media/videos"

# Create your models here.

class Blog(models.Model):
    id=uuid4()
    title = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField()
    user_id = models.ForeignKey(User, related_name='blogs', on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now=True, auto_now_add=False)
    product_id = models.ForeignKey(Product, related_name='products', null= True, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)

    def __unicode__(self):
        return str(self.id)
        
        
class Photo_blog(models.Model):
    id=uuid4()
    name = models.CharField(max_length=200, blank=True, null=True)
    file = models.ImageField( upload_to ='media/photos/blogs', height_field=None, width_field=None, max_length=1000)
    blog_id = models.ForeignKey(Blog, related_name='photo_blogs', on_delete=models.CASCADE)
    type = models.BooleanField()
    def __str__(self):
        return str(self.id)

    def __unicode__(self):
        return str(self.id)
    def save(self, *args , **kwargs):
        try :
            file_ext = str(self.file).split('.')[-1]
            image = Image.open(self.file)
            width, height = image.size
            new_width = 700
            new_height = int(height * (new_width / width))
            new_image = image.resize((new_width, new_height))
            bio = BytesIO()
            new_image.save(bio, format='jpeg')
            name_file = "blog-" + str(uuid.uuid4())+"." + file_ext
            with open( os.path.join(path_upload_image, "blogs" , name_file), 'wb+') as decoded_image_file:
                decoded_image_file.write(bio.getvalue())
                self.file = 'media/photos/blogs/' + name_file
        except:
            pass
        return super().save(*args,**kwargs)

class Comment(MPTTModel):
    id = uuid4()
    parent = TreeForeignKey('self', on_delete = models.CASCADE, null = True, blank = True, related_name = 'children')
    content = models.TextField()
    heart = models.IntegerField()
    blog_id = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now=True, auto_now_add=False)
    user_id = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    user_profile = models.TextField()
    user_email = models.CharField(max_length=200)
    def __str__(self):
        return str(self.content)

    def __unicode__(self):
        return str(self.id)
class Heart( models.Model):
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True,related_name='hearts')
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True,blank=True,related_name='hearts')
    blog_id = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True,blank=True,related_name='hearts')
    comment_id = models.ForeignKey(Comment, on_delete=models.SET_NULL, null=True,blank=True,related_name='hearts')