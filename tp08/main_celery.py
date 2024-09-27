#!/usr/bin/env python

from celery import Celery
import os
import sys
from pprint import pprint

def main():
    app = Celery('celery_tasks', backend='rpc://', broker='pyamqp://guest@localhost//')
    task = app.send_task("celery_tasks.add",args=[2,3])
    result = task.get()

    
    print(result)
if __name__=='__main__':
    main()
