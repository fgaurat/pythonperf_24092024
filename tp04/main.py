#!/usr/bin/env python

import os
import sys
from pprint import pprint

from Rectangle import Rectangle

def main():
    # Arrange
    # Act
    # Assert

    r = Rectangle(2,3)
    r.longueur = 12
    print(r.longueur)
    print(r.surface)
    # r.untruc = "toto"
    # print(r.untruc)
    # print(r.__dict__)
    s = str(r)
    print(s)

    r = Rectangle(2,3)
    r1 = Rectangle(2,3)
    if r==r1:
        print("ok")
    else:
        print("ko")
    
    print("r.cpt",r.get_cpt())
    print("Rectangle.cpt",Rectangle.get_cpt())
    print(50*'-')
    r3 = Rectangle()
    print(r)
    line="12;5"

    r4 = Rectangle(4,5)
    r5 = Rectangle.build_from_str(line)
    print(Rectangle.get_cpt())
    del r
    del r1
    # print(r.longueur)
    print(Rectangle.get_cpt())
if __name__=='__main__':
    main()
