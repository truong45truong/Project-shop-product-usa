from django.urls import path

from .views import UserViewSet

user = UserViewSet.as_view({
    'get' : 'get_user',
    'post': 'post_user'
})

urlpatterns = [
    path('user/', user, name = "user_logs")
]
