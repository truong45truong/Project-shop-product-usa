from django.urls import path

from .views import CategoryViewSet,Productviewset

category = CategoryViewSet.as_view({
    'get' : 'get_category'
})
product = Productviewset.as_view({
    'get' : 'get_product',
    #'post' : 'post_product'
})
urlpatterns = [
    path('category/',category, name = "get_category"),
    path('product/',product,name="get_product"),
]
