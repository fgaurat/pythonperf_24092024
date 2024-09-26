#!/usr/bin/env python

import os
import sys
from pprint import pprint
import lib

the_var = 12

def main():
    # global the_var
    a = 2
    b =3
    

    if False:
        the_var = 5467
        print("block the_var",the_var)
    print("the_var",the_var)

    r = lib.add(a,b)

    print("name",__name__) #dunder
    print(r)

    print(lib.v)


if __name__=='__main__':
    print("avant",the_var)
    main()
    print("après",the_var)
