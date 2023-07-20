from rest_framework import serializers
from login.models import User

class UserAdminSerializer(serializers.Serializer):
    username  = serializers.CharField()
    email  = serializers.CharField()
    name  = serializers.CharField()
    date_joined = serializers.DateTimeField()
    is_active = serializers.BooleanField()
