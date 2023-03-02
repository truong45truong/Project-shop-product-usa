from rest_framework import serializers

class VoucherSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    detail = serializers.CharField()
    sale = serializers.FloatField()
    description = serializers.CharField()
    quantity = serializers.IntegerField()