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
                   TESSERACT['URI_CREATE'])
        text = "Welcome the the Repair Job Creation Wizard."
        if text not in driver.page_source:
            logger.error("Create Wizard not detected")
            raise SystemExit(TESSERACT['ERROR']['NAVIGATION_ERROR'])
    except Exception as e:
        logger.error('%s \nnavigation failed', e)
        raise SystemExit(TESSERACT['ERROR']['UNDEFINED'])
    return True


class TestCreate(unittest.TestCase):

    def setUp(self):
        import login
        self.assertTrue(login.navigate())
        self.assertTrue(login.verify_database())
        self.assertTrue(login.enter_credentials())
        self.assertTrue(login.submit_credentials())

    def test_login_one(self):
        self.assertTrue(navigate())
        driver.quit()


if __name__ == '__main__':
    unittest.main()
