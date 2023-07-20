from rest_framework.decorators import api_view,action,permission_classes,authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from login.models import User,PhoneUser , Address


# ---------------------------------------------------------------------------- #
#                                GET INFOR ADMIN                               #
# ---------------------------------------------------------------------------- #
@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def getInforAdmin(request):
    response = Response()
    def notFound():
        response.data = {
            "success" : False , 'error' : {
                'type' : "CGIA-001" , 'value' : "Failed to Login"
            } , 
            'status' : status.HTTP_404_NOT_FOUND
        }
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
    def getInfor():
        response.data = {
            "success" : True ,
            'status' : status.HTTP_200_OK
        }
        response.status_code = status.HTTP_200_OK
        return response
    try:
        jwtToken = request.COOKIES.get('refresh_token')
        refresh_token = RefreshToken(jwtToken)
        decoded_token = refresh_token.payload
    except Exception as e:
        print(e)
        return notFound()
    try:
        user = User.objects.get(id = decoded_token['user_id'])
        print('user.is_superuser',user.is_superuser)
        if user.is_superuser == False:
            return notFound()
        return getInfor()
        
    except Exception as e:
        print(e)
        return notFound()