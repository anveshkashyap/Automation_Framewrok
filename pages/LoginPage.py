from pages.webGeneric import WebGeneric
from data.testData import *


class Login(WebGeneric):
    def __init__(self, driver):
        WebGeneric.__init__(self, driver)
        self.driver = driver
        self.un_id = "username"
        self.pwd_name = "pwd"
        self.loginBtn_xpath = "//*[text()='Login ']"

    def acti_login(self):
        # wg=WebGeneric(self.driver)
        self.enter("id", self.un_id, USERNAME)
        self.enter("name", self.pwd_name, PASSWORD)
        self.submit("xpath", self.loginBtn_xpath)



