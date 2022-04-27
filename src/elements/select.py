import random

from selenium.webdriver.support.ui import Select as SelectUI

from src.drivers.driver import Driver
from src.elements.element import Element
from src.helper.log import Logger


class Select(Element):
    __name = "Select"

    def __init__(self, locator: tuple):
        super(Select, self).__init__(locator)

    def select(self, text: str, timeout=5) -> None:
        Logger.getLogger().debug("Select [{0}] in selector [{1}]".format(text, self.locator))
        element = SelectUI(Driver.wait_element_enable(self.locator, timeout))
        ### for debug ###
        # element = Driver.wait_element_enable(self.locator, timeout)
        # element.click()
        # element = SelectUI(element)
        ###           ###
        element.select_by_visible_text(text)

    def random_select(self, timeout=5) -> None:
        element = SelectUI(Driver.wait_element_enable(self.locator, timeout))
        options = [i.text for i in element.options]
        op = random.choice(options)
        Logger.getLogger().debug("Select [{0}] in selector [{1}]".format(op, self.locator))
        element.select_by_visible_text(op)

    def get_value(self, timeout=5) -> str:
        try:
            # element = SelectUI(Driver.wait_element_enable(self.locator))
            element = SelectUI(Driver.wait_element_visible(self.locator, timeout))
            text = element.first_selected_option.text
            return text
        except:
            return None
