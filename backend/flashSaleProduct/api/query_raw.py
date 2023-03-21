# ---------------------------------------------------------------------------- #
#                               PARAMS : [USER_LEVEL]                             #
# ---------------------------------------------------------------------------- #
QUERY_SQL_GET_VOUCHER_FOR_USER = """
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

# ---------------------------------------------------------------------------- #
#                              PARAMS : [PRODUCT_SLUG]                         #
# ---------------------------------------------------------------------------- #
QUERY_SQL_GET_VOUCHER_FOR_PRODUCT = """
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
        `product_product`.`slug` = %s
        and `product_product`.`id` = `flashSaleProduct_detailvoucher`.`product_id_id`
        and `flashSaleProduct_voucher`.`id` = `flashSaleProduct_detailvoucher`.`voucher_id_id`
"""