from src.drivers.driver import Driver
from src.elements.element import Element
from src.helper.log import Logger


class Button(Element):
    __name = "Button"

    def __init__(self, locator: tuple):
        super(Button, self).__init__(locator)

    def click(self, timeout=5) -> None:
        Logger.getLogger().debug("Click [{0}]".format(self.locator))
        elememt = Driver.wait_element_enable(self.locator, timeout)
        elememt.click()

    def get_value(self, timeout=5) -> str:
        element = Driver.wait_element_visible(self.locator, timeout)
        return element.text
