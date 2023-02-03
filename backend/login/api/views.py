from rest_framework.decorators import api_view,parser_classes,action
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets
from rest_framework.response import Response
from login.models import User
from .serializers import UserSerializer
from django.conf import settings

import json
import base64
import uuid 
import os

path_upload_image = str(settings.BASE_DIR)+"/media/photos"
path_upload_video = str(settings.BASE_DIR)+"/media/videos"

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
                serializer = UserSerializer(user_current,many=False)
                return Response({'user': serializer.data , 'error' : { 'value' : None , 'type' : None }})
            else:
                return Response({ 'user' : False , 'error' : { 'value' : 'password is wrong' , 'type' : 2 }})
        return Response({ 'user' : False , 'error' : { 'value' : None , 'type' : None }})
    # ---------------------------------------------------------------------------- #
    #                                   POST USER                                  #
    # ---------------------------------------------------------------------------- #
    
    @action(methods = ['POST'], detail = False, url_path = 'user', url_name = "post_user")
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