from celery import Celery
import requests
app = Celery('celery_tasks', backend='rpc://', broker='pyamqp://guest@localhost//')


# celery -A celery_tasks worker --loglevel=INFO
@app.task
def add(x, y):
    return x + y

@app.task
def download(url):
    r = requests.get(url)
    content = r.text
    d = {
            "content":content,
            "url":url
    }
    return d

@app.task
def write(d):
    url=d['url']
    content=d['content']
    log_file=url.split("/")[-1]
    with open(log_file,"w") as f:
        f.write(content)
