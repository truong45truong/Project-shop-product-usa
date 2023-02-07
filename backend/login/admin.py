from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User,Address
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username' , 'email')
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user_id' , 'address_content')
admin.site.register(User,UserAdmin)
admin.site.register(Address,AddressAdmin)
