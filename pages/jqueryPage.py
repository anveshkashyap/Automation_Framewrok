from selenium.webdriver import ActionChains

from pages.webGeneric import WebGeneric
from data.testData import *


class DragNDrop(WebGeneric):
    def __init__(self, driver):
        WebGeneric.__init__(self, driver)
        self.driver = driver
        self.droppable_xpath = "//a[text()='Droppable']"
        self.frame_xpath = "//iframe[1]"
        self.src_id = "draggable"
        self.dest_id = "droppable"

    def drag_n_drop(self):
        # wg=WebGeneric(self.driver)
        self.submit("xpath", self.droppable_xpath)
        self.switch_frame("xpath", self.frame_xpath)
        src = self.locator("id", self.src_id)
        dest = self.locator("id",self.dest_id)
        self.drag_and_drop(src, dest)

        # self.enter("id", self.un_id, USERNAME)
#         # self.enter("name", self.pwd_name, PASSWORD)
#         # self.submit("xpath", self.loginBtn_xpath)



