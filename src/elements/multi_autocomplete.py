from time import sleep

from selenium.webdriver.common.keys import Keys

from src.drivers.driver import Driver
from src.elements.element import Element
from src.exception.exception import AutocompleteOptionNotFoundError
from src.helper.log import Logger


class MultiAutocomplete(Element):
    __name = "MultiAutocomplete"

    def __init__(self, select_locator: tuple, input_locator: tuple, clear_locator: tuple = None):
        super(MultiAutocomplete, self).__init__(select_locator)
        self.input_locator = input_locator
        self.clear_locator = clear_locator

    def input(self, datas: str, timeout=10) -> None:
        """
        Delete current datas in the field and input datas. Options are saperated by ';'
        Usage:
            _multi_autocomplete.input("A option;B option;C option")
        """
        self.clear()
        self._input(datas, timeout)

    def add(self, datas: str, timeout=10) -> None:
        """
        Add datas to the field
        """
        self._input(datas, timeout)

    def _input(self, datas: str, timeout=10) -> None:
        Driver.wait_element_enable(self.locator, timeout=timeout / 2).click()
        element = Driver.wait_element_enable(self.input_locator, timeout=timeout / 2)

        datas_list = datas.split(";")
        len_before = self.get_value_len()
        for data in datas_list:
            element.clear()
            element.send_keys(data)
            Logger.getLogger().debug("Send keys [{0}]".format(data))
            sleep(1)
            element.send_keys(Keys.ENTER)
            Logger.getLogger().debug("Send keys [Enter]")

            # To avoid input something but not found
            len_after = self.get_value_len()
            if len_before == len_after:
                raise AutocompleteOptionNotFoundError(data)
            else:
                len_before = len_after

        element.send_keys(Keys.ESCAPE)
        Logger.getLogger().debug("Send keys [Esc]")

    def clear(self, timeout=5) -> None:
        if self.get_value() != "":
            Logger.getLogger().debug(f"Clear value of MultiAutocomplete [{ self.clear_locator }]")
            clear_element = Driver.wait_element_enable(self.clear_locator, timeout)
            clear_element.click()

            # Close the autocomplete dropdown
            input_element = Driver.wait_element_enable(self.input_locator)
            input_element.send_keys(Keys.ESCAPE)

    def get_value(self, timeout=5) -> str:
        try:
            val = ";".join(super()._get_val(timeout).replace("\n×", "").split("\n"))
            return val if "Select..." not in val else ""
        except:
            raise

    def get_value_len(self, timeout=5) -> int:
        got_val = self.get_value(timeout)
        return len(got_val.split(";")) if got_val != "" else 0
