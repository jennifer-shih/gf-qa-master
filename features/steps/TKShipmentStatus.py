from time import sleep

from behave import Then, When

import src.pages as Pages


@When("the user click 'Status' tab of Truck")
def step_impl(context):
    Pages.TKTab.status_tab.click()
    Pages.Common.spin_bar.gone()
    sleep(3)


@Then("OP in TK Status is '{name}'")
def step_impl(context, name):
    op_name = Pages.TKStatusTab.MBL.op_select.get_value()
    assert op_name == name, "OP should be [{0}], but get [{1}]".format(name, op_name)


@Then("SALES in TK Status is '{name}'")
def step_impl(context, name):
    sales_name = Pages.TKStatusTab.MBL.sales_autocomplete.get_value()
    assert sales_name == name, "SALES should be [{0}], but get [{1}]".format(name, sales_name)
