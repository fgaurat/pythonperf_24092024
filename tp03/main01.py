#!/usr/bin/env python

import os
import sys
from pprint import pprint
import traceback

def main():
    try:
        a=3
        b=int(input('b: '))
        c=a/b

        print(c)
    except ZeroDivisionError as e:
        print("ZeroDivisionError",e)
    except ValueError as e:
        print("ValueError",e)
    except Exception as e:
        print("Exception",e)
    else:
        print("pas d'erreur")    
    finally:
        print("s'éxécute erreur ou pas !")    

    print("le code après")

if __name__=='__main__':
    main()
