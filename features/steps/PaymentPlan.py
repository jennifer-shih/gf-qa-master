import re
from pathlib import Path
from random import choices
from time import sleep

import pandas as pd
from behave import Given, Then, When

import src.pages as Pages
from config import globalparameter as gl
from src.drivers.driver import Driver
from src.exception.exception import StepParaNotDefinedError
from src.helper.downloder import Downloader
from src.helper.executor import exec_act_cmd, trnas_ele_cmd
from src.helper.function import wday
from src.helper.script import input_dynamic_datas
from src.step_impl import impl_payment_plan_list


@Then("'Payment Plan List' page will show")
def step_impl(context):
    Pages.PaymentPlanListPage.SearchResult.table_loading_label.is_visible(3)
    Pages.PaymentPlanListPage.SearchResult.table_loading_label.is_invisible(20)
    assert Pages.PaymentPlanListPage.filter_button.is_visible()
    assert Pages.PaymentPlanListPage.SearchResult.table_element.is_visible()


@Given("there are departments configured for '{feature}' Approver in '{office}' office")
def step_impl(context, feature, office):
    Pages.FeatAndApprovalPage.feature_select.select(feature)
    Pages.FeatAndApprovalPage.office_select.select(office)
    assert Pages.FeatAndApprovalPage.ApprovalList(1).department_select.is_visible(), "No approval exists"


@When("the user switches 'Column Config' in 'Payment Plan List'")
def step_impl(context):
    """
    switch on / of column config
    _vp:
        col_config_statuses: a list of ColConfigStatus which trans by the feature table
    """
    Pages.PaymentPlanListPage.config_button.click()
    sleep(0.5)
    statuses = impl_payment_plan_list.trans_col_config_table_to_statuses(context.table)
    impl_payment_plan_list.switch_col_config(statuses)
    col_config_statuses = impl_payment_plan_list.trans_col_config_table_to_statuses(context.table)
    Pages.PaymentPlanListPage.ColConfigModal.apply_button.click()
    Pages.Common.spin_bar.gone()
    context._vp.add_v("col_config_statuses", col_config_statuses)


@When("the user switches 'Excel Column Config' and {next_step} in 'Payment Plan List'")
def step_impl(context, next_step):
    Pages.PaymentPlanListPage.excel_button.click()
    Pages.PaymentPlanListPage.excel_config_button.click()
    sleep(0.5)
    statuses = impl_payment_plan_list.trans_col_config_table_to_statuses(context.table)
    impl_payment_plan_list.switch_col_config(statuses)
    col_config_statuses = impl_payment_plan_list.trans_col_config_table_to_statuses(context.table)
    if next_step == "download excel":
        Pages.PaymentPlanListPage.ColConfigModal.save_n_download_button.click()
    elif next_step == "save":
        Pages.PaymentPlanListPage.ColConfigModal.save_button.click()
    else:
        raise StepParaNotDefinedError(next_step)

    Pages.Common.spin_bar.gone()
    context._vp.add_v("excel_col_config_statuses", col_config_statuses)


@Then("there is Check All checkbox in 'Payment Plan List'")
def step_impl(context):
    Driver.refresh()
    assert (
        Pages.PaymentPlanListPage.Header().check_all_checkbox.is_visible()
    ), "Check All 's visible status should be visible"


@Then("the table column should be the same as above setting in 'Payment Plan List'")
def step_impl(context):
    """
    check table column is match above settings
    """
    Driver.refresh()
    statuses = context._vp.get("col_config_statuses")
    impl_payment_plan_list.verify_headers_show_as_col_config_statuses(statuses)


@Then("the table columns should be the same as 'Column Config' in 'Payment Plan List'")
def step_impl(context):
    """
    check table column
    """
    Driver.refresh()
    pinned_columns = impl_payment_plan_list.get_pinned_config_status()
    normals_columns = impl_payment_plan_list.get_normal_config_status()
    impl_payment_plan_list.verify_headers_show_as_col_config_statuses(pinned_columns)
    impl_payment_plan_list.verify_headers_show_as_col_config_statuses(normals_columns)


@When("the user order column '{column_name}' by {order} order in 'Payment Plan List'")
def step_impl(context, column_name, order):
    impl_payment_plan_list.sort_column(column_name, order)
    Pages.Common.spin_bar.gone()


