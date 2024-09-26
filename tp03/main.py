#!/usr/bin/env python

import os
import sys
from pprint import pprint

def div(a,b):
    return a/b

def call_div(a,b):
    r=0
    try:
        print("OPEN FILE")
        r = div(a,b)
    finally:
        print("CLOSE FILE")
    return r

def main():
    r = call_div(4,2)
    print(r)

if __name__=='__main__':
    main()
