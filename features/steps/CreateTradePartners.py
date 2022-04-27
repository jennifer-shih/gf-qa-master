from copy import deepcopy
from time import sleep
from urllib.parse import urljoin

from behave import *
from behave.model import Table

import src.pages as Pages  # noqa
from config import globalparameter as gl
from src.drivers.driver import Driver
from src.helper.executor import exec_act_cmd
from src.helper.log import Logger
from src.helper.transfer import *
from src.step_impl import impl_tp


@When("the user input the trade partner profile")
def step_impl(context):
    # If there is a column named 'data' in context.table, take it as input data.
    # If not, take context.active_outline.cells as input data.
    if "data" in context.table.headings:
        datas = []
        for row in context.table:
            datas.append(row["data"])
    else:
        datas = context.active_outline.cells

    trade_partner_profile = {}
    context.trade_partner_field_table = context.table

    for row in context.table:
        data = datas.pop(0)
        Logger.getLogger().debug("[{0}]: {1}".format(row["field"], data))

        exec_act_cmd(row["field"], row["attribute"], row["action"], [data], page="Pages.NewTradePartnerPage")
        answer = exec_act_cmd(row["field"], row["attribute"], "get_value", page="Pages.NewTradePartnerPage")

        trade_partner_profile[row["field"]] = answer
        Logger.getLogger().info("Save [{0}]:{1} to data table".format(row["field"], answer))

    trade_partner_profile["Code"] = Pages.NewTradePartnerPage.code_input.get_value()
    context._vp.add_v(v_name="trade_partner_profile", value=trade_partner_profile)


@When("the user input the trade partner profile in Enterprise Version")
def step_impl(context):
    datas = context.active_outline.cells
    trade_partner_profile = {}
    context.trade_partner_field_table = context.table

    for row in context.table:
        data = datas.pop(0)
        Logger.getLogger().debug("[{0}]: {1}".format(row["field"], data))

        exec_act_cmd(row["field"], row["attribute"], row["action"], [data], page="Pages.NewTradePartnerPage")
        answer = exec_act_cmd(row["field"], row["attribute"], "get_value", page="Pages.NewTradePartnerPage")

        trade_partner_profile[row["field"]] = answer

    context._vp.add_v(v_name="trade_partner_profile", value=trade_partner_profile)


@When("verify similar 'Trade Partner' popup message if occurs")
def step_impl(context):
    if Pages.NewTradePartnerPage.notification_popup_msg.is_visible(timeout=1):  # show notification
        msg = Pages.NewTradePartnerPage.notification_popup_msg.get_value()
        assert "Similar trade partner name already exists" in msg, "Popup message: {msg}"
        assert "Are you sure you still want to create?" in msg, "Popup message: {msg}"
        Pages.NewTradePartnerPage.notification_popup_ok_button.click()

        # 之後希望可以改成以下
        # if "Trade partner alias already exists" in msg or \
        # "Similar trade partner name already exists" in msg or \
        # "Trade partner print name already exists" in msg:
        #     Pages.NewTradePartnerPage.notification_popup_cancel_button.click()


@When("the user add 'Contact Person Information' and save it")
def step_impl(context):
    datas = context.active_outline.cells
    context.cpi_field_table = context.table
    trade_partner_profile = context._vp.get("trade_partner_profile")
    if Pages.NewTradePartnerPage.cpi_expand_button.is_visible(timeout=1):
        Pages.NewTradePartnerPage.cpi_expand_button.click()
        # 點開後button會變成cpi_collapse_button
    Pages.NewTradePartnerPage.cpi_add_button.click()
    for row in context.table:
        data = datas.pop(0)
        Logger.getLogger().debug("[{0}]: {1}".format(row["field"], data))
        exec_act_cmd(row["field"], row["attribute"], row["action"], [data], page="Pages.NewTradePartnerPage")
        answer = exec_act_cmd(row["field"], row["attribute"], "get_value", page="Pages.NewTradePartnerPage")

        trade_partner_profile[row["field"]] = answer

    context.execute_steps(
        """
        When the user click save button
        And verify similar 'Trade Partner' popup message if occurs
        Then the data is saved successfully
    """
    )
    trade_partner_profile["Code"] = Pages.NewTradePartnerPage.code_input.get_value()
    context._vp.add_v(v_name="trade_partner_profile", value=trade_partner_profile)


