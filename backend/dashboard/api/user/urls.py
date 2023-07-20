from django.urls import path

from .views import getAllUserPage,DelUsers , searchUserAdmin


# ---------------------------------------------------------------------------- #
#                                     URLS                                     #
# ---------------------------------------------------------------------------- #
urlpatterns = [
    path('get-all-user',getAllUserPage, name = "get_infor_admin"), # get categories
    path('del-user',DelUsers, name = "del_user_admin"), # get categories
    path('search-user',searchUserAdmin, name = "search_user_admin"), # get categories
]
