from selenium.webdriver.common.by import By

from src.elements import *


class OEBookingListPage:
    filter_button = Button((By.XPATH, "//a[@id='filter_btn']"))

    class Filter:
        keyword_input = Input((By.XPATH, "//hc-keyword-filter[@key='keyword']//input[@ng-model='vm.filter.input[vm.key]']"))
        apply_filters_button = Button((By.XPATH, "//button[@type='submit'][@ng-disabled='vm.filter.hasNoInput()']"))

    class Row:
        _rows = {}

        def __new__(cls, index=1):
            index = int(index) - 1
            if index not in cls._rows:
                cls._rows[index] = super().__new__(cls)
            return cls._rows[index]

        def __init__(self, index=1):
            index = int(index) - 1
            def ROW_XPATH(xpath):
                return "//div[@ref='eBodyViewport']//div[@row-index='{0}']{1}".format(index, xpath)

            self.hbl_no_label = Label((By.XPATH, ROW_XPATH("//div[@col-id='booking_hbl_no']")))
            self.booking_no_link = Link((By.XPATH, ROW_XPATH("//div[@col-id='booking_no']//a")))
