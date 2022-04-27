import random
from time import sleep

from selenium.common.exceptions import UnexpectedTagNameException
from selenium.webdriver.support.ui import Select as SelectUI

from src.drivers.driver import Driver
from src.elements.element import Element
from src.helper.log import Logger


class CheckSelect(Element):
    __name = "CheckSelect"

    def __init__(self, check_locator: tuple, select_locator: tuple):
        super(CheckSelect, self).__init__(select_locator)
        self.check_locator = check_locator
        self.select_locator = select_locator

    def select(self, val: str, timeout=5) -> None:
        self._checked()
        Logger.getLogger().debug("Select [{0}] in selector [{1}]".format(val, self.select_locator))
        element = SelectUI(Driver.wait_element_enable(self.select_locator, timeout))
        element.select_by_visible_text(val)

    def random_select(self, timeout=5) -> None:
        # select 隨機
        self._checked()
        element = SelectUI(Driver.wait_element_enable(self.select_locator, timeout))
        options = [i.text for i in element.options]
        op = random.choice(options)
        Logger.getLogger().debug("Select [{0}] in selector [{1}]".format(op, self.select_locator))
        element.select_by_visible_text(op)

    def random_check_and_select(self, timeout=5) -> None:
        # checkbox 和 select 都隨機
        r = random.choice([True, False])
        if r:
            self.random_select(timeout)

    def get_value(self, timeout=5) -> tuple[bool, str]:
        try:
            e_check = Driver.wait_element_visible(self.check_locator, timeout)
            if e_check.tag_name != "input":
                raise UnexpectedTagNameException(
                    "The locator should point to a 'input' tag in DOM, or is_selected() will always return false"
                )
            if e_check.is_selected() == False:
                return (False, None)
            else:
                e_date = Driver.wait_element_enable(self.locator_datepicker, timeout)
                e_date_value = e_date.get_attribute("value")
            return (True, e_date_value if e_date_value != None else e_date.text)
        except:
            return (False, None)

    def tick(self, is_tick: bool, timeout=5) -> bool:
        if not isinstance(is_tick, bool):
            raise TypeError("the first argument should be in bool type")

        Logger.getLogger().debug("Tick [{0}] be [{1}]".format(self.check_locator, is_tick))
        sleep(0.5)
        ele = Driver.wait_element_visible(self.check_locator, timeout)
        if ele.tag_name != "input":
            raise UnexpectedTagNameException(
                "The locator should point to a 'input' tag in DOM, or is_selected() will always return false"
            )
        if ele.is_selected() != is_tick:
            ele.click()
        return is_tick

    def _checked(self, timeout=5) -> None:
        e_check = Driver.wait_element_visible(self.check_locator, timeout)
        if e_check.tag_name != "input":
            raise UnexpectedTagNameException(
                "The locator should point to a 'input' tag in DOM, or is_selected() will always return false"
            )
        if e_check.is_selected() != True:
            Logger.getLogger().debug("Tick [{0}] on".format(self.check_locator))
            e_check.click()
