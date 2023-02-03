from django.contrib import admin
from .models import Product,Category,Price,Photo_product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name')
class PriceAdmin(admin.ModelAdmin):
    list_display = ('id' , 'product_id' , 'price')
class PhotoProduceAdmin(admin.ModelAdmin):
    list_display = ('id' , 'product_id')
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id' , 'parent' , 'name')
admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Price,PriceAdmin)
admin.site.register(Photo_product,PhotoProduceAdmin)
# Register your models here.
