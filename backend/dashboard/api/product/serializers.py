from rest_framework.serializers import ModelSerializer,SerializerMethodField,ListSerializer,UUIDField
from product.models import Category,Price,Photo_product,Product,Price
from rest_framework import serializers
from flashSaleProduct.models import Voucher,DetailVoucher,FlashSale , DetailFlashSale

class CountLengthAdminSerializer(serializers.Serializer):
    count = serializers.IntegerField()
class DetailVoucherAdminORMSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    class Meta:
        model = DetailVoucher
        fields = '__all__'
    def get_product(self, obj):
        print(obj.product_id)
        if obj.product_id:
            product_current = Product.objects.get(slug = str(obj.product_id))
            # category_current = Category.objects.get(id = product_current.category_id)
            price_current = Price.objects.get(product_id = product_current)
            return {
                'id' : product_current.id,
                'name' : product_current.name,
                'category_name' : product_current.category_id.name,
                'price' : price_current.price ,
                'sale' : price_current.sale,
                'price_total' : price_current.price_total ,
                'product_quantity' : product_current.quantity
            }

        return False
class VoucherAdminORMSerializer(serializers.ModelSerializer):
    detail_vouchers = DetailVoucherAdminORMSerializer(many=True)
    class Meta:
        model = Voucher
        fields = '__all__'
class VoucherAdminSerializer(serializers.Serializer):
    id = UUIDField()
    name = serializers.CharField()
    detail = serializers.CharField()
    sale = serializers.IntegerField()
    description = serializers.CharField()
    quantity = serializers.IntegerField()
    level = serializers.IntegerField()
    limited_price = serializers.IntegerField()
    count_product = serializers.IntegerField()
class VoucherNoProductAdminSerializer(serializers.Serializer):
    id = UUIDField()
    name = serializers.CharField()
    detail = serializers.CharField()
    sale = serializers.IntegerField()
    description = serializers.CharField()
    quantity = serializers.IntegerField()
    level = serializers.IntegerField()
    limited_price = serializers.IntegerField()

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
class ProductDetailSerializer(serializers.Serializer):
    file_media_product = serializers.CharField()
    status_heart =  serializers.BooleanField()
    description = serializers.CharField()
    price = serializers.FloatField()
    id = UUIDField()
    slug=serializers.CharField()
    name = serializers.CharField()
    sex = serializers.IntegerField()
    sale = serializers.FloatField()
    count_heart = serializers.IntegerField()
    product_quantity = serializers.IntegerField()
    category_name = serializers.CharField()
    
class ProductCheckoutSerializer(serializers.Serializer):  
    slug=serializers.CharField()
    name = serializers.CharField()
    sex = serializers.IntegerField()
    sale = serializers.FloatField()
    data = serializers.CharField()
    price = serializers.FloatField()
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
class ProductAminSerializer(serializers.Serializer):
    id = UUIDField()
    name = serializers.CharField()
    category_name = serializers.CharField()
    price = serializers.FloatField()
    sale = serializers.FloatField()
    product_quantity = serializers.IntegerField()
    price_total = serializers.FloatField()

class FlashSaleAdminSerializer(serializers.Serializer):
    id = UUIDField()
    name  = serializers.CharField()
    note = serializers.CharField()
    count_product = serializers.IntegerField()

class DetailFlashSaleAdminORMSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    class Meta:
        model = DetailVoucher
        fields = '__all__'
    def get_product(self, obj):
        if obj.product_id:
            product_current = Product.objects.get(slug = str(obj.product_id))
            # category_current = Category.objects.get(id = product_current.category_id)
            price_current = Price.objects.get(product_id = product_current)
            return {
                'id' : product_current.id,
                'name' : product_current.name,
                'category_name' : product_current.category_id.name,
                'price' : price_current.price ,
                'sale' : price_current.sale,
                'price_total' : price_current.price_total ,
                'product_quantity' : product_current.quantity
            }

        return False
class FlashSaleAdminORMSerializer(serializers.ModelSerializer):
    detail_flash_sales = DetailFlashSaleAdminORMSerializer(many=True)
    class Meta:
        model = FlashSale
        fields = ['id' , 'name' , 'note' , 'detail_flash_sales']