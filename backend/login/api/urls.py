from django.urls import path

from .views import UserViewSet,RegisterUserViewSet,InforUserViewSet

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
urlpatterns = [
    path('user/', user, name = "user_logs"),
    path('register-user/', register_user, name = "register_user"),
    path('get-infor-user/', get_infor_user, name = "infor_user"),
]
