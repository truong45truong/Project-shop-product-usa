from .serializers import OrderHandleDataSerializer ,ProductSerializer ,TransportModelSerializer , OrderSerializer , PaymentSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework import status
from order.models import Order , Transport , DetailOrder , Qrcode ,Payment
from product.models import Product , Price ,Photo_product
from login.models import User , Address , PhoneUser 
from flashSaleProduct.models import Voucher , DetailVoucher
from datetime import datetime
from rest_framework_simplejwt.tokens import RefreshToken
from uuid import uuid4
import json
from . import data_processing,raw_query
import shutil
from datetime import  timedelta
import random
import string
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

# ---------------------------------------------------------------------------- #
#                             GENERAL USAGE METHOD                             #
# ---------------------------------------------------------------------------- #
# ------------------ method check order is available to day ------------------ #
def checkTheOrderIsAvailebleToDay(curent_user,now):
    start_datetime = datetime(
        now.year,now.month , now.day, 0, 0, 0
    ) 
    end_datetime = datetime(
        now.year,now.month , now.day, 23, 59, 59
    )
    
    order_current = Order.objects.filter(datetime__range=[start_datetime, end_datetime] , user_id = curent_user)
    print(order_current.query)
    if len(order_current) > 0 :
        return order_current[0]
    else:
        return False
# ---------------------------------------------------------------------------- #
#                           END GENERAL USAGE METHOD                           #
# ---------------------------------------------------------------------------- #

class TransportViewSet(viewsets.ViewSet):
    @action(method=["GET"],detail=False,url_path="get_transport",url_name="get_transport")
    def get_transport(self, request,*args, **kwargs):
        try:
            queryset = Transport.objects.all().order_by('price')
            serializer = TransportModelSerializer(queryset , many = True)
            return Response({"data" : serializer.data})
        except Exception as e:
            print(e)
            return Response({"data" : False})

