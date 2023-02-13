from rest_framework.serializers import ModelSerializer
from login.models import User,Address,PhoneUser

class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
class PhoneUserSerializer(ModelSerializer):
    class Meta:
        model = PhoneUser
        fields = '__all__'
class UserSerializer(ModelSerializer):
    address = AddressSerializer(many= True) 
    phones = PhoneUserSerializer(many = True)
    class Meta:
        model = User
        fields = ['username','email','photo','address','token_permission_infor_user','name','phones']
