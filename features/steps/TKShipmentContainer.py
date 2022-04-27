from behave import Then, When

import src.pages as Pages
from src.drivers.driver import Driver
from src.helper.script import input_dynamic_datas


@When("the user click 'Container & Item' tab of Truck")
def step_impl(context):
    Pages.TKTab.container_and_item_tab.click()
    Pages.Common.spin_bar.gone()


@When("the user add a tag '{po_no}' in P.O. No.")
def step_impl(context, po_no):
    Pages.TKContainerTab.MBL.po_no_tag_list.input(po_no)


@When("the user click 'New' button of 'Container List'")
def step_impl(context):
    Pages.TKContainerTab.MBL.add_container_button.click()


@When("the user input datas in container({index})")
def step_impl(context, index):
    page_class_name = f"Pages.TKContainerTab.MBL.container({index})"
    model = input_dynamic_datas(context.table, page_class_name)
    context._vp.add_dict(dict_name="tk_container_verify_model", value={index: model})


@Then("container({index}) should be saved without any errors")
def step_impl(context, index):
    Driver.refresh()
    Pages.Common.spin_bar.gone()

    verify_model = context._vp.get("tk_container_verify_model")[index]
    verify_model.verify()


@When("the user click 'New' button of 'Commodity'")
def step_impl(context):
    Pages.TKContainerTab.MBL.add_commodity_button.click()


@When("the user input data in commodity({index})")
def step_impl(context, index):
    page_class_name = f"Pages.TKContainerTab.MBL.commodity({index})"
    model = input_dynamic_datas(context.table, page_class_name)
    context._vp.add_dict(dict_name="tk_commodity_verify_model", value={index: model})


@Then("commodity({index}) should be saved without any errors")
def step_impl(context, index):
    Driver.refresh()
    Pages.Common.spin_bar.gone()

    verify_model = context._vp.get("tk_commodity_verify_model")[index]
    verify_model.verify()
