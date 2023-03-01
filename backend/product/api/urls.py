from django.urls import path

from .views import CategoryViewSet,Productviewset,HeartViewSet,ProductHeartViewSet

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
urlpatterns = [
    path('category/',category, name = "get_category"),
    path('product/',product,name="get_product"),
    path('heart/post/' , heart , name = "post_heart"),
    path('product-heart/',product_heart , name = "get_product_heart")
]
