from django.urls import path
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from .views import updateHistoryAction , getProductRecommend
# ---------------------------------------------------------------------------- #
#                                  METHOD URLS                                 #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
#                                     URLS                                     #
# ---------------------------------------------------------------------------- #
urlpatterns = [
    path('api/update-action-history',updateHistoryAction , name = "history_action"),
    path('api/product-recommendation',getProductRecommend , name = "product_recommendation"),
]