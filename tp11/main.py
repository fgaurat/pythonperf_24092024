#!/usr/bin/env python

import os
import sys
from pprint import pprint
from CustomerDAO import CustomerDAO
def main():
    dao = CustomerDAO('customers_db.db')
    r = dao.find_all()
    print(list(r))
if __name__=='__main__':
    main()
