from rest_framework.decorators import api_view,action,permission_classes,authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from django.template.defaultfilters import slugify
from login.models import User
from product.models import Product,Photo_product,Price,Category
from .serializers import ProductAminSerializer ,ProductDetailSerializer , VoucherAdminSerializer
from .serializers import VoucherNoProductAdminSerializer , CountLengthAdminSerializer 
from .serializers import VoucherAdminORMSerializer , FlashSaleAdminSerializer
from .serializers import FlashSaleAdminORMSerializer 
from flashSaleProduct.models import Voucher,DetailVoucher,FlashSale , DetailFlashSale

from . import query_raw
from .method_orthers import handleDecodeFile , removeFile
import json
import shutil
import datetime
from datetime import  timedelta
import random
import string
# ---------------------------------------------------------------------------- #
#                                GET INFOR ADMIN                               #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
#                                    PRODUCT                                   #
# ---------------------------------------------------------------------------- #
@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def getAllProductAdmin(request):
    response = Response()
    queryRaw = query_raw.GET_ALL_PRODUCT_ADMIN
    def notFound():
        response.data = {
            "success" : False , 'error' : {
                'type' : "CGIA-001" , 'value' : "Failed to Login"
            } , 
            'status' : status.HTTP_404_NOT_FOUND
        }
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
    def getIProducts(page,numberQuantity):
        handleRaw = query_raw.HandleQueryRaw(queryRaw)
        handleRaw.setPage(page,numberQuantity)
        queryset = Product.objects.raw(handleRaw.getQueryRaw())
        number_product = Product.objects.all().count()
        serializer = ProductAminSerializer(queryset , many = True)
        response.data = {
            "success" : True ,
            'products' : serializer.data,
            "number_product" : number_product ,
            'status' : status.HTTP_200_OK
        }
        response.status_code = status.HTTP_200_OK
        return response
    try:
        jwtToken = request.COOKIES.get('refresh_token')
        refresh_token = RefreshToken(jwtToken)
        decoded_token = refresh_token.payload
        page = request.GET.get('page')
        numberQuantity = request.GET.get('number_quantity')
    except Exception as e:
        print(e)
        return notFound()
    try:
        user = User.objects.get(id = decoded_token['user_id'])
        print('user.is_superuser',user.is_superuser)
        if user.is_superuser == False:
            return notFound()
        return getIProducts(page,numberQuantity)
        
    except Exception as e:
        print(e)
        return notFound()
    
# ---------------------------------------------------------------------------- #
#                                SEARCH PRODUCT                                #
# ---------------------------------------------------------------------------- #

@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def searchProductAdmin(request):
    response = Response()
    queryRaw = query_raw.GET_ALL_PRODUCT_SEARCH
    def notFound():
        response.data = {
            "success" : False , 'error' : {
                'type' : "CGIA-001" , 'value' : "Failed to Login"
            } , 
            'status' : status.HTTP_404_NOT_FOUND
        }
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
    def getIProducts(page,numberQuantity,key_search):
        handleRaw = query_raw.HandleQueryRaw(queryRaw)
        handleRaw.SetKeySearchProduct(key_search)
        handleRaw.setPage(page,numberQuantity)
        queryset = Product.objects.raw(handleRaw.getQueryRaw())
        number_product = Product.objects.all().count()
        serializer = ProductAminSerializer(queryset , many = True)
        response.data = {
            "success" : True ,
            'products' : serializer.data,
            "number_product" : number_product ,
            'status' : status.HTTP_200_OK
        }
        response.status_code = status.HTTP_200_OK
        return response
    try:
        jwtToken = request.COOKIES.get('refresh_token')
        refresh_token = RefreshToken(jwtToken)
        decoded_token = refresh_token.payload
        key_search = request.GET.get('key_search')
        page = request.GET.get('page')
        numberQuantity = request.GET.get('number_quantity')
    except Exception as e:
        print("ERROR",e)
        return notFound()
    try:
        user = User.objects.get(id = decoded_token['user_id'])
        if user.is_superuser == False:
            return notFound()
        return getIProducts(page,numberQuantity,key_search)
        
    except Exception as e:
        print("ERROR",e)
        return notFound()
