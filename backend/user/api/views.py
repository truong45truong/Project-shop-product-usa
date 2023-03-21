from .serializers import UserSerializer,PhoneUserSerializer,AddressSerializer

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework import status

from login.models import User,PhoneUser,Address

import json


        
class InforUserViewSet (viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = []
    permission_classes = []
    # ---------------------------------------------------------------------------- #
    #                                GET INFOR USER                                #
    # ---------------------------------------------------------------------------- #
    @action(methods = ["GET"], detail = False, url_path = "get_infor_user", url_name = "get_infor_user")
    def get_infor_user(self,request,*args, **kwargs):
        try:
            # ---------------------------- check params input ---------------------------- #
            jwtToken = request.COOKIES.get('refresh_token')
            # decrypt token jwt
            refresh_token = RefreshToken(jwtToken)
            decoded_token = refresh_token.payload
            response = Response()
        except:
            response.data =  { 
                'success' : "get infor user failure"  , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : "Params input wrong" , 'type' : "GIU-0001" }
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
        
        try: 
            # ----------------------------- check information ---------------------------- #
            user_current = User.objects.get(id = decoded_token['user_id'])
            serializer = UserSerializer(user_current,many=False)
            response.data = { 'user' : serializer.data  , 'error' : { 'value' : None , 'type' : None }, 'status' : status.HTTP_200_OK}
            response.status_code = status.HTTP_200_OK
            return response
        except:
            response.data = { 
                'user' : "Information wrong"  , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : "wrong user" , 'type' : "GIU-0002" }
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
class PhoneUserViewSet(viewsets.ModelViewSet):
    queryset = PhoneUser.objects.all()
    serializer_class = PhoneUserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # ---------------------------------------------------------------------------- #
    #                          METHOD GET ADDRESS FOR USER                         #
    # ---------------------------------------------------------------------------- #
    @action(method = ['GET'] , detail= False , url_path='get_phone_user' , url_name= 'get_phone_user')
    def get_phone_user(self , request ,  *args, **kwargs):
        try:
            # ---------------------------- check params input ---------------------------- #
            # decryption token jwt
            jwtToken = request.COOKIES.get('refresh_token')
            refresh_token = RefreshToken(jwtToken)
            decoded_token = refresh_token.payload
        except:
            return Response({ 
                'phone' : 'Get phone failure'  , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : 'Params input wrong' , 'type' : 'GPU-0001' }
            },status.HTTP_404_NOT_FOUND)
        
        try:
            # ----------------------------- check information ---------------------------- #
            user_curent = User.objects.get(id=decoded_token['user_id'])
            queryset = PhoneUser.objects.filter(user_id = user_curent)
            serializer = PhoneUserSerializer(queryset,many = True)
            return Response({
                'success' : serializer.data , 'status' : status.HTTP_200_OK
            }, status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({ 
                'phone' : 'Get phone failure'  , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : 'Information wrong' , 'type' : 'GPU-0002' }
            }, status.HTTP_404_NOT_FOUND)
        
    # ---------------------------------------------------------------------------- #
    #                          METHOD CREATE PHONE OF USER                         #
    # ---------------------------------------------------------------------------- #
    
    @action(method = ['POST'], detail = False , url_path='create_phone_user', url_name='create_phone_user')
    def create_phone_user(self , request , *args, **kwargs):
        try:
            # ---------------------------- check params input ---------------------------- #
            data_request= json.loads(request.body.decode('utf-8'))
            phone_user = data_request['params']['phone_user']
            name_user = data_request['params']['name_user']
            status_phone = data_request['params']['status']
            # decryption token jwt
            jwtToken = request.COOKIES.get('refresh_token')
            refresh_token = RefreshToken(jwtToken)
            decoded_token = refresh_token.payload
        except : 
            return Response({ 
                'phone' : 'Creatte phone wrong'  , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : 'Params input wrong' , 'type' : 'CPU-0001' }
            },status.HTTP_404_NOT_FOUND)
        
        try:
            # ----------------------------- check information ---------------------------- #
            user = User.objects.get(id=decoded_token['user_id'])
            if status_phone == True :
                list_phone_status_true = PhoneUser.objects.filter(user_id = user , status = True)
                for item in list_phone_status_true:
                    phone_status_true = PhoneUser.objects.get(id = item.id)
                    phone_status_true.status = False
                    phone_status_true.save()
            phone_user_create = PhoneUser.objects.create(
                phone = phone_user , name = name_user , user_id = user , status = status_phone
            )
            phone_user_create.save()
            serializer = PhoneUserSerializer(phone_user_create,many = False)
            return Response({
                'phone' : serializer.data , 'status' : status.HTTP_200_OK
            }, status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({ 
                'phone' : 'Creatte phone wrong'  , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : 'Information wrong' , 'type' : 'CPU-0002' }
            }, status.HTTP_404_NOT_FOUND)

    
    # ---------------------------------------------------------------------------- #
    #                          METHOD DELETE PHONE OF USER                         #
    # ---------------------------------------------------------------------------- #
    @action(method = ['POST'] , detail= False , url_path='delete_phone_user' , url_name= 'delete_phone_user')
    def delete_phone_user(self , request ,  *args, **kwargs):
        try:
            # ---------------------------- check params input ---------------------------- #
            data_request = json.loads(request.body.decode('utf-8'))
            phone_user_id = data_request['params']['phone_user_id']
            # decryption token jwt
            jwtToken = request.COOKIES.get('refresh_token')
            refresh_token = RefreshToken(jwtToken)
            decoded_token = refresh_token.payload
        except:
            return Response({ 
                'phone' : 'Delete phone wrong'  , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : 'Params input wrong' , 'type' : 'DPU-0001' }
            },status.HTTP_404_NOT_FOUND)
        
        try:
            # ----------------------------- check information ---------------------------- #
            user_delete_phone = User.objects.get(id=decoded_token['user_id'])
            phone_user_delete = PhoneUser.objects.get(id = phone_user_id, user_id = user_delete_phone , status = False)
            phone_user_delete.delete()
            return Response({
                'success' : "Delete phone success" , 'status' : status.HTTP_200_OK
            }, status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({ 
                'phone' : 'Delete phone wrong'  , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : 'Information wrong' , 'type' : 'DPU-0002' }
            }, status.HTTP_404_NOT_FOUND)
        
    
    # ---------------------------------------------------------------------------- #
    #                           METHOD UPDATE PHONE USER                           #
    # ---------------------------------------------------------------------------- #
     
    @action(method = ['POST'] , detail= False , url_name= 'update_phone_user', url_path= 'update_phone_user')
    def update_phone_user(self , request , *args, **kwargs):
        try:
            # ---------------------------- check params input ---------------------------- #
            data_request = json.loads(request.body.decode('utf-8'))
            phone_user_id = data_request['params']['phone_user_id']
            phone_update = data_request['params']['phone_update']
            name_update = data_request['params']['name_update']
            # decryption token jwt
            jwtToken = request.COOKIES.get('refresh_token')
            refresh_token = RefreshToken(jwtToken)
            decoded_token = refresh_token.payload
        except:
            return Response({ 
                'phone' : 'Update phone wrong'  , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : 'Information wrong' , 'type' : 'UPU-0001' }
            }, status.HTTP_404_NOT_FOUND)
            
        try :
            # ----------------------------- check information ---------------------------- #
            user_update_phone = User.objects.get(id=decoded_token['user_id'])
            phone_user_update = PhoneUser.objects.get(id = user_update_phone)
            phone_user_update.phone = phone_update
            phone_user_update.bane = name_update
            phone_user_update.save()
            serializer = PhoneUserSerializer(queryset = phone_user_update , mang = False)
            return Response({
                'phone' : serializer.data , 'status' : status.HTTP_200_OK
            }, status.HTTP_200_OK)
        except:
            return Response({ 
                'phone' : 'Update phone wrong'  , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : 'Information wrong' , 'type' : 'UPU-0002' }
            }, status.HTTP_404_NOT_FOUND)
        
        
