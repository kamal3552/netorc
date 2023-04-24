"""
celery.py
"""
import os
from celery import Celery
from controller import settings


tasks = [
    (settings.TASK_DIR + x).replace("/", ".").strip(".py")
    for x in os.listdir(settings.TASK_DIR)
    if not x.startswith("__") and x.endswith(".py")
]

celery = Celery(include=tasks)

# Time
celery.conf.timezone = settings.TIMEZONE
celery.conf.enable_utc = settings.UTC

# Broker & Backend
celery.conf.broker_url = settings.REDIS + "/0"
celery.conf.result_backend = settings.REDIS + "/0"

# Censored
celery.conf.humanize(with_defaults=False, censored=settings.CENSORED)
celery.conf.table(with_defaults=False, censored=settings.CENSORED)

# Priorities
celery.conf.broker_transport_options = {
    "priority_steps": list(range(settings.PRIORITY_LEVELS)),
    "sep": ":",
    "queue_order_strategy": "priority",
}

if __name__ == "__main__":
    celery.start()
