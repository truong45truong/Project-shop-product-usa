from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.middleware.csrf import get_token
from django.middleware import csrf
from django.conf import settings
from rest_framework.decorators import api_view,action,permission_classes,authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from login.models import User,PhoneUser , Address
from .serializers import UserSerializer
import uuid
import json
import base64
import uuid 
import os
from decryptRSA.encryptRSA import decrypt_tokens
from decryptRSA.models import DeviceClient
path_upload_image = str(settings.BASE_DIR)+"/media/photos"
path_upload_video = str(settings.BASE_DIR)+"/media/videos"
class RegisterUserViewSet (viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @action(methods = ['POST'], detail = False, url_path = 'register_user', url_name = "post_user")
    def register_user(self, request, *args, **kwargs):
        
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
        # ---------------------------- check params input ---------------------------- #
        try:
            data_request= json.loads(request.body.decode('utf-8'))
            username = data_request['params']['username']
            name = data_request['params']['name']
            email    = data_request['params']['email']
            phone    = data_request['params']['phone']
            address    = data_request['params']['address']
            password = data_request['params']['password'].encode('utf-8')
            deviceId = data_request['params']['device_id']
            device_curent = DeviceClient.objects.get(id = deviceId)   
            decrypt_password = decrypt_tokens(password,device_curent.private_key)
            if (
                username == '' or name == '' or email == ''
                or phone == '' or address == '' or password == ''
            ):  
                print(data_request)
                return Response({ 
                    'user' : False , 'status' : status.HTTP_404_NOT_FOUND ,
                    'error' : { 'value' : 'Params input wrong' , 'type' : 'RU-0000' }
                })
        except Exception as e:
            print(e)
            return Response({ 
                'user' : False , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : 'Params input wrong' , 'type' : 'RU-0000' }
            })
        # -------------------------------- create user ------------------------------- #
        # check username
        try:
            user = User.objects.create(username=username,photo = None ,level=0, name = name)
            user.password  = make_password(decrypt_password)
            user.save()  
        except Exception as e:
            print(e)
            return Response({ 
                'user' : False , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : 'Username available' , 'type' : 'RU-0001' }
            })
        # check email
        try:
            user.email = email
            user.save()
        except:
            user.delete()
            return Response({ 
                'user' : False , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : 'Email available' , 'type' : 'RU-0002' }
            })
        # check phone
        try:
            user.phone = phone
            phoneUser = PhoneUser.objects.create(name =name , phone = phone , user_id = user , status = True  )
        except:
            return Response({ 
                'user' : False , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : 'Phone available' , 'type' : 'RU-0003' }
            })
        #check address
        try:
            addressUser = Address.objects.create(address_content = address , status = True ,user_id = user)
        except :
            return Response({ 
                'user' : False , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : 'Address Wrong' , 'type' : 'RU-0004' }
            })
        # ------------------------------ end create user ----------------------------- #
        try:
            user.save()
            addressUser.save()
            phoneUser.save()
            serializer = UserSerializer(user,many=False)
            return Response({'user'    : serializer.data , 'status' : status.HTTP_200_OK})
        except:
            return Response({ 
                'user' : False , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : 'Information Wrong' , 'type' : 'RU-0004' }
            })
class LoginViewSet (viewsets.ViewSet):
    authentication_classes =[]

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


# ---------------------------------------------------------------------------- #
#                                  LOGIN USER                                  #
# ---------------------------------------------------------------------------- #
@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def login(request):
    def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
    }
    
    data_request= json.loads(request.body.decode('utf-8'))
    print(data_request)
    response = Response()
    username = data_request['username']
    password = data_request['password'].encode('utf-8')
    deviceId = data_request['device_id']
    device_curent = DeviceClient.objects.get(id = deviceId)
    
    decrypt_password = decrypt_tokens(password,device_curent.private_key)

    user = authenticate(username=username, password=decrypt_password)
    #check username
    if user is not None:
        if user.is_active:
            queryset = User.objects.get(username = username)
            tokens = get_tokens_for_user(user)
            response.set_cookie(
                key=settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH'],
                value=tokens["refresh"],
                expires=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
            )

            csrf.get_token(request)
            response.data = {"success" : "login success" , "access_token" : tokens["access"] , 'status' : status.HTTP_200_OK}
            response.status_code = status.HTTP_200_OK
            return response
        else:
            return Response({"No active" : "This account is not active!!"}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"Invalid" : "Invalid username or password!!"}, status=status.HTTP_404_NOT_FOUND)
    
# ---------------------------------------------------------------------------- #
#                                  LOGOUT USER                                 #
# ---------------------------------------------------------------------------- #
@api_view(['POST'])
def logout(request):
    try:
        response = Response()
        response.delete_cookie('refresh_token')
        response.delete_cookie('csrftoken')
        response.data = {
            "success" : "Logout success" , "status" : status.HTTP_200_OK
        }
        response.status_code = status.HTTP_200_OK
    except Exception as e :
        print(e)
        response.data = {
            "success" : "Logout failure" , "status" : status.HTTP_404_NOT_FOUND
        }
        response.status_code = status.HTTP_404_NOT_FOUND
    return response