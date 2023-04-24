"""
NetORC configuration file.

We have kept connection and secret prameters used by modules in this file.
This is not best practice, we recommend using a .env or a secret manager, see <link>

"""

# Default task directory.
# Task modules are auto generated from this path.
TASK_DIR = "controller/worker/tasks/"

# We do NOT recommended to change this setting.
REDIS = "redis://redis:6379"

# Ensure this is the correct timezone.
TIMEZONE = "Europe/London"

UTC = True

# Censors celery configuration, passwords, api keys.
# We do NOT recommended to change this setting.
CENSORED = True

# Tasks can be queued with a priority.
# This is best effort and does not guarantee a faster execution.
# We do NOT recommended to change this setting.
PRIORITY_LEVELS = 10  # 0-9

# The default log handlers are console, file and syslog.
LOG_FORMAT = "%(asctime)s %(levelname)s: %(message)s"

# Syslog messages are sent using UDP, for TCP, see <link>.
# LOG_USER facility.
SYSLOG_SERVER = "localhost"
SYSLOG_PORT = 514
