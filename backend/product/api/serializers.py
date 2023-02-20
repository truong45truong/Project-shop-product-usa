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
    price = serializers.FloatField()
    id = UUIDField()
    slug=serializers.CharField()
    name = serializers.CharField()
    sex = serializers.IntegerField()
    count_heart = serializers.IntegerField()
    # def checkUserLike(self, instance ):
    #     user_id = self.context.get('user_id')
    #     print(instance.hearts)
    #     return False
    # class Meta:
    #     model = Product
    #     fields = ['slug','name','sex','description','category_id','data','status_heart','price']
        
    # def get_prefetch_queryset(self, queryset):
    #     print("queryset")
    #     queryset = queryset.prefetch_related(
    #         Prefetch('prices', queryset=Price.objects.all(), to_attr='prefetched_prices'),
    #         Prefetch('photo_products', queryset=Photo_product.objects.all(), to_attr='prefetched_photo_products'),
    #     )
    #     return queryset
        
    # def to_internal_value(self, data):
    #     # Call the parent class's to_internal_value() method to perform the default validation
    #     print("to_internal_value")
    #     validated_data = super().to_internal_value(data)

    #     # Perform additional validation
    #     if validated_data['my_field'] == 'invalid':
    #         raise serializers.ValidationError('my_field cannot be "invalid"')

    #     return validated_data
    
        

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductListSerializer(ListSerializer):
    price = PriceSerializer(many=False)
    photo_products = PhotoProductSerializer(many=False)
    status = serializers.BooleanField()
    name = serializers.CharField()
    slug = serializers.CharField()
    heart = HeartSerializer(many = True)
    # def get_queryset(self):
    #         queryset = super().get_queryset()
    #         queryset = queryset.prefetch_related(['prices','photo_products','hearts'])
    #         return queryset