@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def DelProduct(request):
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
    def delProduct(products_del):
        productDeleted = []
        for id in products_del:
            try:
                productDel = Product.objects.get(id = id)
                productDeleted.append(productDel.id)
                productDel.delete()
            except:
                pass
        response.data = {
            "success" : True ,
            "products_del" : productDeleted ,
            'status' : status.HTTP_200_OK
        }
        response.status_code = status.HTTP_200_OK
        return response
    try:
        jwtToken = request.COOKIES.get('refresh_token')
        refresh_token = RefreshToken(jwtToken)
        decoded_token = refresh_token.payload
        data_request= json.loads(request.body.decode('utf-8'))
        products_del = data_request['params']['products_del']
    except Exception as e:
        print(e)
        return notFound()
    try:
        user = User.objects.get(id = decoded_token['user_id'])
        if user.is_superuser == False:
            return notFound()
        return delProduct(products_del)
        
    except Exception as e:
        print(e)
        return notFound()

@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def createProductAdmin(request):
    response = Response()
    def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
    def saveMediaFile(product,files):
        for file_data in files:
            file_decode = handleDecodeFile(file_data['data'],file_data['isImage'],file_data['isVideo'])
            print(file_decode)
            mediaProduct = Photo_product.objects.create(
                data = file_decode['file'],
                product_id = product 
            )

            print(mediaProduct)
    def notFound():
        response.data = {
            "success" : False , 'error' : {
                'type' : "CGIA-001" , 'value' : "Failed to Login"
            } , 
            'status' : status.HTTP_404_NOT_FOUND
        }
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
    def createProduct(name,category_id,price,sex,sale,quantity,media_file,description):
        category_current = Category.objects.get(id=category_id)
        product_created = Product.objects.create(
            name=name, category_id=category_current ,
            sex = sex , description = description ,
            quantity = int(quantity) ,
            slug=str(slugify(name) + "-" + id_generator())
        )
        print(product_created )
        price = Price.objects.create(
            price = float(price) , status = True , datetime_create = datetime.datetime.now() ,
            sale = int(sale) , product_id = product_created,
            price_total = float(price)*(1 - (int(sale)/100)) 
        )
        print(price)
        saveMediaFile(product_created,media_file)
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
        name_product = data_request['params']['name']
        category_id = data_request['params']['category_id']
        price = data_request['params']['price']
        sex = data_request['params']['sex']
        sale = data_request['params']['sale']
        quantity = data_request['params']['quantity']
        media_file = data_request['params']['media_file']
        description = data_request['params']['description']
        print((name_product,category_id,price,sex,sale,quantity,description))
    except Exception as e:
        print(e)
        return notFound()
    try:
        user = User.objects.get(id = decoded_token['user_id'])
        if user.is_superuser == False:
            return notFound()
        return createProduct(name_product,category_id,price,sex,sale,quantity,media_file,description)
        
    except Exception as e:
        print(e)
        return notFound()


# ---------------------------------------------------------------------------- #
#                              GET DETAIL PRODUCT                              #
# ---------------------------------------------------------------------------- #
@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def getDetailProductAdmin(request):
    response = Response()
    queryRaw = query_raw.QUERY_SQL_GET_PRODUCT_DETAIL_ADMIN
    def notFound():
        response.data = {
            "success" : False , 'error' : {
                'type' : "CGIA-001" , 'value' : "Failed to Login"
            } , 
            'status' : status.HTTP_404_NOT_FOUND
        }
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
    def getIProduct(product_id):
        product_current = Product.objects.get(id = product_id)
        queryset = Product.objects.raw(queryRaw,[product_current.slug])
        queryset = [{**vars(obj), 'status_heart': False } for obj in queryset]

        serializer = ProductDetailSerializer(queryset,many=True)
        response.data = {
            "success" : True ,
            'product' : serializer.data,
            'category' : product_current.category_id.id,
            'status' : status.HTTP_200_OK
        }
        response.status_code = status.HTTP_200_OK
        return response
    try:
        jwtToken = request.COOKIES.get('refresh_token')
        refresh_token = RefreshToken(jwtToken)
        decoded_token = refresh_token.payload
        product_id = request.GET.get('product_id')
    except Exception as e:
        print("ERROR",e)
        return notFound()
    try:
        user = User.objects.get(id = decoded_token['user_id'])
        if user.is_superuser == False:
            return notFound()
        return getIProduct(product_id)
        
    except Exception as e:
        print("ERROR",e)
        return notFound()

