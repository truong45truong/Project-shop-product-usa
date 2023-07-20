from rest_framework.decorators import api_view,action,permission_classes,authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from login.models import User
from order.models import Order,DetailOrder
from .serializers import OrderRawSerializer , OrderSerializer
from . import query_raw
import uuid
from datetime import datetime
import json
@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def getAllOrderAdmin(request):
    response = Response()
    rawQuery = query_raw.GET_ALL_ORDER_ADMIN
    def notFound():
        response.data = {
            "success" : False , 'error' : {
                'type' : "CGIA-001" , 'value' : "Failed to Login"
            } , 
            'status' : status.HTTP_404_NOT_FOUND
        }
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
    def getOrders(page,numberQuantity , date_start , date_end):
        handleQuery = query_raw.HandleQueryRaw(rawQuery)
        handleQuery.setPage(page,numberQuantity)
        handleQuery.setDate(date_start,date_end)
        queryset = Order.objects.raw(handleQuery.getQueryRaw)
        serializer = OrderRawSerializer(queryset,many = True)
        response.data = {
            "success" : True ,
            'orders' : serializer.data ,
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
        date_start = request.GET.get('date_start')
        date_end = request.GET.get('date_end')
    except Exception as e:
        print(e)
        return notFound()
    try:
        user = User.objects.get(id = decoded_token['user_id'])
        print('user.is_superuser',user.is_superuser)
        if user.is_superuser == False:
            return notFound()
        return getOrders(page,numberQuantity , date_start , date_end)
        
    except Exception as e:
        print(e)
        return notFound()

@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def getAllOrderRequestAdmin(request):
    response = Response()
    rawQuery = query_raw.GET_ALL_ORDER_REQUEST_ADMIN
    def notFound():
        response.data = {
            "success" : False , 'error' : {
                'type' : "CGIA-001" , 'value' : "Failed to Login"
            } , 
            'status' : status.HTTP_404_NOT_FOUND
        }
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
    def getOrders(page,numberQuantity):
        queryset = Order.objects.filter(status = True , confirm = False ,  cancel = False , is_payment = False)
        serializer = OrderSerializer(queryset,many = True)
        print(serializer.data)
        response.data = {
            "success" : True ,
            'orders' : serializer.data ,
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
        if user.is_superuser == False:
            return notFound()
        return getOrders(page,numberQuantity)
        
    except Exception as e:
        print(e)
        return notFound()

@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def getAllOrderConfirmAdmin(request):
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
    def getOrders(page,numberQuantity):
        queryset = Order.objects.filter(status = True , confirm = True ,  cancel = False , is_payment = False)
        serializer = OrderSerializer(queryset,many = True)
        response.data = {
            "success" : True ,
            'orders' : serializer.data ,
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
        if user.is_superuser == False:
            return notFound()
        return getOrders(page,numberQuantity)
        
    except Exception as e:
        print(e)
        return notFound()
    
@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def getAllOrderPaymentedAdmin(request):
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
    def getOrders(page,numberQuantity):
        queryset = Order.objects.filter(status = True , is_payment = True)
        serializer = OrderSerializer(queryset,many = True)
        response.data = {
            "success" : True ,
            'orders' : serializer.data ,
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
        if user.is_superuser == False:
            return notFound()
        return getOrders(page,numberQuantity)
        
    except Exception as e:
        print(e)
        return notFound()
@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def confirmOrderAdmin(request):
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
    def updateOrder(order_selected):
        for order_id in order_selected:
            order = Order.objects.get(id = order_id)
            order.confirm = True
            order.save()
        response.data = {
            "success" : True,
            "status" : status.HTTP_200_OK
        }
        response.status_code = status.HTTP_200_OK
        return response
    try:
        jwtToken = request.COOKIES.get('refresh_token')
        refresh_token = RefreshToken(jwtToken)
        decoded_token = refresh_token.payload
        data_request= json.loads(request.body.decode('utf-8'))
        order_selected = data_request['params']['order_selected']
    except Exception as e:
        print(e)
        return notFound()
    try:
        user = User.objects.get(id = decoded_token['user_id'])
        if user.is_superuser == False:
            return notFound()
        return updateOrder(order_selected)
        
    except Exception as e:
        print(e)
        return notFound()

@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def cancelOrderAdmin(request):
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
    def updateOrder(order_selected):
        for order_id in order_selected:
            order = Order.objects.get(id = order_id)
            order.cancel = True
            order.save()
        response.data = {
            "success" : True,
            "status" : status.HTTP_200_OK
        }
        response.status_code = status.HTTP_200_OK
        return response
    try:
        jwtToken = request.COOKIES.get('refresh_token')
        refresh_token = RefreshToken(jwtToken)
        decoded_token = refresh_token.payload
        data_request= json.loads(request.body.decode('utf-8'))
        order_selected = data_request['params']['order_selected']
    except Exception as e:
        print(e)
        return notFound()
    try:
        user = User.objects.get(id = decoded_token['user_id'])
        if user.is_superuser == False:
            return notFound()
        return updateOrder(order_selected)
        
    except Exception as e:
        print(e)
        return notFound()