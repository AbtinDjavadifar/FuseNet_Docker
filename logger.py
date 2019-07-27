import json
from logging.config import dictConfig
from logging import Logger, getLogger
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def get_logger(name: str = None) -> Logger:
    with open(os.path.join(__location__, './logger.json'), 'rb') as logger_config:
        logging_config = json.load(logger_config)
        dictConfig(logging_config)

    return getLogger(name)
