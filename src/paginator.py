from db_cache import Db_Ops as paginator_db

class Paginator:
    def __init__(self, page_size : int, name_of_the_sqlite_db = None):
        if page_size < 0:
            self.page_size = 0
        else:
            self.page_size = page_size
        
        if name_of_the_sqlite_db == None:
            self.db_name_provided_bool = False
        else:
            self.db_name_provided_bool = True
            self.db_name = name_of_the_sqlite_db

    def fetch_page_size(self):
        return self.page_size
    
    def fetch_db_name(self):
        if self.db_name_provided_bool == True:
            return self.db_name
        else:
            return None
    
    def enable_database_object(self, database_name : str):
        pass

