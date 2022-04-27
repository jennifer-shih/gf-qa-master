from selenium.common.exceptions import UnexpectedTagNameException

from src.drivers.driver import Driver
from src.elements.element import Element
from src.helper.log import Logger


class Checkbox(Element):
    """
    The locator of this element should point to a "input" tag in DOM, since only in
    this case will WebElement.is_selected() return true when the checkbox is ticked.
    Otherwise, it will always return False.
    However, if the "input" tag has no height and width, the click action will fail,
    so it's necessary to provide click_locator argument.
    """

    __name = "Checkbox"

    def __init__(self, locator: tuple, click_locator: tuple = None):
        super(Checkbox, self).__init__(locator)
        self.click_locator = click_locator

    def tick(self, is_tick: bool, timeout=5) -> None:
        if not isinstance(is_tick, bool):
            raise TypeError("the first argument should be in bool type")

        Logger.getLogger().debug("Tick [{0}] be [{1}]".format(self.locator, is_tick))
        ele = Driver.wait_element_visible(self.locator, timeout)

        if ele.tag_name != "input":
            raise UnexpectedTagNameException(
                "The locator should point to a 'input' tag in DOM, or is_selected() will always return false"
            )
        if ele.is_selected() != is_tick:
            if self.click_locator:
                click_ele = Driver.wait_element_visible(self.click_locator, timeout)
                click_ele.click()
            else:
                ele.click()

        assert ele.is_selected() == is_tick

    def get_value(self, timeout=5) -> bool:
        element = Driver.wait_element_visible(self.locator, timeout)
        if element.tag_name != "input":
            raise UnexpectedTagNameException(
                "The locator should point to a 'input' tag in DOM, or is_selected() will always return false"
            )
        return element.is_selected() == True

    def is_enable(self, timeout=5) -> bool:
        return not self.is_disabled(timeout)  # TODO GQT-423 應該用 element enable 就好了?
