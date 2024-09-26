#!/usr/bin/env python

import os
import sys
from pprint import pprint
from collections import deque


# HelloWorld => UpperCamelCase, PascalCase
# helloWorld => camelCase
# hello_world => snake_case
# hello-world => kebab-case


def main():
    l = [10, 20, 30, 40, 50]
    print(l)
    l.append(60)
    print(l)
    print(l)
    a = l.pop()
    print(a, l)

    l.insert(0, -10)
    print(l)
    b = l.pop(0)
    print(l)
    print(b)
    d = deque(l)
    print(d)
    d.appendleft(-10)
    print(d)


if __name__ == '__main__':
    main()
