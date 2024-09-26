#!/usr/bin/env python

import os
import sys
from pprint import pprint

class Truc:

    def __init__(self,i="the value") -> None:
        self.i = i

    def __call__(self):
        print("call",self.i)

def main():
    t = Truc()

    t()

if __name__=='__main__':
    main()
