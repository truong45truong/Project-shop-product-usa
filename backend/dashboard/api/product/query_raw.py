# ---------------------------------------------------------------------------- #
#                             PARAMS : [PRODUCT_ID]                            #
# ---------------------------------------------------------------------------- #
GET_ALL_PRODUCT_ADMIN = """
    SELECT `product_product`.`name` ,
     `product_product`.`id`,
        `product_product`.`quantity` as 'product_quantity' ,
        `product_price`.`price` ,
        `product_price`.`sale` ,
        `product_price`.`price_total`,
        `product_category`.`name` as 'category_name'
    FROM 
        `product_product`,`product_price`,`product_category`
    WHERE
        `product_product`.`id` = `product_price`.`product_id_id`
        AND `product_product`.`id` = `product_price`.`product_id_id`
        AND `product_product`.`category_id_id` = `product_category`.`id`
    LIMIT {start},{end}
"""

GET_ALL_PRODUCT_SEARCH = """
    SELECT `product_product`.`name` ,
     `product_product`.`id`,
        `product_product`.`quantity` as 'product_quantity' ,
        `product_price`.`price` ,
        `product_price`.`sale` ,
        `product_price`.`price_total`,
        `product_category`.`name` as 'category_name'
    FROM 
        `product_product`,`product_price`,`product_category`
    WHERE
        `product_product`.`id` = `product_price`.`product_id_id`
        AND `product_product`.`id` = `product_price`.`product_id_id`
        AND `product_product`.`category_id_id` = `product_category`.`id`
        AND 
            (
                `product_product`.`name` LIKE "%%{key_search}%%"
                OR `product_category`.`name` LIKE "%%{key_search}%%"
                OR `product_price`.`price_total` LIKE "%%{key_search}%%"

            )
    LIMIT {start},{end}
"""
QUERY_SQL_GET_PRODUCT_DETAIL_ADMIN = """
    SELECT  `product_product`.`id`, `product_product`.`slug`, 
            `product_product`.`name`, `product_product`.`sex`, 
            `product_product`.`description`,
            `product_price`.`price`, `product_price`.`sale`, 
            `product_product`.`quantity` as 'product_quantity' ,
            `product_product`.`description`,
            `product_category`.`name` as 'category_name',
            (
                SELECT COUNT(U0.`id`) AS `heart_count` 
                FROM `blog_product_heart` U0 
                WHERE U0.`product_id_id` = `product_product`.`id`
            ) AS `count_heart` ,
            (
                SELECT 
                    GROUP_CONCAT(`product_photo_product`.`data` SEPARATOR ',' )
                FROM 
                    `product_photo_product`
                WHERE 
                    `product_photo_product`.`product_id_id` = `product_product`.`id`
            )  AS `file_media_product` 
            

    FROM `product_product` 
    INNER JOIN `product_price` 
        ON (`product_product`.`id` = `product_price`.`product_id_id`)
    INNER JOIN `product_category`
        ON (`product_product`.`category_id_id` = `product_category`.`id`)
    WHERE 
        (
            `product_price`.`id` IS NOT NULL 
            AND `product_product`.`slug` = %s
        )
"""
# ---------------------------------------------------------------------------- #
#                                    VOUCHER                                   #
# ---------------------------------------------------------------------------- #
QUERY_GET_NUMBER_VOUCHER = """
    SELECT COUNT(`flashSaleProduct_voucher`.`id`) as 'count'
    FROM `flashSaleProduct_voucher`
"""
QUERY_GET_ALL_VOUCHER_NO_PRODUCT = """
    SELECT *
    FROM `flashSaleProduct_voucher`
    WHERE NOT EXISTS (
        SELECT 1
        FROM `flashSaleProduct_detailvoucher`
        WHERE `flashSaleProduct_voucher`.`id` = `flashSaleProduct_detailvoucher`.`voucher_id_id`
    )
    LIMIT {start},{end}
"""

QUERY_GET_ALL_VOUCHER_WITH_PAGE = """
    SELECT *,
        COALESCE((
            SELECT COUNT(`flashSaleProduct_detailvoucher`.id)
            FROM `flashSaleProduct_detailvoucher`
            WHERE `flashSaleProduct_voucher`.`id` = `flashSaleProduct_detailvoucher`.`voucher_id_id`
        ), 0) AS 'count_product'
    FROM `flashSaleProduct_voucher`
    WHERE `flashSaleProduct_voucher`.`level` = {level}
    LIMIT {start},{end}
"""
QUERY_SEARCH_ALL_VOUCHER_WITH_PAGE = """
    SELECT * ,
        COALESCE((
            SELECT COUNT(`flashSaleProduct_detailvoucher`.id)
            FROM `flashSaleProduct_detailvoucher`
            WHERE `flashSaleProduct_voucher`.`id` = `flashSaleProduct_detailvoucher`.`voucher_id_id`
        ), 0) AS 'count_product'
    FROM `flashSaleProduct_voucher` 
    WHERE 
    	`flashSaleProduct_voucher`.`level` = {level}
        AND 
            (
                `flashSaleProduct_voucher`.`name` LIKE "%%{key_search}%%"
                OR `flashSaleProduct_voucher`.`detail` LIKE "%%{key_search}%%" 
                OR `flashSaleProduct_voucher`.`sale` LIKE "%%{key_search}%%"
            )
    LIMIT {start},{end}
"""
# ---------------------------------------------------------------------------- #
#                                  FLASH SALE                                  #
# ---------------------------------------------------------------------------- #

