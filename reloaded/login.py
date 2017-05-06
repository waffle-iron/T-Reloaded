"""Enhancements for Tesseract login screen"""
import unittest

from selenium.webdriver.common.by import By
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
            raise SystemExit(TESSERACT['ERROR']['NAVIGATION_ERROR'])
    except Exception as e:
        logger.error('%s \nnavigation failed', e)
        raise SystemExit(TESSERACT['ERROR']['UNDEFINED'])
    return True


def verify_database():
    try:
        database_element = driver.find_element_by_id('txtDBaseName')
        database_value = database_element.get_attribute('value')
        if "Test" in database_value:
            logger.warning("!!!!!! You are using the test database !!!!!!")
    except Exception as e:
        logger.error('%s\nFailed to verify database', e)
        raise SystemExit(TESSERACT['ERROR']['UNDEFINED'])
    return True


def enter_credentials():
    try:
        elem_username = driver.find_element_by_id('txtUserName')
        elem_username.send_keys(settings['username'])
        elem_password = driver.find_element_by_id('txtPassword')
        elem_password.send_keys(settings['password'])
    except Exception as e:
        logger.error('%s\nFailed to enter credentials', e)
        raise SystemExit(TESSERACT['ERROR']['UNDEFINED'])
    return True


def submit_credentials():
    driver.find_element_by_id('btnsubmit').click()

    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        logger.debug('Alert is present')
        alert.accept()
    except TimeoutException:
        pass

    try:
        wait.until(EC.title_contains("Wincor"))
    except TimeoutException:
        logger.error('%s\nFailed to login', e)
    return True


class TestLogin(unittest.TestCase):
    """Test case for login functionality"""

    def setUp(self):
        pass

    def test_login_one(self):
        self.assertTrue(navigate())
        self.assertTrue(verify_database())
        self.assertTrue(enter_credentials())
        self.assertTrue(submit_credentials())
        driver.get(TESSERACT['URL'] +
                   'SC51/SC_Login/aspx/Logout_Main.aspx')
        wait.until(EC.element_to_be_clickable((By.ID, 'btnsubmit')))
        driver.quit()


if __name__ == '__main__':
    unittest.main()
