from time import sleep

from behave import Given, Then, When

import src.pages as Pages
from config import globalparameter as gl
from src.drivers.driver import Driver
from src.helper.script import login_as
from src.helper.transfer import transfer_data, transfer_keyword


@Given("the user is a '{role}'")
def step_impl(context, role):
    # Driver.open(gl.URL.DASHBOARD)
    login_as(role)


@Given("the user is a '{role}' in '{office}' office")
def step_impl(context, role, office):
    # Driver.open(gl.URL.DASHBOARD)
    login_as(role, office)


@When("the user log in with '{character}'")
def step_impl(context, character):
    # 未登入
    if Driver.is_url_match("login"):
        character_account_map = {
            "operator": {
                "username": gl.companyConfig[gl.company]["op"],
                "password": gl.companyConfig[gl.company]["password"],
            },
            "super_admin": {
                "username": gl.companyConfig[gl.company]["sa"],
                "password": gl.companyConfig[gl.company]["sa_password"],
            },
            "general_manager": {
                "username": gl.companyConfig[gl.company]["gm"],
                "password": gl.companyConfig[gl.company]["password"],
            },
        }
        character_account = character_account_map[transfer_keyword(character)]
        Pages.LoginPage.username_input.input(character_account["username"])
        Pages.LoginPage.password_input.input(character_account["password"])
        Pages.LoginPage.login_button.click()
    # 已登入，檢查 username
    else:
        nickname_map = {
            "operator": "op",
            "super_admin": "super",
            "general_manager": "gm",
        }
        nickname = nickname_map[transfer_keyword(character)]
        name = Pages.PageHeader.profile.get_value()
        assert nickname in name.lower(), "Account not match. expect [{0}] but get [{1}]".format(character, name)


@When("the user log in with {username} and {password}")
def step_impl(context, username, password):
    username = transfer_data(username)
    password = transfer_data(password)
    Pages.LoginPage.username_input.input(username)
    Pages.LoginPage.password_input.input(password)

    # click reCAPTCHA if it emerge
    # try:
    #     iframe = page.driver.find_element(*LoginPageLocators.RECAPTCHA_IFRAME)
    #     page.driver.switch_to.frame(iframe)
    #     checkbox = page.driver.find_element(*LoginPageLocators.RECAPTCHA_CHECKBOX)
    #     checkbox.click()
    #     sleep(2)
    # except:
    #     pass
    Pages.LoginPage.login_button.click()
    sleep(2)


@Then("login failed message should show")
def step_impl(context):
    result = Pages.LoginPage.login_fail_label.is_visible()
    assert result is True, "Did not show login failed message."


@Then("'Dashboard' page should show")
def step_impl(context):
    assert Pages.PageHeader.dashboard_logo.is_visible(timeout=10) is True
    assert Pages.PageHeader.dashboard_icon.is_visible(timeout=10) is True
