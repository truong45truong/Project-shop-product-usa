from django.urls import path

from .views import getAllOrderAdmin , getAllOrderRequestAdmin , getAllOrderConfirmAdmin
from .views import confirmOrderAdmin , cancelOrderAdmin , getAllOrderPaymentedAdmin
# ---------------------------------------------------------------------------- #
#                                     URLS                                     #
# ---------------------------------------------------------------------------- #
urlpatterns = [
    path('get-all-order',getAllOrderAdmin, name = "get_all_order_admin"),
    path('get-all-order-request',getAllOrderRequestAdmin, name = "get_all_order_request_admin"),
    path('get-all-order-confirm',getAllOrderConfirmAdmin, name = "get_all_order_confirm_admin"),
    path('get-all-order-paymented',getAllOrderPaymentedAdmin, name = "get_all_order_paymented_admin"),
    path('confirm-order',confirmOrderAdmin, name = "confirm_order_admin"),
    path('cancel-order',cancelOrderAdmin, name = "cancel_order_admin"),
]
