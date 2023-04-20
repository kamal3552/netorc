"""
decorators.py
"""
from functools import wraps
from controller.tasks.synclock import acquire_lock, release_lock


def sync_lock(func):
    """Applied to tasks which require synchronous execution.
    Workers will acquire a lock on the task before execution.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            if "sync_lock_key" in kwargs:
                key = kwargs.get("sync_lock_key")
            else:
                key = func.__name__
            uid = acquire_lock(key)
            print(uid)
            return func(*args, **kwargs)
        except Exception as exc:
            raise exc
        finally:
            try:
                release_lock(key, uid)
            except UnboundLocalError:
                pass
            except Exception as exc:
                raise exc

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
