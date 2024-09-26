import sqlite3
from Customer import Customer
class CustomerDAO:


    def __init__(self,db_name) -> None:
        self.__con = sqlite3.connect(db_name)

    def __del__(self):
        self.__con.close()

    def find_all(self):
        sql = "SELECT * FROM customers_tbl"
        cur = self.__con.cursor()
        rs = cur.execute(sql)

        for row in rs:
            c= Customer(*row)
            yield c
