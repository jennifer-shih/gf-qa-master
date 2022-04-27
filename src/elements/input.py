from src.drivers.driver import Driver
from src.elements.element import Element
from src.helper.log import Logger


class Input(Element):
    __name = "Input"

    def __init__(self, locator: tuple, disabled_locator: tuple = None):
        super(Input, self).__init__(locator)
        self.disabled_locator = disabled_locator

    def input(self, val: str, timeout=5) -> None:
        Logger.getLogger().debug("Input [{0}] in [{1}]".format(val, self.locator))
        element = Driver.wait_element_enable(self.locator, timeout)
        # Driver.move_mouse_to(element)
        element.clear()
        element.send_keys(val)

    def send_keys(self, keys: str, timeout=5) -> None:
        Logger.getLogger().debug("Send keys [{0}] to [{1}]".format(str(keys), self.locator))
        element = Driver.wait_element_enable(self.locator, timeout)
        element.send_keys(keys)

    def clear(self, timeout=5) -> None:
        Logger.getLogger().debug("Clear [{0}] value".format(self.locator))
        element = Driver.wait_element_enable(self.locator, timeout)
        element.clear()

    def click(self, timeout=5) -> None:
        Logger.getLogger().debug("Click [{0}]".format(self.locator))
        element = Driver.wait_element_enable(self.locator, timeout)
        element.click()

    def get_value(self, timeout=5) -> str:
        element_value = self._get_val(timeout=timeout)
        if element_value is None and self.disabled_locator:
            disabled_locator_element = Driver.wait_element_visible(self.disabled_locator, timeout)
            return disabled_locator_element.text
        return element_value

    def is_enable(self, timeout=5) -> bool:
        return not self.is_disabled(timeout)  # TODO GQT-423 應該用 element enable 就好了?
