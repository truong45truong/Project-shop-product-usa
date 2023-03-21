from django.urls import path

from .views import InforUserViewSet,AddressUserViewset , PhoneUserViewSet
# ---------------------------------------------------------------------------- #
#                                  METHOD URL                                  #
# ---------------------------------------------------------------------------- #

# ----------------------------------- USER ----------------------------------- #
get_infor_user = InforUserViewSet.as_view({
    'get' : 'get_infor_user'
})
# ---------------------------------- ADDRESS --------------------------------- #
create_address_user = AddressUserViewset.as_view({
    'post': 'create_address_user',
})
delete_address_user = AddressUserViewset.as_view({
    'post' : 'delete_address_user'
})
update_address_user =  AddressUserViewset.as_view({
    'post' : 'update_address_user' 
})
get_address_user = AddressUserViewset.as_view({
    'get' : 'get_address_user' 
})
# ----------------------------------- PHONE ---------------------------------- #
create_phone_user = PhoneUserViewSet.as_view({
    'post' : 'create_phone_user',
})
delete_phone_user = PhoneUserViewSet.as_view({
    'post' : 'delete_phone_user',
})
update_phone_user = PhoneUserViewSet.as_view({
    'post' : 'update_phone_user',
})
get_phone_user = PhoneUserViewSet.as_view({
    'get' : 'get_phone_user',
})
# ---------------------------------------------------------------------------- #
#                                     URLS                                     #
# ---------------------------------------------------------------------------- #
urlpatterns = [
    path('get-infor-user/', get_infor_user, name = "infor_user"), # api get information user after login with token jwt
    path('address-user/create/', create_address_user, name = "create_address_user"), # api create address of user after login with token jwt
    path('address-user/delete/', delete_address_user, name = "delete_address_user"), # api delete address of user after login with token jwt
    path('address-user/update/',update_address_user, name = "update_address_user"),# api update address of user after login with token jwt
    path('address-user/', get_address_user, name = "get_phone_user"), # api get address of user after login with token jwt
    path('phone-user/create/', create_phone_user, name = "create_phone_user"), # api create phone of user after login with token jwt
    path('phone-user/delete/', delete_phone_user, name = "delete_phone_user"),# api delete phone of user after login with token jwt
    path('phone-user/', get_phone_user, name = "get_phone_user"),# api get phone of user after login with token jwt
    
]
