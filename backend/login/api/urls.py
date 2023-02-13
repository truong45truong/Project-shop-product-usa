from django.urls import path

from .views import UserViewSet,RegisterUserViewSet,InforUserViewSet,AddressUserViewset , PhoneUserViewSet

user = UserViewSet.as_view({
    'get' : 'get_user',
    # 'get' : 'get_infor_user'
})
register_user = RegisterUserViewSet.as_view({
    'post': 'post_user',
})
get_infor_user = InforUserViewSet.as_view({
    'get' : 'get_infor_user'
})
address_user = AddressUserViewset.as_view({
    'post': 'create_address_user',
})
update_address_user =  AddressUserViewset.as_view({
    'post' : 'update_address_user' 
})
phone_user = PhoneUserViewSet.as_view({
    'post' : 'create_phone_user',
})
update_phone_user = PhoneUserViewSet.as_view({
    'post' : 'update_phone_user',
})
delete_address_user = AddressUserViewset.as_view({
    'post' : 'delete_address_user'
})
urlpatterns = [
    path('user/', user, name = "user_logs"),
    path('register-user/', register_user, name = "register_user"),
    path('get-infor-user/', get_infor_user, name = "infor_user"),
    path('address-user/', address_user, name = "address_user"),
    path('address-user/delete/', delete_address_user, name = "delete_address_user"),
    path('address-user/update/',update_address_user, name = "update_address_user"),
    path('phone-user/', phone_user, name = "phone_user"),
    
]
