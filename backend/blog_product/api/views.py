from rest_framework.decorators import action ,api_view,permission_classes,authentication_classes
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from blog_product.models import Blog, Comment, Photo_blog,Heart ,Media_Comment
from login.models import User
from product.models import Product
from .serializers import BlogSerializer,CommentSerializer,CommentViewSerializer , CommentRawSerializer,HeartSerializer,BlogCommentSeializer
from django.conf import settings
from .query_raw import HandleSqlRaw
from .method_orthers import handleDecodeFile
from . import data_processing
from . import query_raw
import json
import base64
import datetime
import uuid 
import os

path_upload_image = str(settings.BASE_DIR)+"/media/photos"
path_upload_video = str(settings.BASE_DIR)+"/media/videos"


class BlogViewSet (viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
    # ---------------------------------------------------------------------------- #
    #                                   POST BLOG                                  #
    # ---------------------------------------------------------------------------- #
    
    @action(method = ['POST'], detail = False, url_path = 'blog', url_name = 'post_blog')
    def post_blog(self , request, *arg, **kwargs):
        # ----------------------- handle file is video or image ---------------------- #
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
                                                 'file' : 'media/photos/blogs/' + name_file ,
                                                 'type' : False
                    })
            if is_video is True:
                name_file = 'blog' + str(uuid.uuid4()) + '.' + file_ext
                with open( os.path.join(path_upload_video, "blogs",name_file), 'wb+') as decoded_image_file:
                    decoded_image_file.write(file_bytes)
                    list_name_file_blog.append({
                                                 'name' : name_file,
                                                 'file' : 'media/videos/blogs/' + name_file ,
                                                 'type' : True
                    })
        
        #check data post error
        try:
            data_request= json.loads(request.body)
            for file_data in data_request['files']:
                decodeFile(file_data['data'],file_data['isImage'],file_data['isVideo'])
        except:
            return Response({'notify': "Post blog failure" , 'error' : { 'values' : 'Data post wrong' , 'type' : 'B1'}})
        #check user error
        try:
            user_post = User.objects.get( email = data_request['user'])
        except:
            return Response({'notify': "Post blog failure" , 'error' : { 'values' : "User does not exist " , 'type' : 'B2'}})
        #insert blogs , file to database
        try:
            blog_current = Blog.objects.create( content = data_request['content'] , 
                                                title   = data_request['title'] ,
                                                user_id = user_post
                            )
            blog_current.save()
            for file in list_name_file_blog:
                photo_file = Photo_blog.objects.create( blog_id = blog_current ,
                                                        name    = file['name'] ,
                                                        file    = file['file'] ,
                                                        type    = file['type'] 
                            )
                
                photo_file.save()
        except Exception as e:
            print(e)
            blog_current.delete()
            return Response({'notify': "Post blog failure" , 'error' : { 'values' : "Post blog error" , 'type' : 'B3'}})
        return Response({'notify': 'Post blog successs' , 'error' : { 'values' : None , 'type' : None}})
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentViewSerializer
    @action(method = ['POST'], detail = False, url_path = 'delete_comment', url_name = 'delete_comment')
    def delete_comment(self , request, *arg, **kwargs):
        response = Response()
        try:
            data_request = json.loads(request.body)
            jwtToken = request.COOKIES.get('refresh_token')
            refresh_token = RefreshToken(jwtToken)
            decoded_token = refresh_token.payload
            comment_id = data_request['params']['comment_id']
        except:
            response.data = {
                'suceess': "Delete comment failure" , 'status' : status.HTTP_404_NOT_FOUND,
                'error' : { 'values' : 'Data  wrong' , 'type' : 'DCMT-01'}
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
        try:
            user_edit = User.objects.get(id = decoded_token['user_id'] )
            comment_edit = Comment.objects.get(user_id = user_edit, id = comment_id)
            comment_edit.delete()
            response.data = {
                'sucess' : 'delete success',
                'status' : status.HTTP_200_OK
            }
            response.status_code = status.HTTP_200_OK
            return response
        except Exception as e:
            print("ERROR" , e)
            response.data = {
                'notify': "Delete comment failure" , 'status' : status.HTTP_404_NOT_FOUND,
                'error' : { 'values' : 'Information  wrong' , 'type' : 'DCMT-02'}
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
    @action(method = ['POST'], detail = False, url_path = 'edit_comment', url_name = 'edit_comment')
    def edit_comment(self , request, *arg, **kwargs):
        response = Response()
        try:
            # ---------------------------- check params input ---------------------------- #
            data_request = json.loads(request.body)
            jwtToken = request.COOKIES.get('refresh_token')
            refresh_token = RefreshToken(jwtToken)
            decoded_token = refresh_token.payload
            comment_id = data_request['params']['comment_id']
            content_comment = data_request['params']['content_comment']
        except :
            response.data = {
                'notify': "Edit comment failure" , 'status' : status.HTTP_404_NOT_FOUND,
                'error' : { 'values' : 'Data  wrong' , 'type' : 'ECMT-01'}
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
        try:
            user_edit = User.objects.get(id = decoded_token['user_id'] )
            comment_edit = Comment.objects.get(user_id = user_edit, id = comment_id)
            comment_edit.content = content_comment
            comment_edit.is_edit = datetime.datetime.now()
            comment_edit.save()
            response.data = {
                'sucess' : 'edit success' , 'edit_time' : comment_edit.is_edit ,
                'status' : status.HTTP_200_OK
            }
            response.status_code = status.HTTP_200_OK
            return response
        except Exception as e:
            print("ERROR" , e)
            response.data = {
                'notify': "Edit comment failure" , 'status' : status.HTTP_404_NOT_FOUND,
                'error' : { 'values' : 'Information  wrong' , 'type' : 'ECMT-02'}
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
    @action(method = ['POST'], detail = False, url_path = 'comment', url_name = 'post_comment')
    def post_comment_blog(self , request, *arg, **kwargs):
        response = Response()
        try:
            data_request = json.loads(request.body)
            jwtToken = request.COOKIES.get('refresh_token')
            refresh_token = RefreshToken(jwtToken)
            decoded_token = refresh_token.payload
            user_comment =  User.objects.get(id = decoded_token['user_id'])
            print('user_comment',user_comment)
            blog = Blog.objects.get(id = data_request['blog_id'])
            content = data_request['content']
            if data_request['parent'] !=  False:
                comment_parent = Comment.objects.get(id = data_request['parent'])
                comment_current = Comment.objects.create(
                    parent = comment_parent,content = content , type=False,
                    blog_id = blog,heart = 0 , user_id = user_comment,
                    user_profile = user_comment.photo , user_email = user_comment.email
                )
            else:
                comment_current = Comment.objects.create(
                    parent= None ,content = content , blog_id = blog,
                    heart = 0 , user_id = user_comment,type=False,
                    user_profile = user_comment.photo , user_email = user_comment.email
                )
            files = data_request['files']
            for file_data in files:
                file_decode = handleDecodeFile(file_data['data'],file_data['isImage'],file_data['isVideo'])
                mediaComment = Media_Comment.objects.create(
                    name = file_decode['name'],
                    file = file_decode['file'],
                    type = file_decode['type'],
                    comment_id = comment_current
                )
                mediaComment.save()
            comment_current.save()
            response.data = {
                'comment':
                    {
                        'id' : str(comment_current.id),
                        'content' : comment_current.content,
                        'user_email' : str(comment_current.user_email),
                        'user_profile' : str(comment_current.user_profile),
                        'number_heart' : 0,
                        'count_comment_child' : 0,
                        'status_heart_comment' : 0,
                        'level' : comment_current.level
                    }
                ,  "status" : status.HTTP_200_OK,
                'error' : { 'values' : None , 'type' : None }
            }
            response.status_code = status.HTTP_200_OK
            return response
        except Exception as e:
            print("ERROR",e)
            response.data = {
                'notify': "Post comment failure" , 'status' : status.HTTP_404_NOT_FOUND,
                'error' : { 'values' : 'Data post wrong' , 'type' : 'PCMT01'}
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
    
    @action(method = ['GET'], detail = False, url_path = 'comment', url_name='get_comment')
    def get_comment(self, request, *arg, **kwargs):
        try:
            comment_id = request.GET['id']
            if comment_id:
                queryset = Comment.objects.filter(id = comment_id)
                
                serializer = CommentViewSerializer(queryset,many = True)
                return Response({'comment': serializer.data , 'error' : { 'values' : None , 'type' : None}})
        except:
            return Response({'comment': None , 'error' : { 'values' : 'No find comment id' , 'type' : 'C01'}})

class HeartViewSet(viewsets.ModelViewSet):
    queryset = Heart.objects.all()
    serializer_class = HeartSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @action(method=["POST"],detail=False,url_path="heart",url_name="post_heart")
    def post_heart_product(self, request,*args, **kwargs):
        data_request= json.loads(request.body.decode('utf-8'))
        jwtToken = request.COOKIES.get('refresh_token')
        refresh_token = RefreshToken(jwtToken)
        decoded_token = refresh_token.payload
        product_slug = data_request['params']['product_slug']
        try:
            product = Product.objects.get(slug = product_slug)
            user = User.objects.get(id  = decoded_token['user_id'])
            heart_product = Heart.objects.filter(product_id = product.id , user_id = user.id)
            if len(heart_product) == 1 :
                Heart.objects.get(id = heart_product[0].id).delete()
            else :
                heart = Heart.objects.create(user_id = user , product_id = product,type = 0)
                heart.save()
            return Response({ 'status' : True})
        except Exception as e:
            print(e)
        return Response({ 'status' : False})
    @action(method=["POST"],detail=False,url_path="heart",url_name="post_heart")
    def post_heart_blog(self, request,*args, **kwargs):
        response = Response()
        try: 
            # ---------------------------- check params input ---------------------------- #
            data_request= json.loads(request.body.decode('utf-8'))
            jwtToken = request.COOKIES.get('refresh_token')
            refresh_token = RefreshToken(jwtToken)
            decoded_token = refresh_token.payload
            blog = data_request['params']['blog_id']
        except Exception as e:
            print("ERROR",e)
            response.data = {
                "success" : "Heart blog failure" , "status" : status.HTTP_404_NOT_FOUND,
                "error" : {'value' : "Params input wrong" , 'type' : "PHB-01"}
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
            
        try:
            # ----------------------------- check information ---------------------------- #
            blog = Blog.objects.get(id = blog)
            user = User.objects.get(id  = decoded_token['user_id'])
            heart_blog = Heart.objects.filter(blog_id = blog , user_id = user.id)
            if len(heart_blog) == 1 :
                Heart.objects.get(id = heart_blog[0].id).delete()
                response.data = {
                    "success" : "Heart blog success" , "status" : status.HTTP_200_OK,
                    "value" : False
                }
            else :
                heart = Heart.objects.create(user_id = user , blog_id = blog,type = 1)
                heart.save()
                response.data = {
                    "success" : "Heart blog success" , "status" : status.HTTP_200_OK,
                    "value" : True
                }
            response.status_code = status.HTTP_200_OK
            return response
        except Exception as e:
            print(e)
            response.data = {
                "success" : "Heart blog failure" , "status" : status.HTTP_404_NOT_FOUND,
                "error" : {'value' : "Information input wrong" , 'type' : "PHB-02"}
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
    def post_heart_comment(self, request,*args, **kwargs):
        response = Response()
        try: 
            # ---------------------------- check params input ---------------------------- #
            data_request= json.loads(request.body.decode('utf-8'))
            jwtToken = request.COOKIES.get('refresh_token')
            refresh_token = RefreshToken(jwtToken)
            decoded_token = refresh_token.payload
            comment_id = data_request['params']['comment']
        except Exception as e:
            print("ERROR",e)
            response.data = {
                "success" : "Heart comment failure" , "status" : status.HTTP_404_NOT_FOUND,
                "error" : {'value' : "Params input wrong" , 'type' : "PHC-01"}
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
            
        try:
            # ----------------------------- check information ---------------------------- #
            comment = Comment.objects.get(id = comment_id)
            user = User.objects.get(id  = decoded_token['user_id'])
            heart_blog = Heart.objects.filter(comment_id = comment , user_id = user.id)
            if len(heart_blog) == 1 :
                Heart.objects.get(id = heart_blog[0].id).delete()
                response.data = {
                    "success" : "Heart comment success" , "status" : status.HTTP_200_OK,
                    "value" : False
                }
            else :
                heart = Heart.objects.create(user_id = user , comment_id = comment,type = 2)
                heart.save()
                response.data = {
                    "success" : "Heart comment success" , "status" : status.HTTP_200_OK,
                    "value" : True
                }
            response.status_code = status.HTTP_200_OK
            return response
        except Exception as e:
            print(e)
            response.data = {
                "success" : "Heart comment failure" , "status" : status.HTTP_404_NOT_FOUND,
                "error" : {'value' : "Information input wrong" , 'type' : "PHB-02"}
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
# ---------------------------------------------------------------------------- #
#                              GET BLOG OF PRODUCT                             #
# ---------------------------------------------------------------------------- #
@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def get_blog_product(request):
    try:
        jwtToken = request.COOKIES.get('refresh_token')
        refresh_token = RefreshToken(jwtToken)
        decoded_token = refresh_token.payload
        user_get = User.objects.get(id = decoded_token['user_id'])
        sqlRaw =  query_raw.QUERY_SQL_GET_BLOG_OF_PRODUCT_WITH_USER
    except:
        user_get = False
        sqlRaw =  query_raw.QUERY_SQL_GET_BLOG_OF_PRODUCT
    response = Response()
    try:
        product_slug = request.GET['product_slug']
        if ' ' in product_slug:
            response.data = {
            'blogs' : False , "status" : status.HTTP_404_NOT_FOUND,
            "error" : { "value" : "error have /t" , "type" : "GBP-01"}
            }
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
        if user_get == False:
            queryset = Blog.objects.raw(sqlRaw,[product_slug])
        else:
            queryset = Blog.objects.raw(sqlRaw,[user_get.id,user_get.id,product_slug])
        querysetHandled = data_processing.handleRawQuery(queryset)
        serializer = BlogCommentSeializer(querysetHandled,many = True)
        response.data = {
            'blogs' : serializer.data , "status" : status.HTTP_200_OK , 'number_blog' : len(querysetHandled),
        }
        return response
    except Exception as e:
        print("ERROR",e)
        response.data = {
            'blogs' : False , "status" : status.HTTP_404_NOT_FOUND,
            "error" : { "value" : "Infomation error" , "type" : "GBP-01"}
            }
        response.status_code = status.HTTP_404_NOT_FOUND
        return response

@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def get_comment_child(request):
    try:
        jwtToken = request.COOKIES.get('refresh_token')
        refresh_token = RefreshToken(jwtToken)
        decoded_token = refresh_token.payload
        user_get = User.objects.get(id = decoded_token['user_id'])
        rawSql =  query_raw.QUERY_SQL_GET_COMMET_CHILD_WITH_USER
    except:
        user_get = False
        rawSql = query_raw.QUERY_SQL_GET_COMMET_CHILD
    response = Response()
    try:
        comment_id = request.GET['id']
        handleRawSql = HandleSqlRaw(rawSql)
        if comment_id != False:
            parent = Comment.objects.get(id =comment_id )
            if user_get == False:
                queryset = Comment.objects.raw(handleRawSql.getQuery(),[parent.id])
            else:
                queryset = Comment.objects.raw(handleRawSql.getQuery(),[user_get.id,parent.id])
            serializer = CommentRawSerializer(queryset,many = True)
            response.data = {
                'comments' : serializer.data , 'status' : status.HTTP_200_OK ,
            }
            response.status_code = status.HTTP_200_OK
        else :
            response.data = {
                'comments' : False , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : 'no find comment parent' , 'type' : 'GCMTC-01' }
            }
            response.status_code = status.HTTP_404_NOT_FOUND
        return response
    except Exception as e :
        print('ERROR' , e)
        response.data = {
                'comments' : False , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : 'Params wrong' , 'type' : 'GCMTC-01' }
        }
        response.status_code = status.HTTP_404_NOT_FOUND
        return response

@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def get_comment_product(request):
    try:
        jwtToken = request.COOKIES.get('refresh_token')
        refresh_token = RefreshToken(jwtToken)
        decoded_token = refresh_token.payload
        user_get = User.objects.get(id = decoded_token['user_id'])
        rawSql =  query_raw.QUERY_GET_COMMENT_PRODUCT_WITH_USER
    except:
        user_get = False
        rawSql = query_raw.QUERY_GET_COMMENT_PRODUCT_NOT_USER
    response = Response()
    try:
        product_slug = request.GET['product_slug']
        handleRawSql = HandleSqlRaw(rawSql)
    
        if product_slug not in '':
            if user_get == False:
                queryset = Comment.objects.raw(handleRawSql.getQuery(),[product_slug])
            else:
                queryset = Comment.objects.raw(handleRawSql.getQuery(),[user_get.id,product_slug])
            print(queryset,len(queryset))
            serializer = CommentRawSerializer(queryset,many = True)
            response.data = {
                'comments' : serializer.data , 'status' : status.HTTP_200_OK ,
            }
            response.status_code = status.HTTP_200_OK
        else :
            response.data = {
                'comments' : False , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : 'no find comment product' , 'type' : 'GCMTP-01' }
            }
            response.status_code = status.HTTP_404_NOT_FOUND
        return response
    except Exception as e :
        print('ERROR' , e)
        response.data = {
                'comments' : False , 'status' : status.HTTP_404_NOT_FOUND ,
                'error' : { 'value' : 'Params wrong' , 'type' : 'GCMTP-01' }
        }
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
    
@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def post_comment_product( request):
    response = Response()
    try:
        data_request = json.loads(request.body)
        jwtToken = request.COOKIES.get('refresh_token')
        refresh_token = RefreshToken(jwtToken)
        decoded_token = refresh_token.payload
        user_comment =  User.objects.get(id = decoded_token['user_id'])
        user_comment_photo = user_comment.photo
        user_comment_email = user_comment.email
    except :
        user_comment = None
        user_comment_photo = None
        user_comment_email = data_request['infor_customer'].split(',')[-1].split(': ')[2].split("\n")[0]
    try:
        product = Product.objects.get(slug = data_request['product_slug'])
        content = data_request['content']
        infor_customer = data_request['infor_customer']
        if data_request['parent'] !=  False:
            comment_parent = Comment.objects.get(id = data_request['parent'])
            comment_current = Comment.objects.create(
                parent = comment_parent,content = content , type = True,
                product_id = product,heart = 0 , user_id = user_comment,
                user_profile = user_comment_photo, user_email = user_comment_email,
                information_customer = infor_customer
            )
        else:
            comment_current = Comment.objects.create(
                parent= None ,content = content , product_id = product,
                heart = 0 , user_id = user_comment,type = True,
                user_profile = user_comment_photo , user_email = user_comment_email,
                information_customer = infor_customer
            )
        files = data_request['files']
        file_media_comment =""
        print("file_media_comment")
        for file_data in files:
            file_decode = handleDecodeFile(file_data['data'],file_data['isImage'],file_data['isVideo'])
            file_media_comment = {
                file_media_comment + str(file_decode['file']) + ":" + str(int(file_decode['type'])) +","
            }
            file_media_comment = ",".join(file_media_comment)

            print(file_media_comment)
            
            mediaComment = Media_Comment.objects.create(
                name = file_decode['name'],
                file = file_decode['file'],
                type = file_decode['type'],
                comment_id = comment_current
            )
            mediaComment.save()
        comment_current.save()
        comment = {
                    'id' : str(comment_current.id),
                    'content' : comment_current.content,
                    'user_email' : str(comment_current.user_email),
                    'user_profile' : str(comment_current.user_profile) if user_comment != None else None,
                    'number_heart' : 0,
                    'count_comment_child' : 0,
                    'status_heart_comment' : 0,
                    'level' : comment_current.level,
                    'file_media_comment' : file_media_comment[0:-1],
                    'date_create' : comment_current.date_create,
                    'parent_id' : comment_current.parent.id if data_request['parent'] !=  False  else None ,
                    'comment_is_edit' : None
        }
        response.data = {
            'comment':comment, "status" : status.HTTP_200_OK,
            'error' : { 'values' : None , 'type' : None }
        }
        response.status_code = status.HTTP_200_OK
        return response
    except Exception as e:
        print("ERROR",e)
        response.data = {
            'notify': "Post comment failure" , 'status' : status.HTTP_404_NOT_FOUND,
            'error' : { 'values' : 'Data post wrong' , 'type' : 'PCMT01'}
        }
        response.status_code = status.HTTP_404_NOT_FOUND
        return response