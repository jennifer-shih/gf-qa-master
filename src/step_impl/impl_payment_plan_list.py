import re
from copy import deepcopy
from dataclasses import dataclass
from time import sleep

import pandas as pd
from behave.model import Table
from parse import parse
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By

import config.globalparameter as gl
import src.pages as Pages
from src.drivers.driver import Driver
from src.elements.col_config import ColConfig
from src.elements.element import Element
from src.elements.table_header import TableHeader
from src.helper.executor import exec_act_cmd, trnas_ele_cmd
from src.helper.transfer import transfer_data
from src.models import ColConfigStatus


@dataclass
class IssuedVal:
    """
    value of column 'Issued'
    """

    issued_info: str = ""
    issued_cnt: str = ""
    all_issued_cnt: str = ""


def check_data_loading(func):
    def wrapper(*args, **kwargs):
        timeout = 30
        is_loading = Pages.PaymentPlanListPage.SearchResult.table_loading_label.is_invisible(timeout)
        if is_loading == False:
            raise Exception("Table data is loading over {timeout}sec")
        return func(*args, **kwargs)

    return wrapper


def check_data_loading_done_after_func(func):
    def wrapper(*args, **kwargs):
        timeout = 30
        r = func(*args, **kwargs)
        is_loading = Pages.PaymentPlanListPage.SearchResult.table_loading_label.is_invisible(timeout)
        if is_loading == False:
            raise Exception("Table data is loading over {timeout}sec")
        return r

    return wrapper


def switch_col_config(config_statuses: list[ColConfigStatus]) -> None:
    """
    switch on/off column configs
    """
    for config in config_statuses:
        col_name = config.name
        switch = config.status
        if switch == None:  # Don't mind switch is on or off
            continue
        attr = "col config"
        page = "Pages.PaymentPlanListPage.ColConfigModal"
        config_ele: ColConfig = trnas_ele_cmd(col_name, attr, page)
        config_ele.tick(switch)


def trans_col_config_table_to_statuses(switch_table: Table) -> list[ColConfigStatus]:
    """
    tras table to ColConfigStatus
    Table: | column config   | switch |
           | Approval Status | {on}   |
    return: A list of column config status. index of list is the order of configs
    """
    statuses = []
    for row in switch_table:
        col_name = row["column config"]
        switch = transfer_data(row["switch"])
        config_status = ColConfigStatus(col_name, switch)
        statuses.append(config_status)
    return statuses


@check_data_loading
def scroll_to_left_bound() -> None:
    """
    scroll table to left bound
    """
    pre_first_view_col = None
    first_view_col = get_table_visible_bound_cell(by_last=False)
    while pre_first_view_col == None or pre_first_view_col.locator != first_view_col.locator:
        Driver.scroll_left_by_element(first_view_col)
        pre_first_view_col = first_view_col
        first_view_col = get_table_visible_bound_cell(by_last=False)


@check_data_loading
def scroll_to_column(column_name: str, times: int = 10, retry: int = 10, reverse: bool = False) -> None:
    """
    scroll to see the header column (header strategies is not important)
    times: times to click down button
    retry: set the limit to prevent endless loop
    """
    header_ele = trnas_ele_cmd(column_name, "table_header", f"Pages.PaymentPlanListPage.Header()")
    while header_ele.is_invisible(0.5) and retry > 0:
        if reverse:
            Driver.scroll_left_by_element(Pages.PaymentPlanListPage.SearchResult.table_element, times)
        else:
            Driver.scroll_right_by_element(Pages.PaymentPlanListPage.SearchResult.table_element, times)
        retry -= 1


@check_data_loading
def scroll_to_row(row_index: int, times: int = 10, retry: int = 15) -> None:
    """
    scroll down the table until the row appear
    times: times to click down button
    retry: set the limit to prevent endless loop
    """
    row_ele = Pages.PaymentPlanListPage.SearchResult(row_index).row_element
    while not row_ele.is_visible(0.5) and retry > 0:
        Driver.scroll_down_by_element(Pages.PaymentPlanListPage.SearchResult.table_element, times)
        retry -= 1


@check_data_loading_done_after_func
def sort_column(column_name: str, order) -> None:
    """
    scroll to see the header column, and sort by specified order (header strategies is not important)
    """
    header_ele: TableHeader = trnas_ele_cmd(column_name, "table_header", f"Pages.PaymentPlanListPage.Header()")
    scroll_to_column(column_name)
    header_ele.sort(order)


