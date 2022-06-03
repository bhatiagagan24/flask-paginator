import sqlite3 as sq


class Db_Ops:
    def __init__(self, database_name: str):
        command = f'''CREATE TABLE IF NOT EXISTS table_paginator (uid STRING, start INTEGER, end INTEGER)'''
        self.con = sq.connect(database_name + ".db")
        self.con.execute(command)
    def insert_into_db(self, uid: str, start_range : int, end_range: int):
        self.con.execute('''INSERT INTO ''')        
    def remove_from_db(self, uid : str):
        pass
    def fetch_from_db(self, uid : str):
        pass