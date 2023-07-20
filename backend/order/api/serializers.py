from rest_framework.serializers import ModelSerializer,SerializerMethodField,ListSerializer,UUIDField
from order.models import Order, Transport , DetailOrder , Payment
from rest_framework import serializers
    
class TransportSerializer(serializers.Serializer):
    # ------------------------- params model detail order ------------------------ #
    transport_slug = serializers.CharField(max_length=50)
    transport_name = serializers.CharField(max_length=50)
    transport_price = serializers.FloatField()
    transport_logo = serializers.CharField()

class ProductSerializer(serializers.Serializer):
    # --------------------------- params model product --------------------------- #
    product_slug = serializers.CharField()
    product_name = serializers.CharField()
    product_description = serializers.CharField()
    product_price = serializers.FloatField()
    product_sale = serializers.FloatField()
    product_price_status = serializers.BooleanField()
    product_price_total = serializers.FloatField()
    photo_product = serializers.CharField()
    category_name = serializers.CharField()
    product_quantity = serializers.IntegerField()
class OrderSerializer (serializers.Serializer):
    # ---------------------------- params model order ---------------------------- #
    name = serializers.CharField(max_length=200)
    datetime = serializers.DateTimeField()
    receiver = serializers.CharField(max_length=50)
    address_receiver = serializers.CharField(max_length=200)
    phone_receiver = serializers.CharField(max_length=10)
    status = serializers.BooleanField()
    note = serializers.CharField(max_length=50)
    logs = serializers.CharField()
    total_price = serializers.FloatField()
    cancel = serializers.BooleanField()
    request_cancel = serializers.BooleanField()
    
class OrderHandleDataSerializer(serializers.Serializer):
    order = OrderSerializer(many = False)
    transport = TransportSerializer(many = False)
    products = ProductSerializer(many = True)
    
class TransportModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = "__all__" 
        
class OrderModelSerializer(serializers.ModelSerializer):
    transport = TransportModelSerializer(many = False)
    detail_orders = TransportModelSerializer(many = True)
    class Meta:
        model = Order
        fields = "__all__"
class DetailOrderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailOrder
        fields = "__all__"
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['total_price' , 'cod' , 'created_at']
        