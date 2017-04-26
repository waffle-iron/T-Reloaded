import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='info.log',level=logging.INFO)


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

config = {}
config['baseUrl'] = "https://tesseract-cloud2.co.uk/SC51/SC_Login/aspx/Login_Launch.aspx?source=wn93kn83"
config['user'] = "kieranw"
config['pass'] = "kieranw"
config['max_wait_time'] = 10

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





login()




# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
