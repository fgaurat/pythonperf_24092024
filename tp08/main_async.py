#!/usr/bin/env python
import asyncio

import os
import sys
from pprint import pprint

async def add(a,b):
    await asyncio.sleep(1)
    return a+b

async def main():

    # a = await add(2,3)
    # print(a)
    # a = await add(21,33)
    # print(a)
    l = [add(2,3),add(2,3),add(2,3),add(2,3)]


    r = await asyncio.gather(*l)
    print(r)

if __name__=='__main__':
    asyncio.run(main())

