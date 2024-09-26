#!/usr/bin/env python

import os
import sys
from pprint import pprint
from multiprocessing import Pool
import time

def f(x):
    return x*x

def slow_f(x):
    start = time.time()
    while time.time()-start<1:
        pass

    return x*x


def main():
    print(os.cpu_count())
    with Pool(3) as p:
        print(p.map(slow_f, range(10)))


if __name__=='__main__':
    main()
