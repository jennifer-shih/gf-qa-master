from behave import Given, Then, When

import src.pages as Pages
from config import globalparameter as gl
from src.drivers.driver import Driver
from src.helper.script import input_dynamic_datas
from src.helper.transfer import transfer_to_feature_table


@When("the user enter receiving basic datas as '{name}'")
def step_impl(context, name):
    current_page_class_name = "Pages.WHReceivingBasicTab"
    model = input_dynamic_datas(context.table, current_page_class_name)
    context._vp.add_dict(dict_name="wh_receiving_model", value={"{}".format(name): model})


@Then("the receiving '{name}' will be created")
def step_impl(context, name):
    model = context._vp.get("wh_receiving_model")[name]

    # go to the receipt which just created
    Driver.open(context._vp.get("url"))
    Pages.Common.spin_bar.gone()

    # url should be https://fms-stage-qa-5.gofreight.co/warehouse/receiving/entry/{File_No}/
    file_no = Driver.get_url().split("/")[-2]
    model.add(field="file_no", attribute="input", data=file_no)
    model.verify()


@Given("the user has a WH Receiving as '{name}' with only required fields filled")
def step_impl(context, name):
    create_wh_receiving_table = transfer_to_feature_table(
        """
        | field             | attribute    | action                   | data                    |
        | Customer          | autocomplete | input and close memo     | {randomTradePartner}    |
    """
    )

    # create a new MBL
    Driver.open(gl.URL.WH_NEW_RECEIVING)
    model = input_dynamic_datas(create_wh_receiving_table, "Pages.WHReceivingBasicTab", None)
    Pages.Common.save_button.click()
    assert Pages.Common.save_msg.is_visible(timeout=30) is True

    # add additional field
    model.add(
        field="File No.",
        attribute="input",
        data=Pages.WHReceivingBasicTab.file_no_input.get_value(),
    )
    model.add(
        field="Office",
        attribute="autocomplete",
        data=Pages.WHReceivingBasicTab.office_autocomplete.get_value(),
    )

    context._vp.add_dict(dict_name="mbl_model", value={name: model})

    context._vp.add_dict(dict_name="shipment_url", value={name: Driver.get_url()})
