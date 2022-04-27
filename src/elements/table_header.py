from src.drivers.driver import Driver
from src.elements.element import Element
from src.helper.log import Logger


class TableHeader(Element):
    __name = "TableHeader"

    def __init__(self, locator: tuple, is_sortable=False):
        super(TableHeader, self).__init__(locator)
        self.locator = locator
        self.is_sortable = is_sortable

    def _check_sorting_enable(func):
        def wrapper(self, *args, **kwargs):
            if self.is_sortable == False:
                raise Exception("The table header can NOT be sorted")
            func(self, *args, **kwargs)

        return wrapper

    @_check_sorting_enable
    def sort_by_asc(self, timeout=5) -> None:
        ele = Driver.wait_element_visible(self.locator, timeout)
        class_vals = [c for c in self.get_attribute("class", 0.5).split()]
        if "asc" in class_vals:
            Logger.getLogger().info("Current header sorting is [ASC]")
        elif "desc" in class_vals:
            Logger.getLogger().info("Change header sorting by [DESC] to [ASC]")
            ele.click()
        else:
            Logger.getLogger().info("Change header sorting by [NONE] to [ASC]")
            ele.click()

    @_check_sorting_enable
    def sort_by_desc(self, timeout=5) -> None:
        ele = Driver.wait_element_visible(self.locator, timeout)
        class_vals = [c for c in self.get_attribute("class", 0.5).split()]
        if "asc" in class_vals:
            Logger.getLogger().info("Change header sorting by [ASC] to [DESC]")
            ele.click()
        elif "desc" in class_vals:
            Logger.getLogger().info("Current header sorting is [DESC]")
        else:
            Logger.getLogger().info("Change header sorting by [NONE] to [DESC]")
            ele.click()  # None to ASC
            ele.click()  # ASC to DESC

    def sort(self, order: str, timeout=5) -> None:
        if order.upper() == "ASC":
            self.sort_by_asc(timeout)
        elif order.upper() == "DESC":
            self.sort_by_desc(timeout)
        else:
            raise Exception(f"sorted order: [{order}] is Not valid")

    def get_value(self, timeout=5) -> str:
        class_vals = [c for c in self.get_attribute("class", timeout).split()]
        if "asc" in class_vals:
            Logger.getLogger().info("header is sorting by [ASC]")
            return "ASC"
        elif "desc" in class_vals:
            Logger.getLogger().info("header is sorting by [DESC]")
            return "DESC"
        else:
            Logger.getLogger().info("header is sorting by [NONE]")
            return "NONE"