class OrderViewSet (viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderHandleDataSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    # ---------------------------------------------------------------------------- #
    #                           METHOD GET ORDER CHECKOUT                          #
    # ---------------------------------------------------------------------------- #
    @action(method=["GET"],detail=False,url_path="get_order_checkout",url_name="get_order_checkout")
    def get_order_checkout(self, request,*args, **kwargs):
        response = Response()
        try:
            jwtToken = request.COOKIES.get('refresh_token')
            refresh_token = RefreshToken(jwtToken)
            decoded_token = refresh_token.payload
            nameOrder = request.GET['nameOrder']
        except:
            response.data = {
                "success" : False , "status" : status.HTTP_404_NOT_FOUND ,
                "error" : {
                    "value" : "Params wrong" , "type" : "GOC-0001"
                }
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
        try:
            curent_user = User.objects.get(id = decoded_token['user_id'])
            queryRaw = raw_query.QUERY_SQL_GET_ALL_PRODUCT_ORDER_FOR_USER
            queryset = Order.objects.raw(queryRaw , [nameOrder , curent_user.id ])
            queryset,numberProduct = data_processing.handleRawQuery(queryset)
            serializer = OrderHandleDataSerializer(queryset,many = True) 
            response.data = {
                "success" : serializer.data , "status" : status.HTTP_200_OK ,
                "numberProduct" : numberProduct
            }
            response.status_code = status.HTTP_200_OK
            return response
        except Exception as e:
            print(e)
            response.data = {
                "success" : False , "status" : status.HTTP_404_NOT_FOUND ,
                "error" : {
                    "value" : "Infomation wrong" , "type" : "GOC-0002"
                }
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
    @action(method=["GET"],detail=False,url_path="get_product_order",url_name="get_product_order")
    def get_product_order(self, request,*args, **kwargs):
        response = Response()
        try:
            jwtToken = request.COOKIES.get('refresh_token')
            refresh_token = RefreshToken(jwtToken)
            decoded_token = refresh_token.payload
            nameOrder = request.GET['nameOrder']
        except:
            response.data = {
                "success" : False , "status" : status.HTTP_404_NOT_FOUND ,
                "error" : {
                    "value" : "Params wrong" , "type" : "GOC-0001"
                }
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
        try:
            curent_user = User.objects.get(id = decoded_token['user_id'])
            queryRaw = raw_query.QUERY_SQL_GET_ALL_PRODUCT_ORDER_INFOR
            queryset = Order.objects.raw(queryRaw , [nameOrder , curent_user.id ])
            queryset,numberProduct = data_processing.handleRawQuery(queryset)
            serializer = OrderHandleDataSerializer(queryset,many = True) 
            response.data = {
                "success" : serializer.data , "status" : status.HTTP_200_OK ,
                "numberProduct" : numberProduct
            }
            response.status_code = status.HTTP_200_OK
            return response
        except Exception as e:
            print(e)
            response.data = {
                "success" : False , "status" : status.HTTP_404_NOT_FOUND ,
                "error" : {
                    "value" : "Infomation wrong" , "type" : "GOC-0002"
                }
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
    # ---------------------------------------------------------------------------- #
    #                               METHOD GET ORDER                               #
    # ---------------------------------------------------------------------------- #
    @action(method=["GET"],detail=False,url_path="get_order",url_name="get_order")
    def get_order(self, request,*args, **kwargs):
        jwtToken = request.COOKIES.get('refresh_token')
        refresh_token = RefreshToken(jwtToken)
        decoded_token = refresh_token.payload
        try:
            curent_user = User.objects.get(id = decoded_token['user_id'])
        except:
            return Response({"success":False})
        check_order_today = checkTheOrderIsAvailebleToDay(curent_user,datetime.now())
        if check_order_today != False :
           check_order_today = True
        orderQuery = Order.objects.raw(raw_query.QUERY_SQL_GET_ALL_ORDER_FOR_USER,[curent_user.id])
        print(len(orderQuery))
        if len(orderQuery) > 0:
            queryset,numberProduct = data_processing.handleRawQuery(orderQuery)
        
            serializer = OrderHandleDataSerializer(queryset,many = True) 
            
            return Response({"success":serializer.data , "number_product" : numberProduct , "check_order_today" : check_order_today })
        else:
            return Response({"success":[], "number_product" : 0 , "check_order_today" : check_order_today})
    
    # ---------------------------------------------------------------------------- #
    #                         GET ALL ORDER BE WAITING PAID                        #
    # ---------------------------------------------------------------------------- #

    @action(method=["GET"],detail=False,url_path="get_all_order_be_waiting_paid_for_user",url_name="get_all_order_be_waiting_paid_for_user")
    def get_all_order_be_waiting_paid_for_user(self, request,*args, **kwargs):
        response = Response()
        try:
            jwtToken = request.COOKIES.get('refresh_token')
            refresh_token = RefreshToken(jwtToken)
            decoded_token = refresh_token.payload
        except:
            response.data = {
                "success" : False , "status" : status.HTTP_404_NOT_FOUND ,
                "error" : {
                    "value" : "Params wrong" , "type" : "GAOBWFU-0001"
                }
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
        try:
            curent_user = User.objects.get(id = decoded_token['user_id'])
            queryset = Order.objects.filter(is_payment = False , status = True , user_id = curent_user)
            serializer = OrderSerializer(queryset , many = True)
            response.data = {
                "success" : serializer.data , "status" : status.HTTP_200_OK 
            }
            response.status_code = status.HTTP_200_OK
            return response
        except Exception as e:
            print(e)
            response.data = {
                "success" : False , "status" : status.HTTP_404_NOT_FOUND ,
                "error" : {
                    "value" : "Infomation wrong" , "type" : "GAOBWFU-0002"
                }
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
    @action(method=["GET"],detail=False,url_path="get_order_be_paymented_for_user",url_name="get_order_be_paymented_for_user")
    def get_order_be_paymented_for_user(self, request,*args, **kwargs):
        response = Response()
        try:
            jwtToken = request.COOKIES.get('refresh_token')
            refresh_token = RefreshToken(jwtToken)
            decoded_token = refresh_token.payload

        except:
            response.data = {
                "success" : False , "status" : status.HTTP_404_NOT_FOUND ,
                "error" : {
                    "value" : "Params wrong" , "type" : "GAOBWFU-0001"
                }
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
        try:
            curent_user = User.objects.get(id = decoded_token['user_id'])
            queryset = Order.objects.filter(
                is_payment = True , status = True , 
                user_id = curent_user 
            )
            # queryset_payment = Payment.objects.get(order_id =  queryset[0].id)
            serializer = OrderSerializer(queryset , many = True)
            # serializer_payment = PaymentSerializer(queryset_payment , many = False)
            response.data = {
                "success" : serializer.data , 
                "status" : status.HTTP_200_OK 
            }
            response.status_code = status.HTTP_200_OK
            return response
        except Exception as e:
            print(e)
            response.data = {
                "success" : False , "status" : status.HTTP_404_NOT_FOUND ,
                "error" : {
                    "value" : "Infomation wrong" , "type" : "GAOBWFU-0002"
                }
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
    @action(method=["GET"],detail=False,url_path="get_info_order",url_name="get_info_order")
    def get_info_order(self, request,*args, **kwargs):
        response = Response()
        try:
            jwtToken = request.COOKIES.get('refresh_token')
            refresh_token = RefreshToken(jwtToken)
            decoded_token = refresh_token.payload
            name_order = request.GET.get('name_order')
        except:
            response.data = {
                "success" : False , "status" : status.HTTP_404_NOT_FOUND ,
                "error" : {
                    "value" : "Params wrong" , "type" : "GAOBWFU-0001"
                }
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
        try:
            curent_user = User.objects.get(id = decoded_token['user_id'])
            queryset = Order.objects.filter(
                name = name_order , user_id = curent_user
            )
            isPayment = False
            try:
                queryset_payment = Payment.objects.get(order_id =  queryset[0].id)
                serializer_payment = PaymentSerializer(queryset_payment , many = False)
                isPayment = True
            except:
                pass
            
            serializer = OrderSerializer(queryset , many = True)
            if isPayment:
                response.data = {
                    "order" : serializer.data , 
                    'payment' : serializer_payment.data ,
                    "status" : status.HTTP_200_OK 
                }
            else:
                response.data = {
                    "order" : serializer.data , 
                    'payment' : False,
                    "status" : status.HTTP_200_OK 
                }
            response.status_code = status.HTTP_200_OK
            return response
        except Exception as e:
            print(e)
            response.data = {
                "success" : False , "status" : status.HTTP_404_NOT_FOUND ,
                "error" : {
                    "value" : "Infomation wrong" , "type" : "GAOBWFU-0002"
                }
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
    # ---------------------------------------------------------------------------- #
    #                         CREATE ORDER WAITING BE PAID                         #
    # ---------------------------------------------------------------------------- #

    @action(method=["POST"],detail=False,url_path="create_order_waiting_be_paid",url_name="create_order_waiting_be_paid")
    def create_order_waiting_be_paid(self, request,*args, **kwargs):
        # ------------------------------ GLOBAL VARIABLE ----------------------------- #
        orderWaitingBePaid = False
        def isHaveinVoucher(listProductSlug , listDetailVoucher,voucher):
            price = 0
            for productSlug in listProductSlug:
                for productVoucher in listDetailVoucher:
                    if productVoucher.product_id.slug == productSlug.product_id.slug:
                        productPrice = Product.objects.get(slug = productVoucher.product_id.slug)
                        priceProduct = Price.objects.get(product_id = productPrice )
                        priceActiveVoucher = ( priceProduct.price_total *  voucher.sale )/100
                        if priceActiveVoucher > voucher.limited_price:
                            price += voucher.limited_price
                        else:
                            price += priceActiveVoucher
            return price
        
        try:
            data_request= json.loads(request.body.decode('utf-8'))
            products = data_request['params']['products']
            address_id = data_request['params']['address_id']
            phone_id = data_request['params']['phone_id']
            transport_id = data_request['params']['transport_id']
            voucher_id = data_request['params']['voucher_id']
            jwtToken = request.COOKIES.get('refresh_token')
            refresh_token = RefreshToken(jwtToken)
            decoded_token = refresh_token.payload
            response = Response()
        except Exception as e:
            print(e)
            response.data = {
                "success" : False , "status" : status.HTTP_404_NOT_FOUND ,
                "error" : {
                    "value" : "Params wrong" , "type" : "COWBP-0001"
                }
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
        try:
            curent_user = User.objects.get(id = decoded_token['user_id'])
            if address_id != False :
                addressSelected =  Address.objects.get(id = address_id , user_id = curent_user)
            else:
                addressSelected =  Address.objects.get(status = True, user_id = curent_user)
            if phone_id != False:
                phoneSelected = PhoneUser.objects.get(id = phone_id)
            else:
                phoneSelected = PhoneUser.objects.get(status = True, user_id = curent_user)
            if transport_id != False:
                transportSelected = Transport.objects.get(id = transport_id)
            else:
                transportSelected = Transport.objects.all().order_by('price').first()
            print('transportSelected',transportSelected)
            qr_code = Qrcode.objects.create()
            qr_code.name=curent_user.email
            qr_code.save()

            print(str(id_generator()) + '-' + str(id_generator()))
            orderWaitingBePaid = Order.objects.create(
                name = str(id_generator()) + '-' + str(id_generator()),
                datetime = datetime.now(),
                receiver = phoneSelected.name,
                address_receiver = addressSelected.address_content ,
                phone_receiver = phoneSelected.phone ,
                status = True ,
                note = 'no',
                logs = 'no',
                cancel = False ,
                is_payment = False ,
                request_cancel = False ,
                user_id = curent_user,
                transport_id = transportSelected,
                qr_code_id = qr_code
            )
            totalPrice = 0
            for product in products:
                productSelected = Product.objects.get(slug = product['slug'])
                priceProduct = Price.objects.get(product_id = productSelected)
                detailOrder = False
                try:
                    detailOrder = DetailOrder.objects.create(
                        product_id = productSelected , 
                        order_id = orderWaitingBePaid, 
                        status = False ,
                        quantity = int(product['quantity'])
                    )
                    detailOrder.save()
                    print('detailOrder',detailOrder.order_id)

                except Exception as e:
                    print(e)
                    if detailOrder != False:
                        detailOrder.delete()
                totalPrice = totalPrice + priceProduct.price_total * detailOrder.quantity
            if voucher_id != False:
                voucher = Voucher.objects.get(id = voucher_id)
                listDetailVoucher = DetailVoucher.objects.filter(voucher_id = voucher)
                listProductSlug = DetailOrder.objects.filter(order_id=orderWaitingBePaid)
                totalPrice  -=  isHaveinVoucher(listProductSlug,listDetailVoucher,voucher)
            orderWaitingBePaid.total_price = totalPrice
            orderWaitingBePaid.save()

            response.data = {
                "name_order" : orderWaitingBePaid.name , "status" : status.HTTP_200_OK
            }
            response.status_code = status.HTTP_200_OK
            return response
        except Exception as e:
            print(e)
            if orderWaitingBePaid != False:
                orderWaitingBePaid.delete()
            response.data = {
                "success" : False , "status" : status.HTTP_404_NOT_FOUND ,
                "error" : {
                    "value" : "Information wrong" , "type" : "COWBP-0002"
                }
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
    
    # ---------------------------------------------------------------------------- #
    #                                UPDATE RECEIVER                               #
    # ---------------------------------------------------------------------------- #

    @action(method=["POST"],detail=False,url_path="update_receiver",url_name="update_receiver")
    def update_receiver(self, request,*args, **kwargs):
        try:
            data_request= json.loads(request.body.decode('utf-8'))
            receiver = data_request['params']['receiver']
            phoneReceiver = data_request['params']['phone_receiver']
            nameOrder = data_request['params']['name_order']
            jwtToken = request.COOKIES.get('refresh_token')
            refresh_token = RefreshToken(jwtToken)
            decoded_token = refresh_token.payload
            response = Response()
        except Exception as e:
            print(e)
            response.data = {
                "success" : False , "status" : status.HTTP_404_NOT_FOUND ,
                "error" : {
                    "value" : "Params wrong" , "type" : "COWBP-0001"
                }
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
        try:
            curent_user = User.objects.get(id = decoded_token['user_id'])
            orderWaitingBePaid = Order.objects.get(name = nameOrder , user_id = curent_user)
            orderWaitingBePaid.receiver = receiver
            orderWaitingBePaid.phone_receiver = phoneReceiver
            orderWaitingBePaid.save()
            response.data = {
                "success" : True , "status" : status.HTTP_200_OK
            }
            response.status_code = status.HTTP_200_OK
            return response
        except Exception as e:
            print(e)
            response.data = {
                "success" : False , "status" : status.HTTP_404_NOT_FOUND ,
                "error" : {
                    "value" : "Information wrong" , "type" : "COWBP-0002"
                }
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
    
    # ---------------------------------------------------------------------------- #
    #                            UPDATE ADDRESS RECEIVER                           #
    # ---------------------------------------------------------------------------- #
    @action(method=["POST"],detail=False,url_path="update_address_receiver",url_name="update_address_receiver")
    def update_address_receiver(self, request,*args, **kwargs):
        try:
            data_request= json.loads(request.body.decode('utf-8'))
            addressReceiver = data_request['params']['address_receiver']
            nameOrder = data_request['params']['name_order']
            jwtToken = request.COOKIES.get('refresh_token')
            refresh_token = RefreshToken(jwtToken)
            decoded_token = refresh_token.payload
            response = Response()
        except Exception as e:
            print(e)
            response.data = {
                "success" : False , "status" : status.HTTP_404_NOT_FOUND ,
                "error" : {
                    "value" : "Params wrong" , "type" : "COWBP-0001"
                }
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
        try:
            curent_user = User.objects.get(id = decoded_token['user_id'])
            orderWaitingBePaid = Order.objects.get(name = nameOrder , user_id = curent_user)
            orderWaitingBePaid.address_receiver = addressReceiver
            orderWaitingBePaid.save()
            response.data = {
                "success" : True , "status" : status.HTTP_200_OK
            }
            response.status_code = status.HTTP_200_OK
            return response
        except Exception as e:
            print(e)
            response.data = {
                "success" : False , "status" : status.HTTP_404_NOT_FOUND ,
                "error" : {
                    "value" : "Information wrong" , "type" : "COWBP-0002"
                }
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
    
    # ---------------------------------------------------------------------------- #
    #                            UPDATE TRANSPORT ORDER                            #
    # ---------------------------------------------------------------------------- #
    @action(method=["POST"],detail=False,url_path="update_transport_order",url_name="update_transport_order")
    def update_transport_order(self, request,*args, **kwargs):
        try:
            data_request= json.loads(request.body.decode('utf-8'))
            transportId = data_request['params']['transport_id']
            nameOrder = data_request['params']['name_order']
            jwtToken = request.COOKIES.get('refresh_token')
            refresh_token = RefreshToken(jwtToken)
            decoded_token = refresh_token.payload
            response = Response()
        except Exception as e:
            print(e)
            response.data = {
                "success" : False , "status" : status.HTTP_404_NOT_FOUND ,
                "error" : {
                    "value" : "Params wrong" , "type" : "UTOBP-0001"
                }
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
        try:
            curent_user = User.objects.get(id = decoded_token['user_id'])
            transport = Transport.objects.get(id = transportId)
            orderWaitingBePaid = Order.objects.get(name = nameOrder , user_id = curent_user)
            orderWaitingBePaid.transport_id = transport
            orderWaitingBePaid.save()
            response.data = {
                "success" : True , "status" : status.HTTP_200_OK
            }
            response.status_code = status.HTTP_200_OK
            return response
        except Exception as e:
            print(e)
            response.data = {
                "success" : False , "status" : status.HTTP_404_NOT_FOUND ,
                "error" : {
                    "value" : "Information wrong" , "type" : "UTOBP-0002"
                }
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response

    # ---------------------------------------------------------------------------- #
    #                                UPDATE VOUCHER                                #
    # ---------------------------------------------------------------------------- #

    @action(method=["POST"],detail=False,url_path="update_voucher_order",url_name="update_voucher_order")
    def update_voucher_order(self, request,*args, **kwargs):
        def isHaveinVoucher(listProductSlug , listDetailVoucher,voucher):
            price = 0
            for productSlug in listProductSlug:
                for productVoucher in listDetailVoucher:
                    if productVoucher.product_id.slug == productSlug.product_id.slug:
                        productPrice = Product.objects.get(slug = productVoucher.product_id.slug)
                        priceProduct = Price.objects.get(product_id = productPrice )
                        priceActiveVoucher = ( priceProduct.price_total *  voucher.sale )/100
                        if priceActiveVoucher > voucher.limited_price:
                            price += voucher.limited_price
                        else:
                            price += priceActiveVoucher
            return price
        try:
            data_request= json.loads(request.body.decode('utf-8'))
            voucher_id = data_request['params']['voucher_id']
            nameOrder = data_request['params']['name_order']
            jwtToken = request.COOKIES.get('refresh_token')
            refresh_token = RefreshToken(jwtToken)
            decoded_token = refresh_token.payload
            response = Response()
        except Exception as e:
            print(e)
            response.data = {
                "success" : False , "status" : status.HTTP_404_NOT_FOUND ,
                "error" : {
                    "value" : "Params wrong" , "type" : "UVOBP-0001"
                }
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
        try:
            curent_user = User.objects.get(id = decoded_token['user_id'])
            orderWaitingBePaid = Order.objects.get(name = nameOrder , user_id = curent_user)
            voucher = Voucher.objects.get(id = voucher_id)
            listDetailVoucher = DetailVoucher.objects.filter(voucher_id = voucher)
            listProductSlug = DetailOrder.objects.filter(order_id=orderWaitingBePaid)
            totalPrice =  isHaveinVoucher(listProductSlug,listDetailVoucher,voucher)

        
            response.data = {
                "success" : totalPrice*1000 , "status" : status.HTTP_200_OK
            }
            response.status_code = status.HTTP_200_OK
            return response
        except Exception as e:
            print(e)
            response.data = {
                "success" : False , "status" : status.HTTP_404_NOT_FOUND ,
                "error" : {
                    "value" : "Information wrong" , "type" : "UVOBP-0002"
                }
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response

    # ---------------------------------------------------------------------------- #
    #                              METHOD ADD TO CART                              #
    # ---------------------------------------------------------------------------- #
    
    @action(method=['POST'],detail=False, url_path="add_to_cart",url_name="add_to_cart")
    def add_to_cart(self, request,*args, **kwargs):
        # ---------------------------------------------------------------------------- #
        #                                global variable                               #
        # ---------------------------------------------------------------------------- #
        check_detail_order = False 
        now = datetime.now()
        quantity = 1
        orderInDetailOrder = False
        # ---------------------------------------------------------------------------- #
        #                              method in function                              #
        # ---------------------------------------------------------------------------- #

        def calcTotalPriceOrder(current_order):
            detailOrderProduct = DetailOrder.objects.filter(order_id = current_order)
            total_price = 0
            for i in detailOrderProduct:
                total_price = total_price + Price.objects.get(product_id = i.product_id).price_total*i.quantity
                print(total_price)
            current_order.total_price = total_price
            current_order.save()
            print(current_order.total_price)
        
        # -------------- method check detail order is available product -------------- #
        def checkDetailOrderIsAvailableProduct(curent_product,curent_order):
            detailOrderProduct = DetailOrder.objects.filter(order_id = curent_order , product_id = curent_product)
            if len(detailOrderProduct) > 0 :
                return detailOrderProduct[0] ,curent_product.slug
            else :
                return False , False
        # ------------ method check product is already in orders previous ------------ #\
        def checkProductIsAlreadyInOrderPrevios(curent_product):
            
            quantity_total = 0
            start_datetime = datetime(
                now.year,now.month , now.day, 0, 0, 0
            )
            detail_orders = DetailOrder.objects.filter(
                order_id__datetime__lt= start_datetime, 
                order_id__user_id = curent_user,
                product_id__slug= curent_product.slug
            )
            orderInDetailOrder = dict()
            if len(detail_orders) > 0 :
                for i in detail_orders:
                    if( i.order_id.id not in orderInDetailOrder):
                        orderInDetailOrder[str(i.order_id.id)] = i.order_id.id
                    quantity_total += i.quantity
                    i.delete()
                return quantity_total,orderInDetailOrder
            else:
                return False,False
        
        # ---------------------------------------------------------------------------- #
        #                            handle logic in fuction                           #
        # ---------------------------------------------------------------------------- #
        # -------------------------------- get params -------------------------------- #
        try:
            data_request= json.loads(request.body.decode('utf-8'))
            product_slug = data_request['params']['product_slug']
            jwtToken = request.COOKIES.get('refresh_token')
            refresh_token = RefreshToken(jwtToken)
            decoded_token = refresh_token.payload
            print("addto cart")
        except :
            return Response({
                "success":False , 'status' : status.HTTP_404_NOT_FOUND ,
                "error" : { "value" : "params wrong" , "type" : "ATC-0001"}
            })
        # ----------------------- check information in database ---------------------- #
        try:
            curent_user = User.objects.get(id = decoded_token['user_id'])
            product = Product.objects.get(slug = product_slug)
            price_product = Price.objects.filter(product_id = product, status = True)
            photo_product = Photo_product.objects.filter(product_id = product)
            address_default = Address.objects.filter(user_id = curent_user , status = True )
            phone_user_default = PhoneUser.objects.filter(user_id = curent_user , status = True)
            transport = Transport.objects.all()
            quantity_check,orderInDetailOrder = checkProductIsAlreadyInOrderPrevios(product)
            if quantity_check !=  False :
                    quantity += quantity_check
        
        except Exception as e:
            # ------------------ failure if information not in database ------------------ #
            print("ERROR :", e)
            return Response({
                "success":False , 'status' : status.HTTP_404_NOT_FOUND ,
                "error" : { "value" : "Information wrong" , "type" : "ATC-0002"}
            })
        # ------------------- check the order is available today ------------------ #
        order_id = checkTheOrderIsAvailebleToDay(curent_user,now)
        print('order_id',order_id)
        if order_id != False:
            # ------------------ check detail order is available product ----------------- #
            checkDetailProduct,check_detail_order = checkDetailOrderIsAvailableProduct(product,order_id)
            if checkDetailProduct != False:
                checkDetailProduct.quantity += 1
                checkDetailProduct.save()
            else :   
                detailproduct = DetailOrder.objects.create(
                    product_id = product , 
                    order_id = order_id , 
                    status = False ,
                    quantity = quantity
                )
                detailproduct.save()
            calcTotalPriceOrder(order_id)
        else :
            # ------------- if not order is available today create order new ------------- #
            try:
                order_new = Order.objects.create(
                    name = uuid4(),
                    datetime = now,
                    receiver = phone_user_default[0].name,
                    address_receiver = address_default[0].address_content ,
                    phone_receiver = phone_user_default[0].phone ,
                    status = False ,
                    note = 'no',
                    logs = 'no',
                    is_payment = False,
                    total_price = price_product[0].price_total,
                    cancel = False ,
                    request_cancel = False ,
                    user_id = curent_user,
                    transport_id = transport[0]
                )
                order_new.save()
                print('order_new',order_new.status)
                try:
                    detailproduct = DetailOrder.objects.create(
                    product_id = product , 
                    order_id = order_new, 
                    status = False ,
                    quantity = quantity
                )
                    detailproduct.save()
                except Exception as e:
                    print(e)
                    detailproduct.delete()
                    order_new.delete()
                    return Response({"success": False , "status" : status.HTTP_404_NOT_FOUND})
            except Exception as e:
                print(e)
                order_new.delete()
                return Response({"success": False , "status" : status.HTTP_404_NOT_FOUND})
        product_response = {
            'category_name' : product.category_id.name,
            'photo_product' : photo_product[0].data ,
            'product_description' : product.description,
            'product_name' : product.name ,
            'product_price' : price_product[0].price,
            'product_price_status' : price_product[0].status,
            'product_price_total' : price_product[0].price_total,
            'product_sale' : price_product[0].sale ,
            'product_slug' : product.slug,
            'product_quantity' : quantity
        }
        serializer = ProductSerializer(product_response,many= False)
        
        return Response({
            "success": serializer.data , "check_detail_order" : check_detail_order ,
            'order_in_detail_order' : orderInDetailOrder , "status" : status.HTTP_200_OK
        })

    # ---------------------------------------------------------------------------- #
    #                         METHOD REMOVE PRODUCT IN CART                        #
    # ---------------------------------------------------------------------------- #
    @action(method=['POST'],detail=False, url_path="remove_product_in_cart",url_name="remove_product_in_cart")
    def remove_product_in_cart(self, request,*args, **kwargs):
        try: 
            # ---------------------------- check params input ---------------------------- #
            data_request= json.loads(request.body.decode('utf-8'))
            name_order = data_request['params']['name_order']
            product_slug = data_request['params']['product_slug']
            jwtToken = request.COOKIES.get('refresh_token')
            refresh_token = RefreshToken(jwtToken)
            decoded_token = refresh_token.payload
        except:
            return Response({
                "sucess" : False , "status" : status.HTTP_404_NOT_FOUND ,
                "error" : { "value" : "Params wrong" , "type" : "RPIC-0001"}
            })
        try:
            # -------------------------- check information post -------------------------- #
            curent_user = User.objects.get(id = decoded_token['user_id'])
            curent_order = Order.objects.get(name = name_order,user_id = curent_user)
            curent_detail_order = DetailOrder.objects.filter(order_id = curent_order , product_id__slug = product_slug )
            priceProduct = Price.objects.filter( product_id__slug = product_slug , status = True)
            curent_order.total_price = curent_order.total_price - priceProduct[0].price_total*curent_detail_order[0].quantity
            curent_detail_order.delete()
            curent_order.save()
            return Response({"success": True , "status" : status.HTTP_200_OK})  
        except Exception as e:
            print(e)
            return Response({
                "sucess" : False , "status" : status.HTTP_404_NOT_FOUND ,
                "error" : { "value" : "Information wrong" , "type" : "RPIC-0002"}
            })
    # ---------------------------------------------------------------------------- #
    #                            METHOD GET ORDER TODAY                            #
    # ---------------------------------------------------------------------------- #

    @action(method=["GET"],detail=False,url_path="get_order_today",url_name="get_order_today")
    def get_order_today(self, request,*args, **kwargs):
        try:
            # ---------------------------- check params input ---------------------------- #
            jwtToken = request.COOKIES.get('refresh_token')
            refresh_token = RefreshToken(jwtToken)
            decoded_token = refresh_token.payload
        except:
            return Response({
                "sucess" : False , "status" : status.HTTP_404_NOT_FOUND ,
                "error" : { "value" : "Params input wrong" , "type" : "GOT-0001"}
            })
        try:
            # ----------------------------- check information ---------------------------- #
            curent_user = User.objects.get(id = decoded_token['user_id'])
            now = datetime.now()
            start_datetime = datetime(
                now.year,now.month , now.day, 0, 0, 0
            ) 
            end_datetime = datetime(
                now.year,now.month , now.day, 23, 59, 59
            )
            orderQuery = Order.objects.raw(
                raw_query.QUERY_SQL_GET_ALL_ORDER_FOR_USER_BETWEEN_DAYS,
                [curent_user.id,start_datetime,end_datetime]
            )
            if len(orderQuery) > 0:
                queryset,numberProduct = data_processing.handleRawQuery(orderQuery)
        
                serializer = OrderHandleDataSerializer(queryset,many = True)
                
                return Response({
                    "data" : serializer.data , "status" : status.HTTP_200_OK , 
                    'numberProduct' : numberProduct
                })
            else :
                return Response({
                    "data" : [] , "status" : status.HTTP_200_OK , 'numberProduct' : 0
                })
        except:
           return Response({
                "sucess" : False , "status" : status.HTTP_404_NOT_FOUND ,
                "error" : { "value" : "Information wrong" , "type" : "GOT-0001"}
            }) 
    
    # ---------------------------------------------------------------------------- #
    #                           METHOD CHANGE ORDER TODAY                          #
    # ---------------------------------------------------------------------------- #
    @action(method=["POST"],detail=False,url_path="get_order_today",url_name="get_order_today")
    def change_order_today(self, request,*args, **kwargs):
        try:
            # ---------------------------- check params input ---------------------------- #
            data_request= json.loads(request.body.decode('utf-8'))
            jwtToken = request.COOKIES.get('refresh_token')
            refresh_token = RefreshToken(jwtToken)
            decoded_token = refresh_token.payload
            type =data_request['params']['type']
        except:
            return Response({
                "sucess" : False , "status" : status.HTTP_404_NOT_FOUND ,
                "error" : { "value" : "Params input wrong" , "type" : "GOT-0001"}
            })
        try:
            # ----------------------------- check information ---------------------------- #
            curent_user = User.objects.get(id = decoded_token['user_id'])
            transport = Transport.objects.all()
            now = datetime.now()
            order_today = checkTheOrderIsAvailebleToDay(curent_user,now)
            if order_today != False :
                # --------------------------------- case type -------------------------------- #
                match type:
                    case 1:
                        address_change = data_request['params']['address_change']
                        phone_change = data_request['params']['phone_change']
                        order_today.address_receiver = address_change['address_content']
                        order_today.receiver = phone_change['name']
                        order_today.phone_receiver = phone_change['phone']
                        order_today.save()
                        return Response({
                            "success" : "change success" , "status" : status.HTTP_200_OK 
                        })
                # --------------------------------- end case --------------------------------- #
            else :
                # --------------------------------- case type -------------------------------- #
                
                match type:
                    case 1:
                        address_change = data_request['params']['address_change']
                        phone_change = data_request['params']['phone_change']
                        order_new = Order.objects.create(
                            name = uuid4(),
                            datetime = now,
                            receiver = phone_change.name,
                            address_receiver = address_change.address_change ,
                            phone_receiver = phone_change.phone ,
                            status = False ,
                            note = 'no',
                            logs = 'no',
                            total_price = 0,
                            cancel = False ,
                            request_cancel = False ,
                            user_id = curent_user,
                            transport_id = transport[0]
                        )
                        order_new.save()
                        return Response({
                            "success" : "change success" , "status" : status.HTTP_200_OK 
                        })
                # --------------------------------- end case --------------------------------- #
                return Response({
                    "success" : "created order today" , 'status': status.HTTP_201_CREATED 
                })
        except Exception as e:
            print(e)
            return Response({
                "sucess" : False , "status" : status.HTTP_404_NOT_FOUND ,
                "error" : { "value" : "Information wrong" , "type" : "GOT-0001"}
            }) 
    
    # ---------------------------------------------------------------------------- #
    #                    METHOD CHANGE QUANTITY PRODUCT IN CART                    #
    # ---------------------------------------------------------------------------- #
    @action(method=['POST'],detail=False, url_path="change_quantity_product_in_cart",url_name="change_quantity_product_in_cart")
    def change_quantity_product_in_cart(self, request,*args, **kwargs):
        try: 
            # ---------------------------- check params input ---------------------------- #
            data_request= json.loads(request.body.decode('utf-8'))
            print(data_request)
            name_order = data_request['params']['name_order']
            product_slug = data_request['params']['product_slug']
            value_change = data_request['params']['value']
            type = data_request['params']['type']
            jwtToken = request.COOKIES.get('refresh_token')
            refresh_token = RefreshToken(jwtToken)
            decoded_token = refresh_token.payload
        except Exception as e:
            print(e)
            return Response({
                "sucess" : False , "status" : status.HTTP_404_NOT_FOUND ,
                "error" : { "value" : "Params wrong" , "type" : "RPIC-0001"}
            })
        try:
            # -------------------------- check information post -------------------------- #
            curent_user = User.objects.get(id = decoded_token['user_id'])
            curent_order = Order.objects.get(name = name_order,user_id = curent_user)
            curent_detail_order = DetailOrder.objects.get(order_id = curent_order , product_id__slug = product_slug )
            if type == 1:
                curent_detail_order.quantity = value_change
            else : 
                curent_detail_order.quantity =  int(curent_detail_order.quantity) + int(value_change)
            curent_detail_order.save()    
            for price_total in Order.objects.raw(raw_query.SUM_TOTAL_PRICE_IN_ORDER.format(order = str(curent_order.id).replace('-',''))):
                curent_order.total_price = price_total.order_total_price
                print("price_total.order_total_price", price_total)     
            curent_order.save()
            
            return Response({"success": True , "status" : status.HTTP_200_OK})  
        except Exception as e:
            print(e)
            return Response({
                "sucess" : False , "status" : status.HTTP_404_NOT_FOUND ,
                "error" : { "value" : "Information wrong" , "type" : "CPIC-0002"}
            })
    
    @action(method=["POST"],detail=False,url_path="update_payment_order",url_name="update_payment_order")
    def update_payment_order(self, request,*args, **kwargs):
        try:
            data_request= json.loads(request.body.decode('utf-8'))
            total_price = data_request['params']['total_price']
            type_payment = data_request['params']['type']
            nameOrder = data_request['params']['name_order']
            jwtToken = request.COOKIES.get('refresh_token')
            refresh_token = RefreshToken(jwtToken)
            decoded_token = refresh_token.payload
            response = Response()
        except Exception as e:
            print(e)
            response.data = {
                "success" : False , "status" : status.HTTP_404_NOT_FOUND ,
                "error" : {
                    "value" : "Params wrong" , "type" : "COWBP-0001"
                }
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
        try:
            curent_user = User.objects.get(id = decoded_token['user_id'])
            orderWaitingBePaid = Order.objects.get(name = nameOrder , user_id = curent_user)
            orderWaitingBePaid.is_payment = True
            orderWaitingBePaid.save()
            if type_payment :
                payment  = Payment.objects.create(
                    order_id = orderWaitingBePaid ,
                    type = True ,
                    total_price = total_price,
                    cod = True ,
                )
                payment.save()
            else:
                payment  = Payment.objects.create(
                    order_id = orderWaitingBePaid ,
                    type = False ,
                    total_price = total_price,
                    cod = False ,
                )
                payment.save()
            response.data = {
                "success" : True , "status" : status.HTTP_200_OK
            }
            response.status_code = status.HTTP_200_OK
            return response
        except Exception as e:
            print(e)
            response.data = {
                "success" : False , "status" : status.HTTP_404_NOT_FOUND ,
                "error" : {
                    "value" : "Information wrong" , "type" : "COWBP-0002"
                }
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response