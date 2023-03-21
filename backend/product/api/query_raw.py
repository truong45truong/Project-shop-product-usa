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
                FROM `product_heart` U0 
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
                        (1) AS `a` FROM `product_heart` U0 
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
                        `product_heart` U0 
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
                `product_heart` U0 
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

QUERY_SQL_GET_PRODUCT_FOR_CATEGORY_SLUG = """
    SELECT *
    FROM 
        (
            (
                    SELECT NULL AS content_id, NULL AS question, NULL AS answer, node.*, 
                        (
                            SELECT COUNT(parent1.id) - 1
                            FROM faq_categories AS node1,
                            faq_categories AS parent1
                            WHERE node1.lft BETWEEN parent1.lft AND parent1.rgt AND node1.id = node.id
                            GROUP BY node1.name
                            ORDER BY node1.lft
                        ) AS level
                FROM `faq_contents` as content
                LEFT JOIN `faq_categories` AS node ON node.`id` = content.`category_id`
                LEFT JOIN `faq_categories` AS parent ON parent.`id` = content.`category_id`
                WHERE node.lft BETWEEN parent.lft AND parent.rgt
                GROUP BY node.id

            )
            UNION ALL
            (
                    SELECT content.id AS content_id, content.question, content.answer, node.*, 
                        (
                                CASE WHEN content.id IS NULL THEN
                                (
                                    SELECT COUNT(parent1.id) - 1
                                    FROM faq_categories AS node1,
                                        faq_categories AS parent1
                                    WHERE node1.lft BETWEEN parent1.lft AND parent1.rgt AND node1.id = node.id
                                    GROUP BY node1.name
                                    ORDER BY node1.lft
                                )
                                ELSE 3 END
                        ) AS level
                    FROM `faq_contents` AS content
                    RIGHT JOIN `faq_categories` AS node ON node.`id` = content.`category_id`
            )
    ) node
    ORDER BY lft
"""
