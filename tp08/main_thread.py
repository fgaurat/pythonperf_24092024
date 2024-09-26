#!/usr/bin/env python

import os
import sys
from pprint import pprint
import threading

lock = threading.Lock()

def thread01():
    with lock:
        for i in range(15):
            print('thread01',i)

def thread02():
    with lock:
        for i in range(15):
            print('thread02',i)

def main():
    th1 = threading.Thread(target=thread01)
    th2 = threading.Thread(target=thread02)
    th1.start()
    th2.start()
    
    th1.join()
    th2.join()
    
    print('fin')

if __name__=='__main__':
    main()
