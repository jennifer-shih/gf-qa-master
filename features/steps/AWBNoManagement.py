from time import sleep

from behave import Then, When

import src.pages as Pages
from config import globalparameter as gl
from src.drivers.driver import Driver
from src.step_impl import impl_awb_no_mng


@When("the user click AWB No.({index}) 'Carrier' trade partner hyperlink button in 'AWB No. Management'")
def step_impl(context, index):
    Pages.AWBNoMngPage.AWBRanges(index).carrier_autocomplete.click_hyper_link()
    Driver.switch_to(window_index=1)
    Pages.Common.spin_bar.gone()


@Then("trade partner '{tp}' page show")
def step_impl(context, tp):
    name = Pages.NewTradePartnerPage.name_input.get_value()
    assert tp == name, "Expect name to be [{0}], but get [{1}]".format(tp, name)
    Driver.close()
    Driver.switch_to(window_index=0)


@When("the user clear AWB No.({index}) 'Carrier' trade partner in 'AWB No. Management'")
def step_impl(context, index):
    Pages.AWBNoMngPage.AWBRanges(index).carrier_autocomplete.clear()


@Then("the AWB No.({index}) 'Carrier' field is empty in 'AWB No. Management'")
def step_impl(context, index):
    name = Pages.AWBNoMngPage.AWBRanges(index).carrier_autocomplete.get_value()
    assert "" == name, "Expect name to be empty, but get [{0}]".format(name)


@When("the user click 'add' button in 'AWB No. Management' AWB No.({index}) 'Carrier' trade partner field")
def step_impl(context, index):
    Pages.AWBNoMngPage.AWBRanges(index).carrier_autocomplete.click_add()
    Driver.switch_to(window_index=1)
    Pages.Common.spin_bar.gone()


@Then("new trade partner page show")
def step_impl(context):
    assert Driver.is_url_match(gl.URL.NEW_TRADE_PARTNER), "url doens't match"
    assert Pages.NewTradePartnerPage.tp_type_select.is_visible(), "Page now showing normally"
    Driver.close()
    Driver.switch_to(window_index=0)
    Driver.refresh()


@When("the user add AWB No. range in 'AWB No. Management'")
def step_impl(context):
    awb_no_ranges = impl_awb_no_mng.add_awb_no_range(context.table)
    context._vp.add_v("awb_no_ranges", awb_no_ranges)


@When("the user edits AWB No. range({carrier})")
def step_impl(context, carrier):
    awb_no_ranges = [impl_awb_no_mng.edit_awb_no_range(context.table[0], carrier)]
    context._vp.add_v("awb_no_ranges", awb_no_ranges)


@Then("'AWB No. range' should be saved correctly")
def step_impl(context):
    Driver.refresh()
    for awb_no_range_model in context._vp.get("awb_no_ranges"):
        awb_no_range_model.verify()


@Then("the MAWB No field will show 'Invalid Format' warning")
def step_impl(context):
    Pages.AEBasicTab.MAWB.mawb_no_invalid_mark_button.hover()
    message = Pages.AEBasicTab.MAWB.mawb_no_invalid_message_label.get_value()
    assert message == "Invalid format (number of digits)"


@When("the user clear 'MAWB No.' in 'Air Export' shipment '{name}'")
def step_impl(context, name):
    Pages.AEBasicTab.MAWB.mawb_no_input.clear()
    model = context._vp.get("mawb_model")[name]
    if model.has_key("MAWB No."):
        model.pop("MAWB No.")
    model.add(
        field="MAWB No.",
        attribute="input",
        data=Pages.AEBasicTab.MAWB.mawb_no_input.get_value(),
    )
    context._vp.add_dict(dict_name="mawb_model", value={name: model})


@Then("the user {can_or_cannot} see 'MAWB Stock List' on the navigator")
def step_impl(context, can_or_cannot):
    if can_or_cannot == "can":
        assert Pages.NavigatorBar.air_export_mawb_stock_list.is_visible(), "MAWB Stock List should be visible"
    elif can_or_cannot == "can NOT":
        assert Pages.NavigatorBar.settings_awb_no_management.is_invisible(), "MAWB Stock List should be invisible"


