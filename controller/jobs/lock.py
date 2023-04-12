"""
lock.py
"""
import time
import uuid
import redis

from controller import settings


def acquire_lock(lock_name: str, acquire_timeout: int = 10,) -> str:
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
            with redis.Redis(
                host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_LOCK_DB,
                decode_responses=True,
            ) as conn:
                if conn.setnx("lock:" + lock_name, str(uid)):
                    return str(uid)
            time.sleep(0.01)
        except Exception as e:
            raise e
    return False


def release_lock(lock_name: str, uid: str,) -> bool:
    """Releases the lock on a task

    :arg obj conn: takes redis connection object.
    :arg obj lock_name: name of the lock key.
    :arg int uid: the task unique id value

    :returns: true
    """
    lockname = "lock:" + lock_name
    try:
        with redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_LOCK_DB,
            decode_responses=True,
        ) as conn:
            pipe = conn.pipeline(True)
            while True:
                try:
                    pipe.watch(lockname)
                    if str(conn.get(lockname)) == uid:
                        pipe.multi()
                        pipe.delete(lockname)
                        pipe.execute()
                        return True
                    pipe.unwatch()
                    break
                except:
                    return False
    except Exception as e:
        raise e
