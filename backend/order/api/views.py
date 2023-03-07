queryRawSql = """
    SELECT order_order.*, order_detailorder.status as 'detail_order_status' ,
        product_product.slug as 'product_slug' , product_product.name as 'product_name',
        product_product.description as 'product_description',
        product_category.name as 'category_name', product_price.price as 'product_price',
        product_price.sale as 'product_sale' , product_price.status as 'product_price_status',
        product_price.price_total as 'product_price_total' , product_photo_product.data as 'photo_product',
        order_transport.slug as 'transport_slug' , order_transport.name as 'transport_name' ,
        order_transport.logo as 'transport_logo' , order_transport.price as 'transport_price',
        `order_detailorder`.`quantity` as 'product_quantity'
    FROM
        order_detailorder,product_product,product_price, order_transport,
        product_photo_product , product_category,order_order,login_user
    WHERE 
        order_order.id = order_detailorder.order_id_id 
        and order_transport.id = order_order.transport_id_id 
        and login_user.id = %s  
        and login_user.id = order_order.user_id_id
        and product_product.id = order_detailorder.product_id_id 
        and product_product.id = product_photo_product.product_id_id 
        and product_product.id = product_price.product_id_id
        and product_product.category_id_id = product_category.id
    ORDER BY
        order_order.datetime DESC
"""

from order.models import Order , Transport , DetailOrder
from login.models import User , Address , PhoneUser 
from product.models import Product , Price ,Photo_product
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import OrderHandleDataSerializer ,ProductSerializer ,TransportModelSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from uuid import uuid4
import json
from . import data_processing

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
        token_permission_infor_user = request.GET['token_permission_infor_user']
        try:
            curent_user = User.objects.get(token_permission_infor_user=token_permission_infor_user)
        except:
            return Response({"success":False})
        check_order_today = checkTheOrderIsAvailebleToDay(curent_user,datetime.now())
        if check_order_today != False :
           check_order_today = True
        queryset,numberProduct = data_processing.handleRawQuery(Order.objects.raw(queryRawSql,[curent_user.id]))
        
        serializer = OrderHandleDataSerializer(queryset,many = True)
        
        return Response({"success":serializer.data , "number_product" : numberProduct , "check_order_today" : check_order_today })
    
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
        
        data_request= json.loads(request.body.decode('utf-8'))
        token_permission_infor_user = data_request['params']['token_permission_infor_user']
        product_slug = data_request['params']['product_slug']

        # ----------------------- check information in database ---------------------- #
        try:
            curent_user = User.objects.get(token_permission_infor_user=token_permission_infor_user)
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
            return Response({"success":False})
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
                    return Response({"success": False})
            except Exception as e:
                print(e)
                order_new.delete()
                return Response({"success": False})
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
        return Response({"success": serializer.data , "check_detail_order" : check_detail_order ,
                         'order_in_detail_order' : orderInDetailOrder
                         })

    # ---------------------------------------------------------------------------- #
    #                         METHOD REMOVE PRODUCT IN CART                        #
    # ---------------------------------------------------------------------------- #
    @action(method=['POST'],detail=False, url_path="remove_product_in_cart",url_name="remove_product_in_cart")
    def remove_product_in_cart(self, request,*args, **kwargs):
        data_request= json.loads(request.body.decode('utf-8'))
        token_permission_infor_user = data_request['params']['token_permission_infor_user']
        name_order = data_request['params']['name_order']
        product_slug = data_request['params']['product_slug']
        
        try:
            # -------------------------- check information post -------------------------- #
            curent_user = User.objects.get(token_permission_infor_user = token_permission_infor_user)
            curent_order = Order.objects.get(name = name_order,user_id = curent_user)
            curent_detail_order = DetailOrder.objects.filter(order_id = curent_order , product_id__slug = product_slug )
            curent_detail_order.delete()
        except Exception as e:
            return Response({"sucess" : False})
        
        return Response({"success": True })

        