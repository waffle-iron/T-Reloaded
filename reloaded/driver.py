from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from configs import settings
from constants import DRIVER
from logger import logger


def create_driver():
    """returns driver"""
    if settings['browser'] == 'CHROME':
        try:
            driver = webdriver.Chrome()
        except WebDriverException as e:
            logger.error('%s \nDriver not in path', e)
            raise SystemExit(DRIVER['NOT_IN_PATH'])
    elif settings['browser'] == 'FIREFOX':
        try:
            driver = webdriver.Firefox()
        except WebDriverException as e:
            logger.error('%s \nDriver not in path', e)
            raise SystemExit(DRIVER['NOT_IN_PATH'])
    else:
        logger.critical('selected browser unavailable')
    return driver


driver = create_driver()
wait = WebDriverWait(driver, 5)
