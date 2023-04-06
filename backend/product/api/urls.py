from django.urls import path

from .views import CategoryViewSet,Productviewset,HeartViewSet,ProductHeartViewSet
# ---------------------------------------------------------------------------- #
#                                  METHOD URL                                  #
# ---------------------------------------------------------------------------- #
category = CategoryViewSet.as_view({
    'get' : 'get_category'
})
category_tree = CategoryViewSet.as_view({
    'get' : 'get_category_tree'
})
product = Productviewset.as_view({
    'get' : 'get_product',
    #'post' : 'post_product'
})
search_product = Productviewset.as_view({
    'get' : 'search_product',
    #'post' : 'post_product'
})
search_product_category = Productviewset.as_view({
    'get' : 'search_product_category',
    #'post' : 'post_product'
})
product_catogory = Productviewset.as_view({
    'get' : 'get_product_category',
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
    path('category-tree/',category_tree, name = "category_tree"), # get categories  
    path('product/',product,name="get_product"), # get all products or product with product_slug
    path('product/search/',search_product,name="search_product"),
    path('product/search-product-category/',search_product_category,name="search_product_category"),
    path('product-category/',product_catogory,name="get_product_category"),# get all products or product with category_slug
    path('heart/post/' , heart , name = "post_heart"), # like or dislike product
    path('product-heart/',product_heart , name = "get_product_heart") # get product liked
]