class AddressUserViewset (viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    # ---------------------------------------------------------------------------- #
    #                          METHOD GET ADDRESS FOR USER                         #
    # ---------------------------------------------------------------------------- #
    @action(method = ['GET'] , detail= False , url_path='get_address_user' , url_name= 'get_address_user')
    def get_address_user(self , request ,  *args, **kwargs):
        try:
            # ---------------------------- check params input ---------------------------- #
            # decryption token jwt
            jwtToken = request.COOKIES.get('refresh_token')
            refresh_token = RefreshToken(jwtToken)
            decoded_token = refresh_token.payload
        except:
            return Response({ 
                'address' : 'Get address failure'  , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : 'Params input wrong' , 'type' : 'GAU-0001' }
            },status.HTTP_404_NOT_FOUND)
        
        try:
            # ----------------------------- check information ---------------------------- #
            user_curent = User.objects.get(id=decoded_token['user_id'])
            queryset = Address.objects.filter(user_id = user_curent)
            serializer = AddressSerializer(queryset,many = True)
            return Response({
                'success' : serializer.data , 'status' : status.HTTP_200_OK
            }, status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({ 
                'address' : 'Get address failure'  , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : 'Information wrong' , 'type' : 'GAU-0002' }
            }, status.HTTP_404_NOT_FOUND)
            
            
    # ---------------------------------------------------------------------------- #
    #                          METHOD CREATE ADDRESS USER                          #
    # ---------------------------------------------------------------------------- #
    
    @action(method = ['POST'], detail = False , url_path='create_address_user', url_name='create_address_user')
    def create_address_user(self , request , *args, **kwargs):
        try:
            # ---------------------------- check params input ---------------------------- #
            data_request = json.loads(request.body.decode('utf-8'))
            address_content = data_request['params']['address_content']
            status_address = data_request['params']['status']
            #decryption token jwt
            jwtToken = request.COOKIES.get('refresh_token')
            refresh_token = RefreshToken(jwtToken)
            decoded_token = refresh_token.payload
        except:
            return Response({ 
                'phone' : 'Create address wrong'  , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : 'Params wrong' , 'type' : 'CAU-0001' }
            }, status.HTTP_404_NOT_FOUND)
        
        try:
            # ----------------------------- check information ---------------------------- #
            user_create_address = User.objects.get(id=decoded_token['user_id'])
            if status_address == True:
                address_status_true = Address.objects.get(user_id = user_create_address , status = True)
                address_status_true.status = False
                address_status_true.save()
            address_user_create = Address.objects.create(address_content= address_content, user_id = user_create_address , status = status_address)
            address_user_create.save()
            serializer = AddressSerializer(address_user_create,many=False)
            return Response({
                'address' : serializer.data , 'status' : status.HTTP_200_OK
            }, status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({ 
                'phone' : 'Create address wrong'  , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : 'Information wrong' , 'type' : 'CAU-0002' }
            }, status.HTTP_404_NOT_FOUND)
    
    # ---------------------------------------------------------------------------- #
    #                          METHOD DELETE ADDRESS USER                          #
    # ---------------------------------------------------------------------------- #
    
    @action(method = ['POST'] , detail= False , url_path='delete_address_user' , url_name= 'delete_address_user')
    def delete_address_user(self , request , *args, **kwargs):
        try:
            # ---------------------------- check params input ---------------------------- #
            data_request = json.loads(request.body.decode('utf-8'))
            address_user_id = data_request['params']['address_user_id']
            #decryption token jwt
            jwtToken = request.COOKIES.get('refresh_token')
            refresh_token = RefreshToken(jwtToken)
            decoded_token = refresh_token.payload
        except:
            return Response({ 
                'address' : 'Delete address wrong'  , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : 'Params wrong' , 'type' : 'DAU-0001' }
            }, status.HTTP_404_NOT_FOUND)
        
        try:
            # ----------------------------- check information ---------------------------- #
            user_delete_address = User.objects.get(id=decoded_token['user_id'])
            address_user_delete = Address.objects.get(id = address_user_id , user_id = user_delete_address , status = False)
            address_user_delete.delete()
            return Response({
                'address' : "delete address success" , 'status' : status.HTTP_200_OK
            }, status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({ 
                'address' : 'Delete address wrong'  , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : 'Information wrong' , 'type' : 'DAU-0002' }
            }, status.HTTP_404_NOT_FOUND)
        
    # ---------------------------------------------------------------------------- #
    #                          METHOD UPDATE ADDRESS USER                          #
    # ---------------------------------------------------------------------------- #

    @action(methods= ['POST'] , detail = False , url_name='update_address_user', url_path='update_address_user')
    def update_address_user(self , request , *args, **kwargs):
        try:
            # ---------------------------- check params input ---------------------------- #
            data_request = json.loads(request.body.decode('utf-8'))
            address_user_id = data_request['params']['address_user_id']
            address_content_update = data_request['params']['address_content_update']
            # decryption token jwt
            jwtToken = request.COOKIES.get('refresh_token')
            refresh_token = RefreshToken(jwtToken)
            decoded_token = refresh_token.payload
        except:
            return Response({ 
                'address' : 'Update address wrong'  , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : 'Params input wrong' , 'type' : 'UAU-0001' }
            }, status.HTTP_404_NOT_FOUND)
            
        try :
            # ----------------------------- check information ---------------------------- #
            user_update_address = User.objects.get(id = decoded_token['user_id'])
            address_user_update = Address.objects.get(id = address_user_id , user_id = user_update_address)
            address_user_update.address_content = address_content_update
            address_user_update.save()
            serializer = AddressSerializer(queryset = address_user_update , many = False)
            return Response({
                'address' : serializer.data , 'status' : status.HTTP_200_OK
            }, status.HTTP_200_OK)
        except :
            return Response({ 
                'address' : 'Update address wrong'  , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : 'Information wrong' , 'type' : 'UAU-0002' }
            }, status.HTTP_404_NOT_FOUND)
        