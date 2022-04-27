from behave.model import Table

import src.pages as Pages
from src.exception.exception import GfqaException
from src.helper.executor import exec_act_cmd
from src.helper.log import Logger
from src.helper.script import input_dynamic_datas
from src.models.verify_model import VerifiedModel


def create_tracking_user(action_table: Table, exist_ok: bool = False) -> VerifiedModel:
    """
    create tracking user
    """
    page_class_name = "Pages.TrackingUserMngCreatePage"
    model = input_dynamic_datas(action_table, page_class_name)
    username = model.get_data("User ID")
    role = model.get_data("Role")
    Logger.getLogger().info(f"Add role: { username }")

    # Password won't appears again in the user profile page, so don't need to verify
    model.pop("Password")
    model.pop("Confirm Password")

    # email notifications that might need to be added into model
    email_notification = [
        "In Gate",
        "Rail",
        "Vessel Departure",
        "Outgate",
        "Vessel Arrival",
        "Unloaded from Vessel",
        "ETD Updated",
        "ETA Updated",
        "New Document Uploaded",
        "Shipment Report",
        "Detention Report",
    ]
    for field in email_notification:
        if field == "Detention Report" and role == "Shipper":  # shipper don't have Detention Report checkbox
            continue
        if field not in model:
            value = exec_act_cmd(field, "checkbox", "get_value", page=page_class_name)
            model.add(field, "checkbox", value)

    # Clicks create user button
    Pages.TrackingUserMngCreatePage.create_user_button.click()

    if Pages.TrackingUserMngCreatePage.id_existing_alert.is_visible(timeout=0.5) == True:
        msg = f"Username: { username } is existed"
        if exist_ok:
            Logger.getLogger().warning(msg)
        else:
            raise GfqaException(msg)

    return model


def checking_tracking_user(model: VerifiedModel, in_profile_page: bool = False) -> None:
    """
    checking tracking user
    """
    if in_profile_page:
        model.verify()

    else:
        user_id = model.get_data("User ID")
        Pages.TrackingUserMngPage.filter_button.click()
        Pages.TrackingUserMngPage.Filter.keyword_input.input(user_id)
        Pages.TrackingUserMngPage.Filter.apply_filters_button.click()
        Pages.Common.spin_bar.gone()

        # verify data in tracking user list
        page_class_name = f'Pages.TrackingUserMngPage.UserRow("{user_id}")'
        mng_page_model = model.copy()
        mng_page_model.set_page_class_name(page_class_name)
        for field in mng_page_model.get_all_fields():
            field_info = mng_page_model.pop(field)
            if field == "Trade Partner":  # tp's format is ({tp_code}) {tp_name} in management page
                value = exec_act_cmd(field, "label", "get_value", page=page_class_name)
                assert (
                    field_info["data"] in value
                ), f'Trade Partner: Expect [(XX-XXXXXX) {field_info["data"]}] but get [{value}]'
                continue
            if field_info["attribute"] != "checkbox":
                mng_page_model.add(field, attribute="label", data=field_info["data"])
        mng_page_model.verify()
        assert (
            Pages.TrackingUserMngPage.UserRow(user_id).status_label.get_value() == "Active"
        ), "Tracking user {user_id}'s status should be Active"
