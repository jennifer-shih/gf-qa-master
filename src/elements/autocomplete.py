from time import sleep

from selenium.webdriver.common.keys import Keys

import src.pages as Pages
from src.drivers.driver import Driver
from src.elements.element import Element
from src.exception.exception import AutocompleteOptionNotFoundError
from src.helper.log import Logger


class Autocomplete(Element):
    __name = "Autocomplete"

    def __init__(
        self,
        select_locator,
        input_locator: tuple,
        disabled_locator: tuple = None,
        advance_locator: tuple = None,
        hyper_link_locator: tuple = None,
        clear_locator: tuple = None,
        new_locator: tuple = None,
        check_after_input: bool = True,
    ):
        super(Autocomplete, self).__init__(select_locator)
        self.input_locator = input_locator
        self.disabled_locator = disabled_locator
        self.advance_locator = advance_locator
        self.hyper_link_locator = hyper_link_locator
        self.clear_locator = clear_locator
        self.new_locator = new_locator
        self.check_after_input = check_after_input

    def input(self, val: str, timeout=10, loading_timeout=2.5) -> None:
        Logger.getLogger().debug("Input [{0}] in autocomplete [{1}, {2}]".format(val, self.locator, self.input_locator))
        if val:
            element = Driver.wait_element_enable(self.locator, timeout=timeout / 2)
            element.click()
            sleep(0.5)
            input_element = Driver.wait_element_enable(self.input_locator, timeout=timeout / 2)
            # ? Walkaround for "[AirImport] Add a HAWB to shipment with required fields only", the Freight Location sometimes cannot click successfully.
            if input_element == None:
                Logger.getLogger().warning("Click [{0}] second time".format(self.locator))
                Driver.wait_element_enable(self.locator, timeout=timeout / 2).click()
                input_element = Driver.wait_element_enable(self.input_locator, timeout=timeout / 2)
            input_element.clear()
            input_element.send_keys(val)
            sleep(loading_timeout)
            input_element.send_keys(Keys.ENTER)
            sleep(1)

            # To avoid input something but not found, then the blank is treated as the answer
            if self.check_after_input:
                if val != "" and self.get_value() == "":
                    raise AutocompleteOptionNotFoundError(val)

    def input_and_close_memo(self, val: str, timeout=10) -> None:
        self.input(val, timeout / 2)
        try:
            Logger.getLogger().debug("Click button [OK]")
            Pages.Common.notice_modal_ok_button.click(timeout=timeout / 4)
            Pages.Common.notice_modal_ok_button.is_invisible(timeout=timeout / 4)
        except:
            Logger.getLogger().warning("Click button [OK] failed")

        sleep(2)

    def is_disabled(self, timeout=5) -> bool:
        """
        the element is in DOM, and it has a "disabled" attribute
        """
        if self.disabled_locator:
            locator = self.disabled_locator
        else:
            locator = self.locator

        assert Driver.wait_element_exist(locator, timeout), f"locator [{locator}] does not exist in DOM"

        result = Driver.wait_element_disabled(locator, timeout) != None
        Logger.getLogger().debug(f"locator [{locator}] is disable? [{result}]")
        return result

    def open_advance_modal(self, timeout=10) -> None:
        ele = Driver.wait_element_enable(self.advance_locator, timeout=timeout / 2)
        if ele == None:
            Logger.getLogger().debug("Click autocomplete [{0}]".format(self.locator))
            Driver.wait_element_enable(self.locator, timeout=timeout / 2).click()
        Logger.getLogger().debug(
            "Open advance modal in autocomplete [{0}, {1}]".format(self.locator, self.advance_locator)
        )
        Driver.wait_element_enable(self.advance_locator, timeout=timeout / 2).click()

    def click_hyper_link(self, timeout=10) -> None:
        Logger.getLogger().debug("Click hyoer link of autocomplete [{0}]".format(self.locator))
        Driver.wait_element_enable(self.hyper_link_locator, timeout=timeout / 2).click()

    def clear(self, timeout=10) -> None:
        Logger.getLogger().debug("Clear value of autocomplete [{0}]".format(self.locator))
        Driver.wait_element_enable(self.clear_locator, timeout=timeout / 2).click()

    def click_add(self, timeout=10) -> None:
        ele = Driver.wait_element_enable(self.advance_locator, timeout=timeout / 2)
        if ele == None:
            Logger.getLogger().debug("Click autocomplete [{0}]".format(self.locator))
            Driver.wait_element_enable(self.locator, timeout=timeout / 2).click()
        Logger.getLogger().debug("Click new tp modal in autocomplete [{0}, {1}]".format(self.locator, self.new_locator))
        Driver.wait_element_enable(self.new_locator, timeout=timeout / 2).click()

    def get_value(self, timeout=5) -> str:
        try:
            val = super()._get_val(timeout).split("\n")[0]
            return val if val != "Select..." else ""
        except:
            if self.disabled_locator:
                element = Driver.wait_element_visible(self.disabled_locator, timeout)
                return element.text
            else:
                raise
