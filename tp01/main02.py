#!/usr/bin/env python

import os
import sys
from pprint import pprint

def main():
    print(sys.getrefcount(738))
    a=738
    print(sys.getrefcount(738))
    # b=738
    # c=738
    # print(hex(id(a)))
    # print(hex(id(b)))
    # print(hex(id(c)))
    # print(type(a))
    # # a=3738
    # print(hex(id(a)))



if __name__=='__main__':
    main()
