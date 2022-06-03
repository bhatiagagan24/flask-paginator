from db_cache import Db_Ops as paginator_db
from uid_gen import user_id_gen
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

    # Object maker method, declares all the existing objects
    def object_maker(self):
        # Declaring the database ops object
        self.db_object = self.enable_database_object(database_name=self.db_name)
        self.user_id_object = user_id_gen()

    def enable_database_object(self, database_name : str) -> paginator_db:
        return paginator_db(database_name=database_name)


    def fetch_page_size(self):
        return self.page_size
    
    def fetch_db_name(self):
        if self.db_name_provided_bool == True:
            return self.db_name
        else:
            return None
    


