from src.drivers.driver import Driver
from src.elements.element import Element


class Label(Element):
    __name = "Label"

    def __init__(self, locator: tuple):
        super(Label, self).__init__(locator)

    def get_value(self, timeout=5) -> str:
        element = Driver.wait_element_visible(self.locator, timeout)
        return element.text
