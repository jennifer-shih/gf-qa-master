from selenium.webdriver.common.by import By

from src.elements import *


class FeatAndApprovalPage:
    feature_select = Select((By.XPATH, "//label[contains(., 'Feature')]/select"))
    office_select = Select((By.XPATH, "//label[contains(., 'Office')]/select"))

    class ApprovalList:
        _rows = {}
        def __new__(cls, index=1):
            index = int(index)
            if index not in cls._rows:
                cls._rows[index] = super().__new__(cls)
            return cls._rows[index]

        def __init__(self, index=1):
            index = int(index)
            def ROW_XPATH(xpath):
                return '//tbody//tr[{0}]{1}'.format(index, xpath)

            self.department_select = Select((By.XPATH, ROW_XPATH('//hcdepartmentselect')))
