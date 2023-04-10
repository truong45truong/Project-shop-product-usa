# ---------------------------------------------------------------------------- #
#                            PARAMS : [PRODUCT_SLUG]                           #
# ---------------------------------------------------------------------------- #
QUERY_SQL_GET_PRODUCT_DETAIL_NOT_USER = """
    SELECT  `product_product`.`id`, `product_product`.`slug`, 
            `product_product`.`name`, `product_product`.`sex`, 
            `product_product`.`description`, `product_photo_product`.`data`, 
            `product_price`.`price`, `product_price`.`sale`, 
            `product_product`.`description`,
            (
                SELECT COUNT(U0.`id`) AS `heart_count` 
                FROM `blog_product_heart` U0 
                WHERE U0.`product_id_id` = `product_product`.`id`
            ) AS `count_heart` FROM `product_product` 
    INNER JOIN `product_photo_product` 
        ON (`product_product`.`id` = `product_photo_product`.`product_id_id`) 
    INNER JOIN `product_price` 
        ON (`product_product`.`id` = `product_price`.`product_id_id`) 
    WHERE 
        (
            `product_photo_product`.`id` IS NOT NULL 
            AND `product_price`.`id` IS NOT NULL 
            AND `product_product`.`slug` = %s 
        )
"""

# ---------------------------------------------------------------------------- #
#                              PARAMS : [USER_ID]                              #
# ---------------------------------------------------------------------------- #

QUERY_SQL_GET_ALL_PRODUCT_FOR_USER = """
    SELECT  `product_product`.`id`, `product_product`.`slug`, 
            `product_product`.`name`, `product_product`.`sex`, 
            `product_product`.`description`, `product_photo_product`.`data`, 
            `product_price`.`price`, `product_price`.`sale`, 
            `product_product`.`description`,
            EXISTS
                (
                    SELECT 
                        (1) AS `a` FROM `blog_product_heart` U0 
                    WHERE 
                    (
                        U0.`user_id_id` = %s 
                        AND U0.`product_id_id` = `product_product`.`id`
                    ) 
                    LIMIT 1
                ) AS `status_heart`, 
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
    WHERE 
        (   
            `product_photo_product`.`id` IS NOT NULL 
            AND `product_price`.`id` IS NOT NULL
        )
"""

# ---------------------------------------------------------------------------- #
#                                PARAMS : EMPTY                                #
# ---------------------------------------------------------------------------- #

QUERY_SQL_GET_ALL_PRODUCT_NOT_USER = """
    SELECT  
        `product_product`.`id`, `product_product`.`slug`, 
        `product_product`.`name`, `product_product`.`sex`, 
        `product_product`.`description`, `product_photo_product`.`data`, 
        `product_price`.`price`, `product_price`.`sale`, 
        `product_product`.`description` ,
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
    WHERE 
        (
            `product_photo_product`.`id` IS NOT NULL 
            AND `product_price`.`id` IS NOT NULL
        )
"""

# ---------------------------------------------------------------------------- #
#                   PARAMS: [ CATEGORY_LFT, CATEGORY_RGHT  ]                   #
# ---------------------------------------------------------------------------- #
CONSTANTS_FILTER_SORT =  dict()
CONSTANTS_FILTER_SORT['S-1'] = '`product_product`.`name` ASC'
CONSTANTS_FILTER_SORT['S-2'] = '`product_product`.`name` DESC'
CONSTANTS_FILTER_SORT['S-3'] = '`product_price`.`price` ASC'
CONSTANTS_FILTER_SORT['S-4'] = '`product_price`.`price` DESC'

# CONSTANTS_FILTER_SORT['S-5'] = '`product_product`.`price` ASC'
# CONSTANTS_FILTER_SORT['S-6'] = '`product_product`.`price` DESC'

CONSTANTS_FILTER_WHERE =  dict()
CONSTANTS_FILTER_SORT['S-1'] = '`product_product`.`name` ASC'

CONSTANTS_FILTER_LIMIT =  dict()
CONSTANTS_FILTER_LIMIT['up'] = 'AND `product_price`.`price` >= '
CONSTANTS_FILTER_LIMIT['down'] = 'AND `product_price`.`price` <= '
CONSTANTS_FILTER_LIMIT['category'] = 'AND `product_category`.`slug` in ('
CONSTANTS_FILTER_LIMIT['category_main'] = 'AND `product_category`.`slug` in ('
CONSTANTS_INSERT_TABLE = dict()
CONSTANTS_INSERT_TABLE['category'] = """
    INNER JOIN `product_category`
            ON ( `product_product`.`category_id_id` = `product_category`.`id` )
"""
QUERY_SQL_GET_ALL_PRODUCT_WITH_CATEGORY_AND_NOT_USER = """
    SELECT  
        `product_product`.`id`, `product_product`.`slug`, 
        `product_product`.`name`, `product_product`.`sex`, 
        `product_product`.`description`, `product_photo_product`.`data`, 
        `product_price`.`price`, `product_price`.`sale`, 
        `product_product`.`description` ,`product_category`.`slug` as 'category_slug',
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
        ON ( `product_product`.`category_id_id` = `product_category`.`id` )
    WHERE 
        (
            `product_photo_product`.`id` IS NOT NULL 
            AND `product_price`.`id` IS NOT NULL
            AND `product_category`.`tree_id` = %s
            AND `product_category`.`lft` >= %s
            AND `product_category`.`rght` <= %s
            {filter}
            {filter_category}
        )
    {order_by}
"""
QUERY_SQL_SEARCH_ALL_PRODUCT = """
    SELECT  
        `product_product`.`id`, `product_product`.`slug`, 
        `product_product`.`name`, `product_product`.`sex`, 
        `product_product`.`description`, `product_photo_product`.`data`, 
        `product_price`.`price`, `product_price`.`sale`, 
        `product_product`.`description` ,
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
    {insert_table}
    WHERE 
        (
            `product_photo_product`.`id` IS NOT NULL 
            AND `product_price`.`id` IS NOT NULL
            AND  
            	(
                    `product_product`.`name` LIKE "%%{key_search}%%"
                    OR `product_product`.`description` LIKE "%%{key_search}%%"
            	)
            {filter_category}
            {filter}
        )
    {order_by}
    LIMIT {limit_search}
"""

