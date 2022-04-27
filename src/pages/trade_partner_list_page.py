from selenium.webdriver.common.by import By

from src.elements import *


class TradePartnerListPage:
    filter_button = Button((By.XPATH, "//a[@ng-click='vm.filter.reset()']"))

    class Filter:
        keyword_input = Input((By.XPATH, "//input[../label[contains(., 'Keyword')]]"))
        apply_filters_button = Button((By.XPATH, "//button[@ng-disabled='vm.filter.hasNoInput()']"))
    class searchResult:
            _rows = {}
            def __new__(cls, index=1):
                index = int(index)
                if index not in cls._rows:
                    cls._rows[index] = super().__new__(cls)
                return cls._rows[index]

            def __init__(self, index=1):

                def ROW_XPATH(xpath):
                    return "//tr[@ng-repeat='tp in vm.tp.data_list'][{0}]{1}".format(index, xpath)

                self.name_link = Link((By.XPATH, ROW_XPATH("//a[contains(@class, 'col-link-target ng-binding')]")))
