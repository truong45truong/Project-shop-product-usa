from rest_framework.decorators import api_view,permission_classes ,action
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response
from new.models import New,Photo_new

from .serializers import NewSerializer,PhotoNewSerializer

class NewViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    authentication_classes = []
    permission_classes = []
    
    @action(method=['GET'], detail = False , url_name='new',url_path="get_new")
    def get_new(self, request, *args, **kwargs):
        queryset = New.objects.all()
        serializer = NewSerializer(queryset,many = True)
        
        return Response(serializer.data)
    
# class PhotoNewViewSet(viewsets.ModelViewSet):
    
#     queryset = Photo_new.objects.all()
    
#     @action(method =['GET'] , detail = False, url_name="photo_new" , url_path="get_photo_new")
#     def get_photo_new(self , request, *args, **kwargs)
#         slug = request.GET['slug']
#         if slug:
#             Photo