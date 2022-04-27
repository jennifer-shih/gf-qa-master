from behave.model import Table

import src.pages as Pages
from config import globalparameter as gl
from src.drivers.driver import Driver
from src.exception.exception import GfqaException
from src.helper.executor import trnas_ele_cmd
from src.helper.script import input_dynamic_datas
from src.helper.transfer import trans_data_to_value, transfer_data


def create_tp(action_table: Table, exist_ok: bool = True) -> bool:
    """
    建立 tp (目前只有做Trade Partner Information的部分)
    如果num_of_tp > 1 (要建立多個tp)，tp name 加上 '_{index}'
    """
    for r in action_table:
        if r["field"] == "Name":
            tp_name = r["data"]
            break
    is_tp_existd = is_tp_existed(tp_name)

    if not exist_ok and is_tp_existd:
        raise GfqaException(f"TP [{tp_name}] is existed.")

    elif exist_ok and is_tp_existd:
        Pages.TradePartnerListPage.searchResult(1).name_link.click()
        Pages.Common.spin_bar.gone()

        for row in action_table:
            element = trnas_ele_cmd(
                row["field"],
                row["attribute"],
                page_class_name="Pages.NewTradePartnerPage",
            )
            value = element.get_value()
            exp_value = trans_data_to_value(transfer_data(row["data"]), row["attribute"], get_value=value)
            assert value == exp_value, "Wrong Trade Partner Info"
    else:
        Driver.open(gl.URL.NEW_TRADE_PARTNER)
        vm = input_dynamic_datas(action_table, "Pages.NewTradePartnerPage")
        Pages.Common.save_button.click()
        has_similar_name_alert = Pages.NewTradePartnerPage.similar_trade_partner_name_existed_label.is_visible()
        if has_similar_name_alert:
            Pages.NewTradePartnerPage.ok_button.click()
        Pages.Common.spin_bar.gone()
        Driver.refresh()
        Pages.Common.spin_bar.gone()
        vm.verify()


def is_tp_existed(tp_name: str) -> bool:
    Driver.open(gl.URL.TRADE_PARTNER_LIST)
    Pages.TradePartnerListPage.filter_button.click()
    Pages.TradePartnerListPage.Filter.keyword_input.input(tp_name)
    Pages.TradePartnerListPage.Filter.apply_filters_button.click()
    Pages.Common.spin_bar.gone()
    has_result = Pages.TradePartnerListPage.searchResult(1).name_link.is_visible()
    return has_result