@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def uploadProductAdmin(request):
    response = Response()
    def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
    def delMediaFile(product,files):
        for file_data in files:
            print(file_data)
            mediaProduct = Photo_product.objects.get(
                data = file_data,
                product_id = product 
            )
            mediaProduct.delete()
            removeFile(file_data)
    def saveMediaFile(product,files):
        for file_data in files:
            file_decode = handleDecodeFile(file_data['data'],file_data['isImage'],file_data['isVideo'])
            print(file_decode)
            mediaProduct = Photo_product.objects.create(
                data = file_decode['file'],
                product_id = product 
            )
            print(mediaProduct)
    def notFound():
        response.data = {
            "success" : False , 'error' : {
                'type' : "CGIA-001" , 'value' : "Failed to Login"
            } , 
            'status' : status.HTTP_404_NOT_FOUND
        }
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
    def updateProduct(
                product_id,name_product_update ,category_id_update ,
                price_update ,sex_update ,sale_update ,quantity_update ,
                media_file_update ,media_file_del,description_update 
        ):
        product_update = Product.objects.get( id = product_id)
        if category_id_update != '' and category_id_update != None:
            category_update = Category.objects.get(id=category_id_update)
            product_update.category_id = category_update

        if name_product_update != '' and name_product_update != None:
            product_update.name = name_product_update
            product_update.slug = str(slugify(name_product_update) + "-" + id_generator())

        if sex_update != '' and sex_update != None:
            product_update.sex = sex_update

        if quantity_update != '' and quantity_update != None:
            product_update.quantity = quantity_update

        if description_update != '' and description_update != None:
            product_update.description = description_update

        product_update.save()
        price_product_update = Price.objects.get(product_id = product_update , status = True)
        if price_update != '' and price_update != None:
            price_product_update.price = price_update
        
        if sale_update != '' and sale_update != None:
            price_product_update.sale = sale_update

        price_product_update.save()
        if media_file_update != '' and media_file_update != None:
            saveMediaFile(product_update,media_file_update)
        if media_file_del != '' and media_file_del != None:
            delMediaFile(product_update,media_file_del)
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
        product_id = data_request['params']['product_id']
        name_product_update  = data_request['params']['name']
        category_id_update = data_request['params']['category_id']
        price_update  = data_request['params']['price']
        sex_update  = data_request['params']['sex']
        sale_update  = data_request['params']['sale']
        quantity_update  = data_request['params']['quantity']
        media_file_update  = data_request['params']['media_file']
        media_file_del = data_request['params']['media_file_del']
        description_update  = data_request['params']['description']
    except Exception as e:
        print(e)
        return notFound()
    try:
        user = User.objects.get(id = decoded_token['user_id'])
        if user.is_superuser == False:
            return notFound()
        return  updateProduct(
                    product_id,name_product_update ,category_id_update ,
                    price_update ,sex_update ,sale_update ,quantity_update ,
                    media_file_update ,media_file_del,description_update 
                )
        
    except Exception as e:
        print(e)
        return notFound()
# ---------------------------------------------------------------------------- #
#                                    VOUCHER                                   #
# ---------------------------------------------------------------------------- #

