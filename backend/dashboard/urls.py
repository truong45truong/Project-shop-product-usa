from django.urls import path,include


urlpatterns = [
    path('admin/',include('dashboard.api.login.urls')),
    path('admin/',include('dashboard.api.user.urls')),
    path('admin/',include('dashboard.api.product.urls')),
    path('admin/',include('dashboard.api.order.urls')),

]