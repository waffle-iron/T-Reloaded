"""
    reloaded.configs
    ----------------

"""
import os
import configparser
import traceback

from constants import CONFIG
from logger import logger


def get_config_file(file_name='.reloaded.cfg'):
    """Returns config file path"""

    file_path = os.path.join(os.path.expanduser('~'), file_name)
    if os.path.isfile(file_path):
        return file_path
    else:
        logger.info(CONFIG['FILE_NOT_FOUND'])
        raise SystemExit(CONFIG['FILE_NOT_FOUND'])


def parse_config_file(config_file):
    """Parse config file
    return settings"""
    settings = {}
    user_config = configparser.ConfigParser(delimiters=('='), strict=False)
    user_config.read_file(open(config_file))
    # set browser
    if user_config.has_option('settings', 'browser'):
        supported_browsers = ['CHROME', 'FIREFOX']
        settings['browser'] = user_config.get('settings', 'browser').upper()
        if settings['browser'] not in supported_browsers:
            logger.critical('Browser is not supoorted')
            raise SystemExit(CONFIG['CONFIG_ERROR'])
    # set username
    if user_config.has_option('settings', 'username'):
        settings['username'] = user_config.get('settings', 'username')
    else:
        logger.critical('username is not set in config')
        raise SystemExit(CONFIG['CONFIG_ERROR'])
    # set password
    if user_config.has_option('settings', 'password'):
        settings['password'] = user_config.get('settings', 'password')
    else:
        logger.critical('password is not set in config')
        raise SystemExit(CONFIG['CONFIG_ERROR'])
    # set workshop site
    if user_config.has_option('settings', 'workshop_site'):
        settings['workshop_site'] = user_config.get('settings',
                                                    'workshop_site')
    else:
        logger.critical('workshop_site is not set in config')
        raise SystemExit(CONFIG['CONFIG_ERROR'])
    return settings


config_file = get_config_file()
settings = parse_config_file(config_file)
