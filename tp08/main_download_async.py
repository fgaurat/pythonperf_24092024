#!/usr/bin/env python

import os
import sys
from pprint import pprint
import requests
from bs4 import BeautifulSoup
import time
import asyncio
import httpx
import aiohttp

async def download(url,log_file):
    r = await requests.get(url)
    with open(log_file,"w") as f:
        f.write(r.text)

async def download_httpx(url,log_file):
    async with httpx.AsyncClient() as client:    
        r = await client.get(url)
        with open(log_file,"w") as f:
            f.write(r.text)


async def download_aiohttp(url,log_file):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            # content = await r.text()
            with open(log_file,"w") as f:
                f.write(await r.text())

async def download_requests(url,log_file):
    loop = asyncio.get_event_loop()
    r = await loop.run_in_executor(None, requests.get, url)
    with open(log_file,"w") as f:
        f.write(r.text)

async def main():
    start = time.perf_counter()
    url = "https://logs.eolem.com"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    # all_a = soup.css.select("body > pre > a")
    all_a = [a['href'] for a in soup.find_all("a") if "apache_logs" in a['href']]
    
    tasks=[]
    for a in all_a:
        url_a = f"{url}/{a}"
        tasks.append(download_aiohttp(url_a,a))

    await asyncio.gather(*tasks)

    
    end = time.perf_counter()
    print(f"time: {end-start:.3}")


if __name__=='__main__':
   asyncio.run(main())
