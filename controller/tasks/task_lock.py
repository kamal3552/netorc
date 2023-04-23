"""
task_lock.py
"""
import time
import uuid
import redis

from controller import settings
from controller.misc.exceptions import AcquireLockException
from controller.metrics.logger import logger


class TaskLock:
    """Distributed lock mechanism to Add/Remove lock on a task"""

    def __init__(self, task_lock_key: str = None, timeout: int = 10):
        try:
            self.conn = redis.from_url(settings.REDIS + "/0")
            logger.info("Connected to redis instance: %s", settings.REDIS)
        except Exception as exc:
            logger.critical(exc_info=True)
            raise exc

        self.task_lock_key = "lock:" + task_lock_key
        self.uid = str(uuid.uuid4())
        self.timeout = timeout

    def add(self):
        """Add the lock

        :returns: True
        """
        end = time.time() + self.timeout
        while time.time() < end:
            try:
                if self.conn.setnx(self.task_lock_key, self.uid):
                    logger.info("Added %s with uid: %s", self.task_lock_key, self.uid)
                    return True
                time.sleep(0.01)
            except Exception as exc:
                logger.critical(exc_info=True)
                raise exc
        raise AcquireLockException

    def remove(self):
        """Remove the lock

        :returns: True
        """
        try:
            pipe = self.conn.pipeline(True)
            while True:
                try:
                    pipe.watch(self.task_lock_key)
                    if self.conn.get(self.task_lock_key).decode("utf-8") == self.uid:
                        pipe.multi()
                        pipe.delete(self.task_lock_key)
                        pipe.execute()
                        logger.info(
                            "Removed %s with uid: %s", self.task_lock_key, self.uid
                        )
                        return True
                    pipe.unwatch()
                    break
                except (
                    redis.exceptions.WatchError
                ) as exc:  # TODO: How to handle retries
                    raise exc
        except Exception as exc:
            logger.critical(exc_info=True)
            raise exc
