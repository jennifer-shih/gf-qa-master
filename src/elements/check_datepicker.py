from time import sleep

from selenium.common.exceptions import UnexpectedTagNameException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.drivers.driver import Driver
from src.elements.element import Element
from src.helper.log import Logger


class CheckDatepicker(Element):
    __name = "CheckDatepicker"

    def __init__(self, check_locator: tuple, datepicker_locator: tuple):
        super(CheckDatepicker, self).__init__(datepicker_locator)
        self.locator_check = check_locator
        self.locator_datepicker = datepicker_locator

    def input(self, val: str, timeout=5) -> None:
        e_check = Driver.wait_element_visible(self.locator_check, timeout)
        if e_check.tag_name != "input":
            raise UnexpectedTagNameException(
                "The locator should point to a 'input' tag in DOM, or is_selected() will always return false"
            )
        if e_check.is_selected() == False:
            Logger.getLogger().debug("Tick [{0}] on".format(self.locator_check))
            e_check.click()

        # datepicker 輸入完需要按 Enter
        Logger.getLogger().debug("Input [{0}] in [{1}]".format(val, self.locator_datepicker))
        e_date = Driver.wait_element_enable(self.locator_datepicker, timeout)
        e_date.clear()
        e_date.send_keys(val)
        sleep(0.5)
        e_date.send_keys(Keys.ENTER)

    def get_value(self, timeout=5) -> tuple[bool, str]:
        try:
            e_check = Driver.wait_element_visible(self.locator_check, timeout)
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
            return None

    def clear(self, timeout=5) -> None:
        e_check = Driver.wait_element_visible(self.locator_check, timeout)
        if e_check.tag_name != "input":
            raise UnexpectedTagNameException(
                "The locator should point to a 'input' tag in DOM, or is_selected() will always return false"
            )
        if e_check.is_selected() == True:
            Logger.getLogger().debug("Clear [{0}] value".format(self.locator_datepicker))
            e_date = Driver.wait_element_enable(self.locator_datepicker, timeout)
            e_date.clear()

    def tick(self, is_tick: bool, timeout=5) -> bool:
        if not isinstance(is_tick, bool):
            raise TypeError("the first argument should be in bool type")

        Logger.getLogger().debug("Tick [{0}] be [{1}]".format(self.locator_check, is_tick))
        sleep(0.5)
        ele = Driver.wait_element_visible(self.locator_check, timeout)
        if ele.tag_name != "input":
            raise UnexpectedTagNameException(
                "The locator should point to a 'input' tag in DOM, or is_selected() will always return false"
            )
        if ele.is_selected() != is_tick:
            ele.click()
        return is_tick

    def tick_and_close_memo(self, value: str = None, timeout=10) -> None:
        Logger.getLogger().debug("Tick [{0}] be [{1}]".format(self.locator_check, True))
        ele = Driver.wait_element_visible(self.locator_check, timeout)
        ele.click()
        try:
            # TODO define POP_DIALOG_OK
            Logger.getLogger().debug("Click button [OK] on Memo")
            Driver.wait_element_enable((By.XPATH, "//button[@ng-click='ok()']"), timeout / 4).click()
            Driver.wait_element_invisible((By.XPATH, "//button[@ng-click='ok()']"), timeout / 4)
            if value != None:
                self.input(value)
        except:
            Logger.getLogger().warning("Click button [OK] failed")

        sleep(2)
        e_date = Driver.wait_element_enable(self.locator_datepicker, timeout)
        e_date_value = e_date.get_attribute("value")
        return (True, e_date_value if e_date_value != None else e_date.text)
