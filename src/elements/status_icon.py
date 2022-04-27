from src.drivers.driver import Driver
from src.elements.element import Element
from src.helper.log import Logger


class StatusIcon(Element):
    """
    the pin icon for filter in list pages
    """

    __name = "StatusIcon"

    def __init__(self, locator: tuple, status_mapping: dict[str, tuple]):
        super(StatusIcon, self).__init__(locator)
        self.locator = locator
        self.status_mapping = status_mapping

    def click(self, timeout=5):
        Logger.getLogger().debug("Click [{0}]".format(self.locator))
        ele = Driver.wait_element_enable(self.locator, timeout)
        ele.click()

    def get_value(self, timeout=5) -> str:
        Driver.wait_element_visible(self.locator, timeout)
        for status, loc in self.status_mapping.items():
            try:
                Logger.getLogger().info(f"Get the status of [{loc}]")
                if Driver.get_driver().find_element_by_xpath(loc) != None:
                    return status
            except:
                pass
        raise Exception(f"Status is not defined ({[s for s, l in self.status_mapping.items()]})")
