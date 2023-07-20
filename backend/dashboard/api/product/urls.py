from django.urls import path

from .views import getAllProductAdmin,searchProductAdmin,DelProduct,createProductAdmin
from .views import getDetailProductAdmin,uploadProductAdmin , getAllVoucherAdmin
from .views import searchVoucherAdmin , delVoucherAdmin , createVoucherAdmin
from .views import getAllVoucherNoProductAdmin , addProductVoucherAdmin
from .views import getDetailVoucherAdmin , delProductVoucherAdmin

from .views import searchFlashSaleAdmin , delFlashSaleAdmin , createFlashSaleAdmin
from .views import getAllFlashSaleNoProductAdmin , addProductFlashSaleAdmin
from .views import getDetailFlashSaleAdmin , delProductFlashSaleAdmin , getAllFlashSaleAdmin
# ---------------------------------------------------------------------------- #
#                                     URLS                                     #
# ---------------------------------------------------------------------------- #
urlpatterns = [
    # ---------------------------------- product --------------------------------- #
    path('get-all-product',getAllProductAdmin, name = "get_all_product_admin"), 
    path('search-all-product',searchProductAdmin, name = "search_all_product_admin"), 
    path('del-product',DelProduct, name = "delete_product_admin"), 
    path('create-product',createProductAdmin, name = "create_product_admin"), 
    path('detail-product',getDetailProductAdmin, name = "detail_product_admin"),
    path('update-product',uploadProductAdmin, name = "update_product_admin"), 
    # ---------------------------------- voucher --------------------------------- #
    path('get-all-voucher',getAllVoucherAdmin, name = "get_all_product_admin"), 
    path('search-all-voucher',searchVoucherAdmin, name = "search_all_product_admin"), 
    path('del-voucher',delVoucherAdmin, name = "delete_voucher_admin"), 
    path('create-voucher',createVoucherAdmin, name = "delete_voucher_admin"),
    path('get-voucher-no-product',getAllVoucherNoProductAdmin, name = "get_voucher_admin_no_product"),
    path('add-product-voucher',addProductVoucherAdmin, name = "add_product_voucher_admin"),
    path('detail-voucher',getDetailVoucherAdmin, name = "detail_voucher_admin"),
    path('del-product-voucher',delProductVoucherAdmin, name = "detail_voucher_admin"),
    # -------------------------------- flash sale -------------------------------- #
    path('get-all-flash-sale',getAllFlashSaleAdmin, name = "get_all_product_admin"), 
    path('search-all-flash-sale',searchFlashSaleAdmin, name = "search_all_product_admin"), 
    path('del-flash-sale',delFlashSaleAdmin, name = "delete_flash_sale_admin"), 
    path('create-flash-sale',createFlashSaleAdmin, name = "delete_flash_sale_admin"),
    path('get-flash-sale-no-product',getAllFlashSaleNoProductAdmin, name = "get_flash_sale_admin_no_product"),
    path('add-product-flash-sale',addProductFlashSaleAdmin, name = "add_product_flash_sale_admin"),
    path('detail-flash-sale',getDetailFlashSaleAdmin, name = "detail_flash_sale_admin"),
    path('del-product-flash-sale',delProductFlashSaleAdmin, name = "detail_flash_sale_admin"),
]
