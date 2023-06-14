from django.urls import path

from .views import LoginViewSet,RegisterUserViewSet,login,logout,register_user
# ---------------------------------------------------------------------------- #
#                                  METHOD URL                                  #
# ---------------------------------------------------------------------------- #

# ----------------------------------- USER ----------------------------------- #

change_password_user = LoginViewSet.as_view({
    'post' : 'change_password_user',
})
# register_user = RegisterUserViewSet.as_view({
#     'post': 'register_user',
# })

urlpatterns = [
    path('login/', login, name = "login_user"),
    path('logout/', logout, name = "logout_user"),
    path('user/change-password/', change_password_user, name = "change_password_user"),
    path('register-user/', register_user, name = "register_user")
]
