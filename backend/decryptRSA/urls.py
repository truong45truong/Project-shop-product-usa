from django.urls import path

from .views import get_public_key_rsa



urlpatterns = [
    path('token-decryt-rsa/', get_public_key_rsa, name = "token_decryt_rsa"), #get public key and check public key 
]
