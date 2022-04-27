from time import sleep
from urllib.parse import urljoin

from behave import Then, When

import src.pages as Pages
from config import globalparameter as gl
from src.drivers.driver import Driver
from src.helper.log import Logger
from src.helper.script import input_dynamic_datas
from src.helper.transfer import combine_outline_with_table
from src.step_impl.impl_user import checking_tracking_user, create_tracking_user


@When("the user input user profile and create it")
def step_impl(context):
    # Combining context.table with the first row in Example, becoming an action table
    if "data" not in context.table.headings:
        context.table = combine_outline_with_table(context.active_outline, context.table)

    model = input_dynamic_datas(context.table, "Pages.UserMngCreatePage")
    username = model.get_data("User ID")
    Logger.getLogger().info(f"Add role: { username }")

    # Password won't appears again in the user profile page, so don't need to verify
    model.pop("Password")
    model.pop("Confirm Password")
    # Temporarily save in context instead of context._vp
    context.model = model

    if Pages.UserMngCreatePage.id_existing_alert.is_visible(timeout=0.5) == False:
        # Clicks create user button
        Pages.UserMngCreatePage.create_user_button.click()
        Pages.UserMngCreatePage.create_user_sure_button.click()
    else:
        Logger.getLogger().warning(f"Username: { username } is existed")


@Then("new user should be created successfully")
def step_impl(context):
    if Pages.UserMngCreatePage.id_existing_alert.is_visible(timeout=1) == False:
        assert Pages.UserMngPage.create_message.is_visible(timeout=30) is True
        url = urljoin(gl.companyConfig[gl.company]["url"], "/settings/user/management/")
        assert (
            Driver.is_url_match(url) is True
        ), "Expect [{0}] but get [{1}]. Maybe given a wrong page or page title is change.".format(url, Driver.get_url())

        model = context.model
        user_id = model["User ID"]["data"]
        sleep(8)
        Pages.UserMngPage.filter_button.click()
        Pages.UserMngPage.Filter.keyword_input.input(user_id)
        Pages.UserMngPage.Filter.apply_filters_button.click()
        sleep(3)

        Pages.UserMngPage.UserRow(user_id).user_id_link.click()
        sleep(3)
        model.verify()

    else:
        # refresh page for remove alert
        Driver.refresh()
        assert Pages.UserMngCreatePage.create_user_button.is_visible() is True


@When("the user input tracking user profile and create it")
def step_impl(context):
    # Combining context.table with context.active_outline.cel, if needed
    if "data" not in context.table.headings:
        context.table = combine_outline_with_table(context.active_outline, context.table)
    Pages.Common.spin_bar.gone()
    model = create_tracking_user(context.table)
    context._vp.add_v(v_name="tracking_user_settings_model", value=model)


@Then("new tracking user should be created successfully")
def step_impl(context):
    # if saved successfully, verify data
    if Pages.TrackingUserMngCreatePage.id_existing_alert.is_visible(timeout=1) == False:
        assert (
            Driver.is_url_match(gl.URL.TRACKING_USER_MANAGEMENT) is True
        ), "Expect [{0}] but get [{1}]. Maybe given a wrong page or page title is change.".format(
            gl.URL.TRACKING_USER_MANAGEMENT, Driver.get_url()
        )

        model = context._vp.get("tracking_user_settings_model")

        # verify data in tracking user management
        Pages.Common.spin_bar.gone()
        mng_page_model = model.copy()
        checking_tracking_user(model=mng_page_model, in_profile_page=False)

        # verify data in tracking user profile
        user_id = model.get_data("User ID")
        Pages.TrackingUserMngPage.UserRow(user_id).user_id_link.click()
        Pages.Common.spin_bar.gone()
        checking_tracking_user(model=model, in_profile_page=True)

    else:
        # if not saved, refresh page for remove alert, pretend nothing wrong
        Driver.refresh()
        assert Pages.TrackingUserMngCreatePage.create_user_button.is_visible() is True
