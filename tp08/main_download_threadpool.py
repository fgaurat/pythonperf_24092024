#!/usr/bin/env python

import os
import sys
from pprint import pprint
import requests
from bs4 import BeautifulSoup
import time
import threading
from concurrent.futures import ThreadPoolExecutor

def download(url,log_file):
    r = requests.get(url)
    with open(log_file,"w") as f:
        f.write(r.text)

def main():
    start = time.perf_counter()
    url = "https://logs.eolem.com"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    # all_a = soup.css.select("body > pre > a")
    all_a = [a['href'] for a in soup.find_all("a") if "apache_logs" in a['href']]
    
    urls = []
    log_files = []

    for a in all_a:
        url_a = f"{url}/{a}"
        urls.append(url_a)
        log_files.append(a)

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(download,urls,log_files)


    
    end = time.perf_counter()
    print(f"time: {end-start:.3}")


if __name__=='__main__':
    main()
