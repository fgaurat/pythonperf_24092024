#!/usr/bin/env python

import os
import sys
from pprint import pprint
from pydantic import BaseModel,field_validator,ValidationError

class User(BaseModel):
    id:int
    name:str
    email:str
    is_active:bool=True

    @field_validator('email')
    @classmethod
    def validate_email(cls,v):
        if '@' not in v:
            raise ValueError('Invalid Email')
        return v


def main():
    try:
        u = User(id=1,name="toto",is_active=False,email="toto@truc.com")
        print(u)
        # u1 = User(id=1,name="toto",is_active='toto')
        u2 = User(id="2",name="toto",is_active=False,email="toto_truc.com")
        print(u2)
    except ValidationError as e:
        print(e)
if __name__=='__main__':
    main()