@When("column {index} of '{column_name}' is '{nickname}'")
def step_impl(context, index, column_name, nickname):
    sleep(2)
    if column_name == "Issued":
        val = impl_payment_plan_list.get_issued_value(index)
    else:
        val = exec_act_cmd(column_name, "label", "get_value", page=f"Pages.PaymentPlanListPage.SearchResult({index})")
    context._vp.add_v(v_name=nickname, value=val)


@Then("column '{column_name}' should be sorted by {order} in 'Payment Plan List'")
def step_impl(context, column_name, order):
    Driver.refresh()
    impl_payment_plan_list.scroll_to_column(column_name)
    impl_payment_plan_list.verify_table_datas_sorted_order_by_column(column_name, order)


@When("the user put '{moving_col}' {on_or_under} '{target_col}' in table column config in 'Payment Plan List'")
def step_impl(context, moving_col, on_or_under, target_col):
    Pages.PaymentPlanListPage.config_button.click()
    sleep(0.5)
    moving_ele = trnas_ele_cmd(moving_col, "col_config", page_class_name="Pages.PaymentPlanListPage.ColConfigModal")
    target_ele = trnas_ele_cmd(target_col, "col_config", page_class_name="Pages.PaymentPlanListPage.ColConfigModal")
    if on_or_under == "on":
        pos = 1
    elif on_or_under == "under":
        pos = 2

    moving_ele.drag_and_drop(target_ele, position=pos)
    Pages.PaymentPlanListPage.ColConfigModal.apply_button.click()


@Then("'{config_1}' is {on_or_under} '{config_2}' in table column config in 'Payment Plan List'")
def step_impl(context, config_1, on_or_under, config_2):
    config_statuses = impl_payment_plan_list.get_all_column_config_status(exclude_freeze=False)
    config_1_idx = None
    config_2_idx = None
    for idx, config_status in enumerate(config_statuses):
        if config_status.name == config_1:
            config_1_idx = idx
        if config_status.name == config_2:
            config_2_idx = idx

    if on_or_under == "on":
        assert config_2_idx - 1 == config_1_idx, ""
    elif on_or_under == "under":
        assert config_2_idx + 1 == config_1_idx, ""
    else:
        raise StepParaNotDefinedError(on_or_under)


@Then("the position of columns should match config in 'Payment Plan List'")
def step_impl(context):
    enabled_col_list = [
        {
            "fields": [i for i in impl_payment_plan_list.get_pinned_config_status() if i.status == True],
            "page_class_name": "Pages.PaymentPlanListPage.Header(strategy=2)",
        },
        {
            "fields": [i for i in impl_payment_plan_list.get_normal_config_status() if i.status == True],
            "page_class_name": "Pages.PaymentPlanListPage.Header(strategy=1)",
        },
    ]

    for config_info in enabled_col_list:
        field_cnt = len(config_info["fields"])
        for i in range(0, field_cnt - 1):
            left_field_name = config_info["fields"][i].name
            right_field_name = config_info["fields"][i + 1].name
            page_class_name = config_info["page_class_name"]
            left_ele = trnas_ele_cmd(left_field_name, "table_header", page_class_name=page_class_name)
            right_ele = trnas_ele_cmd(right_field_name, "table_header", page_class_name=page_class_name)

            impl_payment_plan_list.scroll_to_column(left_field_name)
            left_ele_x_pos = left_ele.get_position()["x"]
            right_ele_x_pos = right_ele.get_position()["x"]
            assert left_ele_x_pos < right_ele_x_pos, f"{left_field_name} shoud be in the left of {right_field_name}"


@When("the user open and {pin_or_unpined} the filter in 'Payment Plan List' page")
def step_impl(context, pin_or_unpined):
    if pin_or_unpined == "pin":
        pinned = True
    elif pin_or_unpined == "unpin":
        pinned = False
    else:
        raise StepParaNotDefinedError(pin_or_unpined)

    if Pages.PaymentPlanListPage.Filter.apply_filters_button.is_invisible(3):
        Pages.PaymentPlanListPage.filter_button.click()

    if Pages.PaymentPlanListPage.Filter.pin_status_icon.get_value() == "Unpinned":
        if pinned:
            Pages.PaymentPlanListPage.Filter.pin_status_icon.click()
    else:
        if not pinned:
            Pages.PaymentPlanListPage.Filter.pin_status_icon.click()


@Then("the filter bar {should_or_not} show in 'Payment Plan List' page")
def step_impl(context, should_or_not):
    position = Pages.PaymentPlanListPage.Filter.keyword_input.get_position()
    if should_or_not == "should":
        assert position["x"] != 0 and position["y"] != 0, "The filter bar should be visible."
    elif should_or_not == "should NOT":
        assert position["x"] == 0 and position["y"] == 0, "The filter bar should NOT be visible."
    else:
        raise StepParaNotDefinedError(should_or_not)


