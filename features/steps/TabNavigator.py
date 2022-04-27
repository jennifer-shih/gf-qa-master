from time import sleep

from behave import *

import src.pages as Pages


@When("the user goes to {module_name} Basic Tab")
def step_impl(context, module_name):
    Pages.ShipmentEntryTab.basic_tab.click()
    Pages.Common.spin_bar.gone()
    sleep(3)


@When("the user goes to {module_name} Container Tab")
def step_impl(context, module_name):
    Pages.ShipmentEntryTab.container_tab.click()
    Pages.Common.spin_bar.gone()
    sleep(3)


@When("the user goes to {module_name:S} Accounting Tab")
def step_impl(context, module_name):
    Pages.ShipmentEntryTab.accounting_tab.click()
    Pages.Common.spin_bar.gone()


@When("the user goes to {module_name} Accounting Tab ({mode} Based)")
def step_impl(context, module_name, mode):
    """
    Goes to accounting tab (billing or invoice based)
    Only works when accounting wizard function is on
    """
    Pages.ShipmentEntryTab.accounting_mode_switch_button.click()
    sleep(1)
    if mode == "Billing":
        Pages.ShipmentEntryTab.accounting_billing_based_button.click()
    elif mode == "Invoice":
        Pages.ShipmentEntryTab.accounting_invoice_based_button.click()
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    Pages.Common.spin_bar.gone()
    sleep(3)
