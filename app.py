import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('debug.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

config = {}
config['baseUrl'] = "https://tesseract-cloud2.co.uk/SC51/SC_Login/aspx/Login_Launch.aspx?source=wn93kn83"
config['user'] = "kieranw"
config['pass'] = "kieranw"
config['max_wait_time'] = 10
config['workshop_site'] = 'STOWS'

driver = webdriver.Firefox()
driver.get(config['baseUrl'])

wait = WebDriverWait(driver, 10)

def login():
    assert "Service Centre Login" in driver.title
    logger.info('Login page has been found')

    database = driver.find_element_by_id('txtDBaseName').get_attribute('value')
    logger.info('Using database %s', database)
    if "Test" in database:
        logger.critical('Using test database')
    try:
        driver.find_element_by_id('txtUserName').send_keys(config['user'])
        logger.info('Username is set')
        driver.find_element_by_id('txtPassword').send_keys(config['pass'])
        logger.info('password is set')
    except Exception as e:
        logger.critical('credentials not set')
        return False
    driver.find_element_by_id('btnsubmit').click()
    wait.until(EC.title_contains('Wincor 5.1'))
    logger.info('Page title is %s', driver.title)
    return True

class job_create_wizard():
    createURL = 'https://tesseract-cloud2.co.uk/SC51/SC_RepairJob/aspx/repairjob_create_wzd.aspx'

    def __init__(self, Serial_Number, RO_Number, Product_Code):
        self.Serial_Number = Serial_Number
        self.Product_Code = Product_Code
        self.RO_Number = RO_Number
        if not self.navigate_to_wizard():
            return False
        if not self.fill_workshop_site():
            return False
        if not self.next_page():
            return False


    def navigate_to_wizard(self):
        try:
            driver.get(job_create_wizard.createURL)
            assert "Welcome the the Repair Job Creation Wizard. Please enter your workshop site code." in driver.page_source
            logger.info("Navigated to create page successfully")
            return True
        except Exception as e:
            logger.info("Failed to navigate to wizard")
            return False

    def fill_workshop_site(self):
        try:
            field = driver.find_element_by_id('scmaster_cplMainContent_cboJobWorkshopSiteNum')
            field.clear()
            field.send_keys(config['workshop_site'])
            driver.execute_script("DisplayCombo('cboJobWorkshopSiteNum', 'frmRepairJobCreateWzd');")
            if not self.modal():
                return false
            return True
        except Exception as e:
             return False

    def modal(self):
        try:
            wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'fraModalPopup')))
            driver.implicitly_wait(0.5)
            driver.find_element_by_xpath('./html/body/div/form/div[3]/div[3]/table/tbody/tr/td[text()="' + config['workshop_site'] + '"]').click()
            driver.switch_to_default_content()
            return True
        except Exception as e:
            return False

    def next_page(self):
        try:
             driver.find_element_by_id('scmaster_cplMainContent_cmdNext').click()
             return True
        except Exception as e:
            return False

# def createJob(Serial_Number):

#
#
#     driver.find_element_by_id('scmaster_cplMainContent_cmdNext').click()
#
#     wait.until(EC.element_to_be_clickable((By.ID, 'scmaster_cplMainContent_cboCallSiteNum')))
#     driver.find_element_by_id('scmaster_cplMainContent_cmdNext').click()
#
#     elem = wait.until(EC.element_to_be_clickable((By.ID, 'scmaster_cplMainContent_lblEnterJobItemDetails')))
#     elem.send_keys(Serial_Number)
#     driver.execute_script("javascript:DisplayCombo('cboCallSerNum', 'frmRepairJobCreateWzd');")
#     wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'fraModalPopup')))
#     driver.implicitly_wait(0.5) #This wait is working
#     driver.find_element_by_xpath('./html/body/div/form/div[3]/div[3]/table/tbody/tr/td[text()="' + Serial_Number + '"]').click()
#     driver.switch_to_default_content()
#     driver.find_element_by_id('scmaster_cplMainContent_cmdNext').click()
#
#     print('done')

login()
create = job_create_wizard("1012400509177", "48014014702632", "PDTMC9090-DC")
# createJob("1012400509177")



# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
