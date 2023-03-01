from django.contrib import admin
from .models import Order,Transport,DetailOrder
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name' , 'user_id' ,'status','total_price' ,'cancel')
admin.site.register(Order,OrderAdmin)

class DetailOrderAdmin(admin.ModelAdmin):
    list_display = ('id' , 'status' , 'order_id' , 'product_id' , 'quantity' )
admin.site.register(DetailOrder,DetailOrderAdmin)

class TransportAdmin(admin.ModelAdmin):
    list_display = ('id','slug' , 'name' ,'price')
admin.site.register(Transport,TransportAdmin)
