QUERY_SQL_GET_ALL_PRODUCT_FOR_USER = """
SELECT  `product_product`.`id`, `product_product`.`slug`, 
            `product_product`.`name`, `product_product`.`sex`, 
            `product_product`.`description`, `product_photo_product`.`data`, 
            `product_price`.`price`, `product_price`.`sale`, 
            `product_product`.`description`, 
                (
                    SELECT 
                        COUNT(U0.`id`) AS `heart_count` 
                    FROM 
                        `blog_product_heart` U0 
                    WHERE 
                        U0.`product_id_id` = `product_product`.`id`
                ) AS `count_heart` FROM `product_product` 
    INNER JOIN `product_photo_product` 
        ON (`product_product`.`id` = `product_photo_product`.`product_id_id`) 
    INNER JOIN `product_price` 
        ON (`product_product`.`id` = `product_price`.`product_id_id`) 
    INNER JOIN `product_category`
    	ON ( `product_category`.`id` = `product_product`.`category_id_id` )
    WHERE 
        (   
            `product_photo_product`.`id` IS NOT NULL 
            AND `product_price`.`id` IS NOT NULL
            AND `product_category`.`slug` IN {key_category}
        )
"""

class HandleQueryRaw:
    def __init__(self,raw_query):
        self.raw_query = raw_query
    def setCategory(self,key_category):
        self.raw_query = self.raw_query.format(
            key_category =  str(key_category)
        )
    def getQueryRaw(self):
        return self.raw_query