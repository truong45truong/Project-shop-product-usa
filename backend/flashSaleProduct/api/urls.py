from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import VoucherViewSet

get_order = VoucherViewSet.as_view({
    'get' : 'get_voucher',
})

urlpatterns = [
    path('voucher/',get_order , name = "order_cart"),
]