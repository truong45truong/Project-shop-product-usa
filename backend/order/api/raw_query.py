# ---------------------------------------------------------------------------- #
#                              PARAMS : [user_id]                              #
# ---------------------------------------------------------------------------- #

QUERY_SQL_GET_ALL_ORDER_FOR_USER = """
    SELECT order_order.*, order_detailorder.status as 'detail_order_status' ,
        product_product.slug as 'product_slug' , product_product.name as 'product_name',
        product_product.description as 'product_description',
        product_category.name as 'category_name', product_price.price as 'product_price',
        product_price.sale as 'product_sale' , product_price.status as 'product_price_status',
        product_price.price_total as 'product_price_total' , product_photo_product.data as 'photo_product',
        order_transport.slug as 'transport_slug' , order_transport.name as 'transport_name' ,
        order_transport.logo as 'transport_logo' , order_transport.price as 'transport_price',
        `order_detailorder`.`quantity` as 'product_quantity'
    FROM
        order_detailorder,product_product,product_price, order_transport,
        product_photo_product , product_category,order_order,login_user
    WHERE 
        order_order.id = order_detailorder.order_id_id 
        and order_transport.id = order_order.transport_id_id 
        and login_user.id = %s  
        and login_user.id = order_order.user_id_id
        and product_product.id = order_detailorder.product_id_id 
        and product_product.id = product_photo_product.product_id_id 
        and product_product.id = product_price.product_id_id
        and product_product.category_id_id = product_category.id
    ORDER BY
        order_order.datetime DESC
"""

# ---------------------------------------------------------------------------- #
#                    PARAMS : ['user_id','date_1','date_2']                    #
# ---------------------------------------------------------------------------- #

QUERY_SQL_GET_ALL_ORDER_FOR_USER_BETWEEN_DAYS = """
    SELECT order_order.*, order_detailorder.status as 'detail_order_status' ,
        product_product.slug as 'product_slug' , product_product.name as 'product_name',
        product_product.description as 'product_description',
        product_category.name as 'category_name', product_price.price as 'product_price',
        product_price.sale as 'product_sale' , product_price.status as 'product_price_status',
        product_price.price_total as 'product_price_total' , product_photo_product.data as 'photo_product',
        order_transport.slug as 'transport_slug' , order_transport.name as 'transport_name' ,
        order_transport.logo as 'transport_logo' , order_transport.price as 'transport_price',
        `order_detailorder`.`quantity` as 'product_quantity'
    FROM
        order_detailorder,product_product,product_price, order_transport,
        product_photo_product , product_category,order_order,login_user
    WHERE 
        order_order.id = order_detailorder.order_id_id 
        and order_transport.id = order_order.transport_id_id 
        and login_user.id = %s  
        and login_user.id = order_order.user_id_id
        and product_product.id = order_detailorder.product_id_id 
        and product_product.id = product_photo_product.product_id_id 
        and product_product.id = product_price.product_id_id
        and product_product.category_id_id = product_category.id
        and `order_order`.`datetime` BETWEEN %s AND %s
    ORDER BY
        order_order.datetime DESC
"""