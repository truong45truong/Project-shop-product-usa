from rest_framework.decorators import api_view,action,permission_classes,authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from product.models import Product , Category
from django.template.defaultfilters import slugify
import json
from login.models import User
from .models import HistoryAction
from . import query_raw
from .serializers import ProductSerializer
from . import data_processing
import random
@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def updateHistoryAction(request):
    response = Response()
    def notFound():
        response.data = {
            "success" : False , 'error' : {
                'type' : "CGIA-001" , 'value' : "Failed to Login"
            } , 
            'status' : status.HTTP_404_NOT_FOUND
        }
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
    def updateActionHistory(products_selected,user):
        def checkSlugProduct(slug,products_array):
            for i in products_array:
                print(i,slug, i ==slug)
                if i == slug :
                    return True
            return False
        try:
            historyAction = HistoryAction.objects.get(user_id = user)
            products_array = eval(historyAction.list_selected_products)
            if len(products_array) > 5 :
                if checkSlugProduct(products_selected[0],products_array) == False:
                    products_array = (lambda x: x[1:] + x[:1])(products_array)
                    products_array.append(products_selected[0])
            else :
                if checkSlugProduct(products_selected[0],products_array) == False:
                    products_array.append(products_selected[0])
            historyAction.list_selected_products = str(products_array)
            historyAction.save()
        except:
            historyAction = HistoryAction.objects.create(
                user_id = user ,
                list_selected_products  = str(products_selected)
            )
        response.data = {
            "success" : True ,
            'status' : status.HTTP_200_OK
        }
        response.status_code = status.HTTP_200_OK
        return response
    try:
        jwtToken = request.COOKIES.get('refresh_token')
        refresh_token = RefreshToken(jwtToken)
        decoded_token = refresh_token.payload
        data_request= json.loads(request.body.decode('utf-8'))
        products_selected = data_request['params']['products_selected']
    except Exception as e:
        print(e)
        return notFound()
    try:
        user = User.objects.get(id = decoded_token['user_id'])
        return updateActionHistory(products_selected,user)
        
    except Exception as e:
        print(e)
        return notFound()

@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def getProductRecommend(request):
    response = Response()
    queryRaw = query_raw.QUERY_SQL_GET_ALL_PRODUCT_FOR_USER
    def notFound():
        response.data = {
            "success" : False , 'error' : {
                'type' : "CGIA-001" , 'value' : "Failed to Login"
            } , 
            'status' : status.HTTP_404_NOT_FOUND
        }
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
    def getProducts(user):
        try:
            handleQueryRaw = query_raw.HandleQueryRaw(queryRaw)
            historyAction = HistoryAction.objects.get(user_id = user)
            products_array = eval(historyAction.list_selected_products)
            print(products_array)
            listCategory = []
            try:
                for slug in products_array:
                    product = Product.objects.get(slug = slug)
                    listCategory.append(product.category_id.slug)
            except Exception as e:
                print(e)
                pass
            print(listCategory)
            if len(listCategory) > 0:
                string_representation = "(" + ", ".join(map(str, listCategory)) + ")"
                converted_string = "('" + "', '".join(string_representation.strip('()').split(', ')) + "')"
                print(converted_string)
                handleQueryRaw.setCategory(converted_string)
            print(handleQueryRaw.getQueryRaw())
            queryset = Product.objects.raw(handleQueryRaw.getQueryRaw())
            queryset = [{**vars(obj), 'status_heart': False } for obj in queryset]
            queryset , numberProduct = data_processing.handleRawQuery(queryset)

            serializer = ProductSerializer(queryset,many=True)
            shuffled_data = list(serializer.data)
            random.shuffle(shuffled_data)

        except:
            pass
        response.data = {
            "success" : True ,
            'products' :   shuffled_data,
            'number_product' : numberProduct ,
            'status' : status.HTTP_200_OK
        }
        response.status_code = status.HTTP_200_OK
        return response
    try:
        jwtToken = request.COOKIES.get('refresh_token')
        refresh_token = RefreshToken(jwtToken)
        decoded_token = refresh_token.payload
    except Exception as e:
        print(e)
        return notFound()
    try:
        user = User.objects.get(id = decoded_token['user_id'])
        return getProducts(user)
        
    except Exception as e:
        print(e)
        return notFound()
