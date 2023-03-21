from django.urls import path

from .views import CategoryViewSet,Productviewset,HeartViewSet,ProductHeartViewSet
# ---------------------------------------------------------------------------- #
#                                  METHOD URL                                  #
# ---------------------------------------------------------------------------- #
category = CategoryViewSet.as_view({
    'get' : 'get_category'
})
product = Productviewset.as_view({
    'get' : 'get_product',
    #'post' : 'post_product'
})
heart = HeartViewSet.as_view({
    'post' : 'post_heart'
})
product_heart = ProductHeartViewSet.as_view({
    'get' : 'get_product_heart'
})
# ---------------------------------------------------------------------------- #
#                                     URLS                                     #
# ---------------------------------------------------------------------------- #
urlpatterns = [
    path('category/',category, name = "get_category"), # get categories 
    path('product/',product,name="get_product"), # get all products or product with product_slug
    path('heart/post/' , heart , name = "post_heart"), # like or dislike product
    path('product-heart/',product_heart , name = "get_product_heart") # get product liked
]
