"""
    reloaded.configs
    ----------------

"""
import os
import traceback
import configparser

from constants import CONFIG
from logger import logger


def get_config_file():
    """Returns config file path"""

    file_name = '.reloaded.cfg'
    file_path = os.path.join(os.path.expanduser('~'), file_name)
    if os.path.isfile(file_path):
        return file_path
    else:
        logger.info(CONFIG['FILE_NOT_FOUND'])
        raise SystemExit(CONFIG['FILE_NOT_FOUND'])


def parse_config_file(config_file):
    user_config = configparser.ConfigParser(delimiters=('='), strict=False)
    user_config.read_file(open(config_file))
    # TODO - set all potential config options in here
