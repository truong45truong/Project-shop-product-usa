def handleRawQuery(queryset):
    order_dict = dict()
    for i in queryset:
        if i.id not in order_dict:
            order_dict[i.id] = {
                "order" :{
                    'name' : i.name ,
                    'datetime' : i.datetime,
                    'receiver' : i.receiver,
                    'address_receiver' : i.address_receiver,
                    'phone_receiver' : i.phone_receiver,
                    'status' : i.status,
                    'note' : i.note,
                    'logs' :i.logs,
                    'total_price' : i.total_price,
                    'cancel' : i.cancel,
                    'request_cancel' : i.request_cancel
                },
                "transport" : {
                    "transport_slug" : i.transport_slug,
                    "transport_name" : i.transport_name,
                    "transport_price" : i.transport_price,
                    "transport_logo" : i.transport_logo
                },
                "products" : [
                    {
                        "product_slug" : i.product_slug,
                        "product_name" : i.product_name,
                        "product_description" : i.product_description,
                        "product_price" : i.product_price,
                        "product_sale" : i.product_sale,
                        "product_price_status" : i.product_price_status,
                        "product_price_total" : i.product_price_total ,
                        "photo_product" : i.photo_product,
                        "category_name" : i.category_name
                    }
                ]
            }
        else :
            order_dict[i.id]['products'].append({
                "product_slug" : i.product_slug,
                "product_name" : i.product_name,
                "product_description" : i.product_description,
                "product_price" : i.product_price,
                "product_sale" : i.product_sale,
                "product_price_status" : i.product_price_status,
                "product_price_total" : i.product_price_total ,
                "photo_product" : i.photo_product,
                "category_name" : i.category_name
            })
        order_list = []
    for i in order_dict:
        order_list.append(order_dict[i])
    return order_list,len(queryset)