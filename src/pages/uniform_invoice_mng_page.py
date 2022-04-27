from selenium.webdriver.common.by import By

from src.elements import *


class UniformInvoiceMngPage:
    void_button = Button((By.XPATH, "//div[@class='portlet-tool']//button[.='Void']"))
    valid_button = Button((By.XPATH, "//div[@class='portlet-tool']//button[.='Valid']"))

    class InvoiceList:
        _rows = {}
        def __new__(cls, index=1):
                index = int(index) - 1
                if index not in cls._rows:
                    cls._rows[index] = super().__new__(cls)
                return cls._rows[index]

        def __init__(self, index=1):
            index = int(index) - 1
            def ROW_XPATH(xpath):
                return "//hcgridcontainer//div[@row-id='{0}']{1}".format(index, xpath)

            self.check_checkbox = Checkbox((By.XPATH, ROW_XPATH("//div[@col-id='chk_1']//input")), (By.XPATH, ROW_XPATH("//div[@col-id='chk_1']//span")))
            self.void_success_label = Label((By.XPATH, ROW_XPATH("//div[2]/div//i[contains(@class, 'fa-check')]")))
    class InvoiceModal:
        confirm_button = Button((By.XPATH, "//div[@class='modal-footer']//button[.='Confirm']"))
