from typing import NoReturn

from selenium.common.exceptions import ElementNotInteractableException

from src.drivers.driver import Driver
from src.helper.log import Logger


class Element:
    __name = "Element"

    def __init__(self, locator: tuple):
        self.locator = locator

    def click(self, timeout=5) -> NoReturn:
        Logger.getLogger().error("[{0}] cannot click".format(self.__name))
        raise Exception("[{0}] cannot click".format(self.__name))

    def input(self, val, timeout=5) -> NoReturn:
        Logger.getLogger().error("[{0}] cannot input value".format(self.__name))
        raise Exception("[{0}] cannot input value".format(self.__name))

    def hover(self, timeout=5) -> None:
        Logger.getLogger().debug("Hover [{0}]".format(self.locator))
        ele = Driver.wait_element_enable(self.locator, timeout)
        Driver.move_mouse_to(ele)

    def get_value(self, timeout=5) -> str:
        return self._get_val(timeout=timeout)

    def get_position(self, timeout=5) -> tuple:
        ele = Driver.wait_element_visible(self.locator, timeout)
        return ele.location

    def get_attribute(self, name, timeout=5) -> str:
        return self._get_attribute(name, timeout)

    def is_visible(self, timeout=5) -> bool:
        """
        the element is in DOM (don't care about the area)
        """
        result = Driver.wait_element_visible(self.locator, timeout) != None
        Logger.getLogger().debug("locator [{0}] is visible? [{1}]".format(self.locator, result))
        return result

    def is_invisible(self, timeout=5) -> bool:
        """
        the element is not in DOM or has no area
        """
        result = Driver.wait_element_invisible(self.locator, timeout) != None
        Logger.getLogger().debug("locator [{0}] is invisible? [{1}]".format(self.locator, result))
        return result

    def is_enable(self, timeout=5) -> bool:
        result = Driver.wait_element_enable(self.locator, timeout) != None
        Logger.getLogger().debug("locator [{0}] is enable? [{1}]".format(self.locator, result))
        return result

    #! Deprecated
    def is_disable(self, timeout=1) -> bool:
        try:
            Logger.getLogger().warning("is_disable() is replaced by is_disabled()".format(self.locator, result))
            result = Driver.wait_element_enable(self.locator, timeout) == None
            Logger.getLogger().debug("locator [{0}] is disable? [{1}]".format(self.locator, result))
            return result
        except:
            return True

    def is_disabled(self, timeout=5) -> bool:
        """
        the element is in DOM, and it has a "disabled" attribute
        """
        assert Driver.wait_element_exist(self.locator, timeout), f"locator [{self.locator}] does not exist in DOM"

        result = Driver.wait_element_disabled(self.locator, timeout) != None
        Logger.getLogger().debug(f"locator [{self.locator}] is disable? [{result}]")
        return result

    def is_interactable(self, timeout=5) -> bool:
        """
        Return true if the element "Exists on the DOM" and "Has position"(can move the cursor to)

        This function is usually been used to test if the element is in a folded area or not
        """
        try:
            element = Driver.wait_element_visible(self.locator, timeout)
            Driver.move_mouse_to(element)
            return True
        except (ElementNotInteractableException, AttributeError):
            return False

    # TODO disabled 有可能是 tag 裡面有 disabled 或 readonly (Shipment Entry File no.) 的 attribute，兩者應該合在一起
    # def is_readonly(self, timeout=5) -> bool:
    #     try:
    #         is_readonly = self._get_attribute("readonly")
    #         Logger.getLogger().debug("locator [{0}] is readonly? [{1}]".format(self.locator, is_readonly))
    #         return is_readonly == "true"
    #     except:
    #         return False

    # def is_equal(self, data, timeout=5):
    #     value = self.get_value(timeout)
    #     value = str(value).strip().upper()

    # protected function -- please do implement in subclass
    def _get_val(self, timeout=5) -> str:
        try:
            element = Driver.wait_element_visible(self.locator, timeout)
            element_value = element.get_attribute("value")
            return element_value if element_value != None else element.text
        except:
            return None

    def _get_attribute(self, attr: str, timeout=5) -> str:
        # return string
        try:
            element = Driver.wait_element_visible(self.locator, timeout)
            return element.get_attribute(attr)
        except:
            return None
