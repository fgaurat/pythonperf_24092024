#!/usr/bin/env python

import os
import sys
from pprint import pprint
from pydantic import BaseModel

class User(BaseModel):
    id:int
    name:str
    is_active:bool=True


def main():
    u = User(id=1,name="toto",is_active=False)
    print(u)
    # u1 = User(id=1,name="toto",is_active='toto')
    u2 = User(id="2",name="toto",is_active=False)
    print(u2)
if __name__=='__main__':
    main()
