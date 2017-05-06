import json
import logging
import unittest



with open('config.json') as json_data:
    config = json.load(json_data)


class Login():
    """ all functionality for login is based within this class

    .. automethod:: navigate_to_login_and_verify
    .. automethod:: fill_user_credentials_and_submit

    .. note::
        available via app class *app.login*
    """

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_login_and_verify(self):
        """
        Navigate driver to app login. Verify database.
        """
        driver = self.driver

        # s = ''
        # print(settings['sourceString'])
        # url = s.join(settings['baseUrl']
        #              + "SC51/SC_Login/aspx/Login_Launch.aspx"
        #              + settings['sourceString'])
        # driver.get(url)
        # assert "Service Centre Login" in driver.title
        # database_element = driver.find_element_by_id('txtDBaseName')
        # database_value = database_element.get_attribute('value')
        # if "Test" in database_value:
        #     # TODO - Write to logger & console
        #     pass
        return True

    def fill_user_credentials_and_submit(self):
        """
        Login and verify app.
        """
        driver.find_element_by_id('txtUserName')send_keys(app.settings.username)
        driver.find_element_by_id('txtPassword')send_keys(app.settings.password)
        driver.find_element_by_id('btnsubmit').click()
        self.__alert()

    def __alert(self):
        """
        Accept alert box.
        """
        try:
            WebDriverWait(driver, 3).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            pass
        wait.until(EC.title_contains("Wincor"))


class JobCreateWizard():
    """
    contains all the functionality needed to navigate the job create
    wizard.
     """

    def __init__(self):
        pass

    def navigate_to_wizard(self):
        """
        Navigate browser to create wizard.
        """
        s = ''
        url = s.join(config['baseUrl']
                     + 'SC51/SC_RepairJob/aspx/repairjob_create_wzd.aspx')
        driver.get(job_create_wizard.url)
        text = "Welcome the the Repair Job Creation Wizard."
        assert text in driver.page_source
        return

    def set_workshop_site(self):
        """
        Sets the workshop site in the create job wizard.
        """
        pass

    def set_serial_number(self):
        """
        Set the serial number in the create job wizard.
        """
        pass

    def set_product_code(self):
        """
        Set the product code in the create job wizard.
        """
        pass

    def set_job_type(self):
        pass

    def set_flow_code(self):
        pass

    def set_ro_number(self):
        pass

    def set_job_site_number(self):
        pass

    def set_ship_site_number(self):
        pass

    def set_area(self):
        pass

    def set_engineer(self):
        pass

    def set_problem_code(self):
        pass

    def navigate_modal(self):
        pass

    def set_problem(self):
        pass

    def load_next_page(self, complete=False):
        """Go to next page in create job wizard.

        :complete: As bool, switches between next and finish.
        """
        pass


class Settings():
    """configue all required settings"""

    logger = None
    config = {}

    def __init__(self):
        Settings.logger = self.configure_logger()
        Settings.config = self.config()
        pass

    def configure_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler('./logs/debug.log')
        handler.setLevel(logging.INFO)
        format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(format)
        logger.addHandler(handler)
        return logger


class Tests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.login = Login(self.driver)

    def test_login_navigate(self):
        self.login.navigate_to_login_and_verify()

    def tearDown(self):
        self.driver.close()


print('Running unittests')
unittest.main()