@When("the user search for the following info in 'Payment Plan List' page")
def step_impl(context):
    if Pages.PaymentPlanListPage.Filter.apply_filters_button.is_invisible(3):
        Pages.PaymentPlanListPage.filter_button.click()

    model = input_dynamic_datas(context.table, "Pages.PaymentPlanListPage.Filter")

    filter_dict = {}
    for row in context.table:
        filtered_col = impl_payment_plan_list.map_filter_to_column(row["field"])
        filter_dict[filtered_col] = row["data"]
    context._vp.add_v("filter", value=filter_dict)
    Pages.PaymentPlanListPage.Filter.apply_filters_button.click()
    Pages.Common.spin_bar.gone()
    model.verify()


@Then("the 'Payment Plan List' excel file should be saved in download folder ({timeout} sec)")
def step_impl(context, timeout):
    excel_name = Path("PaymentPlan_" + wday(0) + ".xlsx")
    excel_path = gl.download_path / excel_name
    rename = "PaymentPlan.xlsx"
    dl = Downloader(excel_path, int(timeout), rename)
    dl.start()


@Then("the columns in 'Payment Plan List Excel' should be the same as above 'Excel Column Config'")
def step_impl(context):
    exp_col_statuses = context._vp.get("excel_col_config_statuses")
    filename = "PaymentPlan.xlsx"
    excel_path = gl.download_path / filename
    impl_payment_plan_list.verify_excel_col(excel_path, exp_col_statuses)


@Then("the columns in 'Payment Plan List' excel should only show 'No'")
def step_impl(context):
    filename = "PaymentPlan.xlsx"
    excel_path = gl.download_path / filename
    df = pd.read_excel(str(excel_path))
    excel_cols = df.columns.values.tolist()
    assert len(excel_cols), "Excel file is not only 1 column: \n {excel_cols}"
    assert "No" in excel_cols, "Excel file has no [No] column"


@When("the user copy 'Column Config' to 'Excel Column Config' in 'Payment Plan List' and download excel")
def step_impl(context):
    Pages.PaymentPlanListPage.excel_button.click()
    Pages.PaymentPlanListPage.excel_config_button.click()
    sleep(0.5)
    Pages.PaymentPlanListPage.ColConfigModal.copy_list_view_settings_button.click()
    Pages.PaymentPlanListPage.ColConfigModal.save_n_download_button.click()
    statuses = context._vp.get("col_config_statuses").copy()
    context._vp.add_v("excel_col_config_statuses", statuses)


@When("the user randomly enables {cnt} 'Excel Column Config' in 'Payment Plan List'")
def step_impl(context, cnt):
    all_config_statuses = impl_payment_plan_list.get_all_column_config_status()
    cnt = int(cnt)
    chosen_config_names = [c.name for c in choices(all_config_statuses, k=cnt)]
    for config_status in all_config_statuses:
        if config_status.name in chosen_config_names:
            config_status.status = True
        else:
            config_status.status = False

    Pages.PaymentPlanListPage.excel_button.click()
    Pages.PaymentPlanListPage.excel_config_button.click()
    sleep(0.5)
    impl_payment_plan_list.switch_col_config(all_config_statuses)
    Pages.PaymentPlanListPage.ColConfigModal.save_button.click()
    Pages.Common.spin_bar.gone()
    context._vp.add_v("excel_col_config_statuses", all_config_statuses)


@When("the user download 'Payment Plan List' excel file")
def step_impl(context):
    Pages.PaymentPlanListPage.excel_button.click()
    Pages.PaymentPlanListPage.excel_download_button.click()


@Then("the 'Excel Column Config' match above settings in 'Payment Plan List'")
def step_impl(context):
    config_statuses = context._vp.get("excel_col_config_statuses")
    Pages.PaymentPlanListPage.excel_button.click()
    Pages.PaymentPlanListPage.excel_config_button.click()
    sleep(0.5)
    impl_payment_plan_list.verify_column_config_switch(config_statuses)
    Pages.PaymentPlanListPage.ColConfigModal.cancel_button.click()


