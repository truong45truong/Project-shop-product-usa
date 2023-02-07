from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User,Address,PhoneUser
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username' , 'email')
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user_id' , 'address_content')
class PhoneUserAdmin(admin.ModelAdmin):
    list_display = ('phone','name','user_id')
admin.site.register(User,UserAdmin)
admin.site.register(Address,AddressAdmin)
admin.site.register(PhoneUser,PhoneUserAdmin)
