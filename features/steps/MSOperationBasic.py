from behave import *

import src.pages as Pages  # noqa
from config import globalparameter as gl
from src.drivers.driver import Driver
from src.helper.executor import exec_act_cmd
from src.helper.filters import ExceptedFilter
from src.helper.script import input_dynamic_datas
from src.helper.transfer import transfer_to_feature_table


@When("the user enter 'MS MBL' new shipment page as '{name}' and save it")
def step_impl(context, name):
    """
    Save current date and office, then press save button directly
    """
    current_page_class_name = "Pages.MiscBasicTab.MBL"
    excepted_filter = ExceptedFilter.ms_mbl_filter

    model = input_dynamic_datas([], current_page_class_name, excepted_filter)

    # Get the default value of Post Date and Office, and filling into verified model
    current_post_date = exec_act_cmd("Post Date", "datepicker", "get_value", page=current_page_class_name)
    current_office = exec_act_cmd("Office", "autocomplete", "get_value", page=current_page_class_name)

    model.add(field="Post Date", attribute="datepicker", data=current_post_date)
    model.add(field="Office", attribute="autocomplete", data=current_office)
    context._vp.add_dict(dict_name="mbl_model", value={name: model})

    Pages.Common.save_button.click()
    assert Pages.Common.save_msg.is_visible(timeout=30) is True

    context._vp.add_v(v_name="url", value=Driver.get_url())


@When("the user click MS 'More' button")
def step_impl(context):
    # 如果沒展開再click more button
    if not Pages.MiscBasicTab.MBL.e_commerce_checkbox.is_interactable():
        Pages.MiscBasicTab.MBL.more_button.click()


@Then("the shipment '{name}' of 'Misc' will be created")
def step_impl(context, name):
    model = context._vp.get("mbl_model")[name]

    # Reload the page and expend
    Driver.open(context._vp.get("url"))
    Pages.Common.spin_bar.gone()
    Pages.MiscBasicTab.MBL.more_button.click()

    # The url is https://fms-stage-qa-5.gofreight.co/misc/shipment/{File_No}/
    file_no = Driver.get_url().split("/")[-2]
    # Adding File No. into model to be verified
    model.add(field="file_no", attribute="input", data=file_no)

    model.verify()


@Given("the user has a MS MBL as '{name}' with only required fields filled")
def step_impl(context, name):
    if gl.company in ["OLC", "MASCOT"]:
        create_ms_mbl_table = transfer_to_feature_table(
            """
        | field          | attribute        | action               | data                  |
        | Sales          | autocomplete     | input                | {randomSales}         |
        """
        )
    else:
        create_ms_mbl_table = transfer_to_feature_table(
            """
        | field          | attribute        | action               | data
        """
        )

    # create a new MBL
    Driver.open(gl.URL.MS_NEW_OPERATION)
    Pages.Common.spin_bar.gone()
    Pages.MiscBasicTab.MBL.more_button.click()
    mbl_model = input_dynamic_datas(create_ms_mbl_table, "Pages.MiscBasicTab.MBL")
    Pages.Common.save_button.click()
    assert Pages.Common.save_msg.is_visible(timeout=30) is True

    # add additional field
    mbl_model.add(
        field="File No.",
        attribute="input",
        data=Pages.MiscBasicTab.MBL.file_no_input.get_value(),
    )
    mbl_model.add(
        field="Post Date",
        attribute="datepicker",
        data=Pages.MiscBasicTab.MBL.post_date_datepicker.get_value(),
    )
    mbl_model.add(
        field="Office",
        attribute="autocomplete",
        data=Pages.MiscBasicTab.MBL.office_autocomplete.get_value(),
    )

    context._vp.add_dict(dict_name="mbl_model", value={name: mbl_model})

    context._vp.add_dict(dict_name="shipment_url", value={name: Driver.get_url()})
