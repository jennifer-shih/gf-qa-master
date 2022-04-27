from src.drivers.driver import Driver
from src.elements.element import Element
from src.helper.log import Logger


class AddFileButton(Element):
    __name = "AddFileButton"

    def __init__(self, locator: tuple):
        super(AddFileButton, self).__init__(locator)

    def add_file(self, file, timeout=5):
        Logger.getLogger().debug("Add File [{0}] in [{1}]".format(str(file), self.locator))
        element = Driver.wait_element_visible(self.locator, timeout)
        if file:
            element.send_keys(file)
        return file

    def get_value(self, timeout=5) -> str:
        element = Driver.wait_element_visible(self.locator, timeout)
        return element.text