@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def getAllVoucherAdmin(request):
    response = Response()
    queryRaw = query_raw.QUERY_GET_ALL_VOUCHER_WITH_PAGE
    def notFound():
        response.data = {
            "success" : False , 'error' : {
                'type' : "CGIA-001" , 'value' : "Failed to Login"
            } , 
            'status' : status.HTTP_404_NOT_FOUND
        }
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
    def getVouchers(page,numberQuantity,level):
        handleRaw = query_raw.HandleQueryRaw(queryRaw)
        handleRaw.setPageVoucher(page,numberQuantity)
        handleRaw.setLevelVoucher(level)
        queryset = Voucher.objects.raw(handleRaw.getQueryRaw())
        serializer = VoucherAdminSerializer(queryset , many = True)
        response.data = {
            "success" : True ,
            'vouchers' : serializer.data,
            'status' : status.HTTP_200_OK
        }
        response.status_code = status.HTTP_200_OK
        return response
    try:
        jwtToken = request.COOKIES.get('refresh_token')
        refresh_token = RefreshToken(jwtToken)
        decoded_token = refresh_token.payload
        page = request.GET.get('page')
        numberQuantity = request.GET.get('number_quantity')
        level = request.GET.get('level')
    except Exception as e:
        print(e)
        return notFound()
    try:
        user = User.objects.get(id = decoded_token['user_id'])
        print('user.is_superuser',user.is_superuser)
        if user.is_superuser == False:
            return notFound()
        return getVouchers(page,numberQuantity,level)
        
    except Exception as e:
        print(e)
        return notFound()


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def searchVoucherAdmin(request):
    response = Response()
    queryRaw = query_raw.QUERY_SEARCH_ALL_VOUCHER_WITH_PAGE
    def notFound():
        response.data = {
            "success" : False , 'error' : {
                'type' : "CGIA-001" , 'value' : "Failed to Login"
            } , 
            'status' : status.HTTP_404_NOT_FOUND
        }
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
    def getVouchers(page,numberQuantity,key_search , level):
        handleRaw = query_raw.HandleQueryRaw(queryRaw)
        handleRaw.SetKeySearchVocuher(key_search)
        handleRaw.setPageVoucher(page,numberQuantity)
        handleRaw.setLevelVoucher(level)
        queryset = Voucher.objects.raw(handleRaw.getQueryRaw())
        
        serializer = VoucherAdminSerializer(queryset , many = True)
        response.data = {
            "success" : True ,
            'vouchers' : serializer.data,
            'status' : status.HTTP_200_OK
        }
        response.status_code = status.HTTP_200_OK
        return response
    try:
        jwtToken = request.COOKIES.get('refresh_token')
        refresh_token = RefreshToken(jwtToken)
        decoded_token = refresh_token.payload
        key_search = request.GET.get('key_search')
        page = request.GET.get('page')
        numberQuantity = request.GET.get('number_quantity')
        level = request.GET.get('level')
    except Exception as e:
        print("ERROR",e)
        return notFound()
    try:
        user = User.objects.get(id = decoded_token['user_id'])
        if user.is_superuser == False:
            return notFound()
        return getVouchers(page,numberQuantity,key_search , level)
        
    except Exception as e:
        print("ERROR",e)
        return notFound()


@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def delVoucherAdmin(request):
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
    def delVouchers(vouchers_del):
        voucherDeleted = []
        for id in vouchers_del:
            try:
                voucherDel = Voucher.objects.get(id = id)
                voucherDeleted.append(voucherDel.id)
                voucherDel.delete()
            except:
                pass
        response.data = {
            "success" : True ,
            "vouchers_del" : voucherDeleted ,
            'status' : status.HTTP_200_OK
        }
        response.status_code = status.HTTP_200_OK
        return response
    try:
        jwtToken = request.COOKIES.get('refresh_token')
        refresh_token = RefreshToken(jwtToken)
        decoded_token = refresh_token.payload
        data_request= json.loads(request.body.decode('utf-8'))
        vouchers_del = data_request['params']['vouchers_del']
    except Exception as e:
        print(e)
        return notFound()
    try:
        user = User.objects.get(id = decoded_token['user_id'])
        if user.is_superuser == False:
            return notFound()
        return delVouchers(vouchers_del)
        
    except Exception as e:
        print(e)
        return notFound()
    
