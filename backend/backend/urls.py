"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from django.conf import settings
urlpatterns = [
    path('',include('login.urls')),
    path('admin/', admin.site.urls),
    path('api/',include('product.api.urls')),
    path('api/',include('login.api.urls')),
    path('api/',include('user.api.urls')),
    path('api/',include('new.api.urls')),
    path('api/',include('order.api.urls')),
    path('api/',include('flashSaleProduct.api.urls')),
    path('api/', include('JWT.urls')),
    path('api/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/',include('decryptRSA.urls'))
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)