from rest_framework.decorators import api_view,action,permission_classes,authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from login.models import User,PhoneUser , Address
from . import query_raw
from .serializers import UserAdminSerializer
import json
# ---------------------------------------------------------------------------- #
#                              GET ALL USER PAPGE                              #
# ---------------------------------------------------------------------------- #
@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def getAllUserPage(request):
    response = Response()
    queryRaw = query_raw.QUERY_GET_ALL_USER_WITH_PAGE
    def notFound():
        response.data = {
            "success" : False , 'error' : {
                'type' : "CGIA-001" , 'value' : "Failed to Login"
            } , 
            'status' : status.HTTP_404_NOT_FOUND
        }
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
    def getUser(page,numberQuantity):


        handleRaw = query_raw.HandleQueryRaw(queryRaw)
        handleRaw.setPage(page,numberQuantity)
        queryset = User.objects.raw(handleRaw.getQueryRaw())
        serializer = UserAdminSerializer(queryset , many = True)
        response.data = {
            "success" : True ,
            'users' : serializer.data,
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
        return getUser(page,numberQuantity)
        
    except Exception as e:
        print(e)
        return notFound()
    


# ---------------------------------------------------------------------------- #
#                                  DELETE USER                                 #
# ---------------------------------------------------------------------------- #
@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def DelUsers(request):
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
    def delUser(users_del):
        usersDeleted = []
        for username in users_del:
            try:
                userDel = User.objects.get(username = username)
                usersDeleted.append(userDel.username)
                userDel.delete()
            except:
                pass
        response.data = {
            "success" : True ,
            "users_deleted" : usersDeleted ,
            'status' : status.HTTP_200_OK
        }
        response.status_code = status.HTTP_200_OK
        return response
    try:
        jwtToken = request.COOKIES.get('refresh_token')
        refresh_token = RefreshToken(jwtToken)
        decoded_token = refresh_token.payload
        data_request= json.loads(request.body.decode('utf-8'))
        print(data_request)
        users_del = data_request['params']['users_del']
    except Exception as e:
        print(e)
        return notFound()
    try:
        user = User.objects.get(id = decoded_token['user_id'])
        if user.is_superuser == False:
            return notFound()
        return delUser(users_del)
        
    except Exception as e:
        print(e)
        return notFound()
    
@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def searchUserAdmin(request):
    response = Response()
    queryRaw = query_raw.QUERY_SEARCH_USER
    def notFound():
        response.data = {
            "success" : False , 'error' : {
                'type' : "CGIA-001" , 'value' : "Failed to Login"
            } , 
            'status' : status.HTTP_404_NOT_FOUND
        }
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
    def getUser(key_search):
        handleRaw = query_raw.HandleQueryRaw(queryRaw)
        handleRaw.SetKeySearchUser(key_search)
        print(handleRaw.getQueryRaw())
        queryset = User.objects.raw(handleRaw.getQueryRaw())
        
        serializer = UserAdminSerializer(queryset , many = True)
        response.data = {
            "success" : True ,
            'users' : serializer.data,
            'status' : status.HTTP_200_OK
        }
        response.status_code = status.HTTP_200_OK
        return response
    try:
        jwtToken = request.COOKIES.get('refresh_token')
        refresh_token = RefreshToken(jwtToken)
        decoded_token = refresh_token.payload
        key_search = request.GET.get('key_search')
    except Exception as e:
        print(e)
        return notFound()
    try:
        user = User.objects.get(id = decoded_token['user_id'])
        print('user.is_superuser',user.is_superuser)
        if user.is_superuser == False:
            return notFound()
        return getUser(key_search)
        
    except Exception as e:
        print(e)
        return notFound()