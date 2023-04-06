from rest_framework.serializers import ModelSerializer,SerializerMethodField,ListSerializer,UUIDField
from product.models import Category,Price,Photo_product,Product,Heart
from rest_framework import serializers
from django.db.models import Prefetch

class PriceSerializer(ModelSerializer):
    class Meta:
        model = Price
        fields = ['id','price','sale','datetime_create']
    def create(self, validated_data):
        price =Price.objects.create( **validated_data)
        return price
class PhotoProductSerializer(ModelSerializer):
    class Meta:
        model = Photo_product
        fields = ['id']
class HeartSerializer(ModelSerializer):
    class Meta:
        model = Heart
        fields =['id','user_id']
class ProductSerializer(serializers.Serializer):
    data = serializers.CharField()
    status_heart =  serializers.BooleanField()
    description = serializers.CharField()
    price = serializers.FloatField()
    id = UUIDField()
    slug=serializers.CharField()
    name = serializers.CharField()
    sex = serializers.IntegerField()
    sale = serializers.FloatField()
    count_heart = serializers.IntegerField()
    
        

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductHeartSerializer(serializers.Serializer):
    prices__price = serializers.FloatField()
    photo_products__data = serializers.CharField()
    name = serializers.CharField()
    slug = serializers.CharField()
    prices__sale = serializers.FloatField()

class CategoryWithNumberProductSerializer(serializers.Serializer):
    id =  UUIDField()
    slug=serializers.CharField()
    name = serializers.CharField()
    number_product = serializers.IntegerField()