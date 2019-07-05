from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.webGeneric import WebGeneric


class HomePageWP(WebGeneric):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.opens_id = "wp-admin-bar-my-account"
        self.logoutBtn_xpath = "(//a[text()='Log Out'])[1]"

    def wp_logout(self):
        # wg = WebGeneric(self.driver)
        # action = ActionChains(self.driver)
        # action.move_to_element(self.driver.find_element_by_id(self.opens_id)).perform()
        # val = self.driver.find_element_by_xpath(self.logoutBtn_xpath)
        # wait = WebDriverWait(self.driver, 30)
        # wait.until(EC.visibility_of_element_located(val))
        # val.click()
        self.mouse_hover("id", self.opens_id)
        self.submit("xpath", self.logoutBtn_xpath)
