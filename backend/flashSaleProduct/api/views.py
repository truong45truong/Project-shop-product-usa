from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework import status
from flashSaleProduct.models import Voucher
from .serializers import VoucherHandleRawSQL
from . import  data_processing
from . import  query_raw
from login.models import User


class VoucherViewSet (viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # ---------------------------------------------------------------------------- #
    #                          METHOD GET VOUCHER FOR USER                         #
    # ---------------------------------------------------------------------------- #
    @action(method=['GET'],detail=False, url_path="get_voucher",url_name="get_voucher")
    def get_voucher(self, request,*args, **kwargs):
        try:
            # ---------------------------- check params input ---------------------------- #
            # decryption token jwt
            jwtToken = request.COOKIES.get('refresh_token')
            refresh_token = RefreshToken(jwtToken)
            decoded_token = refresh_token.payload       
        except:
            return Response({
                "success" : False , "status" : status.HTTP_404_NOT_FOUND ,
                "error" : { "value" : "Params wrong" , "type" : "GV-0001" }
            })
            
        try:
            # ----------------------------- check information ---------------------------- #
            user_current = User.objects.get(id = decoded_token["user_id"])
            querySql = query_raw.QUERY_SQL_GET_VOUCHER_FOR_USER
            queryset,numberVoucher = data_processing.handleRawQueryVoucher(Voucher.objects.raw(querySql,[user_current.level]))
            serializer = VoucherHandleRawSQL(queryset,many =True)
            
            return Response({
                "data" : serializer.data , 'number_voucher' : numberVoucher ,
                "success" : "Get voucher success" , "status" :status.HTTP_200_OK
            })
        except Exception as e:
            print(e)
            return Response({
                "success" : False , "status" : status.HTTP_404_NOT_FOUND ,
                "error" : { "value" : "Information wrong" , "type" : "GV-0002" }
            })
            
    # ---------------------------------------------------------------------------- #
    #                        METHOD GET VOUCHER FOR PRODUCT                        #
    # ---------------------------------------------------------------------------- #
    @action(method=['GET'],detail=False, url_path="get_voucher",url_name="get_voucher")
    def get_voucher(self, request,*args, **kwargs):
        try:
            # ---------------------------- check params input ---------------------------- #
            # decryption token jwt
            jwtToken = request.COOKIES.get('refresh_token')
            refresh_token = RefreshToken(jwtToken)
            decoded_token = refresh_token.payload       
        except:
            return Response({
                "success" : False , "status" : status.HTTP_404_NOT_FOUND ,
                "error" : { "value" : "Params wrong" , "type" : "GV-0001" }
            })
            
        try:
            # ----------------------------- check information ---------------------------- #
            user_current = User.objects.get(id = decoded_token["user_id"])
            querySql = query_raw.QUERY_SQL_GET_VOUCHER_FOR_USER
            queryset,numberVoucher = data_processing.handleRawQueryVoucher(Voucher.objects.raw(querySql,[user_current.level]))
            serializer = VoucherHandleRawSQL(queryset,many =True)
            
            return Response({
                "data" : serializer.data , 'number_voucher' : numberVoucher ,
                "success" : "Get voucher success" , "status" :status.HTTP_200_OK
            })
        except Exception as e:
            print(e)
            return Response({
                "success" : False , "status" : status.HTTP_404_NOT_FOUND ,
                "error" : { "value" : "Information wrong" , "type" : "GV-0002" }
            })