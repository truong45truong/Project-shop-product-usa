from django.urls import path
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from .views import OrderViewSet,TransportViewSet
# ---------------------------------------------------------------------------- #
#                                  METHOD URLS                                 #
# ---------------------------------------------------------------------------- #
get_order = OrderViewSet.as_view({
    'get' : 'get_order',
    'post' : 'add_to_cart'
})
get_order_today = OrderViewSet.as_view({
    'get' : 'get_order_today'
})
post_remove_order = OrderViewSet.as_view({
    'post' : 'remove_product_in_cart'
})
get_transport = TransportViewSet.as_view({
    'get' : 'get_transport'
})
change_order_today = OrderViewSet.as_view({
    'post' : 'change_order_today'
})
change_quantity_product_in_cart =  OrderViewSet.as_view({
    'post' : 'change_quantity_product_in_cart'
})
# ---------------------------------------------------------------------------- #
#                                     URLS                                     #
# ---------------------------------------------------------------------------- #
urlpatterns = [
    path('order/',get_order , name = "order_cart"), # get order after login for user
    path('order/today/',get_order_today , name = "order_cart"), # get order today after login for user
    path('order/remove-product/',post_remove_order , name = "order_cart_remove"), # remove product in order for user
    path('order/change-order-today/',change_order_today , name = "change_order_today"), # change order today for user
    path('order/change-quantity-product/',change_quantity_product_in_cart , name = "change_quantity_product_in_cart"), # change order today for user
    path('transport/',get_transport , name="get_transport") # get transport after select product in cart or payment
]