#!/usr/bin/env python

import os
import sys
import csv
from pprint import pprint
import sqlite3


def main():
    con = sqlite3.connect(r"customers_db.db")

    csv_file_name = "MOCK_DATA.csv"
    sql = """INSERT INTO customers_tbl(first_name,last_name,email,gender,ip_address)
    VALUES(?,?,?,?,?)"""
    with open(csv_file_name) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
            del row['id']
            con.execute(sql,list(row.values()))
    con.commit()
    con.close()

if __name__=='__main__':
    main()
