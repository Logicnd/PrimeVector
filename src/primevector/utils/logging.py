"""Logging utilities for PrimeVector.

Keeps logging configuration consistent across scripts and makes CLI output readable.
"""

from __future__ import annotations

import logging
import os


def get_logger(name: str) -> logging.Logger:
    """Get a configured logger with a simple, consistent format."""
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    level_name = os.getenv("PRIMEVECTOR_LOG_LEVEL", "INFO").upper()
    level = getattr(logging, level_name, logging.INFO)

    logger.setLevel(level)
    handler = logging.StreamHandler()
    handler.setLevel(level)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.propagate = False
    return logger