@Then("the values in 'Payment Plan List' excel should be the same as those in webpage")
def step_impl(context):
    web_datas = impl_payment_plan_list.get_table_datas()
    filename = "PaymentPlan.xlsx"
    excel_path = gl.download_path / filename
    df = pd.read_excel(str(excel_path)).fillna("")

    web_datas = impl_payment_plan_list.map_web_data_to_excel_data(web_datas)

    for idx, row in enumerate(web_datas):
        for col_name, val in row.items():
            excel_val = df.loc[idx, col_name]
            assert (
                val == excel_val
            ), f"Row [{idx}] on Web {col_name}:[{val}] should equals to Excel {col_name}:[{excel_val}]"


@When("the user set record quantity for 1 page to {page_offset} in 'Payment Plan List'")
def step_impl(context, page_offset):
    # save the page description for checking
    description = Pages.PaymentPlanListPage.SearchResult.showing_dresciption_label.get_value()
    result = re.search("Showing 1 to (\d+) of (\d+) records", description)
    total_result_cnt = result.group(2)
    context._vp.add_v("total_result_cnt", value=total_result_cnt)

    Pages.PaymentPlanListPage.page_offset_select.select(page_offset)
    Pages.Common.spin_bar.gone()

    # To avoid scroll bar appear in the other position rather than top
    Driver.refresh()
    Pages.Common.spin_bar.gone()


@Then("{page_offset} record shows in table and page description is correctly in 'Payment Plan List' ({timeout} sec)")
def step_impl(context, page_offset, timeout):
    page_offset = int(page_offset)
    # if loading, the hcgridcontainer will get a 'grid-loading-detail' classname
    # and all content div will only have a div as child element,
    # so there's no need to check all conten divs
    assert Pages.PaymentPlanListPage.SearchResult.table_loading_label.is_invisible(
        timeout=int(timeout)
    ), "Records still loading"

    table_len = impl_payment_plan_list.get_table_len()
    assert page_offset == table_len, f"Expect table len is [{page_offset}], but get [{table_len}]"

    # checking the {total_result_cnt} in description is still the same
    total_result_cnt = context._vp.get("total_result_cnt")
    exp_description = "Showing 1 to {} of {} records".format(page_offset, total_result_cnt)
    description = Pages.PaymentPlanListPage.SearchResult.showing_dresciption_label.get_value()
    assert exp_description == description, "Expect description of result to be [{0}], but get [{1}]".format(
        exp_description, description
    )


@When("the user go to entry view of payment plan ({index})")
def step_impl(context, index):
    Pages.PaymentPlanListPage.SearchResult(index).payment_plan_no_link.click()
    Pages.Common.spin_bar.gone()


@When("the user click payment plan ({index})")
def step_impl(context, index):
    Pages.PaymentPlanListPage.SearchResult(index).checkbox_checkbox.tick(True)


@Then("the user {can_or_cannot} see the entry view of payment plan")
def step_impl(context, can_or_cannot):
    if can_or_cannot == "can":
        assert Pages.PaymentPlanPage.payment_plan_no_input.is_visible(), "Entry view of payment plan should be visible"
    elif can_or_cannot == "can NOT":
        assert Driver.is_text_in_page_source(
            "Forbidden: Access Denied."
        ), "Entry view of payment plan should be forbidden"


@Then("the user {can_or_cannot} see the 'Delete' button in 'Payment Plan List'")
def step_impl(context, can_or_cannot):
    if can_or_cannot == "can":
        assert Pages.PaymentPlanListPage.delete_button.is_visible(), "Delete button should be visible"
    elif can_or_cannot == "can NOT":
        assert Pages.PaymentPlanListPage.delete_button.is_invisible(), "Delete button should be invisible"


@Then("the user {can_or_cannot} see the 'Make / Receive Paymen' button in 'Payment Plan List'")
def step_impl(context, can_or_cannot):
    if can_or_cannot == "can":
        assert (
            Pages.PaymentPlanListPage.make_receive_payment_button.is_visible()
        ), "Make / Receive Paymen button should be visible"
    elif can_or_cannot == "can NOT":
        assert (
            Pages.PaymentPlanListPage.make_receive_payment_button.is_invisible()
        ), "Make / Receive Paymen button should be invisible"


@Then("the user {can_or_cannot} see the 'Excel' button in 'Payment Plan List'")
def step_impl(context, can_or_cannot):
    if can_or_cannot == "can":
        assert Pages.PaymentPlanListPage.excel_button.is_visible(), "Excel button should be visible"
    elif can_or_cannot == "can NOT":
        assert Pages.PaymentPlanListPage.excel_button.is_invisible(), "Excel button should be invisible"
    else:
        raise StepParaNotDefinedError(can_or_cannot)
