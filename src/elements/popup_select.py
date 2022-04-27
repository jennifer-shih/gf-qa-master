from time import sleep

from src.drivers.driver import Driver
from src.elements.element import Element
from src.helper.log import Logger


class PopupSelect(Element):
    __name = "PopupSelect"

    def __init__(self, add_locator: tuple, apply_locator: tuple, options_locators_dict: dict):
        super(PopupSelect, self).__init__(add_locator)
        self.apply_locator = apply_locator
        self.options_locators_dict = options_locators_dict

    def click_add(self, timeout=5) -> None:
        Logger.getLogger().debug("Click [{0}]".format(self.locator))
        Driver.wait_element_enable(self.locator, timeout).click()

    def click_apply(self, timeout=5) -> None:
        Logger.getLogger().debug("Click [{0}]".format(self.apply_locator))
        Driver.wait_element_enable(self.apply_locator, timeout).click()

    def select(self, options: str, timeout=15) -> None:
        options = options.split(";")
        self.click_add(timeout=timeout / 3)
        sleep(1)
        for option in options:
            Logger.getLogger().debug("Select option [{0}]".format(option))
            Driver.wait_element_enable(self.options_locators_dict[option], timeout=1).click()
        self.click_apply(timeout=timeout / 3)
        sleep(1)
