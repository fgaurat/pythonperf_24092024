#!/usr/bin/env python

import os
import sys
from pprint import pprint

def main():
    l=[10,20,30,40,50]
    f = 300

    for i in l:
        print(i)
        if i == f:
            print("found !")
            break
    else:
        print("not found !")



if __name__=='__main__':
    main()
