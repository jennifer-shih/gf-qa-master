from logging import Logger
from time import sleep

from behave import *

import src.pages as Pages  # noqa
from config import globalparameter as gl
from src.drivers.driver import Driver
from src.helper.executor import trnas_ele_cmd
from src.helper.log import Logger
from src.helper.script import input_dynamic_datas, wait_reset_db_process_done
from src.helper.transfer import trans_data_to_value, transfer_data


@Then("the reset DB process will be done for a time")
def step_impl(context):
    wait_reset_db_process_done()


@When("the user set language to '{language}'")
def step_impl(context, language):
    if Pages.PageHeader.home_page_navigator_link.get_value() != "Home":
        Pages.ProfilePage.setting_button.click()
        Pages.ProfilePage.language_select.select(language)
        Pages.ProfilePage.save_changes_button.click()


@When("the user set email notifiction settings as listed below")
def step_impl(context):
    Pages.ProfilePage.setting_button.click()
    sleep(0.1)
    model = input_dynamic_datas(context.table, page_class_name="Pages.ProfilePage")
    context._vp.add_v(v_name="user_settings_model", value=model)
    Pages.ProfilePage.save_changes_button.click()


@Then("user settings are correct")
def step_impl(context):
    context._vp.get("user_settings_model").verify()


@Then("GoFreight should show with English")
def step_impl(context):
    # Workaround: Sometimes the language will remain unchanged, so here we refresh the browser twice to ensure
    # the UI changes correponding to the language setting
    Driver.refresh()
    Pages.Common.spin_bar.gone()

    val = Pages.PageHeader.home_page_navigator_link.get_value()
    assert "Home" == val, "Expect get [Home], but get [{0}]".format(val)


@When("the user input 'Office Entry' fields and save it")
def step_impl(context):
    model = input_dynamic_datas(context.table, "Pages.OfficeMngPage")
    model.pop("Add Company Logo", not_exist_ok=True)  # it cannot be verified
    context._vp.add_v(v_name="office_entry_model", value=model)
    sleep(5)
    Pages.Common.save_button.click()
    assert Pages.Common.save_msg.is_visible(timeout=60) is True


@Then("'Office Entry' settings are correct")
def step_impl(context):
    context._vp.get("office_entry_model").verify()


@When("the user input 'Company Management' fields and save it")
def step_impl(context):
    model = input_dynamic_datas(context.table, "Pages.CompanyMngPage")
    context._vp.add_v(v_name="compeny_management_model", value=model)
    if Pages.Common.save_button.is_disabled():
        Logger.getLogger().warning("There was no change.")
    else:
        Pages.Common.save_button.click()
        assert Pages.Common.save_msg.is_visible(timeout=60) is True


@Then("'Company Management' settings are correct")
def step_impl(context):
    context._vp.get("compeny_management_model").verify()


@Given("settings in 'Company Management' page are as listed below")
def step_imple(context):
    require_input = False
    for row in context.table:
        element = trnas_ele_cmd(row["field"], row["attribute"], page_class_name="Pages.CompanyMngPage")
        value = element.get_value()
        exp_value = trans_data_to_value(transfer_data(row["data"]), row["attribute"], get_value=value)
        if value != exp_value:
            require_input = True
            break
    if require_input:
        model = input_dynamic_datas(context.table, "Pages.CompanyMngPage")
        if Pages.Common.save_button.is_disabled():
            Logger.getLogger().warning("There was no change.")
        else:
            Pages.Common.save_button.click()
            Pages.Common.spin_bar.gone()
            sleep(5)
        Driver.refresh()
        Pages.Common.spin_bar.gone()
        model.verify()


@Given("settings in '{office}' 'Office Entry' page are as listed below")
def step_imple(context, office):
    office_link = trnas_ele_cmd("{0} {1}".format(gl.company, office), "link", page_class_name="Pages.OfficeMngPage")

    office_link.click()
    Pages.Common.spin_bar.gone()

    require_input = False
    for row in context.table:
        element = trnas_ele_cmd(row["field"], row["attribute"], page_class_name="Pages.OfficeMngPage")
        value = element.get_value()
        exp_value = trans_data_to_value(transfer_data(row["data"]), row["attribute"], get_value=value)
        # ? Known Issue
        if row["field"] == "Location List":
            value = exp_value
        # 'DIAMOND LAKE, IL\nBIG TREE, NY\nKEELUNG\nKAOHSIUNG'
        # ?
        if value != exp_value:
            require_input = True
            break
    if require_input:
        model = input_dynamic_datas(context.table, "Pages.OfficeMngPage")
        model.pop("Add Company Logo")
        if Pages.Common.save_button.is_disabled():
            Logger.getLogger().warning("There was no change.")
        else:
            Pages.Common.spin_bar.gone()
            Pages.Common.save_button.click()
            Pages.Common.spin_bar.gone()
        Driver.refresh()
        Pages.Common.spin_bar.gone()
        model.verify()


@Given("settings in '{office}' 'System Configuration' page are as listed below")
def step_imple(context, office):
    Pages.SystemConfigPage.target_select.select(office)
    Pages.Common.spin_bar.gone()

    require_input = False
    for row in context.table:
        element = trnas_ele_cmd(row["field"], row["attribute"], page_class_name="Pages.SystemConfigPage")
        value = element.get_value()
        exp_value = trans_data_to_value(transfer_data(row["data"]), row["attribute"], get_value=value)
        if value != exp_value:
            require_input = True
            break
    if require_input:
        model = input_dynamic_datas(context.table, "Pages.SystemConfigPage")
        if Pages.SystemConfigPage.save_button.is_disabled():
            Logger.getLogger().warning("There was no change.")
        else:
            Pages.SystemConfigPage.save_button.click()
            assert Pages.Common.save_msg.is_visible(timeout=60) is True
        Driver.refresh()
        Pages.Common.spin_bar.gone()
        Pages.SystemConfigPage.target_select.select(office)
        Pages.Common.spin_bar.gone()
        model.verify()


@Given("settings in 'Permission Management' page are as listed below")
def step_imple(context):
    for row in context.table:
        require_input = False
        Pages.PermissionMngPage.user_select.select(row["User"])
        Pages.PermissionMngPage.view_button.click()
        Pages.Common.spin_bar.gone()

        for heading in context.table.headings:
            if heading != "Office" and heading != "Office Department" and heading != "User":
                element = trnas_ele_cmd(heading, "select", page_class_name="Pages.PermissionMngPage")
                value = element.get_value()
                exp_value = trans_data_to_value(transfer_data(row[heading]), "select", get_value=value)
                if value != exp_value:
                    require_input = True
                    break
        if require_input:
            action_table = []
            for heading in context.table.headings:
                action = {
                    "field": heading,
                    "attribute": "select",
                    "action": "select",
                    "data": row[heading],
                }
                action_table.append(action)
            model = input_dynamic_datas(action_table, "Pages.PermissionMngPage")
            if Pages.PermissionMngPage.save_button.is_disabled():
                Logger.getLogger().warning("There was no change.")
            else:
                Pages.PermissionMngPage.save_button.click()
                assert Pages.Common.save_msg.is_visible(timeout=60) is True
            Driver.refresh()
            Pages.Common.spin_bar.gone()
            Pages.PermissionMngPage.user_select.select(row["User"])
            Pages.PermissionMngPage.view_button.click()
            Pages.Common.spin_bar.gone()
            model.verify()
