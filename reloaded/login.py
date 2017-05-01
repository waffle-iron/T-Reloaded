class Login():
    """
    Provide functionality need for app login.

    :username: (optional) As string, the users username.
    :password: (optional) As string, the users password.
    """

    def __init__(self):
        pass

    def navigate_to_login_and_verify(self):
        """
        Navigate driver to app login. Verify database.
        """
        s = ''
        url = s.join(app.settings['baseUrl']
                     + "SC51/SC_Login/aspx/Login_Launch.aspx"
                     + app.settings['sourceString'])
        driver.get(url)
        assert "Service Centre Login" in driver.title
        database_element = driver.find_element_by_id('txtDBaseName')
        database_value = database_element.get_attribute('value')
        if "Test" in database_value:
            # TODO - Write to logger & console
            pass
        return True

    def fill_user_credentials_and_submit(self):
        """
        Login and verify app.
        """
        driver.find_element_by_id('txtUserName').send_keys(app.settings.username)
        driver.find_element_by_id('txtPassword').send_keys(app.settings.password)
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
