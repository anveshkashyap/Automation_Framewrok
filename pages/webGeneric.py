class WebGeneric:
    def __init__(self, driver):
        self.driver = driver

    def enter(self, locator_val, input_val, locator):
        run = "self.driver.find_element_by_"+locator+"("+locator_val+").send_keys("+input_val+")"
        exec(run)

    def submit(self, locator_val, locator):
        run = "self.driver.find_element_by_"+locator+"("+locator_val+").click()"
        exec(run)