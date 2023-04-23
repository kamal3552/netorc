"""
celery.py
"""
from celery import Celery
from controller import settings

celery = Celery()

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
