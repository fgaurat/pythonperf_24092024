#!/usr/bin/env python

import os
import sys
from pprint import pprint
from RectangleSingleton import RectangleSingleton
from RectangleDeco import RectangleDeco
from RectangleMetaSingleton import RectangleMetaSingleton


def main():
    r = RectangleMetaSingleton(1,2)
    r1 = RectangleMetaSingleton(1,2)

    print(hex(id(r)))
    print(hex(id(r1)))



def main02():
    r = RectangleDeco(1,2)
    r1 = RectangleDeco(1,2)

def main01():
    a=2
    print(type(a))
    print(type(int))
    r = RectangleSingleton(1,2)
    r1 = RectangleSingleton(1,2)
    print(hex(id(r)))
    print(hex(id(r1)))
    r.longueur = 1000
    print(r1.longueur) # 1000



if __name__=='__main__':
    main()
