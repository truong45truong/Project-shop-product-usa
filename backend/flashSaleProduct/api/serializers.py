from rest_framework import serializers

class VoucherSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    detail = serializers.CharField()
    sale = serializers.FloatField()
    description = serializers.CharField()
    limited_price = serializers.IntegerField()
    quantity = serializers.IntegerField()
class ProductInVoucher(serializers.Serializer):
    product_slug_in_voucher = serializers.CharField()
class VoucherHandleRawSQL(serializers.Serializer):
    voucher = VoucherSerializer()
    product_in_vouchers = ProductInVoucher(many = True)