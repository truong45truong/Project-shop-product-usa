from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from flashSaleProduct.models import Voucher
from .serializers import VoucherSerializer

class VoucherViewSet (viewsets.ViewSet):
    @action(method=['GET'],detail=False, url_path="get_voucher",url_name="get_voucher")

    def get_voucher(self, request,*args, **kwargs):
        querySql = """
                SELECT 
                    `flashSaleProduct_voucher`.`id` as 'id' , 
                    `flashSaleProduct_voucher`.`name` as 'name', 
                    `flashSaleProduct_voucher`.`detail` as 'detail', 
                    `flashSaleProduct_voucher`.`sale` as 'sale',
                    `flashSaleProduct_voucher`.`description` as 'description',
                    `flashSaleProduct_voucher`.`quantity` as 'quantity' 
                FROM 
                    `flashSaleProduct_voucher`
        """
        queryset = Voucher.objects.raw(querySql)
        serializer = VoucherSerializer(queryset,many =True)
        return Response({"data" : serializer.data})