@check_data_loading
def verify_column_config_switch(configs_status: list[ColConfigStatus]) -> None:
    """ """
    page = "Pages.PaymentPlanListPage.ColConfigModal"
    for config in configs_status:
        val = exec_act_cmd(config.name, "col config", "get_value", page=page)
        assert config.status == val, f"Config [{config.name}] should be [{val}]"


@check_data_loading
def verify_headers_show_as_col_config_statuses(configs_status: list[ColConfigStatus]) -> None:
    """
    check columns order, pinning, show on table.
    column_status: key is column name, value is a boolean means the columns is enabled or not.
    """
    Pages.PaymentPlanListPage.SearchResult.table_loading_label.is_invisible(10)
    for config in configs_status:
        pre_last_view_col = None
        last_view_col = get_table_visible_bound_cell()
        while pre_last_view_col == None or pre_last_view_col.locator != last_view_col.locator:
            if config.is_pinned == True:
                page = "Pages.PaymentPlanListPage.Header(strategy=2)"
            elif config.is_pinned == False:
                page = "Pages.PaymentPlanListPage.Header(strategy=1)"
            else:
                page = "Pages.PaymentPlanListPage.Header()"
            is_visible = exec_act_cmd(config.name, "table_header", "is_visible", [0.5], page=page)
            # 期望出現，所以只要一出現就回傳 True
            if config.status == True:
                if is_visible == True:
                    result = True
                    break
                else:
                    result = False
            # 期望不出現，所以只要一出現就回傳 False
            else:
                if is_visible == True:
                    result = False
                    break
                else:
                    result = True
            Driver.scroll_right_by_element(Pages.PaymentPlanListPage.list_table)
            pre_last_view_col = last_view_col
            last_view_col = get_table_visible_bound_cell()
        assert result, "{0}'s visible status should be {1}".format(config.name, config.status)


def verify_excel_col(excel_path: str, col_config_statuses: list[ColConfigStatus]) -> None:
    df = pd.read_excel(str(excel_path))
    excel_cols = df.columns.values.tolist()

    for col_status in col_config_statuses:
        status = col_status.status
        name = col_status.name
        if status == True:
            if "Amount" in name or name == "Balance":  # which is Amount or Payable Amount or Balance
                # find colunms who satisfy '{exp_col}' + '({Currency})'
                # e.g., 'Amount (Payable) (RMB)', 'Balance (USD)'
                r = re.compile(f"^{re.escape(name)} \([A-Z]{{3}}\)$")
                assert any(r.match(col) for col in excel_cols), f"{name} doesn't show up in excel file"
            else:
                assert name in excel_cols, f"{name} doesn't show up in excel file"


@check_data_loading
def verify_table_datas_sorted_order_by_column(column_name: str, order: str) -> None:
    if not order in ["ASC", "DESC"]:
        raise Exception(f"order [{order}] is not valid")

    cnt_row = get_table_len()
    scroll_to_column(column_name)

    for i in range(1, cnt_row):
        current_ele = trnas_ele_cmd(column_name, "label", f"Pages.PaymentPlanListPage.SearchResult({i})")
        next_ele = current_ele = trnas_ele_cmd(column_name, "label", f"Pages.PaymentPlanListPage.SearchResult({i + 1})")
        scroll_to_row(i)
        scroll_to_row(i + 1)

        if column_name in ["Payment Plan No.", "Plan Type", "Party", "Post Date", "Issued by"]:
            curr_val = current_ele.get_value()
            next_val = next_ele.get_value()
        elif column_name == "Issued":
            try:
                curr_val = get_issued_value(i).issued_cnt
                next_val = get_issued_value(i).issued_cnt
            except:
                continue
        elif column_name == "Office":
            curr_dept_name = current_ele.get_value()
            next_dept_name = next_ele.get_value()
            dept_mapping: dict = gl.gofreight_config.department_info[gl.user_info.office]
            curr_val = next_val = 0
            for id, info in dept_mapping.items():
                if curr_dept_name in info["name"]:
                    curr_val = id
                if next_dept_name in info["name"]:
                    next_val = id
        error_msg = f"Compare column [{column_name}], and get [{curr_val}], [{next_val}] .The order of search result should be {order}"
        if order == "ASC":
            assert curr_val <= next_val, error_msg
        elif order == "DESC":
            assert curr_val >= next_val, error_msg


@check_data_loading
def get_col_value(column_name: str, index: int) -> str:
    ele = trnas_ele_cmd(column_name, "label", f"Pages.PaymentPlanListPage.SearchResult({index})")
    if column_name == "Issued":
        return ele.get_attribute("data-original-title", 0.5)
    else:
        return ele.get_value()


