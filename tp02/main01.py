




#!/usr/bin/env python

import os
import sys
from pprint import pprint

def make_incrementor(inc_value):
    l =[]
    def f(value_to_inc):
        return value_to_inc+inc_value
    
    return f

def main():
    do_inc = make_incrementor(3)
    r = do_inc(5)
    print(r) # 8

    r = do_inc(2)
    print(r) # 5
if __name__=='__main__':
    main()
