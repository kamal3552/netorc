"""
decorators.py
"""
from functools import wraps
from controller.jobs.lock import acquire_lock, release_lock
from controller import settings


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
            return func(*args, **kwargs)
        except Exception as e:
            raise e
        finally:
            try:
                release_lock(key, uid)
            except UnboundLocalError:
                pass
            except Exception as e:
                raise e

    return wrapper
