import xlrd


class LocatorGeneric:

    def __init__(self, driver):
        self.driver = driver

    def locator(self, loc_type, loc_val):
        if loc_type == "id":
            ele = self.driver.find_element_by_id(loc_val)
        elif loc_type == "name":
            ele = self.driver.find_element_by_name(loc_val)
        elif loc_type == "tag_name":
            ele = self.driver.find_element_by_tag_name(loc_val)
        elif loc_type == "xpath":
            ele = self.driver.find_element_by_xpath(loc_val)
        elif loc_type == "class_name":
            ele = self.driver.find_element_by_class_name(loc_val)
        return ele

    def get_val_excel(self, sheet_name, wb_path):
        wb = xlrd.open_workbook(wb_path)
        ws = wb.sheet_by_name(sheet_name)
        row_count = ws.nrows
        col_count = ws.ncols
