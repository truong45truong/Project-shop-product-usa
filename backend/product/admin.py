from django.contrib import admin
from .models import Product,Category,Price,Photo_product,Heart
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name')
class PriceAdmin(admin.ModelAdmin):
    list_display = ('id' , 'product_id' , 'price')
class PhotoProduceAdmin(admin.ModelAdmin):
    list_display = ('id' , 'product_id')
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id' , 'parent' , 'name')
class HeartAdmin(admin.ModelAdmin):
    list_display = ('id' , 'user_id' , 'product_id')
admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Price,PriceAdmin)
admin.site.register(Photo_product,PhotoProduceAdmin)
admin.site.register(Heart,HeartAdmin)
# Register your models here.
