"""Enhancements for Tesseract login screen"""
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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
        raise SystemExit(TESSERACT.ERROR['UNDEFINED'])


def verify_database():
    try:
        database_element = driver.find_element_by_id('txtDBaseName')
        database_value = database_element.get_attribute('value')
        if "Test" in database_value:
            logger.warning("!!!!!! You are using the test database !!!!!!")
    except Exception as e:
        logger.error('%s\nFailed to verify database', e)
        raise SystemExit(TESSERACT.ERROR['UNDEFINED'])


def enter_credentials():
    try:
        elem_username = driver.find_element_by_id('txtUserName')
        elem_username.send_keys(settings['username'])
        elem_password = driver.find_element_by_id('txtPassword')
        elem_password.send_keys(settings['password'])
    except Exception as e:
        logger.error('%s\nFailed to enter credentials', e)
        raise SystemExit(TESSERACT.ERROR['UNDEFINED'])


def submit_credentials():
    driver.find_element_by_id('btnsubmit').click()

    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
    except TimeoutException:
        pass

    try:
        wait.until(EC.title_contains("Wincor"))
    except TimeoutException:
        logger.error('%s\nFailed to login', e)


navigate()
verify_database()
enter_credentials()
submit_credentials()
