from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from product.models import Category,Product,Heart
from django.db.models import Q,F, Func,Exists ,Subquery , OuterRef ,Count , FilteredRelation
from .serializers import CategorySerializer,ProductSerializer,HeartSerializer,ProductHeartSerializer
from django.core import serializers
import querycount
from login.models import User
import json
import time
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
class ProductHeartViewSet(viewsets.ViewSet):
    serializer_class = HeartSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    @action(method=['GET'], detail = False , url_name= 'product_heart' , url_path='product_heart')
    def get_product_heart(self , request , *args, **kwargs):
        token_permission_infor_user = request.GET['token_permission_infor_user']
        try:
            user = User.objects.get(token_permission_infor_user=token_permission_infor_user)
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
    @action(method=["GET"],detail=False,url_path="product",url_name="get_product")
    def get_product(self, request,*args, **kwargs):

        token_permission_infor_user = request.GET['token_permission_infor_user']
        print('token_permission_infor_user',token_permission_infor_user)
        if token_permission_infor_user == False:
            token_permission_infor_user =''
        try:
            user_get = User.objects.get(token_permission_infor_user = token_permission_infor_user)
        except:
            user_get = False
        print(user_get)
        try:
            slug = request.GET['product_slug']
        except:
            slug = False
        if slug != False and user_get != False :
            rawQuerySqlProductSlug = """
                SELECT  `product_product`.`id`, `product_product`.`slug`, `product_product`.`name`, `product_product`.`sex`, 
                        `product_product`.`description`, `product_photo_product`.`data`, `product_price`.`price`, `product_price`.`sale`, `product_product`.`description`,
                        (SELECT COUNT(U0.`id`) AS `heart_count` FROM `product_heart` U0 WHERE U0.`product_id_id` = `product_product`.`id`) 
                            AS `count_heart` FROM `product_product` 
                INNER JOIN `product_photo_product` ON (`product_product`.`id` = `product_photo_product`.`product_id_id`) 
                INNER JOIN `product_price` ON (`product_product`.`id` = `product_price`.`product_id_id`) 
                WHERE (`product_photo_product`.`id` IS NOT NULL AND `product_price`.`id` IS NOT NULL AND `product_product`.`slug` = %s )
            """
            if  ' ' in slug :
                return Response({"products" : False , "error" : "slug_product Wrong"})
            else:
                queryset = Product.objects.raw(rawQuerySqlProductSlug,[slug])
                queryset = [{**vars(obj), 'status_heart': False } for obj in queryset]
                serializer = ProductSerializer(queryset,many=True)
                return Response({"products" : serializer.data })
                
        rawQuerySql =  """
            SELECT  `product_product`.`id`, `product_product`.`slug`, `product_product`.`name`, `product_product`.`sex`, 
                    `product_product`.`description`, `product_photo_product`.`data`, `product_price`.`price`, `product_price`.`sale`, `product_product`.`description`,
                    EXISTS(SELECT (1) AS `a` FROM `product_heart` U0 
                        WHERE (U0.`user_id_id` = %s AND U0.`product_id_id` = `product_product`.`id`) LIMIT 1) AS `status_heart`, 
                    (SELECT COUNT(U0.`id`) AS `heart_count` FROM `product_heart` U0 WHERE U0.`product_id_id` = `product_product`.`id`) 
                        AS `count_heart` FROM `product_product` 
            INNER JOIN `product_photo_product` ON (`product_product`.`id` = `product_photo_product`.`product_id_id`) 
            INNER JOIN `product_price` ON (`product_product`.`id` = `product_price`.`product_id_id`) 
            WHERE (`product_photo_product`.`id` IS NOT NULL AND `product_price`.`id` IS NOT NULL)
        """
        if(user_get == False ) :
            rawQuerySql =  """
                SELECT  `product_product`.`id`, `product_product`.`slug`, `product_product`.`name`, `product_product`.`sex`, 
                        `product_product`.`description`, `product_photo_product`.`data`, `product_price`.`price`, `product_price`.`sale`, `product_product`.`description` ,
                        (SELECT COUNT(U0.`id`) AS `heart_count` FROM `product_heart` U0 WHERE U0.`product_id_id` = `product_product`.`id`) 
                            AS `count_heart` FROM `product_product` 
                INNER JOIN `product_photo_product` ON (`product_product`.`id` = `product_photo_product`.`product_id_id`) 
                INNER JOIN `product_price` ON (`product_product`.`id` = `product_price`.`product_id_id`) 
                WHERE (`product_photo_product`.`id` IS NOT NULL AND `product_price`.`id` IS NOT NULL)
            """
            queryset = Product.objects.raw(rawQuerySql)
            if slug:
                pass
            else:
                queryset = [{**vars(obj), 'status_heart': False } for obj in queryset]
        else:
            if slug:
                pass
            else:
                queryset = Product.objects.raw(rawQuerySql,[user_get.id])
        # queryset = Product.objects.prefetch_related('prices','photo_products').filter(
        #         prices__isnull = False,photo_products__isnull = False ,).values(
        #         'id','slug','name','sex','description','photo_products__data','prices__price').annotate(status_heart=Exists(
        #         Heart.objects.filter(user_id=user_get.id).filter(product_id =  OuterRef('id')))).annotate(
        #             count_heart =Subquery(Heart.objects.filter(product_id = OuterRef('id')).annotate(heart_count = Count('id')).values('heart_count')[:1]
        #             ))

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
        token_permission_infor_user = data_request['params']['token_permission_infor_user']
        product_slug = data_request['params']['product_slug']
        try:
            product = Product.objects.get(slug = product_slug)
            user = User.objects.get(token_permission_infor_user = token_permission_infor_user)
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