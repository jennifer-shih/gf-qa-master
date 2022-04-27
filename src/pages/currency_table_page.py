from time import sleep

from selenium.webdriver.common.by import By

from src.drivers.driver import Driver
from src.elements import *


class CurrencyTablePage:
    from_currency_select = Select((By.XPATH, "//select[@ng-model='vm.ccy1']"))
    to_currency_select = Select((By.XPATH, "//select[@ng-model='vm.ccy2']"))
    new_button = Button((By.XPATH, "//button[@ng-click='vm.addNewMapping()']"))
    delete_button = Button((By.XPATH, "//button[@ng-click='vm.mappingRowList.markCheckedRowsDeleted()']"))
    save_button = Button((By.XPATH, "//button[@ng-click='vm.save()']"))

    # table
    check_all_checkbox = Checkbox((By.XPATH, "//thead//input[@ng-click='vm.mappingRowList.checkAllRows()']"))

    class row:
            _rows = {}

            def __new__(cls, index=1):
                index = int(index)
                if index not in cls._rows:
                    cls._rows[index] = super().__new__(cls)
                return cls._rows[index]

            def __init__(self, index=1):
                index = int(index)
                def ROW_XPATH(xpath):
                    return "//tbody//tr[not(contains(@class,'ng-hide'))][{0}]{1}".format(index, xpath)

                self.as_of_datepicker = Input((By.XPATH, ROW_XPATH("//input[@name='as_of_date']")))
                self.rate_internal_input = Input((By.XPATH, ROW_XPATH("//input[@name='rate_internal']")))
                self.rate_external_input = Input((By.XPATH, ROW_XPATH("//input[@name='rate_external']")))

            @staticmethod
            def get_len():
                sleep(2)
                return Driver.num_of_element("//tbody//tr[not(contains(@class,'ng-hide'))]")
