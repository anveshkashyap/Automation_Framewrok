from pages.webGeneric import WebGeneric
from data.testData import *


class LoginWP(WebGeneric):
    def __init__(self, driver):
        WebGeneric.__init__(self, driver)
        self.driver = driver
        self.un_id = "user_login"
        self.pwd_id = "user_pass"
        self.loginBtn_id = "wp-submit"

    def wp_login(self):
        # wg=WebGeneric(self.driver)
        self.enter("id", self.un_id, USERNAME)
        self.enter("id", self.pwd_id, PASSWORD)
        self.submit("name", self.loginBtn_id)



