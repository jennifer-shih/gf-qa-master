from time import sleep

from selenium.webdriver.common.keys import Keys

from src.drivers.driver import Driver
from src.elements.element import Element
from src.helper.log import Logger


class AutocompleteMultiSelect(Element):
    __name = "AutocompleteMultiSelect"

    def __init__(
        self,
        select_locator: tuple,
        input_locator: tuple,
        first_search_locator: tuple,
        cancel_locator: tuple,
    ):
        super(AutocompleteMultiSelect, self).__init__(select_locator)
        self.select_locator = select_locator
        self.input_locator = input_locator
        self.first_search_locator = first_search_locator
        self.cancel_locator = cancel_locator

    def input(self, values: str, timeout=10) -> None:
        ele = Driver.wait_element_enable(self.select_locator, timeout=timeout / 2)
        ele.click()

        vals = values.split(";")
        for val in vals:
            Logger.getLogger().debug("Input [{0}] in AutocompleteMultiSelect [{1}]".format(val, self.select_locator))
            sleep(0.5)
            element = Driver.wait_element_enable(self.input_locator, timeout=timeout / 2)
            element.clear()
            element.send_keys(val)
            sleep(2.5)
            element.send_keys(Keys.ENTER)

            # TODO Check if the corresponding option is found like in multi_autocomplete (Now self.get_value() not works)

        element.send_keys(Keys.ESCAPE)

    def get_value(self, timeout=5) -> str:
        # ! Only gets the value of the firest option
        val = super()._get_val(timeout).split("\n")[0]
        return val if val != "Select..." else ""

    # ! this funtion will not work when val is unselect
    def clear_val(self, val: str, timeout=10) -> None:
        Logger.getLogger().debug("Clear [{0}] in AutocompleteMultiSelect [{1}]".format(val, self.select_locator))
        ele = Driver.wait_element_enable(self.select_locator, timeout=timeout / 2)
        ele.click()
        ele_input = Driver.wait_element_enable(self.input_locator, timeout=timeout / 2)
        ele_input.clear()
        ele_input.send_keys(val)
        sleep(2.5)
        ele_first = Driver.wait_element_enable(self.first_search_locator, timeout=timeout / 2)
        ele_first.click()

    def clear(self, timeout=5) -> None:
        Logger.getLogger().debug("Clear All in AutocompleteMultiSelect [{}]".format(self.select_locator))
        v = self.get_value()
        if v:
            ele = Driver.wait_element_enable(self.cancel_locator, timeout=timeout / 2)
            ele.click()
