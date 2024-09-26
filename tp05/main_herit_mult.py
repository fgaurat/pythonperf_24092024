#!/usr/bin/env python

import os
import sys
from pprint import pprint


class A:
    def show(self):
        print('A')
class B(A):
    def show(self):
        print('B')
class C(A):
    def show(self):
        print('C')
class D(B,C):
    def show(self):
        super().show()
        super(B,self).show()
        super(C,self).show()
        print('D')


def main():
    print(D.mro())
    d = D()
    d.show()
    super(C,d)
    print(B.mro())

if __name__=='__main__':
    main()
