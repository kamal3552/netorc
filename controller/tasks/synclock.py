"""
synclock.py
"""
import time
import uuid
import redis

from controller import settings
from controller.misc.exceptions import AcquireLockException


def acquire_lock(
    lock_name: str,
    acquire_timeout: int = 10,
) -> str:
    """Acquires the lock on a task

    :arg obj conn: takes redis connection object.
    :arg obj lock_name: name of the lock key.
    :arg int, optional acquire_timeout: timeout on acquiring lock.

    :returns: str
    """
    uid = uuid.uuid4()
    end = time.time() + acquire_timeout
    while time.time() < end:
        try:
            with redis.from_url(settings.REDIS) as conn:
                if conn.setnx("lock:" + lock_name, str(uid)):
                    return str(uid)
            time.sleep(0.01)
        except Exception as exc:
            raise exc
    raise AcquireLockException


def release_lock(
    lock_name: str,
    uid: str,
) -> bool:
    """Releases the lock on a task

    :arg obj conn: takes redis connection object.
    :arg obj lock_name: name of the lock key.
    :arg int uid: the task unique id value

    :returns: true
    """
    lockname = "lock:" + lock_name
    try:
        with redis.from_url(settings.REDIS) as conn:
            pipe = conn.pipeline(True)
            while True:
                try:
                    pipe.watch(lockname)
                    if conn.get(lockname).decode("utf-8") == uid:
                        pipe.multi()
                        pipe.delete(lockname)
                        pipe.execute()
                        return True
                    pipe.unwatch()
                    break
                except redis.exceptions.WatchError as exc:
                    raise exc

    except Exception as exc:
        raise exc
