from time import sleep

from selenium.webdriver.common.keys import Keys

from src.drivers.driver import Driver
from src.elements.element import Element
from src.helper.log import Logger


class Datepicker(Element):
    __name = "Datepicker"

    def __init__(self, locator: tuple, disabled_locator: tuple = None):
        super(Datepicker, self).__init__(locator)
        self.disabled_locator = disabled_locator

    def input(self, val: str, timeout=5) -> None:
        # datepicker 輸入完需要按 Enter
        Logger.getLogger().debug("Input [{0}] in [{1}]".format(val, self.locator))
        element = Driver.wait_element_enable(self.locator, timeout)
        element.clear()
        element.send_keys(val)
        sleep(0.5)
        element.send_keys(Keys.ENTER)

    def get_value(self, timeout=5) -> str:
        val = self._get_val(timeout=timeout)
        if val is None and self.disabled_locator:
            element = Driver.wait_element_visible(self.disabled_locator, timeout)
            return element.get_attribute("value")
        return val

    def clear(self, timeout=5) -> None:
        Logger.getLogger().debug("Clear [{0}] value".format(self.locator))
        element = Driver.wait_element_enable(self.locator, timeout)
        element.clear()
