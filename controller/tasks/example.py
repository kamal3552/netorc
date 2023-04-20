"""
example.py

`sync_lock` can be used to ensure tasks are executed
synchronously with each worker obtaining the lock before 
executing the task. 

for more information, see <link>

@celery.task()
@sync_lock
def a_sync_lock_task() -> str:
    print("Starting a task with sync_lock...")
    time.sleep(10)
    print("Finished task with sync_lock.")


@celery.task()
@sync_lock
def a_sync_lock_task(sync_lock_key: str = None) -> str:
    print(f"Starting task: {sync_lock_key}, with sync_lock...")
    time.sleep(10)
    print(f"Finished task: {sync_lock_key}, with sync_lock.")

"""
import time
from controller.settings import celery
from controller.misc.decorators import sync_lock


@celery.task()
@sync_lock
def example_task() -> str:
    print("Starting task")
    time.sleep(5)
    print("Finished task")
    return 8