@check_data_loading
def get_issued_value(row_index: int) -> IssuedVal:
    """
    parse the issued value and return a object 'IssuedVal'
    """
    result = IssuedVal()
    result.issued_info = Pages.PaymentPlanListPage.SearchResult(row_index).issued_info_label.get_attribute(
        "data-original-title", 0.5
    )
    if result.issued_info:
        parser = parse("{issued} of {all_issued} issued", result.issued_info.strip())
        result.issued_cnt = parser["issued"]
        result.all_issued_cnt = parser["all_issued"]
    return result


def get_all_column_config_status(keep_page: bool = False, exclude_freeze: bool = True) -> list[ColConfigStatus]:
    """
    return: A list of column config status. index of list is the order of configs
    keep_page: True -> 需要在已經開啟 config modal 的狀況下才可以使用這個function(如果取得order後還要在config model做其他操作可以設成True)
    """
    if not keep_page:
        Pages.PaymentPlanListPage.config_button.click()

    Pages.PaymentPlanListPage.ColConfigModal.freeze_column_divider_col_config.is_visible()
    rows = Driver.get_driver().find_elements_by_xpath(Pages.PaymentPlanListPage.ColConfigModal.ENTIRE_CONFIG_XPATH)
    names_list = [r.text for r in rows]
    divider_index = names_list.index("Freeze Column Divider")

    result = []
    configs_without_divider = Driver.get_driver().find_elements_by_xpath(
        Pages.PaymentPlanListPage.ColConfigModal.CONFIG_WITHOUT_DIVIER
    )
    configs_has_checkbox = Driver.get_driver().find_elements_by_xpath(
        Pages.PaymentPlanListPage.ColConfigModal.CONFIG_HAS_CHECKBOX
    )
    configs_with_checkbox = zip(configs_without_divider, configs_has_checkbox)
    index = 0
    for r, checkbox in configs_with_checkbox:
        is_enabled = checkbox.is_selected()
        if index < divider_index:
            is_pinned = True
        else:
            is_pinned = False
        result.append(ColConfigStatus(name=r.text, status=is_enabled, is_pinned=is_pinned))
        index += 1

    if not exclude_freeze:
        result.insert(divider_index, ColConfigStatus(name="Freeze Column Divider", status=None, is_pinned=None))

    if not keep_page:
        Pages.PaymentPlanListPage.ColConfigModal.cancel_button.click()
        sleep(1)
    return result


def get_excel_column_config_status(keep_page: bool = False):
    if not keep_page:
        Pages.PaymentPlanListPage.excel_button.click()
        Pages.PaymentPlanListPage.excel_config_button.click()

    result = []
    configs_without_divider = Driver.get_driver().find_elements_by_xpath(
        Pages.PaymentPlanListPage.ColConfigModal.CONFIG_WITHOUT_DIVIER
    )
    configs_has_checkbox = Driver.get_driver().find_elements_by_xpath(
        Pages.PaymentPlanListPage.ColConfigModal.CONFIG_HAS_CHECKBOX
    )
    configs_with_checkbox = zip(configs_without_divider, configs_has_checkbox)

    for r, checkbox in configs_with_checkbox:
        is_enabled = checkbox.is_selected()
        result.append(ColConfigStatus(name=r.text, status=is_enabled, is_pinned=None))

    if not keep_page:
        Pages.PaymentPlanListPage.ColConfigModal.cancel_button.click()
    return result


def get_pinned_config_status(keep_page: bool = False) -> list[ColConfigStatus]:
    """
    return pinned configs. Index of list is the order of configs
    """
    configs_status = get_all_column_config_status(keep_page=keep_page)
    result = [config for config in configs_status if config.is_pinned == True]
    return result


def get_normal_config_status(keep_page: bool = False) -> list[ColConfigStatus]:
    """
    return normal(unpinned) configs
    """
    configs_status = get_all_column_config_status(keep_page=keep_page)
    result = [config for config in configs_status if config.is_pinned == False]
    return result


def get_enable_config_status(keep_page: bool = False) -> list[ColConfigStatus]:
    """
    return normal(unpinned) configs
    """
    configs_status = get_all_column_config_status(keep_page=keep_page)
    result = [config for config in configs_status if config.status == True]
    return result


def get_config_index(name: str, configs_status: list[ColConfigStatus]) -> int:
    """
    return colunmn index by configs_status. Index of list is the order of configs
    """
    index = 0
    for config in configs_status:
        if config.name == name:
            return index
        index += 1
    raise Exception(f"[name] is not in the config")


