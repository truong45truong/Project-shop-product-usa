GET_ALL_ORDER_ADMIN = """
SELECT * , `login_user`.`email` as 'user_email',
`order_transport`.`name` as 'transport_name'
FROM `order_order`
INNER JOIN `login_user` 
	ON ( `order_order`.`user_id_id` = `login_user`.`id` )
INNER JOIN `order_transport` 
	ON ( `order_order`.`transport_id_id` = `order_transport`.`id` )
WHERE
	`order_order`.`datetime` BETWEEN {date_start} AND {date_end}
LIMIT {start},{end}
"""
GET_ALL_ORDER_REQUEST_ADMIN = """
SELECT * , `login_user`.`email` as 'user_email',
`order_transport`.`name` as 'transport_name'
FROM `order_order`
INNER JOIN `login_user` 
	ON ( `order_order`.`user_id_id` = `login_user`.`id` )
INNER JOIN `order_transport` 
	ON ( `order_order`.`transport_id_id` = `order_transport`.`id` )
WHERE `order_order`.`status` = 1 AND `order_order`.`confirm` = 0
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
            date_start = "{date_start}" , 
            date_end = "{date_end}"
        )
    def setPageRequest(self,page,numberquantity):
        start = (int(page)-1)*int(numberquantity)
        end = int(numberquantity)
        self.raw_query = self.raw_query.format(
            start =  str(start), end = str(end)
        )
    def setDate(self,date_start,date_end):
        self.raw_query = self.raw_query.format(
            date_start = str(date_start), date_end = str(date_end)
        )

    def SetKeySearch(self, key_search):
        self.raw_query = self.raw_query.format(
            key_search =  str(key_search) , 
            start = "{start}" ,
            end = "{end}"
        )
    def getQueryRaw(self):
        return self.raw_query