@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def createVoucherAdmin(request):
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
    def createVoucher(
            name , level , sale , detail ,
            limited_price , quantity , description
        ):
        voucherCreate = Voucher.objects.create(
            name = name , level = level , sale = sale , detail = detail ,
            limited_price = limited_price , quantity = quantity , description = description
        )
        voucherCreate.save()
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
        name = data_request['params']['name']
        level = data_request['params']['level']
        sale = data_request['params']['sale']
        limited_price = data_request['params']['limited_price']
        detail = data_request['params']['detail']
        quantity = data_request['params']['quantity']
        description = data_request['params']['description']
    except Exception as e:
        print(e)
        return notFound()
    try:
        user = User.objects.get(id = decoded_token['user_id'])
        if user.is_superuser == False:
            return notFound()
        return createVoucher(
            name , level , sale  , detail ,
            limited_price , quantity , description
        )
        
    except Exception as e:
        print(e)
        return notFound()

@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def getAllVoucherNoProductAdmin(request):
    response = Response()
    queryRaw = query_raw.QUERY_GET_ALL_VOUCHER_NO_PRODUCT
    def notFound():
        response.data = {
            "success" : False , 'error' : {
                'type' : "CGIA-001" , 'value' : "Failed to Login"
            } , 
            'status' : status.HTTP_404_NOT_FOUND
        }
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
    def getVouchers(page,numberQuantity,level):
        handleRaw = query_raw.HandleQueryRaw(queryRaw)
        handleRaw.setPageVoucher(page,numberQuantity)
        handleRaw.setLevelVoucher(level)
        queryset = Voucher.objects.raw(handleRaw.getQueryRaw())
        serializer = VoucherNoProductAdminSerializer(queryset , many = True)
        response.data = {
            "success" : True ,
            'vouchers' : serializer.data,
            'status' : status.HTTP_200_OK
        }
        response.status_code = status.HTTP_200_OK
        return response
    try:
        jwtToken = request.COOKIES.get('refresh_token')
        refresh_token = RefreshToken(jwtToken)
        decoded_token = refresh_token.payload
        page = request.GET.get('page')
        numberQuantity = request.GET.get('number_quantity')
        level = request.GET.get('level')
    except Exception as e:
        print(e)
        return notFound()
    try:
        user = User.objects.get(id = decoded_token['user_id'])
        print('user.is_superuser',user.is_superuser)
        if user.is_superuser == False:
            return notFound()
        return getVouchers(page,numberQuantity,level)
        
    except Exception as e:
        print(e)
        return notFound()


@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def addProductVoucherAdmin(request):
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
    def addProductVoucher(voucher_id ,products_selected):
        voucher_current = Voucher.objects.get(id = voucher_id)
        for product_id in products_selected:
            product_add = Product.objects.get(id = product_id)
            detailVoucher = DetailVoucher.objects.create(
                product_id = product_add ,
                voucher_id = voucher_current
            )
            detailVoucher.save()
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
        voucher_id = data_request['params']['voucher_id']
        products_selected = data_request['params']['products_selected']
    except Exception as e:
        print(e)
        return notFound()
    try:
        user = User.objects.get(id = decoded_token['user_id'])
        if user.is_superuser == False:
            return notFound()
        return addProductVoucher(voucher_id ,products_selected)
        
    except Exception as e:
        print(e)
        return notFound()


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def getDetailVoucherAdmin(request):
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
    def getVoucher(voucher_id):
        queryset = Voucher.objects.get(id = voucher_id)
        serializer = VoucherAdminORMSerializer(queryset , many = False)
        response.data = {
            "success" : True ,
            'voucher' : serializer.data,
            'status' : status.HTTP_200_OK
        }
        response.status_code = status.HTTP_200_OK
        return response
    try:
        jwtToken = request.COOKIES.get('refresh_token')
        refresh_token = RefreshToken(jwtToken)
        decoded_token = refresh_token.payload
        voucher_id = request.GET.get('voucher_id')
    except Exception as e:
        print(e)
        return notFound()
    try:
        user = User.objects.get(id = decoded_token['user_id'])
        print('user.is_superuser',user.is_superuser)
        if user.is_superuser == False:
            return notFound()
        return getVoucher(voucher_id)
        
    except Exception as e:
        print(e)
        return notFound()

