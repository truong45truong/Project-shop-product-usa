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
get_order_checkout = OrderViewSet.as_view({ 
    'get' : 'get_order_checkout'
})
get_all_order_be_waiting_paid_for_user = OrderViewSet.as_view({ 
    'get' : 'get_all_order_be_waiting_paid_for_user'
})
get_order_be_paymented_for_user = OrderViewSet.as_view({ 
    'get' : 'get_order_be_paymented_for_user'
})
get_product_order = OrderViewSet.as_view({ 
    'get' : 'get_product_order'
})
get_info_order = OrderViewSet.as_view({ 
    'get' : 'get_info_order'
})
create_order_waiting_be_paid = OrderViewSet.as_view({
    'post' : 'create_order_waiting_be_paid'
})
update_receiver = OrderViewSet.as_view({
    'post' : 'update_receiver'
})
update_address_receiver = OrderViewSet.as_view({
    'post' : 'update_address_receiver'
})
update_transport_order = OrderViewSet.as_view({
    'post' : 'update_transport_order'
})
update_voucher_order = OrderViewSet.as_view({ 
    'post' : 'update_voucher_order'
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
update_payment_order = OrderViewSet.as_view({
    'post' : 'update_payment_order'
})
# ---------------------------------------------------------------------------- #
#                                     URLS                                     #
# ---------------------------------------------------------------------------- #
urlpatterns = [
    path('order/',get_order , name = "order_cart"), # get order after login for user
    path('order/infor',get_info_order , name = "get_info_order"), # get order after login for user
    path('order/infor/product',get_product_order , name = "get_product_order"), # get order after login for user
    path('order/today/',get_order_today , name = "order_cart"), # get order today after login for user
    path('order/checkout/',get_order_checkout , name = "get_order_checkout"), # get order checkout
    path('order/paid/',get_all_order_be_waiting_paid_for_user , name = "get_all_order_be_waiting_paid_for_user"), # get order after login for user
    path('order/paid/paymented',get_order_be_paymented_for_user , name = "get_order_be_paymented_for_user"), # get order after login for user
    path('order/paid/create',create_order_waiting_be_paid , name = "create_order_waiting_be_paid"), # create order waiting be paid
    path('order/payment/success',update_payment_order , name = "update_payment_order"), # create order waiting be paid
    path('order/paid/voucher/update/',update_voucher_order , name = "update_voucher_order"), # create order waiting be paid
    path('order/update/phone/',update_receiver , name = "update_receiver"), # create order waiting be paid
    path('order/update/address/',update_address_receiver , name = "update_address_receiver"), # create order waiting be paid
    path('order/update/transport/',update_transport_order , name = "update_transport_order"), # create order waiting be paid
    path('order/remove-product/',post_remove_order , name = "order_cart_remove"), # remove product in order for user
    path('order/change-order-today/',change_order_today , name = "change_order_today"), # change order today for user
    path('order/change-quantity-product/',change_quantity_product_in_cart , name = "change_quantity_product_in_cart"), # change order today for user
    path('transport/',get_transport , name="get_transport") # get transport after select product in cart or payment
]