@check_data_loading
def get_table_visible_bound_cell(row_index: int = 0, by_last: bool = True) -> Element:
    """
    get table last/first cell in view (for checking scrollbar is reach bottom or not)
    by_last: True-> check last(right) cell; False-> check first(left) cell
    """
    cells_in_row_xpath = (
        f"//hcgridcontainer//div[@role='row'][@row-index='{row_index}']//div[@role='gridcell'][@aria-colindex]"
    )
    view_row_eles = Driver.get_driver().find_elements_by_xpath(cells_in_row_xpath)
    try:
        colcells = [int(ele.get_attribute("aria-colindex")) for ele in view_row_eles]
    except StaleElementReferenceException:
        # Table 還未 loading 結束，重抓一次 (view_row_eles 抓到正準備消失的 element, 導致 element 消失後無法被操作而產生 Error)
        sleep(0.5)
        return get_table_visible_bound_cell(row_index, by_last)

    target_col_index = max(colcells) if by_last else min(colcells)
    return Element(
        (
            By.XPATH,
            f"//hcgridcontainer//div[@role='row'][@row-index='0']//div[@role='gridcell'][@aria-colindex='{target_col_index}']",
        )
    )


@check_data_loading
def get_table_len() -> int:
    """
    return count of rows in list
    """
    pre_max_index = None
    curr_max_index = get_max_row_index_in_DOM()
    while pre_max_index != curr_max_index:
        Driver.scroll_bottom_by_element(Pages.PaymentPlanListPage.SearchResult.table_element)
        sleep(1.5)  # wait for datas loading
        pre_max_index = curr_max_index
        curr_max_index = get_max_row_index_in_DOM()
    cnt_row = curr_max_index + 1
    Driver.scroll_top_by_element(Pages.PaymentPlanListPage.SearchResult.table_element)
    sleep(1.5)
    return cnt_row


def get_tatal_by_showing_desc_label():
    description = Pages.PaymentPlanListPage.SearchResult.showing_dresciption_label.get_value()
    result = re.search("Showing 1 to (\d+) of (\d+) records", description)
    total_result_cnt = result.group(2)
    return total_result_cnt


@check_data_loading
def get_max_row_index_in_DOM() -> int:
    """
    return the max row index which has been loaded in DOM
    """
    ROW_XPATH = "//hcgridcontainer//div[@role='rowgroup']/div[@role='row'][@row-index]"
    bottom_view_row_eles = Driver.get_driver().find_elements_by_xpath(ROW_XPATH)
    try:
        max_row_index = max([int(e.get_attribute("row-index")) for e in bottom_view_row_eles])
    except StaleElementReferenceException:
        # retry
        sleep(0.5)
        return get_max_row_index_in_DOM()
    return max_row_index


@check_data_loading
def get_table_datas() -> list[dict]:
    table = []
    configs = get_enable_config_status()
    len = get_table_len()
    is_reserved = False
    for r_idx in range(1, len + 1):
        row = {}
        scroll_to_row(r_idx)
        for config in configs:
            col = config.name
            scroll_to_column(col, reverse=is_reserved)
            val = get_col_value(col, r_idx)
            row[col] = val

        is_reserved = not is_reserved
        configs = list(reversed(configs))
        table.append(row)
    return table


def map_filter_to_column(filter_field: str) -> dict:
    """
    filter fields map to table columns
    return: {filtered column: value, ...}
    """
    mapping = {
        "Keyword": "keyword field",
        "E-Invoice": "Issued",
        "Latest Status": "Approval Status",
    }
    if filter_field in mapping:
        return mapping[filter_field]
    else:
        return filter_field


def map_web_data_to_excel_data(web_datas: list[dict]) -> list[dict]:
    return_web_datas = deepcopy(web_datas)
    copied_web_datas = deepcopy(web_datas)
    for row_idx, row in enumerate(copied_web_datas):
        for col, val in row.items():
            if col in [
                "Amount",
                "Amount (Receivable)",
                "Amount (Payable)",
                "Paid Amount",
                "Paid Amount (Collected)",
                "Paid Amount (Paid Out)",
                "Balance",
            ]:
                del return_web_datas[row_idx][col]
                results = re.finditer(r"([A-Z]{3})\n([\d\.,]+)", val)
                for pair in results:  # e.g., RMB 0.0
                    currency = pair.group(1)
                    amount = pair.group(2)
                    amount_num = float(amount.replace(",", ""))
                    return_web_datas[row_idx][f"{col} ({currency})"] = amount_num
            elif col == "Issued":
                if val == None:
                    return_web_datas[row_idx][col] = "0 of 0 issued"
    return return_web_datas
