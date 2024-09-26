


#!/usr/bin/env python

import os
import sys
from pprint import pprint
from Carre import Carre
from Cercle import Cercle
def main():
    c = Carre(2)
    ce = Cercle(3)
    print(c.surface) #4
    print(c)
    print(ce.surface)

if __name__=='__main__':
    main()
