# add settings import
from celery import Celery

# values should be retrieved from settings file
job = Celery('tasks', broker='amqp://localhost//')

# test task
@job.task
def device_task(name):
    print(name)