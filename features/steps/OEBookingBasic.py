from time import sleep

from behave import Given, Then, When

import src.models as Models
import src.pages as Pages
from config import globalparameter as gl
from src.drivers.driver import Driver
from src.helper.function import wday
from src.helper.mark_diff_img import MarkDiffImg
from src.helper.script import input_dynamic_datas


@When("the user click booking Tools => Copy => OK")
def step_impl(context):
    Pages.OEBookingBasicTab.tools_button.click()
    Pages.OEBookingBasicTab.tools_copy_button.click()
    Pages.OEBookingBasicTab.tools_copy_ok_button.click()
    Pages.Common.spin_bar.gone()


@Then("the copy booking should show normally")
def step_impl(context):
    sleep(2)
    Pages.OEBookingBasicTab.booking_date_datepicker.input("05-03-2021")  # for ui checking
    Pages.PageHeader.for_evaluation_propose_only_bar.click()
    sleep(2)
    Driver.get_screenshot_as_file(r".\ui_screenshot\GFG-8542\result\running.png")
    result = MarkDiffImg.mark_diff_img(
        base_png=r".\ui_screenshot\GFG-8542\base.png",
        running_png=r".\ui_screenshot\GFG-8542\result\running.png",
        diff_dir=r".\ui_screenshot\GFG-8542\result",
        name="GFG-8542",
    )

    assert result.is_diff == False, "Copy Booking UI is failed"


@Then("the copy booking can be saved successfully")
def step_impl(context):
    Pages.OEBookingBasicTab.booking_date_datepicker.input(wday(2))
    Pages.OEBookingBasicTab.save_button.click()
    assert Pages.Common.save_msg.is_visible(timeout=10), "Save successfully msg is not showing"
    Driver.refresh()
    Pages.Common.spin_bar.gone()
    assert Pages.OEBookingBasicTab.booking_no_input.get_value() != "", "Booking No. is NULL"


@Given("the user has a OE Booking")
def step_impl(context):
    Driver.open(gl.URL.OE_NEW_BOOKING)
    Pages.Common.save_button.click()
    Pages.Common.spin_bar.gone()
    context._vp.add_v("oe_booking_no", Pages.OEBookingBasicTab.booking_no_input.get_value())


@When("the user click 'Accounting' tab of OE Booking")
def step_impl(context):
    Pages.OEBookingTab.accounting_tab.click()
    Pages.Common.spin_bar.gone()


@When("the user add freights to OE Booking AR")
def step_impl(context):
    freight_index = 1
    sleep(2)  # TODO can remove when new_button has ng-model
    for row in context.table:
        Pages.OEBookingAccountingBillingBasedTab.revenue.new_button.click()
        sleep(1)
        action_table = [
            {
                "field": "Bill To",
                "attribute": "autocomplete",
                "action": "input",
                "data": row["Bill To"],
            },
            {
                "field": "Freight Code",
                "attribute": "autocomplete",
                "action": "input",
                "data": row["Freight Code"],
            },
            {
                "field": "Rate",
                "attribute": "input",
                "action": "input",
                "data": row["Rate"],
            },
            {
                "field": "Tax",
                "attribute": "select",
                "action": "select",
                "data": row["Tax"],
            },
        ]
        booking_freight_model = input_dynamic_datas(
            action_table,
            "Pages.OEBookingAccountingBillingBasedTab.revenue({})".format(freight_index),
        )
        context._vp.add_dict(
            dict_name="booking_freight_model",
            value={"{}".format(freight_index): booking_freight_model},
        )
        freight_index += 1


@When("the user click OE Booking Accounting 'Save' Button")
def step_impl(context):
    Pages.OEBookingAccountingBillingBasedTab.save_button.click()
    Pages.Common.spin_bar.gone()


@Given("the user has a OE Booking as '{name}' with only required fields filled")
def step_impl(context, name):
    # create a new MBL
    Driver.open(gl.URL.OE_NEW_BOOKING)
    Pages.Common.spin_bar.gone()
    booking_model = Models.VerifiedModel("Pages.OEBookingBasicTab")
    Pages.Common.save_button.click()
    assert Pages.Common.save_msg.is_visible(timeout=30) is True

    # add additional field
    booking_model.add(
        field="File No.",
        attribute="input",
        data=Pages.OEBookingBasicTab.booking_no_input.get_value(),
    )
    booking_model.add(
        field="Office",
        attribute="autocomplete",
        data=Pages.OEBookingBasicTab.office_autocomplete.get_value(),
    )

    context._vp.add_dict(dict_name="booking_model", value={name: booking_model})

    context._vp.add_dict(dict_name="shipment_url", value={name: Driver.get_url()})


@When("the user enter OEBK 'Container List' datas")
def step_impl(context):
    input_dynamic_datas(context.table, "Pages.OEBookingBasicTab.ContainerList")


@When("the user links the OEBK to the shipment '{shipment_name}'")
def step_impl(context, shipment_name):
    model = context._vp.get("mbl_model")[shipment_name]

    shipment_no = model.get_data("File No.")
    Pages.OEBookingBasicTab.reference_no_autocomplete.input(shipment_no)
    sleep(3)
    Pages.OEBookingBasicTab.ApplyFromMBLToThisBookingPopup.yes_button.click()
