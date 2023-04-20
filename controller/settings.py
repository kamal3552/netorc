"""
NetORC configuration file.

We have kept connection and secret prameters used by modules in this file.
This is not best practice, we recommend using a .env or a secret manager, see <link>

"""

from celery import Celery

# SyncLock

## Database
REDIS = "redis://redis:6379/0"

# Celery
celery = Celery()

## Time - Please synchronise using NTP!
celery.conf.timezone = "Europe/London"
celery.conf.enable_utc = True

## Broker & Backend
celery.conf.broker_url = "redis://redis:6379/0"
celery.conf.result_backend = "redis://redis:6379/0"

## Censored
celery.conf.humanize(with_defaults=False, censored=True)
celery.conf.table(with_defaults=False, censored=True)

## Priorities
celery.conf.broker_transport_options = {
    "priority_steps": list(range(10)),  # 0-9
    "sep": ":",
    "queue_order_strategy": "priority",
}
