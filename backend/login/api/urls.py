from django.urls import path

from .views import UserViewSet,RegisterUserViewSet,InforUserViewSet,AddressUserViewset , PhoneUserViewSet

# ---------------------------------------------------------------------------- #
#                                  METHOD URL                                  #
# ---------------------------------------------------------------------------- #

# ----------------------------------- USER ----------------------------------- #
user = UserViewSet.as_view({
    'get' : 'get_user',
    # 'get' : 'get_infor_user'
})
change_password_user = UserViewSet.as_view({
    'post' : 'change_password_user',
})
register_user = RegisterUserViewSet.as_view({
    'post': 'post_user',
})
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

urlpatterns = [
    path('user/', user, name = "user_logs"),
    path('user/change-password/', change_password_user, name = "change_password_user"),
    path('register-user/', register_user, name = "register_user"),
    path('get-infor-user/', get_infor_user, name = "infor_user"),
    path('address-user/create/', create_address_user, name = "create_address_user"),
    path('address-user/delete/', delete_address_user, name = "delete_address_user"),
    path('address-user/update/',update_address_user, name = "update_address_user"),
    path('phone-user/create/', create_phone_user, name = "create_phone_user"),
    path('phone-user/delete/', delete_phone_user, name = "delete_phone_user"),
]
