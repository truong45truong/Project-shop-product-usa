from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.response import Response
from rest_framework import status

from . import encryptRSA
from .models import DeviceClient
import json
import datetime

# ---------------------------------------------------------------------------- #
#                       METHOD GET PUBLIC KEY DECRYPT RSA                      #
# ---------------------------------------------------------------------------- #
@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def get_public_key_rsa(request):
    try:
        # ---------------------------- check params input ---------------------------- #
        data_request= json.loads(request.body.decode('utf-8'))
        ip_address = request.META.get('REMOTE_ADDR')
        print(ip_address)
        response = Response()
        deviceId = data_request['params']['device_id']
        
    except:
        response.data = { 
            'success' : 'success failure' , "status" : status.HTTP_404_NOT_FOUND ,
            "error" : { "value" : "Params input wrong" , "type" : "GPKR-0001"}           
        }
        response.status = status.HTTP_404_NOT_FOUND
        return response
    try:
        # ----------------------------- check information ---------------------------- #
        if deviceId != False :
            datetimeActivate = datetime.datetime.now()
            device_current = DeviceClient.objects.filter(id = deviceId)
            if len(device_current) == 1 :
                publicKey = encryptRSA.getPublicKey(device_current[0].public_key)
                device_current[0].date_activate = datetimeActivate
                device_current[0].save()
                
                response.data = { 'success' : 'success' , 
                                'public_key' :publicKey,
                                'device_id' : deviceId
                }
                response.status = status.HTTP_200_OK
                return response
            
            else :
                response.data = { 'success' : 'success failure' ,"status" : status.HTTP_204_NO_CONTENT }
                response.status = status.HTTP_204_NO_CONTENT
                return response
            
        else:
            datetimeCreated = datetime.datetime.now()
            
            device_created = DeviceClient.objects.create(
                created = datetimeCreated,
                expired = 5 ,
            )
            device_created.save()
            key = encryptRSA.generateKey(device_created.id)
            device_created.private_key = str(key['name_private_key']),
            device_created.public_key = key['name_public_key']
            device_created.date_activate = datetimeCreated
            device_created.save()
            
            response.data = { 
                'success' : 'get token decrypt rsa success' , 'public_key' :key['public_key'],
                'device_id' : device_created.id , "status" : status.HTTP_200_OK
            }
            response.status = status.HTTP_201_CREATED
            return response
        
    except Exception as e:
        print(e)
        response.data = { 
            'success' : 'success failure' , "status" : status.HTTP_404_NOT_FOUND ,
            "error" : { "value" : "Information wrong" , "type" : "GPKR-0001"}           
        }
        response.status = status.HTTP_404_NOT_FOUND
        return response