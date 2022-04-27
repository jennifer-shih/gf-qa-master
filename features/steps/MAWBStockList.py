from time import sleep

from behave import Then, When

import src.pages as Pages
from src.drivers.driver import Driver
from src.exception.exception import GfqaException, StepParaNotDefinedError
from src.step_impl import impl_mawb_stock_list


@When("the user ticks 'MAWB Stock'")
def step_impl(context):
    # TODO: fix filed "Reserved"
    mawb_stocks = impl_mawb_stock_list.trans_mawb_stock_table(context.table)
    for stock in mawb_stocks:
        index = impl_mawb_stock_list.get_mawb_stock_index_in_stock_list(stock)
        Pages.MAWBStockListPage.StockList(index).check_checkbox.tick(True)


@When("the user clicks 'Create MAWB' button")
def step_impl(context):
    Pages.MAWBStockListPage.create_mawb_button.click()
    Driver.switch_to("AE - New Shipment")
    sleep(2)


@When("the user clicks 'Reserve' button")
def step_impl(context):
    Pages.MAWBStockListPage.reserve_button.click()
    Pages.Common.spin_bar.gone()


@When("the user clicks 'Unreserve' button")
def step_impl(context):
    Pages.MAWBStockListPage.unreserve_button.click()
    Pages.Common.spin_bar.gone()


@When("the user clicks 'File No.' link in 'MAWB Stock List'")
def step_impl(context):
    mawb_stocks = impl_mawb_stock_list.trans_mawb_stock_table(context.table)
    mawb_stock = mawb_stocks[0]
    index = impl_mawb_stock_list.get_mawb_stock_index_in_stock_list(mawb_stock)
    Pages.MAWBStockListPage.StockList(index).file_no_link.click()
    Pages.Common.spin_bar.gone()


@Then("'MAWB Stock List' should be")
def step_impl(context):
    mawb_stocks = impl_mawb_stock_list.trans_mawb_stock_table(context.table)
    for mawb_stock in mawb_stocks:
        try:
            impl_mawb_stock_list.get_mawb_stock_index_in_stock_list(mawb_stock)
        except GfqaException:
            assert False, "Not found any mawb stock matched"


@Then("'Create MAWB' button is {enabled_or_disabled}")
def step_impl(context, enabled_or_disabled):
    if enabled_or_disabled == "enabled":
        assert Pages.MAWBStockListPage.create_mawb_button.is_enable()
    elif enabled_or_disabled == "disabled":
        assert Pages.MAWBStockListPage.create_mawb_button.is_disable()
    else:
        raise StepParaNotDefinedError(enabled_or_disabled)


@Then("'Reserve' button is {enabled_or_disabled}")
def step_impl(context, enabled_or_disabled):
    if enabled_or_disabled == "enabled":
        assert Pages.MAWBStockListPage.reserve_button.is_enable()
    elif enabled_or_disabled == "disabled":
        assert Pages.MAWBStockListPage.reserve_button.is_disable()
    else:
        raise StepParaNotDefinedError(enabled_or_disabled)


@Then("'Unreserve' button is {enabled_or_disabled}")
def step_impl(context, enabled_or_disabled):
    if enabled_or_disabled == "enabled":
        assert Pages.MAWBStockListPage.unreserve_button.is_enable()
    elif enabled_or_disabled == "disabled":
        assert Pages.MAWBStockListPage.unreserve_button.is_disable()
    else:
        raise StepParaNotDefinedError(enabled_or_disabled)
