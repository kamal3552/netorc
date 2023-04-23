"""
decorators.py
"""
from functools import wraps
from controller.tasks.task_lock import TaskLock


def task_lock(func):
    """Applied to tasks which require synchronous execution.
    Workers will acquire a lock on the task before execution.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            if "task_lock_key" in kwargs:
                task_lock_key = kwargs.get("tasklock_key")
            else:
                task_lock_key = func.__name__

            lock = TaskLock(task_lock_key)
            lock.add()
            return func(*args, **kwargs)
        except Exception as exc:
            raise exc
        finally:
            lock.remove()

    return wrapper


def queue_task(func, priority: int = 0, *args, **kwargs):
    """Applied to tasks. Allows the calling of a Celery task
    and its arguments to be abstracted.
    """

    def inner():
        try:
            task = func.apply_async(args=[*args], kwargs={**kwargs}, priority=priority)
            return task
        except Exception as exc:
            raise exc

    return inner()