@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def delProductVoucherAdmin(request):
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
    def delProductVoucher(voucher_id ,products_selected):
        productDel = []
        voucher_current = Voucher.objects.get(id = voucher_id)
        for product_id in products_selected:
            product_del = Product.objects.get(id = product_id)
            detailVoucher = DetailVoucher.objects.get(
                product_id = product_del ,
                voucher_id = voucher_current
            )
            detailVoucher.delete()
            productDel.append(product_del.id)
        response.data = {
            "success" : True ,
            'product_del' : productDel ,
            'status' : status.HTTP_200_OK
        }
        response.status_code = status.HTTP_200_OK
        return response
    try:
        jwtToken = request.COOKIES.get('refresh_token')
        refresh_token = RefreshToken(jwtToken)
        decoded_token = refresh_token.payload
        data_request= json.loads(request.body.decode('utf-8'))
        voucher_id = data_request['params']['voucher_id']
        products_selected = data_request['params']['products_selected']
    except Exception as e:
        print(e)
        return notFound()
    try:
        user = User.objects.get(id = decoded_token['user_id'])
        if user.is_superuser == False:
            return notFound()
        return delProductVoucher(voucher_id ,products_selected)
        
    except Exception as e:
        print(e)
        return notFound()

# ---------------------------------------------------------------------------- #
#                                  FLASH SALE                                  #
# ---------------------------------------------------------------------------- #


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def getAllFlashSaleAdmin(request):
    response = Response()
    queryRaw = query_raw.QUERY_GET_ALL_FLASH_SALE_WITH_PAGE
    def notFound():
        response.data = {
            "success" : False , 'error' : {
                'type' : "CGIA-001" , 'value' : "Failed to Login"
            } , 
            'status' : status.HTTP_404_NOT_FOUND
        }
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
    def getFlashSales(page,numberQuantity,level):
        handleRaw = query_raw.HandleQueryRaw(queryRaw)
        handleRaw.setPageFlashSale(page,numberQuantity)
        queryset = Voucher.objects.raw(handleRaw.getQueryRaw())
        serializer = FlashSaleAdminSerializer(queryset , many = True)
        response.data = {
            "success" : True ,
            'flash_sales' : serializer.data,
            'status' : status.HTTP_200_OK
        }
        response.status_code = status.HTTP_200_OK
        return response
    try:
        jwtToken = request.COOKIES.get('refresh_token')
        refresh_token = RefreshToken(jwtToken)
        decoded_token = refresh_token.payload
        page = request.GET.get('page')
        numberQuantity = request.GET.get('number_quantity')
        level = request.GET.get('level')
    except Exception as e:
        print(e)
        return notFound()
    try:
        user = User.objects.get(id = decoded_token['user_id'])
        print('user.is_superuser',user.is_superuser)
        if user.is_superuser == False:
            return notFound()
        return getFlashSales(page,numberQuantity,level)
        
    except Exception as e:
        print(e)
        return notFound()


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def searchFlashSaleAdmin(request):
    response = Response()
    queryRaw = query_raw.QUERY_SEARCH_ALL_FLASH_SALE_WITH_PAGE
    def notFound():
        response.data = {
            "success" : False , 'error' : {
                'type' : "CGIA-001" , 'value' : "Failed to Login"
            } , 
            'status' : status.HTTP_404_NOT_FOUND
        }
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
    def getFlashSales(page,numberQuantity,key_search):
        handleRaw = query_raw.HandleQueryRaw(queryRaw)
        handleRaw.SetKeySearchVocuher(key_search)
        handleRaw.setPageVoucher(page,numberQuantity)
        queryset = Voucher.objects.raw(handleRaw.getQueryRaw())
        
        serializer = FlashSaleAdminSerializer(queryset , many = True)
        response.data = {
            "success" : True ,
            'flash_sales' : serializer.data,
            'status' : status.HTTP_200_OK
        }
        response.status_code = status.HTTP_200_OK
        return response
    try:
        jwtToken = request.COOKIES.get('refresh_token')
        refresh_token = RefreshToken(jwtToken)
        decoded_token = refresh_token.payload
        key_search = request.GET.get('key_search')
        page = request.GET.get('page')
        numberQuantity = request.GET.get('number_quantity')
    except Exception as e:
        print("ERROR",e)
        return notFound()
    try:
        user = User.objects.get(id = decoded_token['user_id'])
        if user.is_superuser == False:
            return notFound()
        return getFlashSales(page,numberQuantity,key_search)
        
    except Exception as e:
        print("ERROR",e)
        return notFound()


