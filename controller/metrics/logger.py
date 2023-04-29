"""
logger.py
"""
import logging
from controller import settings

logger = logging.getLogger(__name__)

logger.setLevel(settings.LOG_LEVEL)

console = logging.StreamHandler()

file = logging.handlers.RotatingFileHandler(
    filename="logs/netorc.log", mode="w", maxBytes=10000000, backupCount=5
)

syslog = logging.handlers.SysLogHandler(
    address=(settings.SYSLOG_SERVER, settings.SYSLOG_PORT)
)

formatter = logging.Formatter(settings.LOG_FORMAT)

console.setFormatter(formatter)
logger.addHandler(console)

file.setFormatter(formatter)
logger.addHandler(file)

syslog.setFormatter(formatter)
logger.addHandler(syslog)
