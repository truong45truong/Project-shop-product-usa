from rest_framework.serializers import ModelSerializer,SerializerMethodField
from product.models import Category,Price,Photo_product,Product,Heart
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
    status = SerializerMethodField('checkUserLike')
    
    def checkUserLike(self, obj):
        user_id = self.context.get('user_id')
        try:
            heart = Heart.objects.get(user_id = user_id, product_id = obj.id)
            print(heart)
            return True
        except Exception as e:
            print(e)
            return False
    class Meta:
        model = Product
        fields = ['slug','name','sex','description','category_id','prices','photo_products','status']

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"