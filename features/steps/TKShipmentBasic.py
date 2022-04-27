import json

from behave import *

import src.pages as Pages  # noqa
from config import globalparameter as gl
from src.drivers.driver import Driver
from src.helper.executor import exec_act_cmd
from src.helper.script import input_dynamic_datas
from src.helper.transfer import transfer_data, transfer_to_feature_table


@Given("the user already has a TK shipment")
def step_impl(context):
    with gl.tk_info_file.open(mode="r") as data_file:
        info = json.load(data_file)
    Driver.open(info["shipment_url"])
    Pages.Common.spin_bar.gone()


@When("the user click TK 'More' button")
def step_impl(context):
    # 如果沒展開再click more button
    if not Pages.TKBasicTab.MBL.e_commerce_checkbox.is_interactable():
        Pages.TKBasicTab.MBL.more_button.click()


@When("the user switch 'Ship Type' to {ship_type}")
def step_impl(context, ship_type):
    Pages.TKBasicTab.MBL.ship_type_select.select(ship_type)


@Then("{linked_field_1}({attribute_1}) and {linked_field_2}({attribute_2}) will show")
def step_impl(context, linked_field_1, attribute_1, linked_field_2, attribute_2):
    result_1 = exec_act_cmd(linked_field_1, attribute_1, action="is_enable", page="Pages.TKBasicTab.MBL")
    result_2 = exec_act_cmd(linked_field_2, attribute_2, action="is_enable", page="Pages.TKBasicTab.MBL")

    assert True == result_1, "expect: [{0}] exist, but no".format(linked_field_1)
    assert True == result_2, "expect: [{0}] exist, but no".format(linked_field_2)


@Then("the shipment '{name}' of 'Truck' will be created")
def step_impl(context, name):
    model = context._vp.get("mbl_model")[name]

    # go to the shipment which just created
    Driver.open(context._vp.get("url"))
    Pages.Common.spin_bar.gone()
    Pages.TKBasicTab.MBL.more_button.click()

    # url should be https://fms-stage-qa-5.gofreight.co/truck/shipment/{File_No}/
    file_no = Driver.get_url().split("/")[-2]
    model.add(field="file_no", attribute="input", data=file_no)

    model.verify()


@Then("default datas and unit conversion are correct")
def step_impl(context):
    for row in context.table:
        field = row["field"]
        attribute = row["attribute"]
        data = row["data"]
        value = exec_act_cmd(field, attribute, action="get_value", page="Pages.TKBasicTab.MBL")
        if data == "None":
            if field == "Weight LB":
                expect = float(Pages.TKBasicTab.MBL.weight_kg_input.get_value()) * gl.KG2LB
                assert abs(expect - float(value)) < 0.01, "{0}: [{1}] must be [{2}]".format(field, value, expect)
            elif field == "Measurement CFT":
                expect = float(Pages.TKBasicTab.MBL.measurement_cbm_input.get_value()) * gl.CBM2CFT
                assert abs(expect - float(value)) < 0.01, "{0}: [{1}] must be [{2}]".format(field, value, expect)
        else:
            expect = transfer_data(data)
            assert expect == value, "{0}: [{1}] must be [{2}]".format(field, value, expect)


@Given("the user has a TK MBL as '{name}' with only required fields filled")
def step_impl(context, name):
    if gl.company in ["OLC", "MASCOT"]:
        create_tk_mbl_table = transfer_to_feature_table(
            """
        | field          | attribute        | action               | data                  |
        | Sales          | autocomplete     | input                | {randomSales}         |
        """
        )
    else:
        create_tk_mbl_table = transfer_to_feature_table(
            """
        | field          | attribute        | action               | data
        """
        )

    # create a new MBL
    Driver.open(gl.URL.TK_NEW_SHIPMENT)
    Pages.Common.spin_bar.gone()
    Pages.TKBasicTab.MBL.more_button.click()
    mbl_model = input_dynamic_datas(create_tk_mbl_table, "Pages.TKBasicTab.MBL")
    Pages.Common.save_button.click()
    assert Pages.Common.save_msg.is_visible(timeout=30) is True

    # add additional field
    mbl_model.add(
        field="File No.",
        attribute="input",
        data=Pages.TKBasicTab.MBL.file_no_input.get_value(),
    )
    mbl_model.add(
        field="Post Date",
        attribute="datepicker",
        data=Pages.TKBasicTab.MBL.post_date_datepicker.get_value(),
    )
    mbl_model.add(
        field="Office",
        attribute="autocomplete",
        data=Pages.TKBasicTab.MBL.office_autocomplete.get_value(),
    )

    context._vp.add_dict(dict_name="mbl_model", value={name: mbl_model})

    context._vp.add_dict(dict_name="shipment_url", value={name: Driver.get_url()})
