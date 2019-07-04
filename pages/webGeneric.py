from pages.LocatorGeneric import LocatorGeneric


class WebGeneric(LocatorGeneric):
    def __init__(self, driver):
        LocatorGeneric.__init__(self, driver)
        self.driver = driver

    def enter(self, loc_type, locator_val, input_val):
        self.locator(loc_type, locator_val).send_keys(input_val)

    def submit(self, loc_type, locator_val):
        self.locator(loc_type, locator_val).click()

