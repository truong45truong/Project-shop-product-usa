
# ---------------------------------------------------------------------------- #
#                    GET ALL USER WITH PAPGE PARAMS : [PAGE]                   #
# ---------------------------------------------------------------------------- #

QUERY_GET_ALL_USER_WITH_PAGE = """
    SELECT * FROM `login_user` WHERE `login_user`.is_superuser != 1 LIMIT {start},{end} ;
"""
QUERY_SEARCH_USER = """
    SELECT * FROM `login_user` 
    WHERE 
        `login_user`.is_superuser != 1
        AND 
        (
            `login_user`.`email` LIKE "%%{key_search}%%"
            OR `login_user`.`username` LIKE "%%{key_search}%%"
            OR `login_user`.`username` LIKE "%%{key_search}%%"
        )
"""
class HandleQueryRaw:
    def __init__(self,raw_query):
        self.raw_query = raw_query
    def setPage(self,page,numberquantity):
        start = (int(page)-1)*int(numberquantity)
        end = (int(page)-1)*int(numberquantity) + int(numberquantity)
        self.raw_query = self.raw_query.format(
            start =  str(start), end = str(end)
        )
    def SetKeySearchUser(self, key_search):
        self.raw_query = self.raw_query.format(
            key_search =  str(key_search)
        )
    
    def getQueryRaw(self):
        return self.raw_query
