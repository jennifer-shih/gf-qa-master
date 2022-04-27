from time import sleep

from src.drivers.driver import Driver
from src.elements.element import Element
from src.helper.log import Logger


class SpinBar(Element):
    __name = "SpinBar"

    def __init__(self, locator: tuple):
        super(SpinBar, self).__init__(locator)

    def gone(self, timeout=5) -> None:
        Logger.getLogger().debug("Wait Spin Bar gone")
        ele = Driver.wait_element_exist(self.locator, timeout=5)

        if ele != None:
            Driver.wait_element_invisible(self.locator, timeout=timeout)
        else:
            Logger.getLogger().warning("Not detect Spin Bar, wait for 2 sec.")
            sleep(2)
