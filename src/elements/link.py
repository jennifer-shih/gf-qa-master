from src.drivers.driver import Driver
from src.elements.element import Element
from src.helper.log import Logger


class Link(Element):
    __name = "Link"

    def __init__(self, locator: tuple):
        super(Link, self).__init__(locator)

    def click(self, timeout=5) -> None:
        Logger.getLogger().debug("Click [{0}]".format(self.locator))
        Driver.wait_element_enable(self.locator, timeout).click()

    def get_value(self, timeout=5) -> str:
        return self._get_val(timeout=timeout)
