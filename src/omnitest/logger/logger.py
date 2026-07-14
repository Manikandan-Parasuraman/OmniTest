"""
Logging utilities for the OmniTest Browser SDK.
"""

from __future__ import annotations

import logging
from pathlib import Path


_DEFAULT_FORMAT = (
    "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
)


def get_logger(
    name: str = "omnitest",
    *,
    level: int = logging.INFO,
    log_file: str | Path | None = None,
) -> logging.Logger:
    """
    Return a configured logger.

    Parameters
    ----------
    name:
        Logger name.

    level:
        Logging level.

    log_file:
        Optional file path for log output.

    Returns
    -------
    logging.Logger
    """

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(level)

    formatter = logging.Formatter(_DEFAULT_FORMAT)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    if log_file is not None:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    logger.propagate = False

    return logger
