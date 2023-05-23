from .serializers import OrderHandleDataSerializer ,ProductSerializer ,TransportModelSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework import status
from order.models import Order , Transport , DetailOrder
from product.models import Product , Price ,Photo_product
from login.models import User , Address , PhoneUser 
from datetime import datetime
from rest_framework_simplejwt.tokens import RefreshToken
from uuid import uuid4
import json
from . import data_processing,raw_query

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
                    total_price = price_product[0].price_total,
                    cancel = False ,
                    request_cancel = False ,
                    user_id = curent_user,
                    transport_id = transport[0]
                )
                order_new.save()
                print(order_new)
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