def handleRawQueryVoucher(queryset):
    voucher_dict = dict()
    for i in queryset:
        if i.id not in voucher_dict:
            voucher_dict[i.id] = {
                "voucher" :{
                    'id' : i.id ,
                    'detail' : i.detail,
                    'sale' : i.sale,
                    'description' : i.description,
                    'quantity' : i.quantity,
                    'limited_price' : i.limited_price
                },
                "product_in_vouchers" : [
                    {
                        "product_slug_in_voucher" : i.product_slug_in_voucher
                    }
                ]
            }
        else :
            voucher_dict[i.id]['product_in_vouchers'].append({
                "product_slug_in_voucher" : i.product_slug_in_voucher
            })
        voucher_list = []
    for i in voucher_dict:
        voucher_list.append(voucher_dict[i])
    print(voucher_list)
    return voucher_list,len(queryset)