@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def delFlashSaleAdmin(request):
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
    def delFLashSales(flash_sales_del):
        flashSaleDeleted = []
        for id in flash_sales_del:
            try:
                flashSaleDel = FlashSale.objects.get(id = id)
                flashSaleDeleted.append(flashSaleDel.id)
                flashSaleDel.delete()
            except:
                pass
        response.data = {
            "success" : True ,
            "flash_sale_del" : flashSaleDeleted ,
            'status' : status.HTTP_200_OK
        }
        response.status_code = status.HTTP_200_OK
        return response
    try:
        jwtToken = request.COOKIES.get('refresh_token')
        refresh_token = RefreshToken(jwtToken)
        decoded_token = refresh_token.payload
        data_request= json.loads(request.body.decode('utf-8'))
        flash_sales_del = data_request['params']['flash_sales_del']
    except Exception as e:
        print(e)
        return notFound()
    try:
        user = User.objects.get(id = decoded_token['user_id'])
        if user.is_superuser == False:
            return notFound()
        return delFLashSales(flash_sales_del)
        
    except Exception as e:
        print(e)
        return notFound()
    
@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def createFlashSaleAdmin(request):
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
    def createFlashSale(name , note):
        flashSaleCreate = FlashSale.objects.create( name = name , note = note )
        flashSaleCreate.save()
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
        name = data_request['params']['name']
        note = data_request['params']['note']
    except Exception as e:
        print(e)
        return notFound()
    try:
        user = User.objects.get(id = decoded_token['user_id'])
        if user.is_superuser == False:
            return notFound()
        return createFlashSale(name,note)
        
    except Exception as e:
        print(e)
        return notFound()

@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def getAllFlashSaleNoProductAdmin(request):
    response = Response()
    queryRaw = query_raw.QUERY_GET_ALL_FLASH_SALE_NO_PRODUCT
    def notFound():
        response.data = {
            "success" : False , 'error' : {
                'type' : "CGIA-001" , 'value' : "Failed to Login"
            } , 
            'status' : status.HTTP_404_NOT_FOUND
        }
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
    def getFlashSales(page,numberQuantity):
        handleRaw = query_raw.HandleQueryRaw(queryRaw)
        handleRaw.setPageFlashSale(page,numberQuantity)
        queryset = Voucher.objects.raw(handleRaw.getQueryRaw())
        serializer = FlashSaleAdminSerializer(queryset , many = True)
        response.data = {
            "success" : True ,
            'flash_sales' : serializer.data,
            'status' : status.HTTP_200_OK
        }
        response.status_code = status.HTTP_200_OK
        return response
    try:
        jwtToken = request.COOKIES.get('refresh_token')
        refresh_token = RefreshToken(jwtToken)
        decoded_token = refresh_token.payload
        page = request.GET.get('page')
        numberQuantity = request.GET.get('number_quantity')
    except Exception as e:
        print(e)
        return notFound()
    try:
        user = User.objects.get(id = decoded_token['user_id'])
        print('user.is_superuser',user.is_superuser)
        if user.is_superuser == False:
            return notFound()
        return getFlashSales(page,numberQuantity)
        
    except Exception as e:
        print(e)
        return notFound()


