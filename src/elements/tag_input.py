from time import sleep

from selenium.webdriver.common.keys import Keys

from src.drivers.driver import Driver
from src.elements.element import Element
from src.helper.log import Logger


class TagInput(Element):
    __name = "TagInput"

    def __init__(self, locator: tuple, new_tag_input_locator: tuple):
        super(TagInput, self).__init__(locator)
        self.new_tag_input_locator = new_tag_input_locator

    def input(self, tags: str, timeout=5) -> None:
        self.clear()
        self._input(tags, timeout)

    def add(self, tags: str, timeout=5) -> None:
        self._input(tags, timeout)

    def _input(self, tags: str, timeout=5) -> None:
        tags = tags.split(";")
        element = Driver.wait_element_enable(self.new_tag_input_locator, timeout=timeout / 2)
        for tag in tags:
            Logger.getLogger().debug("Add tag [{0}] to [{1}]".format(str(tag), self.locator))
            element.send_keys(tag)
            sleep(0.5)
            element.send_keys(Keys.ENTER)
            sleep(0.5)

    def clear(self) -> None:
        while self.get_value() != "":
            element = Driver.wait_element_enable(self.new_tag_input_locator)
            element.click()
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Keys.BACKSPACE)

    def get_value(self, timeout=5) -> str:
        """
        e.g., the element has three values
            "123 ×444 ×555 ×"
            we will return '123,444,555'
        """
        element = Driver.wait_element_visible(self.locator, timeout)
        values = element.text.split("×")[:-1]
        return ";".join([v.strip() for v in values if v])
