from django.urls import path
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from .views import OrderViewSet,TransportViewSet

get_order = OrderViewSet.as_view({
    'get' : 'get_order',
    'post' : 'add_to_cart'
})
post_remove_order = OrderViewSet.as_view({
    'post' : 'remove_product_in_cart'
})
get_transport = TransportViewSet.as_view({
    'get' : 'get_transport'
})
urlpatterns = [
    path('order/',get_order , name = "order_cart"),
    path('order/remove-product/',post_remove_order , name = "order_cart_remove"),
    path('transport/',get_transport , name="get_transport")
]