from selenium.common.exceptions import ElementNotInteractableException

import src.pages as Pages  # noqa
from src.elements.element import Element
from src.exception.exception import ElementTransError, PageElementManipulationError
from src.helper.transfer import get_execute_script, transfer_str_element
from src.pages import *  # noqa


def trnas_ele_cmd(field: str, attr: str, page_class_name: str) -> Element:
    """
    Use field, attr, page_class_name to find the page element
    """
    try:
        element = eval(transfer_str_element(field=field, attribute=attr, page_class_name=page_class_name))
        return element
    except AttributeError:
        raise ElementTransError(field, attr, page_class_name)


def exec_act_cmd(field: str, attr: str, act: str, datas: list = [], page: str = ""):
    """
    Transfer the given argument into a page manipulation command, and then execute it.
    For example:
        exec_act_cmd("MBL No.", "input", "input", ["AAA-64"], page="Pages.TKBasicTab.MBL")
        -> this will execute: Pages.TKBasicTab.MBL.mbl_no_input.input("AAA-64")
    """
    act_cmd = get_execute_script(
        field=field,
        attribute=attr,
        action=act,
        datas=datas,
        page_class_name=page,
    )
    return manip_cmd(act_cmd)


def manip_cmd(cmd: str):
    """
    Try to execute the given python code in string.
    Use try keyword to catch the error if the page element manipulation is failed,
    so that we can know which command failed directly from the allure report.
    """
    try:
        return eval(cmd)
    except (AttributeError, ElementNotInteractableException) as err:
        original_err_msg = err.args[0]
        err_msg = f'Execute script "{ cmd }" failed\n' + f"Original error message: { original_err_msg }"
        raise PageElementManipulationError(err_msg)
