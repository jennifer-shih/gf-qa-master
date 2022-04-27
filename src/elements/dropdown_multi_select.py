import random

from src.drivers.driver import Driver
from src.elements.element import Element
from src.helper.log import Logger


class DropdownMultiSelect(Element):
    __name = "DropdownMultiSelect"

    """
    structure:
    <ng-dropdown-multiselect>
        <ul>
            <li>
                <span>
                    <span>option1</span>
                </span>
                <span>
                    <span>option2</span>
                </span>
            </li>
        </ul>
    </ng-dropdown-multiselect>
    """

    def __init__(self, locator):
        super(DropdownMultiSelect, self).__init__(locator)

    def select(self, text, timeout=5):
        Logger.getLogger().debug("Select [{0}] in selector [{1}]".format(text, self.locator))
        element = Driver.wait_element_enable(self.locator, timeout)
        element.click()

        values = text.split(",")
        for val in values:
            locator = list(self.locator)
            locator[1] += "//li//span[.='{}']".format(val)  # xpath may be
            opt_locator = tuple(locator)
            opt_ele = Driver.wait_element_enable(opt_locator, timeout)
            opt_ele.click()

    def random_select(self, timeout=5):
        element = Driver.wait_element_enable(self.locator, timeout)
        options = element.text.split("\n")
        op = random.choice(options)
        Logger.getLogger().debug("Select [{0}] in selector [{1}]".format(op, self.locator))

        locator = list(self.locator)
        locator[1] += "//li//span[.='{}']".format(op)
        opt_locator = tuple(locator)
        opt_ele = Driver.wait_element_enable(opt_locator, timeout)
        opt_ele.click()

    def get_value(self, timeout=5):
        try:
            element = Driver.wait_element_enable(self.locator, timeout)
            text = element.text
            text = text.split("\n")[
                0
            ]  # e.g. Draft, Amount Confirmed, Fully Paid\nDraft\nAmount\nConfirmed\nPartial Paid\nFully Paid
            return text
        except:
            return None
