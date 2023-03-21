from .serializers import CategorySerializer,ProductSerializer,HeartSerializer,ProductHeartSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from product.models import Category,Product,Heart
from login.models import User
from . import query_raw
import json
class CategoryViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
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
class ProductHeartViewSet(viewsets.ViewSet):
    serializer_class = HeartSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    @action(method=['GET'], detail = False , url_name= 'product_heart' , url_path='product_heart')
    def get_product_heart(self , request , *args, **kwargs):
        jwtToken = request.COOKIES.get('refresh_token')
        refresh_token = RefreshToken(jwtToken)
        decoded_token = refresh_token.payload
        try:
            user = User.objects.get(id = decoded_token['user_id'])
            queryset = Product.objects.prefetch_related('prices','photo_products','hearts').filter(
                            prices__isnull = False,photo_products__isnull = False , hearts__user_id = user
                            ).values(
                                'name','prices__price','photo_products__data','slug' , 'prices__sale'
                            )
            serializer = ProductHeartSerializer(queryset,many=True)
            return Response({'data' : serializer.data})
        except Exception as e:
            print(e)
            return Response({'error' : e})
        
    
class Productviewset(viewsets.ViewSet):
    authentication_classes = []
    permission_classes = []
    @action(method=["GET"],detail=False,url_path="product",url_name="get_product")
    
    def get_product(self, request,*args, **kwargs):
        # ---------------------------------------------------------------------------- #
        #                                   QUERY RAW                                  #
        # ---------------------------------------------------------------------------- #
        rawQuerySqlProductSlug = query_raw.QUERY_SQL_GET_PRODUCT_DETAIL_NOT_USER
        rawQuerySql =  query_raw.QUERY_SQL_GET_ALL_PRODUCT_FOR_USER
        # ------------------------------------ END ----------------------------------- #

        try:
            jwtToken = request.COOKIES.get('refresh_token')
            refresh_token = RefreshToken(jwtToken)
            decoded_token = refresh_token.payload
            user_get = User.objects.get(id = decoded_token['user_id'])
        except:
            user_get = False
        try:
            slug = request.GET['product_slug']
        except:
            slug = False
        if slug != False and user_get != False :
            if  ' ' in slug :
                return Response({"products" : False , "error" : "slug_product Wrong"})
            else:
                queryset = Product.objects.raw(rawQuerySqlProductSlug,[slug])
                queryset = [{**vars(obj), 'status_heart': False } for obj in queryset]
                serializer = ProductSerializer(queryset,many=True)
                return Response({"products" : serializer.data })
                
        if(user_get == False ) :
            rawQuerySql =  query_raw.QUERY_SQL_GET_ALL_PRODUCT_NOT_USER
            queryset = Product.objects.raw(rawQuerySql)
            if slug:
                if  ' ' in slug:
                    return Response({"products" : False , "error" : "slug_product Wrong"})
                queryset = Product.objects.raw(rawQuerySqlProductSlug,[slug])
                queryset = [{**vars(obj), 'status_heart': False } for obj in queryset]
            else:
                queryset = [{**vars(obj), 'status_heart': False } for obj in queryset]
        else:
            if slug:
                queryset = Product.objects.raw(rawQuerySqlProductSlug,[slug])
                queryset = [{**vars(obj), 'status_heart': False } for obj in queryset]
            else:
                queryset = Product.objects.raw(rawQuerySql,[user_get.id])

        serializer = ProductSerializer(queryset,many=True,context={'user_id': user_get})
        return Response({"products" : serializer.data})
            
class HeartViewSet(viewsets.ModelViewSet):
    queryset = Heart.objects.all()
    serializer_class = HeartSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    @action(method=["POST"],detail=False,url_path="heart",url_name="post_heart")
    def post_heart(self, request,*args, **kwargs):
        data_request= json.loads(request.body.decode('utf-8'))
        jwtToken = request.COOKIES.get('refresh_token')
        refresh_token = RefreshToken(jwtToken)
        decoded_token = refresh_token.payload
        product_slug = data_request['params']['product_slug']
        try:
            product = Product.objects.get(slug = product_slug)
            user = User.objects.get(id  = decoded_token['user_id'])
            heart_product = Heart.objects.filter(product_id = product.id , user_id = user.id)
            if len(heart_product) == 1 :
                Heart.objects.get(id = heart_product[0].id).delete()
            else :
                heart = Heart.objects.create(user_id = user , product_id = product)
                heart.save()
            return Response({ 'status' : True})
        except Exception as e:
            print(e)
        return Response({ 'status' : False})