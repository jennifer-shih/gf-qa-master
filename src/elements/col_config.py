from src.drivers.driver import Driver
from src.elements.element import Element
from src.helper.log import Logger


class ColConfig(Element):
    __name = "ColConfig"

    def __init__(self, locator: tuple, checked_locator: tuple = None):
        super(ColConfig, self).__init__(locator)
        self.checked_locator = checked_locator

    def get_value(self, timeout=5) -> bool:
        if self.checked_locator == None:
            raise Exception("The column config setting has no checkbox")
        ele = Driver.wait_element_visible(self.checked_locator, timeout)
        return ele.is_selected()

    def get_name(self, timeout=5) -> str:
        """
        return config view text (name)
        """
        ele = Driver.wait_element_visible(self.locator, timeout)
        return ele.text

    def drag_and_drop(self, target: Element, position: int = 0, move_unit: int = 40, timeout=5) -> None:
        """
        1. ele 在 target 上面第一個
        2. ele 在 target 下面第一個
        """
        ele = Driver.wait_element_enable(self.locator, timeout)
        target_ele = Driver.wait_element_enable(target.locator, timeout)
        tar_rect = target_ele.rect
        ele_rect = ele.rect

        if position == 1:  # on
            while tar_rect["y"] - ele_rect["y"] < 0:
                Driver.drag_and_drop_by_offset(ele, (0, -1 * move_unit))
                ele_rect = ele.rect
                tar_rect = target_ele.rect
            while tar_rect["y"] - ele_rect["y"] > move_unit:
                Driver.drag_and_drop_by_offset(ele, (0, move_unit))
                ele_rect = ele.rect
                tar_rect = target_ele.rect
        elif position == 2:  # under
            while ele_rect["y"] - tar_rect["y"] < 0:
                Driver.drag_and_drop_by_offset(ele, (0, move_unit))
                ele_rect = ele.rect
                tar_rect = target_ele.rect
            while ele_rect["y"] - tar_rect["y"] > move_unit:
                Driver.drag_and_drop_by_offset(ele, (0, -1 * move_unit))
                ele_rect = ele.rect
                tar_rect = target_ele.rect
        else:
            raise ValueError(f"No implementaion match position [{position}]")

    def tick(self, is_tick: str, timeout=5) -> None:
        Logger.getLogger().debug("Tick [{0}] be [{1}]".format(self.checked_locator, is_tick))
        ele = Driver.wait_element_visible(self.checked_locator, timeout)
        if ele.is_selected() != bool(int(is_tick)):
            ele.click()
