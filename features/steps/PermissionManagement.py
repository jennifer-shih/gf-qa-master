from time import sleep

from behave import *

import src.pages as Pages


@When("the user clicks '{filter_name}' filter in Permission Management page")
def step_impl(context, filter_name):
    if filter_name == "Invoice":
        Pages.PermissionMngPage.invoice_filter_button.click()
    else:
        assert False, "Under construction."


@When("the user selects office to '{office}' in Permission Management page")
def step_impl(context, office):
    Pages.PermissionMngPage.office_select.select(office)


@When("the user clicks 'View' button in permission management page")
def step_impl(context):
    Pages.PermissionMngPage.view_button.click()
    Pages.Common.spin_bar.gone()
    sleep(2)


@When("the user sets '{role}' '{function}' permission to '{permission}'")
def step_impl(context, role, function, permission):
    """
    role = [Admim, Accounting, AM, Sales, SM, SA, OP, OPM, OPA, GM]
    """
    if permission != "Allow" and permission != "Deny" and permission != "Inherit":
        assert False, "Syntax Error: {0}".format(context.step_name)

    if function == "Invoice AR View":
        Pages.PermissionMngPage.PermissionTable(role).invoice_ar_view_select.select(permission)
    elif function == "Invoice AP View":
        Pages.PermissionMngPage.PermissionTable(role).invoice_ap_view_select.select(permission)
    elif function == "Invoice Block":
        Pages.PermissionMngPage.PermissionTable(role).invoice_block_select.select(permission)
    elif function == "Invoice Block/Unblock Button Visible":
        Pages.PermissionMngPage.PermissionTable(role).invoice_block_unblock_button_visible_select.select(permission)
    elif function == "Invoice Delete":
        Pages.PermissionMngPage.PermissionTable(role).invoice_delete_select.select(permission)
    elif function == "Invoice Edit":
        Pages.PermissionMngPage.PermissionTable(role).invoice_edit_select.select(permission)
    elif function == "Invoice Unblock":
        Pages.PermissionMngPage.PermissionTable(role).invoice_unblock_select.select(permission)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)
