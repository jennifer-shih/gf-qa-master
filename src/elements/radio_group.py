import random

from src.drivers.driver import Driver
from src.elements.element import Element
from src.helper.log import Logger


class RadioGroup(Element):
    __name = "RadioGroup"

    def __init__(self, options_locators_dict: dict):
        super(RadioGroup, self).__init__(list(options_locators_dict.values())[0])
        self.options_locators_dict = options_locators_dict

    def click(self, key: str, timeout=5) -> None:
        locator = self.options_locators_dict[key]
        Logger.getLogger().debug("Click [{0}]".format(locator))

        # ? For an unknown reason, a RadioGroup won't be taken as enabled.
        # ? so we call Driver.wait_element_visible() instead of wait_element_enabled()
        Driver.wait_element_visible(locator, timeout).click()

    def get_value(self, timeout=5) -> str:
        for key, locator in self.options_locators_dict.items():
            element = Driver.wait_element_visible(locator, timeout / 3)
            if element.is_selected():
                return key

        return None

    def random_click(self, timeout=5) -> None:
        r = random.choice(list(self.options_locators_dict.keys()))
        Logger.getLogger().debug("Click [{0}]".format(self.options_locators_dict[r]))
        Driver.wait_element_visible(self.options_locators_dict[r], timeout).click()
