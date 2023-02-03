from django.contrib import admin
from .models import New,Photo_new
# Register your models here.
class NewAdmin(admin.ModelAdmin):
    list_display = ('id' , 'slug' , 'product_id')

class PhotoNewAdmin(admin.ModelAdmin):
    list_display = ('id' , 'data' , 'new_id')
# Register your models here.

admin.site.register(New, NewAdmin)
admin.site.register(Photo_new,PhotoNewAdmin)