#!/usr/bin/env python

import os
import sys
from pprint import pprint
import requests
from bs4 import BeautifulSoup
import time
import asyncio
import aiohttp


async def download(queue_download:asyncio.Queue,queue_save:asyncio.Queue):
    while True:
        url,log_file = await queue_download.get()
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as r:
                content = await r.text()
                d = {
                     "content":content,
                     "log_file":log_file
                }
                queue_save.put_nowait(d)
        queue_download.task_done()

async def write(queue_save:asyncio.Queue):
    while True:
        d = await queue_save.get()
        log_file=d['log_file']
        content=d['content']
        with open(log_file,"w") as f:
            f.write(content)
        queue_save.task_done()


async def main():
    start = time.perf_counter()
    queue_download = asyncio.Queue()
    queue_save = asyncio.Queue()

    nb_download_workers = 10
    nb_write_workers = 5



    url = "https://logs.eolem.com"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    # all_a = soup.css.select("body > pre > a")
    all_a = [a['href'] for a in soup.find_all("a") if "apache_logs" in a['href']]
    
    tasks=[]


    for i in range(nb_download_workers):
        task = asyncio.create_task(download(queue_download,queue_save))
        tasks.append(task)

    for i in range(nb_write_workers):
        task = asyncio.create_task(write(queue_save))
        tasks.append(task)

    for a in all_a:
        url_a = f"{url}/{a}"
        p = (url_a,a)
        queue_download.put_nowait(p)

    await queue_download.join()
    await queue_save.join()
    [task.cancel() for task in tasks]


    
    end = time.perf_counter()
    print(f"time: {end-start:.3}")


if __name__=='__main__':
   asyncio.run(main())
