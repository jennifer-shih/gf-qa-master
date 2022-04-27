from time import sleep

from selenium.webdriver.common.keys import Keys

from src.drivers.driver import Driver
from src.elements.element import Element
from src.helper.log import Logger

"""
Doc Center 中的 Name
"""


class EditInput(Element):
    __name = "EditInput"

    def __init__(self, text_locator: tuple, editing_text_locator: tuple, edit_btn_locator: tuple):
        super(EditInput, self).__init__(text_locator)
        self.text_locator = text_locator
        self.editing_text_locator = editing_text_locator
        self.edit_btn_locator = edit_btn_locator

    def input(self, text: str, timeout=5) -> None:
        Driver.wait_element_enable(self.edit_btn_locator, timeout / 2).click()
        textbox = Driver.wait_element_visible(self.editing_text_locator, timeout / 2)
        textbox.clear()
        textbox.send_keys(text)
        Logger.getLogger().debug("Input [{0}] in [{1}]".format(text, self.edit_btn_locator))
        sleep(0.5)
        textbox.send_keys(Keys.ENTER)

    def get_value(self, timeout=5) -> str:
        element = Driver.wait_element_visible(self.text_locator, timeout)
        element_value = element.get_attribute("value")
        return element_value if element_value != None else element.text
