# ---------------------------------------------------------------------------- #
#                            PARAMS : [USER_ID,PRODUCT_SLUG]                           #
# ---------------------------------------------------------------------------- #
QUERY_SQL_GET_BLOG_OF_PRODUCT_WITH_USER = """
    SELECT 
        `blog_product_blog`.* ,`blog_product_blog`.`id`,
        `blog_product_blog`.`content` ,`blog_product_blog`.`date_create` , 
        `blog_product_blog`.`user_id_id` , `blog_product_blog`.`title`,
        `blog_product_comment`.`id` as 'comment_id',
        `blog_product_comment`.`content` as 'comment_content',
        `blog_product_comment`.`date_create` as 'comment_date_create',
        `blog_product_comment`.`level` as 'comment_level',
        `blog_product_comment`.`heart` as 'comment_heart',
        `blog_product_comment`.`user_id_id` as 'comment_user_id',
        `blog_product_comment`.`user_email` as 'comment_user_email',
        `blog_product_comment`.`user_profile` as 'comment_user_profile',
        `blog_product_comment`.`parent_id` as 'parent',
        `blog_product_comment`.`is_edit` as 'comment_is_edit',
        (
            SELECT 
                COUNT(U0.`id`) AS `heart_count` 
            FROM 
                `blog_product_heart` U0 
            WHERE 
                U0.blog_id_id = `blog_product_blog`.`id`

        ) AS `number_heart` ,
        (
            SELECT 
                COUNT(U0.`id`) 
            FROM 
                `blog_product_comment` U0
            WHERE 
                U0.blog_id_id = `blog_product_blog`.`id`

        ) AS `number_comment` ,
        (
            SELECT 
                COUNT(U0.`id`) AS `heart_count` 
            FROM 
                `blog_product_heart` U0 
            WHERE 
                U0.comment_id_id = `blog_product_comment`.`id`

        ) AS `comment_number_heart` ,
        (
            SELECT 
                GROUP_CONCAT( CONCAT(`blog_product_photo_blog`.`file` , ":" , `blog_product_photo_blog`.`type`) SEPARATOR ',' )
            FROM 
                `blog_product_photo_blog`
            WHERE 
                `blog_product_photo_blog`.`blog_id_id` = `blog_product_blog`.id

        ) AS `file_img_blog` ,
        (
            SELECT 
            COUNT(U0.`id`)
            FROM 
                `blog_product_comment` U0
            WHERE 
                U0.`parent_id` = `blog_product_comment`.id

        ) AS `count_comment_child` ,
        (
            SELECT 
                (1) AS `a` FROM `blog_product_heart` U0 
            WHERE 
            (
                U0.`user_id_id` = %s
                AND U0.blog_id_id = `blog_product_blog`.`id`
            ) 
            LIMIT 1
        ) AS `status_heart` ,
        (
            SELECT 
                (1) AS `a` FROM `blog_product_heart` U0 
            WHERE 
            (
                U0.`user_id_id` = %s
                AND U0.comment_id_id = `blog_product_comment`.`id`
            ) 
            LIMIT 1
        ) AS `status_heart_comment` ,
        (
            SELECT 
                GROUP_CONCAT( CONCAT( `blog_product_media_comment`.`file`, ":" , `blog_product_media_comment`.`type`) SEPARATOR ',' )
            FROM 
                `blog_product_media_comment`
            WHERE 
                `blog_product_media_comment`.`comment_id_id` = `blog_product_comment`.`id`

        ) AS `file_media_comment` 
    FROM 
        `blog_product_blog`, `blog_product_comment`,`product_product`
    WHERE 
        `product_product`.`id` = `blog_product_blog`.`product_id_id`
        AND `blog_product_comment`.`level` = 0
        AND `blog_product_blog`.`id` = `blog_product_comment`.`blog_id_id`
        AND `product_product`.`slug`= %s
"""
# ---------------------------------------------------------------------------- #
#                            PARAMS : [PRODUCT_SLUG]                           #
# ---------------------------------------------------------------------------- #
QUERY_SQL_GET_BLOG_OF_PRODUCT = """
    SELECT 
        `blog_product_blog`.* ,`blog_product_blog`.`id`,
        `blog_product_blog`.`content` ,`blog_product_blog`.`date_create` , 
        `blog_product_blog`.`user_id_id` , `blog_product_blog`.`title`,
        `blog_product_comment`.`id` as 'comment_id',
        `blog_product_comment`.`content` as 'comment_content',
        `blog_product_comment`.`date_create` as 'comment_date_create',
        `blog_product_comment`.`level` as 'comment_level',
        `blog_product_comment`.`heart` as 'comment_heart',
        `blog_product_comment`.`user_id_id` as 'comment_user_id',
        `blog_product_comment`.`user_email` as 'comment_user_email',
        `blog_product_comment`.`user_profile` as 'comment_user_profile',
        `blog_product_comment`.`parent_id` as 'parent',
        `blog_product_comment`.`is_edit` as 'comment_is_edit',
        0 as 'status_heart',
        0 as 'status_heart_comment',
        (
            SELECT 
                COUNT(U0.`id`) AS `heart_count` 
            FROM 
                `blog_product_heart` U0 
            WHERE 
                U0.blog_id_id = `blog_product_blog`.`id`

        ) AS `number_heart` ,
        (
            SELECT 
                COUNT(U0.`id`) 
            FROM 
                `blog_product_comment` U0
            WHERE 
                U0.blog_id_id = `blog_product_blog`.`id`

        ) AS `number_comment` ,
        (
            SELECT 
                COUNT(U0.`id`) AS `heart_count` 
            FROM 
                `blog_product_heart` U0 
            WHERE 
                U0.comment_id_id = `blog_product_comment`.`id`

        ) AS `comment_number_heart` ,
        (
            SELECT 
                GROUP_CONCAT( CONCAT(`blog_product_photo_blog`.`file` , ":" , `blog_product_photo_blog`.`type`) SEPARATOR ',' )
            FROM 
                `blog_product_photo_blog`
            WHERE 
                `blog_product_photo_blog`.`blog_id_id` = `blog_product_blog`.id

        ) AS `file_img_blog` ,
        (
            SELECT 
            COUNT(U0.`id`)
            FROM 
                `blog_product_comment` U0
            WHERE 
                U0.`parent_id` = `blog_product_comment`.id

        ) AS `count_comment_child` ,
        (
            SELECT 
                GROUP_CONCAT( CONCAT( `blog_product_media_comment`.`file`, ":" , `blog_product_media_comment`.`type`) SEPARATOR ',' )
            FROM 
                `blog_product_media_comment`
            WHERE 
                `blog_product_media_comment`.`comment_id_id` = `blog_product_comment`.`id`

        ) AS `file_media_comment`
    FROM 
        `blog_product_blog`, `blog_product_comment`,`product_product`
    WHERE 
        `product_product`.`id` = `blog_product_blog`.`product_id_id`
        AND `blog_product_comment`.`level` = 0
        AND `blog_product_blog`.`id` = `blog_product_comment`.`blog_id_id`
        AND `product_product`.`slug`= %s
"""
# ---------------------------------------------------------------------------- #
#                              PARAMS : [PARENT_ID]                            #
# ---------------------------------------------------------------------------- #
QUERY_SQL_GET_COMMET_CHILD = """
SELECT 
	`blog_product_comment`.`id`,
    `blog_product_comment`.`content`,
    `blog_product_comment`.`date_create`,
    `blog_product_comment`.`level`,
    `blog_product_comment`.`user_profile`,
    `blog_product_comment`.`user_email`,
    `blog_product_comment`.`parent_id`,
    0 as 'status_heart_comment',
    `blog_product_comment`.`is_edit` as 'comment_is_edit',
    (
            SELECT 
                COUNT(U0.`id`) AS `heart_count` 
            FROM 
                `blog_product_heart` U0 
            WHERE 
                U0.comment_id_id = `blog_product_comment`.`id`
        		AND U0.type = 2

        ) AS `number_heart` ,
        (
            SELECT 
            COUNT(U0.`id`)
            FROM 
                `blog_product_comment` U0
            WHERE 
                U0.`parent_id` = `blog_product_comment`.`id`
        ) AS `count_comment_child`,
        (
            SELECT 
                GROUP_CONCAT( CONCAT( `blog_product_media_comment`.`file`, ":" , `blog_product_media_comment`.`type`) SEPARATOR ',' )
            FROM 
                `blog_product_media_comment`
            WHERE 
                `blog_product_media_comment`.`comment_id_id` = `blog_product_comment`.`id`

        ) AS `file_media_comment`
      FROM
      	`blog_product_comment`
      WHERE
      	`blog_product_comment`.`parent_id` = %s
"""
# ---------------------------------------------------------------------------- #
#                       PARAMS : [USER_ID,COMMET_PARENT]                       #
# ---------------------------------------------------------------------------- #
QUERY_SQL_GET_COMMET_CHILD_WITH_USER = """
SELECT 
	`blog_product_comment`.`id`,
    `blog_product_comment`.`content`,
    `blog_product_comment`.`date_create`,
    `blog_product_comment`.`level`,
    `blog_product_comment`.`user_profile`,
    `blog_product_comment`.`user_email`,
    `blog_product_comment`.`parent_id`,
    0 as 'status_heart_comment',
    `blog_product_comment`.`is_edit` as 'comment_is_edit',
    (
            SELECT 
                COUNT(U0.`id`) AS `heart_count` 
            FROM 
                `blog_product_heart` U0 
            WHERE 
                U0.comment_id_id = `blog_product_comment`.`id`
        		AND U0.type = 2

        ) AS `number_heart` ,
        (
            SELECT 
            COUNT(U0.`id`)
            FROM 
                `blog_product_comment` U0
            WHERE 
                U0.`parent_id` = `blog_product_comment`.`id`
        ) AS `count_comment_child`,
        (
            SELECT 
                IF(COUNT(*) > 0, 1, 0) AS `status_heart_comment`
            FROM `blog_product_heart` U0 
            WHERE 
            (
                U0.user_id_id = %s
                AND U0.comment_id_id = `blog_product_comment`.id
            ) 
            LIMIT 1
        ) AS `status_heart_comment` ,
        (
            SELECT 
                GROUP_CONCAT( CONCAT( `blog_product_media_comment`.`file`, ":" , `blog_product_media_comment`.`type`) SEPARATOR ',' )
            FROM 
                `blog_product_media_comment`
            WHERE 
                `blog_product_media_comment`.`comment_id_id` = `blog_product_comment`.`id`

        ) AS `file_media_comment`
      FROM
      	`blog_product_comment`
      WHERE
      	`blog_product_comment`.`parent_id` = %s
"""
QUERY_GET_COMMENT_PRODUCT_WITH_USER = """
    SELECT 
	`blog_product_comment`.`id`,
    `blog_product_comment`.`content`,
    `blog_product_comment`.`date_create`,
    `blog_product_comment`.`level`,
    `blog_product_comment`.`user_profile`,
    `blog_product_comment`.`user_email`,
    `blog_product_comment`.`parent_id`,
    0 as 'status_heart_comment',
    `blog_product_comment`.`is_edit` as 'comment_is_edit',
    (
            SELECT 
                COUNT(U0.`id`) AS `heart_count` 
            FROM 
                `blog_product_heart` U0 
            WHERE 
                U0.comment_id_id = `blog_product_comment`.`id`
        		AND U0.type = 2

        ) AS `number_heart` ,
        (
            SELECT 
            COUNT(U0.`id`)
            FROM 
                `blog_product_comment` U0
            WHERE 
                U0.`parent_id` = `blog_product_comment`.`id`
        ) AS `count_comment_child`,
        (
            SELECT 
                IF(COUNT(*) > 0, 1, 0) AS `status_heart_comment`
            FROM `blog_product_heart` U0 
            WHERE 
            (
                U0.user_id_id = %s
                AND U0.comment_id_id = `blog_product_comment`.id
            ) 
            LIMIT 1
        ) AS `status_heart_comment` ,
        (
            SELECT 
                GROUP_CONCAT( CONCAT( `blog_product_media_comment`.`file`, ":" , `blog_product_media_comment`.`type`) SEPARATOR ',' )
            FROM 
                `blog_product_media_comment`
            WHERE 
                `blog_product_media_comment`.`comment_id_id` = `blog_product_comment`.`id`

        ) AS `file_media_comment`
      FROM
      	`blog_product_comment`
      INNER JOIN `product_product` ON `product_product`.`id` = `blog_product_comment`.`product_id_id`
      WHERE
      	`product_product`.`slug` = %s
       AND `blog_product_comment`.`level` = 0
    ORDER BY 
        `blog_product_comment`.`date_create` DESC
"""
QUERY_GET_COMMENT_PRODUCT_NOT_USER = """
    SELECT 
	`blog_product_comment`.`id`,
    `blog_product_comment`.`content`,
    `blog_product_comment`.`date_create`,
    `blog_product_comment`.`level`,
    `blog_product_comment`.`user_profile`,
    `blog_product_comment`.`user_email`,
    `blog_product_comment`.`parent_id`,
    0 as 'status_heart_comment',
    `blog_product_comment`.`is_edit` as 'comment_is_edit',
    (
            SELECT 
                COUNT(U0.`id`) AS `heart_count` 
            FROM 
                `blog_product_heart` U0 
            WHERE 
                U0.comment_id_id = `blog_product_comment`.`id`
        		AND U0.type = 2

        ) AS `number_heart` ,
        (
            SELECT 
            COUNT(U0.`id`)
            FROM 
                `blog_product_comment` U0
            WHERE 
                U0.`parent_id` = `blog_product_comment`.`id`
        ) AS `count_comment_child`,
        (
            SELECT 
                GROUP_CONCAT( CONCAT( `blog_product_media_comment`.`file`, ":" , `blog_product_media_comment`.`type`) SEPARATOR ',' )
            FROM 
                `blog_product_media_comment`
            WHERE 
                `blog_product_media_comment`.`comment_id_id` = `blog_product_comment`.`id`

        ) AS `file_media_comment`
      FROM
      	`blog_product_comment`
      INNER JOIN `product_product` ON `product_product`.`id` = `blog_product_comment`.`product_id_id`
      WHERE
      	`product_product`.`slug` = %s
       AND `blog_product_comment`.`level` = 0
    ORDER BY 
        `blog_product_comment`.`date_create` DESC
"""
class HandleSqlRaw:
    def __init__(self,raw_query):
        self.raw_query = raw_query
    def addLimit(self,start,end):
        self.raw_query += "\n LIMIT" + "\n {limit_filter_start}, {limit_filter_end}"
        self.raw_query = self.raw_query.format(
               limit_filter_start =  start ,
            limit_filter_end = end,
        )
    def getQuery( self):
        return self.raw_query