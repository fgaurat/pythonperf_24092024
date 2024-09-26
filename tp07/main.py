#!/usr/bin/env python

import os
import sys
from pprint import pprint
from CustomerDAO import CustomerDAO

def main():
    dao = CustomerDAO("customers_db.db")
    customers = dao.find_all()
    breakpoint()
    print(next(customers))
    print(next(customers))
    # print(len(list(customers) ))
    # for customer in customers:
    #     print(customer)

if __name__=='__main__':
    main()
