from .serializers import CategorySerializer,ProductSerializer
from .serializers import ProductHeartSerializer,CategoryWithNumberProductSerializer
from .serializers import ProductCheckoutSerializer
from .serializers import ProductDetailSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework import status
from product.models import Category,Product
from login.models import User
from . import query_raw
from .query_raw import HandleProductCategory
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
    
    @action(method="GET", detail=False , url_path='category_tree', url_name='category_tree')
    def get_category_tree(self, request , *args, **kwargs):
        response = Response()
        try:
            category_slug = request.GET['category_slug']
        except Exception as e:
            print("ERROR",e)
            response.data =  { 
                'success' : "get category failure"  , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : "Params input wrong" , 'type' : "GPC-0001" }
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
        try:
            category_main = Category.objects.get(slug= category_slug)
            queryset = Category.objects.filter(tree_id = category_main.tree_id,parent = category_main)
            serializer_category_main = CategorySerializer(category_main,many = False)
            serializer = CategorySerializer(queryset,many = True)
            
            response.data = {
                'categories': serializer.data, 'category_main' : serializer_category_main.data ,
                'error' : {'value' : None , 'type' : False} ,'status' : status.HTTP_200_OK
            }
            return response
        except:
            response.data =  { 
                'success' : "get  category failure"  , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : "Information wrong" , 'type' : "GPC-0001" }
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
class ProductHeartViewSet(viewsets.ViewSet):
    serializer_class = ProductHeartSerializer
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
    @action(method=["GET"],detail=False,url_path="search_product_category",url_name="search_product_category")
    def search_product_category(self, request,*args, **kwargs):
        rawQuerySql = query_raw.QUERY_SQL_SEARCH_ALL_PRODUCT
        rawQuerySqlSearchCategory = query_raw.QUERY_SEARCH_PRODUCT_IN_CATEGORY
        response = Response()
        try:
            
            filter_sort = json.loads(request.GET['filter_sort'])
            key_search = request.GET['key_search']
            categories_slug = request.GET['categories_slug']
            limit_search = request.GET['limit_search']
            filter_limit = json.loads(request.GET['filter_limit'])
            filter_limit_price_up = json.loads(request.GET['up'])
            filter_limit_price_down = json.loads(request.GET['down'])
            
            print('categories_slug',categories_slug)
            handleRawQuerySql = HandleProductCategory(rawQuerySql)    
            if limit_search == 'false':
                handleRawQuerySql.searchProductWithKeyValue(key_search,False)
                handleRawQuerySql.removeLimit()
            else:
                handleRawQuerySql.searchProductWithKeyValue(key_search,limit_search)
            if categories_slug != 'true' :
                handleRawQuerySql.insertTableWithKey('category')
                handleRawQuerySql.addFilterWithKey('category',False,False,categories_slug)
            if filter_sort != False :
                for i in filter_sort:
                    handleRawQuerySql.addOrderByWithKey(i)
            if filter_limit_price_up != False:
                handleRawQuerySql.addFilterWithKey(False,filter_limit_price_up,False,'')
            if filter_limit_price_down != False:
                handleRawQuerySql.addFilterWithKey(False,False,filter_limit_price_down,'')
                
            rawQuerySql = handleRawQuerySql.getQuery()
            print(rawQuerySql)
        except Exception as e:
            print('ERROE',e)
            response.data =  { 
                'success' : "search product with category failure"  , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : "Params input wrong" , 'type' : "SP-0001" }
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
        try:
            queryset = Product.objects.raw(rawQuerySql)
            if len(queryset) == 0:
                response.data = { 
                    'products' : [] , 'number_product_in_category' : [],  
                    'error' : { 'value' : None , 'type' : None }, 'status' : status.HTTP_200_OK
                }
                response.status_code = status.HTTP_200_OK
                return response
            
            queryset = [{**vars(obj), 'status_heart': False } for obj in queryset]
            serializer = ProductSerializer(queryset,many=True)
            
            querysetCategory = Category.objects.raw(rawQuerySqlSearchCategory)
            serializerCategory = CategoryWithNumberProductSerializer(querysetCategory,many = True)
            response.data = { 
                'products' : serializer.data  , 'number_product_in_category' : serializerCategory.data ,
                'error' : { 'value' : None , 'type' : None }, 'status' : status.HTTP_200_OK
            }
            response.status_code = status.HTTP_200_OK
            return response
        except Exception as e:
            print("ERROE",e) 
            response.data =  { 
                'success' : "search product with category failure"  , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : "Params input wrong" , 'type' : "SP-0002" }
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
        
    @action(method=["GET"],detail=False,url_path="search_product",url_name="search_product")
    def search_product(self, request,*args, **kwargs):
        rawQuerySql = query_raw.QUERY_SQL_SEARCH_ALL_PRODUCT
        rawQuerySqlSearchCategory = query_raw.QUERY_SEARCH_PRODUCT_IN_CATEGORY
        response = Response()
        try:
            key_search = request.GET['key_search']
            handleRawQuerySql = HandleProductCategory(rawQuerySql)  
            handleRawQuerySql.searchProductWithKeyValue(key_search,4)
            rawQuerySql = handleRawQuerySql.getQuery()
            
            handleRawQuerySqlCategory = HandleProductCategory(rawQuerySqlSearchCategory)  
            handleRawQuerySqlCategory.searchProductWithKeyValue(key_search,4)
            rawQuerySqlSearchCategory = handleRawQuerySqlCategory.getQuery()
            print('rawQuerySqlSearchCategory',rawQuerySqlSearchCategory)
        except:
            response.data =  { 
                'success' : "search product with category failure"  , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : "Params input wrong" , 'type' : "SP-0001" }
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
        try:
            queryset = Product.objects.raw(rawQuerySql)
            if len(queryset) == 0:
                response.data = { 
                    'products' : [] , 'number_product_in_category' : [],  
                    'error' : { 'value' : None , 'type' : None }, 'status' : status.HTTP_200_OK
                }
                response.status_code = status.HTTP_200_OK
                return response
            
            queryset = [{**vars(obj), 'status_heart': False } for obj in queryset]
            serializer = ProductSerializer(queryset,many=True)
            
            querysetCategory = Category.objects.raw(rawQuerySqlSearchCategory)
            serializerCategory = CategoryWithNumberProductSerializer(querysetCategory,many = True)
            response.data = { 
                'products' : serializer.data  , 'number_product_in_category' : serializerCategory.data ,
                'error' : { 'value' : None , 'type' : None }, 'status' : status.HTTP_200_OK
            }
            response.status_code = status.HTTP_200_OK
            return response
        except Exception as e:
            print("ERROE",e) 
            response.data =  { 
                'success' : "search product with category failure"  , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : "Params input wrong" , 'type' : "SP-0002" }
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response

    @action(method=["GET"],detail=False,url_path="product",url_name="get_product")
    def get_product_category(self, request,*args, **kwargs):
        # ---------------------------------------------------------------------------- #
        #                                   QUERY RAW                                  #
        # ---------------------------------------------------------------------------- #
        rawQuerySql = query_raw.QUERY_SQL_GET_ALL_PRODUCT_WITH_CATEGORY_AND_NOT_USER
        response = Response()
        try: 
            # ---------------------------- check params input ---------------------------- #
            filter_sort = json.loads(request.GET['filter_sort'])
            slug_categories = json.loads(request.GET['slug_categories'])
            filter_limit = json.loads(request.GET['filter_limit'])
            filter_limit_price_up = json.loads(request.GET['up'])
            filter_limit_price_down = json.loads(request.GET['down'])
            category_slug = request.GET['category_slug']
            handleRawQuerySql = HandleProductCategory(rawQuerySql)
            print('slug_categories',slug_categories)
            if filter_sort != False :
                for i in filter_sort:
                    handleRawQuerySql.addOrderByWithKey(i)
            if filter_limit_price_up != False:
                handleRawQuerySql.addFilterWithKey(False,filter_limit_price_up,False,'')
            if filter_limit_price_down != False:
                handleRawQuerySql.addFilterWithKey(False,False,filter_limit_price_down,'')
                
            if slug_categories != False:
                for i in slug_categories:
                    categoryItem = Category.objects.get(slug = i)
                    listCategoryChild = Category.objects.filter(tree_id = categoryItem.tree_id, lft__gte=categoryItem.lft , rght__lte = categoryItem.rght)
                    for child in listCategoryChild:
                        handleRawQuerySql.addFilterWithKey('category',False,False,child.slug)

            rawQuerySql=handleRawQuerySql.getQuery()
            print('rawQuerySql',rawQuerySql)
            category = Category.objects.get(slug = category_slug)
        except Exception as e:
            print(e)
            response.data =  { 
                'success' : "get product with category failure"  , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : "Params input wrong" , 'type' : "GPC-0001" }
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
        try: 
            # ----------------------------- check information ---------------------------- #
            queryset = Product.objects.raw(rawQuerySql,[category.tree_id,category.lft,category.rght])
            queryset = [{**vars(obj), 'status_heart': False } for obj in queryset]
            serializer = ProductSerializer(queryset,many=True)
            response.data = { 'products' : serializer.data  , 'error' : { 'value' : None , 'type' : None }, 'status' : status.HTTP_200_OK}
            response.status_code = status.HTTP_200_OK
            return response
        except:
            response.data = { 
                'products' : "Information wrong"  , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : "wrong information" , 'type' : "GPC-0002" }
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
        
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
                serializer = ProductDetailSerializer(queryset,many=True)
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
                if  ' ' in slug:
                    return Response({"products" : False , "error" : "slug_product Wrong"})
                queryset = Product.objects.raw(rawQuerySqlProductSlug,[slug])
                queryset = [{**vars(obj), 'status_heart': False } for obj in queryset]
                serializer = ProductDetailSerializer(queryset,many=True)
                return Response({"products" : serializer.data })
            else:
                queryset = Product.objects.raw(rawQuerySql,[user_get.id])

        serializer = ProductSerializer(queryset,many=True)
        return Response({"products" : serializer.data})

    @action(method=["GET"],detail=False,url_path="product_list",url_name="get_list_product")
    def get_list_product(self, request,*args, **kwargs):
        rawQuerySql = query_raw.QUERY_SQL_GET_LIST_PRODUCT_DETAIL_NOT_USER
        response = Response()
        try:
            listSlugProduct = request.GET['list_slug_product']
            queryset = Product.objects.raw(rawQuerySql,[listSlugProduct])         

            serializer = ProductCheckoutSerializer(queryset,many=True)
            response.data = {
               'data' : serializer.data
            }
            response.status_code = status.HTTP_200_OK
            return response
        except Exception as e:
            pass     
        return response