@Then("the user {can_or_cannot} see 'AWB No. Management' on the navigator")
def step_impl(context, can_or_cannot):
    if can_or_cannot == "can":
        assert Pages.NavigatorBar.settings_awb_no_management.is_visible(), "AWB No. Management should be visible"
    elif can_or_cannot == "can NOT":
        assert Pages.NavigatorBar.settings_awb_no_management.is_invisible(), "AWB No. Management should be invisible"


@Then("the checkbox and remark field for stock({index}) in 'MAWB Stock List' is '{enable_or_disable}'")
def step_impl(context, index, enable_or_disable):
    if enable_or_disable == "Enable":
        assert Pages.MAWBStockListPage.StockList(index).check_checkbox.is_enable(), "Checkbox should be enable"
        assert Pages.MAWBStockListPage.StockList(index).remark_input.is_enable(), "Remark should be enable"
    elif enable_or_disable == "Disable":
        assert Pages.MAWBStockListPage.StockList(index).check_checkbox.is_disabled(), "Checkbox should be disable"
        assert Pages.MAWBStockListPage.StockList(index).remark_input.is_disabled(), "Remark should be disable"


@Then("the user {can_or_cannot} see 'MAWB Stock List' page")
def step_impl(context, can_or_cannot):
    if can_or_cannot == "can":
        assert Pages.MAWBStockListPage.title_label.is_visible(10)
        assert Pages.MAWBStockListPage.reserve_button.is_visible()
        assert Pages.MAWBStockListPage.unreserve_button.is_visible()
        assert Pages.MAWBStockListPage.create_mawb_button.is_visible()
    elif can_or_cannot == "can NOT":
        assert Pages.MAWBStockListPage.title_label.is_invisible()
        assert Pages.MAWBStockListPage.reserve_button.is_invisible()
        assert Pages.MAWBStockListPage.unreserve_button.is_invisible()
        assert Pages.MAWBStockListPage.create_mawb_button.is_invisible()


@Then("the user {can_or_cannot} see 'AWB No. Management' page")
def step_impl(context, can_or_cannot):
    if can_or_cannot == "can":
        assert Pages.AWBNoMngPage.title_label.is_visible(10)
        assert Pages.AWBNoMngPage.new_awb_no_range_button.is_visible()
    elif can_or_cannot == "can NOT":
        assert Pages.AWBNoMngPage.title_label.is_invisible()
        assert Pages.AWBNoMngPage.new_awb_no_range_button.is_invisible()


@Then("the user can NOT edit AWB No in 'AWB No. Management' page")
def step_impl(context):
    assert Pages.Common.save_fail_msg.is_visible(timeout=30)
    Driver.refresh()


@When("the user selects AWB No. range")
def step_impl(context):
    awb_no_range: dict = context.table[0].as_dict()
    index = impl_awb_no_mng.get_awb_no_range_index(awb_no_range)
    Pages.AWBNoMngPage.AWBRanges(index).checked_checkbox.tick(True)


@When("the user clicks delete button on AWB No. Management")
def step_impl(context):
    Pages.AWBNoMngPage.delete_button.click()


@Then("AWB No. range should NOT be existed")
def step_impl(context):
    Driver.refresh()
    awb_no_range: dict = context.table[0].as_dict()
    index = impl_awb_no_mng.get_awb_no_range_index(awb_no_range)
    assert index == None, f"Still find awb no range: {awb_no_range}"


@When("the user clicks 'system generate' button in 'MAWB No.'")
def step_impl(context):
    Pages.AEBasicTab.MAWB.mawb_no_system_generate_button.click()


@When("the user clicks 'system generate' button in 'MAWB No.' and apply pupup dialog")
def step_impl(context):
    Pages.AEBasicTab.MAWB.mawb_no_system_generate_button.click()
    times = 2
    for _ in range(times):
        if Pages.Common.popup_modal_msg_label.is_visible(3):
            Pages.Common.ok_button.click()
            sleep(1)


@Then("AWB No. range({carrier}) should be enabled/disabled")
def step_impl(context, carrier):
    impl_awb_no_mng.verify_col_enable(carrier, context.table[0])


@Then("'AWB No. range' should be")
def step_impl(context):
    for row in context.table:
        awb_no_range: dict = row.as_dict()
        index = impl_awb_no_mng.get_awb_no_range_index(awb_no_range)
        assert index != None, f"AWB No. range not match: {awb_no_range}"
