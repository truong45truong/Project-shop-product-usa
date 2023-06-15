def handleRawQuery(queryset):
    product_dict = dict()
    for i in queryset:
        if i['id'] not in product_dict:
            product_dict[i['id']] = {
                'data' : i['data'] ,
                'status_heart' : i['status_heart'],
                'description' : i['description'],
                'price' : i['price'],
                'slug' : i['slug'],
                'name' : i['name'],
                'sex' :i['sex'],
                'sale' : i['sale'],
                'count_heart' : i['count_heart'] ,
                'id' : i['id'],
            }
        product_list = []
    for i in product_dict:
        product_list.append(product_dict[i])
    return product_list,len(queryset)