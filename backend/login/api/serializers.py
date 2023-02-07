from rest_framework.serializers import ModelSerializer
from login.models import User,Address

class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
class UserSerializer(ModelSerializer):
    address = AddressSerializer(many= True) 
    class Meta:
        model = User
        fields = ['username','email','photo','address','token_permission_infor_user','phone']