from django.contrib import admin

from .models import DetailFlashSale,FlashSale,Voucher,DetailVoucher

class FlashSaleAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name' , 'note')
admin.site.register(FlashSale,FlashSaleAdmin)

class DetailFlashSaleAdmin(admin.ModelAdmin):
    list_display = ('flash_sale_id' , 'product_id' , 'datetime_created' , 'datetime_finished' , 'status' )
admin.site.register(DetailFlashSale,DetailFlashSaleAdmin)

class VoucherAdmin(admin.ModelAdmin):
    list_display = ('id','detail' , 'sale' ,'description' , 'quantity')
admin.site.register(Voucher,VoucherAdmin)

class DetailVoucherAdmin(admin.ModelAdmin):
    list_display = ( 'id' , 'product_id' , 'voucher_id' )
admin.site.register(DetailVoucher, DetailVoucherAdmin)