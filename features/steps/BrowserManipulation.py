from behave import Given, When

import src.pages as Pages
from src.drivers.driver import Driver


@Given("the user opens a new browser")
def step_impl(context):
    Driver.restart()
    assert Driver._instance != None, "Page init failed."


@When("the user refresh browser")
def step_impl(context):
    Driver.refresh()


@When("the user switch to main window")
def step_impl(context):
    Driver.switch_to(window_index=0)


@When("the user switch to '{window_name}' window")
def step_impl(context, window_name):
    Driver.switch_to(window_name=window_name)
    Pages.Common.spin_bar.gone(30)


@When("the user closes current tab")
def step_impl(context):
    Driver.close()
    Driver.switch_to()


@When("the user goes back to the previous page")
def step_impl(context):
    Driver.previous()
    Pages.Common.spin_bar.gone()


@When("the user open new tab")
def step_impl(context):
    Driver.open_new_tab()
    Driver.switch_to(window_index=-1)
