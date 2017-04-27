import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p :', filename='info.log',level=logging.INFO)


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

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
    logging.info('Login page has been found')

    database = driver.find_element_by_id('txtDBaseName').get_attribute('value')
    logging.info('Using database %s', database)

    driver.find_element_by_id('txtUserName').send_keys(config['user'])
    logging.info('Username is set')
    driver.find_element_by_id('txtPassword').send_keys(config['pass'])
    logging.info('password is set')

    driver.find_element_by_id('btnsubmit').click()
    element = wait.until(EC.title_contains('Wincor 5.1'))

    logging.info('Page title is %s', driver.title)

def createJob():
    driver.get('https://tesseract-cloud2.co.uk/SC51/SC_RepairJob/aspx/repairjob_create_wzd.aspx')
    assert "Welcome the the Repair Job Creation Wizard. Please enter your workshop site code." in driver.page_source

    elem = driver.find_element_by_id('scmaster_cplMainContent_cboJobWorkshopSiteNum')
    elem.clear()
    elem.send_keys(config['workshop_site'])
    driver.execute_script("DisplayCombo('cboJobWorkshopSiteNum', 'frmRepairJobCreateWzd');")
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'fraModalPopup')))
    driver.implicitly_wait(0.5) #This wait is working
    driver.find_element_by_xpath('./html/body/div/form/div[3]/div[3]/table/tbody/tr/td[text()="' + config['workshop_site'] + '"]').click()
    driver.switch_to_default_content()
    driver.find_element_by_id('scmaster_cplMainContent_cmdNext').click()
    wait.until(EC.element_to_be_clickable((By.ID, 'scmaster_cplMainContent_cboCallSiteNum')))
    driver.find_element_by_id('scmaster_cplMainContent_cmdNext').click()

    print('done')

login()
createJob()



# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
