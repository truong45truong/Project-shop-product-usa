from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from flashSaleProduct.models import Voucher
from .serializers import VoucherHandleRawSQL
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from login.models import User
from . import  data_processing
class VoucherViewSet (viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    @action(method=['GET'],detail=False, url_path="get_voucher",url_name="get_voucher")
    def get_voucher(self, request,*args, **kwargs):
        token_permission_infor_user = request.GET['token_permission_infor_user']
        email_user = request.GET['email_user']
        try:
            user_current = User.objects.get(email = email_user,token_permission_infor_user=token_permission_infor_user)
        except Exception as e:
            print(e)
            return Response({"data" : False})
        querySql = """
                SELECT 
                    `flashSaleProduct_voucher`.`id` as 'id' , 
                    `flashSaleProduct_voucher`.`name` as 'name', 
                    `flashSaleProduct_voucher`.`detail` as 'detail', 
                    `flashSaleProduct_voucher`.`sale` as 'sale',
                    `flashSaleProduct_voucher`.`description` as 'description',
                    `flashSaleProduct_voucher`.`quantity` as 'quantity',
                    `product_product`.`slug` as 'product_slug_in_voucher',
                    `flashSaleProduct_voucher`.`limited_price`
                FROM 
                    `flashSaleProduct_voucher`, `flashSaleProduct_detailvoucher` ,`product_product`
                WHERE
                    `flashSaleProduct_voucher`.`level` = %s 
                    and `product_product`.`id` = `flashSaleProduct_detailvoucher`.`product_id_id`
                    and `flashSaleProduct_voucher`.`id` = `flashSaleProduct_detailvoucher`.`voucher_id_id`
        """
        queryset,numberVoucher = data_processing.handleRawQueryVoucher(Voucher.objects.raw(querySql,[user_current.level]))
        serializer = VoucherHandleRawSQL(queryset,many =True)
        return Response({"data" : serializer.data , 'number_voucher' : numberVoucher})