QUERY_SEARCH_PRODUCT_IN_CATEGORY = """
        SELECT `product_category`.*,
            (
                SELECT 
                    COUNT(U.`id`) AS `number_product` 
                FROM 
                    `product_product` U
                WHERE 
                    U.`category_id_id` = `product_category`.`id`
                    AND 
                        (
                            U.`name` LIKE "%%{key_search}%%"
                            OR U.`description` LIKE "%%{key_search}%%"
                        )

            ) AS `number_product` 
        FROM `product_category`
        WHERE `product_category`.`name` LIKE "%%{key_search}%%"
        ORDER BY `number_product` DESC
        LIMIT 8
"""
class HandleProductCategory:
    def __init__(self,raw_query):
        self.raw_query = raw_query
        self.order_by_number = 0
        self.filter_by_number = 0
        self.stringQueryOrderBy = "ORDER BY "
        self.stringQueryFilter = ''
        self.filter_category = False
        self.stringFilterCategory = ''
        self.stringInsertTable = ''
        self.insert_category = False
        
    def addFilterWithKey(self,key,up,down,value):
        if up != False:
            self.stringQueryFilter = self.stringQueryFilter + CONSTANTS_FILTER_LIMIT['up']+ str(up) + '\n'
            self.filter_by_number = self.filter_by_number + 1
        if down != False:
            self.stringQueryFilter = self.stringQueryFilter + CONSTANTS_FILTER_LIMIT['down']+ str(down) + '\n'
            self.filter_by_number = self.filter_by_number + 1

        if key in CONSTANTS_FILTER_LIMIT.keys() == False or key == False:
            return
        else:
            print("key in CONSTANTS_FILTER_LIMIT.keys()",key in CONSTANTS_FILTER_LIMIT.keys())
            if self.filter_category == False:
                self.stringFilterCategory = self.stringFilterCategory + CONSTANTS_FILTER_LIMIT['category'] + "'" +str(value) + "'"
                self.filter_category = True
            else:
                self.stringFilterCategory = self.stringFilterCategory + "," + "'" +str(value) + "'"
    def addOrderByWithKey(self,key):
        if key in CONSTANTS_FILTER_SORT.keys() == False:
            return
        if(self.order_by_number == 0):
            self.stringQueryOrderBy = self.stringQueryOrderBy + CONSTANTS_FILTER_SORT[key]
        else:
                self.stringQueryOrderBy = self.stringQueryOrderBy + ', ' + CONSTANTS_FILTER_SORT[key]
        self.order_by_number = self.order_by_number + 1
    def insertTableWithKey(self,key):
        if key in CONSTANTS_INSERT_TABLE.keys() == False:
            return
        self.stringInsertTable = self.stringInsertTable + CONSTANTS_INSERT_TABLE[key]
        self.insert_category = True
    def getQuery(self):
        if self.filter_category == True:
            self.stringFilterCategory = self.stringFilterCategory + ')'
            self.raw_query = self.raw_query.format(
                filter_category = self.stringFilterCategory ,filter = '{filter}',
                order_by = '{order_by}' ,insert_table  = '{insert_table}'
            )
        else:
            self.raw_query = self.raw_query.format(
                filter_category = '' ,filter = '{filter}',
                order_by = '{order_by}',insert_table  = '{insert_table}' 
            )
            
        if self.insert_category == True:
            self.raw_query = self.raw_query.format(insert_table = self.stringInsertTable ,filter = '{filter}',order_by = '{order_by}' )
        else:
            self.raw_query = self.raw_query.format(insert_table = '' ,filter = '{filter}',order_by = '{order_by}' )
            
        if self.filter_by_number == 0 and self.order_by_number == 0:
            return self.raw_query.format(filter = '',order_by = '' )
        
        if  self.filter_by_number != 0 and self.order_by_number == 0:
            return self.raw_query.format(filter = self.stringQueryFilter  ,order_by = '' )  
        
        if  self.filter_by_number == 0 and self.order_by_number != 0:
            print('elf.stringQueryOrderBy',self.stringQueryOrderBy)
            return self.raw_query.format(filter = ''  ,order_by = self.stringQueryOrderBy )
        
        if  self.filter_by_number != 0 and self.order_by_number != 0:
            return self.raw_query.format(filter = self.stringQueryFilter  ,order_by = self.stringQueryOrderBy )
        
    def searchProductWithKeyValue(self,key_value,limit_search):
        if limit_search == False:
            self.raw_query = self.raw_query.format(
                key_search =  key_value,limit_search = '',filter_category = '{filter_category}',
                insert_table= '{insert_table}' ,filter =  '{filter}' , order_by ='{order_by}'
            )
        else:
            self.raw_query = self.raw_query.format(
                key_search =  key_value,limit_search = str(limit_search),filter_category = '{filter_category}',
                insert_table= '{insert_table}' ,filter =  '{filter}' , order_by ='{order_by}'
            )
    def removeLimit(self):
        self.raw_query = self.raw_query.replace("LIMIT" , '')
