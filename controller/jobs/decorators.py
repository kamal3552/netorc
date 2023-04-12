"""
decorators.py
"""
from functools import wraps
from controller.jobs.lock import acquire_lock, release_lock
from controller import settings


def sync_lock(func):
    """Applied to tasks which require synchronous execution.
    Workers will acquire a lock on the task before execution.

    :arg obj conn: takes redis connection object.
    :arg obj func: takes task function.
    :arg int, optional timeout: timeout on acquiring lock.

    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            try:
                key = kwargs["sync_lock_key"]
            except Exception:
                key = func.__name__
            uid = acquire_lock(key)
            print(uid)
            func(*args, **kwargs)

        except Exception as e:
            raise e

        finally:
            release_lock(key, uid)

    return wrapper
