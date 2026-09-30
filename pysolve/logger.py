"""Simple logging so errors and actions can be monitored (non-functional req)."""

import logging

logging.basicConfig(
    filename="pysolve.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


def log_info(message):
    logging.info(message)


def log_error(message):
    logging.error(message)
