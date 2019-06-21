from pages.LocatorGeneric import LocatorGeneric


class WebGeneric(LocatorGeneric):
    def __init__(self, driver):
        LocatorGeneric.__init__(self, driver)
        self.driver = driver

    def enter(self, locator_val, input_val, loc_type):
        self.locator(loc_type, locator_val).send_keys(input_val)

    def submit(self, locator_val, loc_type):
        self.locator(loc_type, locator_val).click()

