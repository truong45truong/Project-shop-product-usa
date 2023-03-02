queryRawSql = """
    SELECT order_order.*, order_detailorder.status as 'detail_order_status' ,
        product_product.slug as 'product_slug' , product_product.name as 'product_name',
        product_product.description as 'product_description',
        product_category.name as 'category_name', product_price.price as 'product_price',
        product_price.sale as 'product_sale' , product_price.status as 'product_price_status',
        product_price.price_total as 'product_price_total' , product_photo_product.data as 'photo_product',
        order_transport.slug as 'transport_slug' , order_transport.name as 'transport_name' ,
        order_transport.logo as 'transport_logo' , order_transport.price as 'transport_price'
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
class TransportViewSet(viewsets.ViewSet):
    @action(method=["GET"],detail=False,url_path="get_transport",url_name="get_transport")
    def get_transport(self, request,*args, **kwargs):
        querySql = """
                SELECT 
                    `order_transport`.`id` as transport_id, 
                    `order_transport`.`slug` as transport_slug, 
                    `order_transport`.`name` as transport_name, 
                    `order_transport`.`logo` as transport_logo,
                    `order_transport`.`price`as transport_price
                FROM 
                    `order_transport`
        """
        try:
            queryset = Transport.objects.all()
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
        queryset,numberProduct = data_processing.handleRawQuery(Order.objects.raw(queryRawSql,[curent_user.id]))
        
        serializer = OrderHandleDataSerializer(queryset,many = True)
        
        return Response({"success":serializer.data , "number_product" : numberProduct})
    
    # ---------------------------------------------------------------------------- #
    #                              METHOD ADD TO CART                              #
    # ---------------------------------------------------------------------------- #
    
    @action(method=['POST'],detail=False, url_path="add_to_cart",url_name="add_to_cart")
    def add_to_cart(self, request,*args, **kwargs):
        data_request= json.loads(request.body.decode('utf-8'))
        token_permission_infor_user = data_request['params']['token_permission_infor_user']
        product_slug = data_request['params']['product_slug']
        try:
            curent_user = User.objects.get(token_permission_infor_user=token_permission_infor_user)
            product = Product.objects.get(slug = product_slug)
            price_product = Price.objects.filter(product_id = product, status = True)
            photo_product = Photo_product.objects.filter(product_id = product)
            address_default = Address.objects.filter(user_id = curent_user , status = True )
            phone_user_default = PhoneUser.objects.filter(user_id = curent_user , status = True)
            transport = Transport.objects.all()
        except Exception as e:
            print("ERROR :", e)
            return Response({"success":False})
        now = datetime.now()
        print(now)
        start_datetime = datetime(
            now.year,now.month , now.day, 0, 0, 0
        ) 
        end_datetime = datetime(
            now.year,now.month , now.day, 23, 59, 59
        )
        
        order_current = Order.objects.filter(datetime__range=[start_datetime, end_datetime] , user_id = curent_user)
        if len(order_current) > 0:
            
            detailproduct = DetailOrder.objects.create(
                product_id = product , 
                order_id = order_current[0] , 
                status = False ,
                quantity = 1
            )
            print(order_current)
            detailproduct.save()
        else :
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
                    quantity = 1
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
            'product_slug' : product.slug
        }
        serializer = ProductSerializer(product_response,many= False)
        return Response({"success": serializer.data})

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
            print(curent_detail_order)
        except Exception as e:
            return Response({"sucess" : False})
        
        return Response({"success": curent_detail_order})

        