@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def addProductFlashSaleAdmin(request):
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
    def addProductFlashSale(flash_sale_id ,products_selected,datetime_finished):
        flash_sale_current = FlashSale.objects.get(id = flash_sale_id)
        delta = timedelta(days=datetime_finished) 
        datetimeFinished = datetime.datetime.now() + delta
        for product_id in products_selected:
            product_add = Product.objects.get(id = product_id)
            detailFlashSale = DetailFlashSale.objects.create(
                product_id = product_add ,
                flash_sale_id = flash_sale_current,
                status = True ,
                datetime_finished = datetimeFinished
            )
            detailFlashSale.save()
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
        flash_sale_id = data_request['params']['flash_sale_id']
        products_selected = data_request['params']['products_selected']
        datetime_finished = data_request['params']['datetime_finished']
    except Exception as e:
        print(e)
        return notFound()
    try:
        user = User.objects.get(id = decoded_token['user_id'])
        if user.is_superuser == False:
            return notFound()
        return addProductFlashSale(flash_sale_id ,products_selected,datetime_finished)
        
    except Exception as e:
        print(e)
        return notFound()


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def getDetailFlashSaleAdmin(request):
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
    def getFlashSale(flash_sale_id):
        queryset = FlashSale.objects.get(id = flash_sale_id)
        serializer = FlashSaleAdminORMSerializer(queryset , many = False)
        response.data = {
            "success" : True ,
            'flash_sale' : serializer.data,
            'status' : status.HTTP_200_OK
        }
        response.status_code = status.HTTP_200_OK
        return response
    try:
        jwtToken = request.COOKIES.get('refresh_token')
        refresh_token = RefreshToken(jwtToken)
        decoded_token = refresh_token.payload
        flash_sale_id = request.GET.get('flash_sale_id')
    except Exception as e:
        print(e)
        return notFound()
    try:
        user = User.objects.get(id = decoded_token['user_id'])
        print('user.is_superuser',user.is_superuser)
        if user.is_superuser == False:
            return notFound()
        return getFlashSale(flash_sale_id)
        
    except Exception as e:
        print(e)
        return notFound()

@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def delProductFlashSaleAdmin(request):
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
    def delProductFlashSale(flash_sale_id ,products_selected):
        productDel = []
        flash_sale_current = FlashSale.objects.get(id = flash_sale_id)
        for product_id in products_selected:
            product_del = Product.objects.get(id = product_id)
            detailFlashSale = DetailFlashSale.objects.get(
                product_id = product_del ,
                flash_sale_id = flash_sale_current
            )
            detailFlashSale.delete()
            productDel.append(product_del.id)
        response.data = {
            "success" : True ,
            'product_del' : productDel ,
            'status' : status.HTTP_200_OK
        }
        response.status_code = status.HTTP_200_OK
        return response
    try:
        jwtToken = request.COOKIES.get('refresh_token')
        refresh_token = RefreshToken(jwtToken)
        decoded_token = refresh_token.payload
        data_request= json.loads(request.body.decode('utf-8'))
        flash_sale_id = data_request['params']['flash_sale_id']
        products_selected = data_request['params']['products_selected']
    except Exception as e:
        print(e)
        return notFound()
    try:
        user = User.objects.get(id = decoded_token['user_id'])
        if user.is_superuser == False:
            return notFound()
        return delProductFlashSale(flash_sale_id ,products_selected)
        
    except Exception as e:
        print(e)
        return notFound()