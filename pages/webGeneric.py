from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.LocatorGeneric import LocatorGeneric


class WebGeneric(LocatorGeneric):
    def __init__(self, driver):
        LocatorGeneric.__init__(self, driver)
        self.driver = driver

    def enter(self, loc_type, locator_val, input_val):
        self.locator(loc_type, locator_val).send_keys(input_val)

    def submit(self, loc_type, locator_val):
        val = self.locator(loc_type, locator_val)
        # wait = WebDriverWait(self.driver, 30)
        # wait.until(expected_conditions.element_to_be_clickable(val))
        val.click()

    def mouse_hover(self, loc_type, loc_val):
        action = ActionChains(self.driver)
        action.move_to_element(self.locator(loc_type, loc_val)).perform()

    def switch_frame(self, loc_type, frame_locator):
        iframe = self.locator(loc_type, frame_locator)
        self.driver.switch_to.frame(iframe)

    def drag_and_drop(self, src, dest):
        action = ActionChains(self.driver)
        action.drag_and_drop(src, dest).perform()

