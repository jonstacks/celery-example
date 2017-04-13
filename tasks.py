from celery import Celery
import requests

app = Celery('tasks', broker='amqp://guest@localhost//')

app.conf.broker_url = 'redis://redis:6379/0'

@app.task
def get_webpage():
    print requests.get('https://google.com')
