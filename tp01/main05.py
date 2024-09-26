#!/usr/bin/env python

import os
import sys
from pprint import pprint


def add(*args):
    print(*args)
    r = 0
    for i in args:
        r+=i
    return r

def hello(**kwargs):
    
    print(kwargs)
    print(kwargs['name'],kwargs['firstName'])


def hello2(name,firstName,/): # positional only
    print(name,firstName)

def hello3(*,name,firstName): # kw only
    print(name,firstName)

def main():
    l=[10,20,30,40,50]
    l1=[10,20,30,40,50]
    
    r = add(*l,*l1) # add(2,10,20,30,40,50) 
    
    # r = add(10,20,30,40) # 150
    print(r)

    # lecture => déballage = unpacking
    # écriture => emballage => packing
    a,*b = [2,3,4]

    print(a,b)
    a,*_ = [2,3,4]

    # hello(name="GAURAT",firstName="Frédéric")
    # hello(firstName="Frédéric",name="GAURAT")
    # hello("GAURAT","Frédéric")


    a = 2
    b=3
    c = a/b
    r = f"{c:.2}"
    r = f"{c=}"
    print(r)
    r = "a:{}, b{},c{}".format(a,b,c)
    l = [a,b,c]

    # r = "a:{k1}, b{k2},c{k3}".format(k1=a,k2=b,k3=c)

    d = {"k1":a,"k2":b,"k3":c}
    r = "a:{k1}, b{k2},c{k3}".format(**d)
    print(r)

if __name__=='__main__':
    main()
