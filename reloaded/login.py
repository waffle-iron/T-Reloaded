"""Enhancements for Tesseract login screen"""
from selenium import webdriver

from configs import settings
from constants import TESSERACT
from driver import driver
from driver import wait
from logger import logger


def navigate():
    try:
        driver.get(TESSERACT['URL'] +
                   TESSERACT['URI_LOGIN'] +
                   TESSERACT['DB_SOURCE'])
        if "Service Centre Login" not in driver.title:
            logger.error("Service center not detected")
            raise SystemExit(TESSERACT.ERROR['NAVIGATION_ERROR'])
    except Exception as e:
        logger.error('%s \nnavigation failed', e)
        raise SystemExit(TESSERACT.ERROR['NAVIGATION_ERROR'])


def verify_database():
    database_element = driver.find_element_by_id('txtDBaseName')
    database_value = database_element.get_attribute('value')
    if "Test" in database_value:
        logger.warning("!!!!!! You are using the test database !!!!!!")


navigate()
verify_database()
