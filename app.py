"""Root of T-Reloaded application
"""

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from reloaded.config import Settings as Settings
from reloaded.login import Login as Login


class app():
    driver = None
    wait = None
    settings = None
    create = None
    login = None

    def __init__(self):
        """Initialize all classes"""
        app.driver = webdriver.Firefox()
        app.wait = WebDriverWait(app.driver, 10)
        app.settings = Settings().config
        app.login = Login()


if __name__ == '__main__':
    app = app()
else:
    pass
