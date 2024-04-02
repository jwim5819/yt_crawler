import logging
import os

logger = logging.getLogger("custom_logger")
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
console = logging.StreamHandler()
console.setFormatter(formatter)
logger.addHandler(console)


def print_line():
    try:
        width = os.get_terminal_size().columns
    except OSError:
        width = 80
    logger.info('=' * width)
