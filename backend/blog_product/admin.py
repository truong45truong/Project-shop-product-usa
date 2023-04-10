from django.contrib import admin
from .models import Blog,Comment,Photo_blog,Heart
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id' , 'title')
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id' , 'content' ,'blog_id' , 'user_id','level')
class PhotoBlogAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name' , 'file' ,'blog_id')
class HeartAdmin(admin.ModelAdmin):
    list_display = ('id' , 'user_id' , 'product_id')
admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Photo_blog,PhotoBlogAdmin)
admin.site.register(Heart,HeartAdmin)
