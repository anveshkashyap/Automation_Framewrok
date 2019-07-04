from pages.webGeneric import WebGeneric


class HomePage(WebGeneric):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.logoutBtn_xpath = "//*[contains(text(),'Logout')]"

    def acti_logout(self):
        #wg = WebGeneric(self.driver)
        self.submit("xpath", self.logoutBtn_xpath)
