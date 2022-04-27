from time import sleep

from selenium.webdriver.common.keys import Keys

from src.drivers.driver import Driver
from src.elements.element import Element
from src.helper.log import Logger


class EmailTags(Element):
    __name = "EmailTags"

    def __init__(self, edit_locator: tuple, val_locator: tuple, input_locator: tuple):
        super(EmailTags, self).__init__(edit_locator)
        self.edit_locator = edit_locator  # pencil icon
        self.val_locator = val_locator
        self.input_locator = input_locator  # validate input field

    def input(self, emails: str, timeout=5) -> None:
        emails = emails.split(";")
        Driver.wait_element_enable(self.edit_locator, timeout=timeout / 2).click()
        input_ele = Driver.wait_element_enable(self.input_locator, timeout=timeout / 2)
        for email in emails:
            Logger.getLogger().debug("Add mail [{0}] to [{1}]".format(str(email), self.val_locator))
            input_ele.send_keys(email)
            sleep(0.5)
            input_ele.send_keys(Keys.ENTER)
            sleep(0.5)

    def get_value(self, timeout=5) -> str:
        element = Driver.wait_element_visible(self.val_locator, timeout)
        return element.text
