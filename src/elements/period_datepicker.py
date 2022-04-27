from time import sleep

from selenium.webdriver.common.keys import Keys

from src.drivers.driver import Driver
from src.elements.element import Element
from src.helper.log import Logger


class PeriodDatepicker(Element):
    __name = "PeriodDatepicker"

    def __init__(self, view_locator: tuple, start_locator: tuple, end_locator: tuple):
        super(PeriodDatepicker, self).__init__(view_locator)
        self.view_locator = view_locator
        self.start_locator = start_locator
        self.end_locator = end_locator

    def input(self, val: str, timeout=5) -> None:
        """
        Usage:
            example_period_datepicker.input("2020-01-01 ~ 2020-02-28")
        """
        val_list = val.split("~")
        start_date = val_list[0].strip()
        end_date = val_list[1].strip()

        Logger.getLogger().debug("Click [{0}]".format(self.view_locator))
        Driver.wait_element_enable(self.view_locator, timeout).click()
        Logger.getLogger().debug("Input [{0}] [{1}] in [{2}]".format(start_date, end_date, self.start_locator))
        ele_start = Driver.wait_element_enable(self.start_locator, timeout)
        ele_end = Driver.wait_element_enable(self.end_locator, timeout)
        ele_start.clear()
        ele_end.clear()
        ele_start.send_keys(start_date)
        sleep(0.5)
        ele_end.send_keys(end_date)
        sleep(0.5)
        ele_end.send_keys(Keys.ENTER)

    def get_value(self, timeout=5) -> str:
        return self._get_val(timeout=timeout)
