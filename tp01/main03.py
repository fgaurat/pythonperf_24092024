#!/usr/bin/env python

import os
import sys
from pprint import pprint
import copy
def main():
    l=[10,20,30,40,50]
    print(l)
    print(len(l))
    last_value = l[-2]
    print(last_value)
    l2 = l[2:4] # [2:4[
    print(l2)
    l2 = l[2:] # [2:4[
    print(50*'-')
    
    # l3 = l
    # l3 = l[:]
    l3 = l.copy()
    l3 = copy.copy(l)

    l[0] = 1000
    print(l) # 
    print(l3)

    print(50*'-')
    l =[
        [10,20,30],
        [40,50,60],
        [70,80,90],
    ]

    
    print(50*'-')
    print(l)
    l4 = copy.deepcopy(l)
    l[1][1] = 1000
    print(l)
    print(l4)

    a = 2


if __name__=='__main__':
    main()
