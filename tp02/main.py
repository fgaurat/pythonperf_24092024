#!/usr/bin/env python

import os
import sys
from pprint import pprint


# def old_do_log(func):
#     print(func)
#     def wrapper(*args,**kwargs):
#         print(f"LOG",args,kwargs)
#         r = func(*args,**kwargs)
#         print(f"LOG RETURN",r)
#         return r
#     return wrapper

def do_log(file_name):
    def decorator(func):
        print(func)
        def wrapper(*args,**kwargs):
            print(f"LOG to {file_name}",args,kwargs)
            r = func(*args,**kwargs)
            print(f"LOG RETURN to {file_name}",r)
            return r
        return wrapper
    return decorator

# @old_do_log
@do_log("thelog.log")
def say_hello(name):
    r = f"Hello {name}"
    return r


def main():
    print("start")
    h = say_hello("fred")
    print(h)

if __name__=='__main__':
    main()
