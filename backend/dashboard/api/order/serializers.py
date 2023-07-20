from rest_framework.serializers import ModelSerializer,SerializerMethodField,ListSerializer,UUIDField
from product.models import Category,Price,Photo_product,Product,Price
from rest_framework import serializers
from order.models import Order ,Qrcode
from login.models import User

class QrCodeSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Qrcode
        fields = "__all__"
class OrderRawSerializer(serializers.Serializer):
    id = UUIDField()
    name = serializers.CharField()
    datetime = serializers.DateTimeField()
    receiver = serializers.CharField()
    address_receiver = serializers.CharField()
    phone_receiver = serializers.CharField()
    status = serializers.BooleanField()
    is_payment = serializers.BooleanField()
    note = serializers.CharField()
    logs = serializers.CharField()
    total_price = serializers.FloatField()
    cancel = serializers.BooleanField()
    request_cancel = serializers.BooleanField()
    transport_name = serializers.CharField()
    user_email = serializers.CharField()
class OrderSerializer(serializers.ModelSerializer):
    user_email = serializers.SerializerMethodField()
    transport_name = serializers.SerializerMethodField()
    qr_code_id = QrCodeSerialzier(many = False)
    class Meta:
        model = Order
        fields = '__all__'

    def get_user_email(self, obj):
        return obj.user_id.email

    def get_transport_name(self, obj):
        return obj.transport_id.name
