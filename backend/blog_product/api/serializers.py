from rest_framework.serializers import ModelSerializer,CharField,SerializerMethodField
from rest_framework import serializers
from blog_product.models import Blog,Comment,Photo_blog,Heart
from login.api.serializers import UserSerializer

# ---------------------------------------------------------------------------- #
#                              Comment serializer                              #
# ---------------------------------------------------------------------------- #

class CommentSerializer(ModelSerializer):
    user_id =  SerializerMethodField()
    
    def get_user_id(self, obj):
        user = {
            'email' : obj.user_id.email,
            'username' : obj.user_id.username,
            'photo' :"http://127.0.0.1:8000/" + str(obj.user_id.photo)
        }
        return user
    
    class Meta:
        model = Comment
        fields = '__all__'
class CommentRawSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    content = serializers.CharField()
    date_create = serializers.DateTimeField()
    level = serializers.IntegerField()
    parent_id = serializers.IntegerField()
    user_profile = serializers.CharField()
    number_heart = serializers.IntegerField()
    user_email =serializers.CharField()
    count_comment_child = serializers.IntegerField()
    status_heart_comment = serializers.BooleanField()
# ---------------------------------------------------------------------------- #
#                                  Photo Blog                                  #
# ---------------------------------------------------------------------------- #

class PhotoBlogSerializer(ModelSerializer):
    class Meta:
        model = Photo_blog
        fields = ['name' , 'file' , 'type']

# ---------------------------------------------------------------------------- #
#                                Blog serializer                               #
# ---------------------------------------------------------------------------- #

class BlogSerializer(ModelSerializer) :
    # ----------------------------------- attri ---------------------------------- #
    comments    = CommentSerializer(many   = True)
    photo_blogs = PhotoBlogSerializer(many = True)
    user_id =  SerializerMethodField()
    
    def get_user_id(self, obj):
        user = {
            'email' : obj.user_id.email,
            'username' : obj.user_id.username,
            'photo' : "http://127.0.0.1:8000/" + str(obj.user_id.photo)
        }
        return user
    class Meta:
        model = Blog
        fields = [  'id' ,'comments' , 'title' , 'content' , 
                    'user_id' , 'photo_blogs' , 'date_create']
class CommentViewSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
class BlogRawSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    content = serializers.CharField()
    date_created =  serializers.DateTimeField()
    user_id_id =  serializers.CharField()
    number_heart = serializers.IntegerField()
    number_comment = serializers.IntegerField()
    status_heart = serializers.BooleanField()
class BlogCommentSeializer(serializers.Serializer):
    comments    = CommentRawSerializer(many   = True)
    blog = BlogRawSerializer(many=False)
    img = CharField()
class HeartSerializer(ModelSerializer):
    class Meta:
        model = Heart
        fields =['id','user_id']