@When("the user add 'Memo'")
def step_impl(context):
    datas = context.active_outline.cells
    # 判斷memo expand button 是否存在，存在表示還未展開 memo block
    if Pages.NewTradePartnerPage.memo_expand_button.is_visible(timeout=1):
        Pages.NewTradePartnerPage.memo_expand_button.click()
    Pages.NewTradePartnerPage.memo_add_button.click()
    sleep(2)
    for row in context.table:
        data = datas.pop(0)
        Logger.getLogger().debug("[{0}]: {1}".format(row["field"], data))
        exec_act_cmd(row["field"], row["attribute"], row["action"], [data], page="Pages.NewTradePartnerPage")

    Pages.NewTradePartnerPage.memo_save_button.click()
    Pages.Common.spin_bar.gone()


@Then("the trade partner will be created")
def step_impl(context):
    trade_partner_profile = context._vp.get("trade_partner_profile")
    failed_case = []  # 暫存錯誤欄位，避免一格欄位錯誤剩餘的都無法檢查到
    # go to the shipment which just created
    shipment_url = urljoin(
        gl.companyConfig[gl.company]["url"],
        "/sales/trade-partner/{0}/".format(trade_partner_profile["Code"]),
    )
    Driver.open(shipment_url)
    Pages.Common.spin_bar.gone()
    sleep(2)
    # verify datas are correct
    for table in [context.trade_partner_field_table, context.cpi_field_table]:
        for row in table:
            value = exec_act_cmd(row["field"], row["attribute"], "get_value", page="Pages.NewTradePartnerPage")
            value = str(value).strip().upper()  # .replace("\n",r"\n")
            expect = trade_partner_profile[row["field"]]
            expect = str(expect).strip().upper()
            Logger.getLogger().info("[{0}]: [{1}]".format(row["field"], value))
            if expect != value:
                failed_case.append("{0}: [{1}] must be [{2}]".format(row["field"], value, expect))

    if len(failed_case) != 0:
        msg = ""
        for case in failed_case:
            msg = msg + "\n" + case
        assert False, msg


@Given("the user has a TP named '{name}' with below info")
def step_impl(context, name):
    impl_tp.create_tp(context.table)


@Given("the user has No.{index_start}~{index_end} TP named '{tp_name_prefix}' with below info")
def step_impl(context, index_start, index_end, tp_name_prefix):
    tp_info_table: Table = context.table
    for i in range(int(index_start), int(index_end) + 1):
        curr_tp_info = deepcopy(tp_info_table)
        tp_name = f"{tp_name_prefix}_{i}"
        tp_name_col = ["Name", "input", "input", tp_name]
        curr_tp_info.add_row(tp_name_col)
        impl_tp.create_tp(curr_tp_info)


@Then("the filter bar {should_or_not} show in 'Trade Partner List' page")
def step_impl(context, should_or_not):
    position = Pages.TradePartnerListPage.Filter.keyword_input.get_position()
    if should_or_not == "should":
        assert position["x"] != 0 and position["y"] != 0, "The filter bar should be visible."
    elif should_or_not == "should Not":
        assert position["x"] == 0 and position["y"] == 0, "The filter bar should NOT be visible."


@Given("the user dismiss 'Local name has moved' popover")
def step_impl(context):
    if Pages.NewTradePartnerPage.LocalNameHasMovedPopover.close_button.is_visible():
        Pages.NewTradePartnerPage.LocalNameHasMovedPopover.never_show_this_again_checkbox.tick(True)
        Pages.NewTradePartnerPage.LocalNameHasMovedPopover.close_button.click()
