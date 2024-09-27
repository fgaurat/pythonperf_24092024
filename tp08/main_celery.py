#!/usr/bin/env python

from celery import Celery,signature,chain
import os
import sys
from pprint import pprint
import requests
from bs4 import BeautifulSoup



def main():
    app = Celery('celery_tasks', backend='rpc://', broker='pyamqp://guest@localhost//')
    # task = app.send_task("celery_tasks.add",args=[2,3])
    # result = task.get()

    
    # print(result)
    url = "https://logs.eolem.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    logs = [url+l['href'] for l in soup.find_all("a") if ".log" in l['href']]
    # print(logs)

    # download = signature('celery_tasks.download')
    # r = download.delay(logs[0])
    # print(r.get())

    #Download
    # download_tasks = [signature('celery_tasks.download',args=[url]) for url in logs]
    # download_group =group(download_tasks)
    # result = download_group()
    # all_downloads = result.get()

    # #Save
    # save_tasks = [signature('celery_tasks.write',args=[to_save]) for to_save in all_downloads]
    # save_group =group(save_tasks)
    # save_group()


    for url in logs:
         chain(
            signature('celery_tasks.download',args=[url]),
            signature('celery_tasks.write')
        )()  

if __name__=='__main__':
    main()