QUERY_GET_ALL_FLASH_SALE_NO_PRODUCT = """
    SELECT * , 0 as 'count_product'
    FROM `flashSaleProduct_flashsale`
    WHERE NOT EXISTS (
        SELECT 1
        FROM `flashSaleProduct_detailflashsale`
        WHERE `flashSaleProduct_flashsale`.`id` = `flashSaleProduct_detailflashsale`.`flash_sale_id_id`
    )
    LIMIT {start},{end}
"""
QUERY_GET_ALL_FLASH_SALE_WITH_PAGE = """
    SELECT *,
        COALESCE((
            SELECT COUNT(`flashSaleProduct_detailflashsale`.id)
            FROM `flashSaleProduct_detailflashsale`
            WHERE `flashSaleProduct_flashsale`.`id` = `flashSaleProduct_detailflashsale`.`flash_sale_id_id`
        ), 0) AS 'count_product'
    FROM `flashSaleProduct_flashsale`
    LIMIT {start},{end}
"""

QUERY_SEARCH_ALL_FLASH_SALE_WITH_PAGE = """
    SELECT *,
        COALESCE((
            SELECT COUNT(`flashSaleProduct_detailflashsale`.id)
            FROM `flashSaleProduct_detailflashsale`
            WHERE `flashSaleProduct_flashsale`.`id` = `flashSaleProduct_detailflashsale`.`flash_sale_id_id`
        ), 0) AS 'count_product'
    FROM `flashSaleProduct_flashsale`
    WHERE 
            (
                `flashSaleProduct_flashsale`.`name` LIKE "%%{key_search}%%"
                OR `flashSaleProduct_flashsale`.`note` LIKE "%%{key_search}%%" 
            )
    LIMIT {start},{end}
"""
class HandleQueryRaw:
    def __init__(self,raw_query):
        self.raw_query = raw_query
    def setPage(self,page,numberquantity):
        start = (int(page)-1)*int(numberquantity)
        end = int(numberquantity)
        self.raw_query = self.raw_query.format(
            start =  str(start), end = str(end) ,
        )
    def SetKeySearchProduct(self, key_search):
        self.raw_query = self.raw_query.format(
            key_search =  str(key_search) , 
            start = "{start}" ,
            end = "{end}"
        )
    # ---------------------------------- VOUCHER --------------------------------- #
    def SetKeySearchVocuher(self, key_search):
        self.raw_query = self.raw_query.format(
            key_search =  str(key_search) , 
            level = "{level}" ,
            start = "{start}" ,
            end = "{end}"
        )
    def setPageVoucher(self,page,numberquantity):
        start = (int(page)-1)*int(numberquantity)
        end = (int(page)-1)*int(numberquantity) + int(numberquantity)
        self.raw_query = self.raw_query.format(
            start =  str(start), end = str(end) ,
            level = "{level}",
        )
    def setLevelVoucher(self,level):
        self.raw_query = self.raw_query.format(
            level =  str(level)
        )
    # -------------------------------- FLASH SALE -------------------------------- #
    def SetKeySearchFlashSale(self, key_search):
        self.raw_query = self.raw_query.format(
            key_search =  str(key_search) , 
            start = "{start}" ,
            end = "{end}"
        )
    def setPageFlashSale(self,page,numberquantity):
        start = (int(page)-1)*int(numberquantity)
        end = int(numberquantity)
        self.raw_query = self.raw_query.format(
            start =  str(start), end = str(end) ,
        )
    
    def getQueryRaw(self):
        return self.raw_query
    
def handleRawQuery(queryset):
    try:
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
    except:
        product_dict = dict()
        for i in queryset:
            if i.id not in product_dict:
                product_dict[i.id] = {
                    'data' : i.data ,
                    'status_heart' : i.status_heart,
                    'description' : i.description,
                    'price' : i.price,
                    'slug' : i.slug,
                    'name' : i.name,
                    'sex' :i.sex,
                    'sale' : i.sale,
                    'count_heart' : i.count_heart ,
                    'id' : i.id,
                }
            product_list = []
        for i in product_dict:
            product_list.append(product_dict[i])
    return product_list,len(queryset)