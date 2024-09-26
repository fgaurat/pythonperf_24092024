#!/usr/bin/env python

import os
import sys
from pprint import pprint
import requests
from bs4 import BeautifulSoup
import time
import threading

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
    threads = []
    for a in all_a:
        url_a = f"{url}/{a}"
        th = threading.Thread(target=download,args=(url_a,a))
        th.start()
        threads.append(th)

    [th.join() for th in threads]
    
    end = time.perf_counter()
    print(f"time: {end-start:.3}")


if __name__=='__main__':
    main()
