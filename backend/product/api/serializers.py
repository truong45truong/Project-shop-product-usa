from rest_framework.serializers import ModelSerializer

from product.models import Category,Price,Photo_product,Product

class PriceSerializer(ModelSerializer):
    class Meta:
        model = Price
        fields = ['price','sale','datetime_create']
    def create(self, validated_data):
        price =Price.objects.create( **validated_data)
        return price
class PhotoProductSerializer(ModelSerializer):
    class Meta:
        model = Photo_product
        fields = '__all__'
class ProductSerializer(ModelSerializer):
    prices = PriceSerializer(many=True)
    photo_products = PhotoProductSerializer(many=True)
    class Meta:
        model = Product
        fields = ['slug','name','sex','description','category_id','prices','photo_products']

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"