from rest_framework.decorators import api_view,parser_classes,action
from django.middleware.csrf import get_token
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets
from rest_framework.response import Response
from login.models import User,PhoneUser,Address
from .serializers import UserSerializer,PhoneUserSerializer,AddressSerializer
from django.views.decorators.csrf import csrf_exempt,csrf_protect,requires_csrf_token
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.conf import settings
import uuid
import json
import base64
import uuid 
import os
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except Exception as e:
            return None
        
path_upload_image = str(settings.BASE_DIR)+"/media/photos"
path_upload_video = str(settings.BASE_DIR)+"/media/videos"
class RegisterUserViewSet (viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @action(methods = ['POST'], detail = False, url_path = 'register_user', url_name = "post_user")
    def post_user(self, request, *args, **kwargs):
        
        list_name_file_blog = []
        def decodeFile(image_data,is_image,is_video):
            
            file_format, file_string = image_data.split(';base64,')
            file_ext = file_format.split('/')[-1]
            file_bytes = base64.b64decode(file_string)
            if is_image is True:
                name_file = 'blog' + str(uuid.uuid4()) + '.' + file_ext
                with open( os.path.join(path_upload_image, "blogs" , name_file), 'wb+') as decoded_image_file:
                    decoded_image_file.write(file_bytes)
                    list_name_file_blog.append({ 'name' : name_file ,
                                                 'file' : 'media/photos/blogs/' + name_file
                    })
            if is_video is True:
                name_file = 'blog' + str(uuid.uuid4()) + '.' + file_ext
                with open( os.path.join(path_upload_video, "blogs",name_file), 'wb+') as decoded_image_file:
                    decoded_image_file.write(file_bytes)
                    list_name_file_blog.append({
                                                 'name' : name_file,
                                                 'file' : 'media/videos/blogs' + name_file
                    })
        
        data_request= json.loads(request.body.decode('utf-8'))
        print(data_request)
        username = data_request['params']['username']
        password = data_request['params']['password']
        email    = data_request['params']['email']
        phone    = data_request['params']['phone']
        # -------------------------------- create user ------------------------------- #
        # check username
        try:
            user = User.objects.create(username=username,photo = None)
        except:
            return Response({ 'user' : False , 'error' : { 'value' : 'Username available' , 'type' : 3 }})
        # check email
        try:
            user.email = email
            user.save()
        except:
            user.delete()
            return Response({ 'user' : False , 'error' : { 'value' : 'Email available' , 'type' : 4 }})
        # check phone
        try:
            user.phone = phone
            user.save()
        except:
            return Response({ 'user' : False , 'error' : { 'value' : 'Phone available' , 'type' : 5 }})
        user.password  = make_password(password)
        user.save()      
        # ------------------------------ end create user ----------------------------- #
        
        serializer = UserSerializer(user,many=False)
        return Response({'user'    : serializer.data , 'error': { 'value': None , 'type': None }})
class UserViewSet (viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # ---------------------------------------------------------------------------- #
    #                                   GET USER                                   #
    # ---------------------------------------------------------------------------- #
    @action(methods = ["GET"], detail = False, url_path = "user", url_name = "get_user")
    def get_user(self,request,*args, **kwargs):
        
        username = request.GET['username']
        password = request.GET['password']
        #check username
        try:
            user_current = User.objects.get(username = username)
        except:
            return Response({ 'user' : False , 'error' : { 'value' : 'username is wrong' , 'type' : 1 }})
        #check password
        if user_current :
            if user_current.check_password(password):
                user = authenticate(request, username=username, password=password)
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                user_current.token_permission_infor_user = uuid.uuid4()
                user_current.save()
                print(request.META.get('CSRF_COOKIE'))
                # csrf_token = request.META.get('CSRF_COOKIE')
                csrf_token = get_token(request)
                serializer = UserSerializer(user_current,many=False)
                response = Response({'user': serializer.data ,'csrf_token': csrf_token, 'error' : { 'value' : None , 'type' : None }})
                response.set_cookie('csrftoken', csrf_token)
                return response
            else:
                return Response({ 'user' : False ,'csrf_token': request.META.get('CSRF_COOKIE') , 'error' : { 'value' : 'password is wrong' , 'type' : 2 }})
        return Response(request,{ 'user' : False , 'error' : { 'value' : None , 'type' : None }})
    
    # ---------------------------------------------------------------------------- #
    #                             CHANGE PASSWORD USER                             #
    # ---------------------------------------------------------------------------- #
    @action(methods = ["POST"], detail = False, url_path = "change_password_user", url_name = "change_password_user")
    def change_password_user(self,request,*args, **kwargs):
        data_request= json.loads(request.body.decode('utf-8'))
        token_permission_infor_user = data_request['params']['token_permission_infor_user']
        email_user = data_request['params']['email_user']
        password = data_request['params']['password']
        password_new = data_request['params']['password_new']
        print("data_request",data_request)
        try:
            user_current = User.objects.get(email = email_user,token_permission_infor_user=token_permission_infor_user)
            if user_current.check_password(password) :
                
                user_current.password  = make_password(password_new)
                user_current.token_permission_infor_user = uuid.uuid4()
                user_current.save()
            else:
                return Response({'user': False ,'error' : { 'value' : "Nhập sai password" , 'type' : "ChangePassWordFailure" }})
            serializer = UserSerializer(user_current,many=False)
            return Response({'user': serializer.data ,'error' : { 'value' : None , 'type' : None }})
        except Exception as e:
            print(e)
            return Response({'user': False ,'error' : { 'value' : str(e) , 'type' : "ChangePassWordFailure" }})
        
class InforUserViewSet (viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # ---------------------------------------------------------------------------- #
    #                                GET INFOR USER                                #
    # ---------------------------------------------------------------------------- #
    @action(methods = ["GET"], detail = False, url_path = "get_infor_user", url_name = "get_infor_user")
    def get_infor_user(self,request,*args, **kwargs):
        token_permission_infor_user = request.GET['token_permission_infor_user']
        email_user = request.GET['email_user']
        try:
            user_current = User.objects.get(email = email_user,token_permission_infor_user=token_permission_infor_user)
            serializer = UserSerializer(user_current,many=False)
            return Response({ 'user' : serializer.data  , 'error' : { 'value' : None , 'type' : None }})
        except:
            return Response({ 'user' : serializer.data , 'error' : { 'value' : None , 'type' : None }})
class PhoneUserViewSet(viewsets.ModelViewSet):
    queryset = PhoneUser.objects.all()
    serializer_class = PhoneUserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    # ---------------------------------------------------------------------------- #
    #                          METHOD CREATE PHONE OF USER                         #
    # ---------------------------------------------------------------------------- #
    
    @action(method = ['POST'], detail = False , url_path='create_phone_user', url_name='create_phone_user')
    def create_phone_user(self , request , *args, **kwargs):
        data_request= json.loads(request.body.decode('utf-8'))
        print(data_request)
        token_permission_infor_user = data_request['params']['token_permission_infor_user']
        phone_user = data_request['params']['phone_user']
        name_user = data_request['params']['name_user']
        status = data_request['params']['status']
        
        try:
            user = User.objects.get(token_permission_infor_user=token_permission_infor_user)
            if status == True :
                list_phone_status_true = PhoneUser.objects.filter(user_id = user , status = status)
                for item in list_phone_status_true:
                    phone_status_true = PhoneUser.objects.get(id = item.id)
                    phone_status_true.status = False
                    phone_status_true.save()
            phone_user_create = PhoneUser.objects.create(phone = phone_user , name = name_user , user_id = user , status = status)
            phone_user_create.save()
            serializer = PhoneUserSerializer(phone_user_create,many = False)
            return Response({'phone' : serializer.data , 'error' : { 'value' : None , 'type' : None}})
        except Exception as e:
            print(e)
            return Response({ 'phone' : 'Creatte phone wrong'  , 'error' : { 'value' : 'Failure Create' , 'type' : 'P1' }})

    
    # ---------------------------------------------------------------------------- #
    #                          METHOD DELETE PHONE OF USER                         #
    # ---------------------------------------------------------------------------- #
    @action(method = ['POST'] , detail= False , url_path='delete_phone_user' , url_name= 'delete_phone_user')
    def delete_phone_user(self , request ,  *args, **kwargs):
        data_request = json.loads(request.body.decode('utf-8'))
        phone_user_id = data_request['params']['phone_user_id']
        token_permission_infor_user = data_request['params']['token_permission_infor_user']
        
        try:
            user_delete_phone = User.objects.get(token_permission_infor_user=token_permission_infor_user)
            phone_user_delete = PhoneUser.objects.get(id = phone_user_id, user_id = user_delete_phone)
            phone_user_delete.delete()
            return Response({'phone': 'Delete phone Success' , 'error' : {'value' : None , 'type' : None}})
        except:
            return Response({'phone' : 'Delete phone wrong' , 'error' : { 'value' : 'Failure Delete' , 'type' : 'DP1'}})
        
    
    # ---------------------------------------------------------------------------- #
    #                           METHOD UPDATE PHONE USER                           #
    # ---------------------------------------------------------------------------- #
     
    @action(method = ['POST'] , detail= False , url_name= 'update_phone_user', url_path= 'update_phone_user')
    def update_phone_user(self , request , *args, **kwargs):
        data_request = json.loads(request.body.decode('utf-8'))
        phone_user_id = data_request['params']['phone_user_id']
        phone_update = data_request['params']['phone_update']
        name_update = data_request['params']['name_update']
        token_permission_infor_user = data_request['params']['token_permission_infor_user']
        
        try : 
            user_update_phone = User.objects.get(token_permission_infor_user=token_permission_infor_user)
            phone_user_update = PhoneUser.objects.get(id = phone_user_id)
            phone_user_update.phone = phone_update
            phone_user_update.bane = name_update
            phone_user_update.save()
            serializer = PhoneUserSerializer(queryset = phone_user_update , mang = False)
            return Response({ 'phone' : serializer.data , 'error' : { 'value' : None , 'type' : None } })
        except:
            return Response({'phone' : 'Update phone user wrong' , 'error' : { 'value' : 'Failure Update' , 'type' : 'UP1' }})
        
        
class AddressUserViewset (viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    # ---------------------------------------------------------------------------- #
    #                          METHOD CREATE ADDRESS USER                          #
    # ---------------------------------------------------------------------------- #
    
    @action(method = ['POST'], detail = False , url_path='create_address_user', url_name='create_address_user')
    def create_address_user(self , request , *args, **kwargs):
        data_request = json.loads(request.body.decode('utf-8'))
        token_permission_infor_user_access = data_request['params']['token_permission_infor_user']
        address_content = data_request['params']['address_content']
        status = data_request['params']['status']
        try:
            user_create_address = User.objects.get(token_permission_infor_user=token_permission_infor_user_access)
            if status == True:
                address_status_true = Address.objects.get(user_id = user_create_address , status = True)
                address_status_true.status = False
                address_status_true.save()
            address_user_create = Address.objects.create(address_content= address_content, user_id = user_create_address , status = status)
            address_user_create.save()
            serializer = AddressSerializer(address_user_create,many=False)
            return Response({'address' : serializer.data , 'error' : { 'value' : None , 'type' : None}})
        except Exception as e:
            print(e)
            return Response({ 'address' : 'Create address wrong'  , 'error' : { 'value' : 'Failure Create' , 'type' : 'CA1' }})
    
    # ---------------------------------------------------------------------------- #
    #                          METHOD DELETE ADDRESS USER                          #
    # ---------------------------------------------------------------------------- #
    
    @action(method = ['POST'] , detail= False , url_path='delete_address_user' , url_name= 'delete_address_user')
    def delete_address_user(self , request , *args, **kwargs):
        data_request = json.loads(request.body.decode('utf-8'))
        address_user_id = data_request['params']['address_user_id']
        token_permission_infor_user = data_request['params']['token_permission_infor_user']
        try:
            user_delete_address = User.objects.get(token_permission_infor_user=token_permission_infor_user)
            address_user_delete = Address.objects.get(id = address_user_id , user_id = user_delete_address , status = False)
            address_user_delete.delete()
            return Response({'address' : 'Delete address success', 'error' : { 'value' : None , 'type' : None}})
        except Exception as e:
            print(e)
            return Response({ 'address' : 'Delete address wrong'  , 'error' : { 'value' : 'Failure Delete' , 'type' : 'DA1' }})
        
    # ---------------------------------------------------------------------------- #
    #                          METHOD UPDATE ADDRESS USER                          #
    # ---------------------------------------------------------------------------- #

    @action(methods= ['POST'] , detail = False , url_name='update_address_user', url_path='update_address_user')
    def update_address_user(self , request , *args, **kwargs):
        data_request = json.loads(request.body.decode('utf-8'))
        address_user_id = data_request['params']['address_user_id']
        token_permission_infor_user = data_request['params']['token_permission_infor_user']
        address_content_update = data_request['params']['address_content_update']
        
        try :
            user_update_address = User.objects.get(token_permission_infor_user = token_permission_infor_user)
            address_user_update = Address.objects.get(id = address_user_id , user_id = address_user_id)
            address_user_update.address_content = address_content_update
            address_user_update.save()
            serializer = AddressSerializer(queryset = address_user_update , many = False)
            return Response({ 'address' : serializer.data , 'error' : { 'value' : None , 'error' : None } })
        except :
            return Response({ 'address' : 'Update adress wrong' , 'error' : { 'value' : 'Failure Update' , 'error' : 'UA1' } })
        