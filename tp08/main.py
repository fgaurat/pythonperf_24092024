#!/usr/bin/env python

import os
import sys
from pprint import pprint
import requests
from bs4 import BeautifulSoup
import time


def main():
    start = time.perf_counter()
    url = "https://logs.eolem.com"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    
    # all_a = soup.css.select("body > pre > a")

    all_a = [a['href'] for a in soup.find_all("a") if "apache_logs" in a['href']]
    for a in all_a:
        url_a = f"{url}/{a}"
        print(url_a)
        r = requests.get(url_a)
        with open(a,"w") as log_file:
            log_file.write(r.text)

    end = time.perf_counter()
    print(f"time: {end-start:.3}")


if __name__=='__main__':
    main()
