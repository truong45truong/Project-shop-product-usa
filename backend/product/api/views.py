from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from product.models import Category,Product
from .serializers import CategorySerializer,ProductSerializer
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    # ---------------------------------------------------------------------------- #
    #                                 GET CATOGORY                                 #
    # ---------------------------------------------------------------------------- #
    
    @action(method="GET", detail=False , url_path='category', url_name='get_category')
    def get_category(self, request , *args, **kwargs):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset,many = True)
        
        return Response({'category': serializer.data,'error' : {'value' : None , 'type' : False}})

class Productviewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()

    @action(method=["GET"],detail=False,url_path="product",url_name="get_product")
    def get_product(self, request,*args, **kwargs):
        slug=request.GET.get('slug')
        if slug :
            queryset = Product.objects.filter(slug=slug)
        else:
            queryset = Product.objects.all()
        user_test = "test"
        serializer = ProductSerializer(queryset,many=True,context={'user_id': 'false'})
        return Response(serializer.data)
    