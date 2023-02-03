from rest_framework.serializers import ModelSerializer

from new.models import New,Photo_new

        
class PhotoNewSerializer(ModelSerializer):
    class Meta:
        model = Photo_new
        fields = "__all__"

class NewSerializer(ModelSerializer):
    photo_news = PhotoNewSerializer(many = True)
    class Meta:
        model = New
        fields = ['slug','name','description','product_id','photo_news']
