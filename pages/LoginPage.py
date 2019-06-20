from pages.webGeneric import WebGeneric


class Login(WebGeneric):
    def __init__(self, driver):
        WebGeneric.__init__(self, driver)
        self.driver = driver
        self.un_id = "'username'"
        self.pwd_name = "'pwd'"
        self.loginBtn_xpath = " \"//*[text()='Login ']\" "

    def acti_login(self, un, pwd):
        wg=WebGeneric(self.driver)
        wg.enter(self.un_id, un, locator='id')
        wg.enter(self.pwd_name, pwd, locator='name')
        wg.submit(self.loginBtn_xpath, locator='xpath')



