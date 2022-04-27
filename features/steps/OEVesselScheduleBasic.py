from time import sleep

from behave import Given, Then, When

import src.models as Models
import src.pages as Pages
from config import globalparameter as gl
from src.drivers.driver import Driver
from src.helper.script import input_dynamic_datas
from src.helper.transfer import transfer_data, transfer_str_of_indices_to_list, transfer_to_feature_table
from src.models import VerifiedModel


@Given("the user has a OEVS VS with {count} BK as '{name}' with only required fields filled")
def step_impl(context, count, name):
    create_oevs_vs_table = transfer_to_feature_table(
        """
        | field                | attribute    | action        | data                       |
        | Vessel Schedule No.  | input        | input         | HACO-{randN(6)}            |
        | ETD                  | datepicker   | input         | {today+5}                  |
    """
    )

    Driver.open(gl.URL.OE_NEW_VESSEL_SCHEDULE)
    Pages.OEVSBasicTab.VS.more_button.click()
    # If multiple POL & POD function is on, uncheck the checkbox to close it
    if Pages.OEVSBasicTab.VS.multiple_pol_pod_checkbox.is_visible():
        Pages.OEVSBasicTab.VS.multiple_pol_pod_checkbox.tick(False)

    vs_model = input_dynamic_datas(create_oevs_vs_table, "Pages.OEVSBasicTab.VS", None)
    Pages.Common.save_button.click()
    sleep(3)
    # Pages.Common.save_msg.is_visible(timeout=30) is True

    # add additional field
    vs_model.add(
        field="Vessel Schedule No.",
        attribute="input",
        data=Pages.OEVSBasicTab.VS.vessel_schedule_no_input.get_value(),
    )
    vs_model.add(
        field="Office",
        attribute="autocomplete",
        data=Pages.OEVSBasicTab.VS.office_autocomplete.get_value(),
    )

    context._vp.add_dict(dict_name="vs_model", value={name: vs_model})

    # create new BKs
    for i in range(1, int(count) + 1):
        Pages.OEVSBasicTab.add_booking_button.click()
        sleep(4)

        Pages.Common.save_button.click()
        # Pages.Common.spin_bar.gone()
        assert Pages.Common.save_msg.is_visible(timeout=20) is True
        bk_model = Models.VerifiedModel(f"Pages.OEVSBasicTab.BK({ i })")
        bk_model.add(
            field="Booking No.",
            attribute="input",
            data=Pages.OEVSBasicTab.BK(i).booking_no_input.get_value(),
        )
        bk_model.add(
            field="Booking Date",
            attribute="date picker",
            data=Pages.OEVSBasicTab.BK(i).booking_date_datepicker.get_value(),
        )

        context._vp.add_dict(dict_name="bk_model", value={"{}_{}".format(name, i): bk_model})

    context._vp.add_dict(dict_name="shipment_url", value={name: Driver.get_url()})


@When("the user click OEVS 'Add Booking' button")
def step_impl(context):
    Pages.OEVSBasicTab.add_booking_button.click()
    sleep(5)


@When("the user create a HBL by '1 to 1' from OEVS BK({index})")
def step_impl(context, index):
    index_int = int(index)

    # Switch to the Booking of the index
    Pages.OEVSSidePanel.booking_button.click()
    sleep(1)
    Pages.OEVSSidePanel.booking_select_button(index_int).click()
    sleep(2)

    Pages.OEVSBasicTab.BK(index_int).tools_button.click()
    Pages.OEVSBasicTab.BK(index_int).tools_create_hbl_1to1_button.click()
    sleep(5)
    Pages.OEVSBasicTab.CreateHBL1to1Popup.hbl_no_input.input("OneToOne-HBL")
    Pages.OEVSBasicTab.CreateHBL1to1Popup.create_button.click()
    Pages.Common.spin_bar.gone()


@When("the user create {number} HBL by 'Split' from OEVS BK({index})")
def step_impl(context, number, index):
    index_int = int(index)

    # Switch to the Booking of the index
    Pages.OEVSSidePanel.booking_button.click()
    sleep(1)
    Pages.OEVSSidePanel.booking_select_button(index_int).click()
    sleep(2)

    Pages.OEVSBasicTab.BK(index_int).tools_button.click()
    Pages.OEVSBasicTab.BK(index_int).tools_create_hbl_split_button.click()

    Pages.OEVSBasicTab.CreateHBLSplitPopop.hb_l_no_input.input("SPLIT-HBL")
    Pages.OEVSBasicTab.CreateHBLSplitPopop.copy_input.input(number)
    Pages.OEVSBasicTab.CreateHBLSplitPopop.split_button.click()
    Pages.Common.spin_bar.gone()
    sleep(3)


@When("the user create a HBL by 'Merge' from OEVS BK({indices})")
def step_impl(context, indices):
    index_list = transfer_str_of_indices_to_list(indices)
    first_index = index_list.pop(0)

    # Switch to the Booking of the first index
    Pages.OEVSSidePanel.booking_button.click()
    Pages.Common.spin_bar.gone()
    Pages.OEVSSidePanel.booking_select_button(first_index).click()
    sleep(2)

    Pages.OEVSBasicTab.BK(first_index).tools_button.click()
    Pages.OEVSBasicTab.BK(first_index).tools_create_hbl_merge_button.click()

    # Get the Booking Number of the bookings we want to use to create hbl
    bk_no_list = []
    for index in index_list:
        bK_no = Pages.OEVSSidePanel.booking_select_button(index).get_value()
        bk_no_list.append(bK_no)

    # Search the booking no in the popup's left-hand-side
    for bk_no in bk_no_list:
        Pages.OEVSBasicTab.CreateHBLMergePopup.bk_not_yet_converted_select_button(bk_no).click()
    Pages.OEVSBasicTab.CreateHBLMergePopup.move_to_to_be_merged_list_button.click()

    Pages.OEVSBasicTab.CreateHBLMergePopup.hbl_no_input.input("MERGE-HBL")
    Pages.OEVSBasicTab.CreateHBLMergePopup.merge_button.click()
    Pages.Common.spin_bar.gone()


@When("the user enter OEVS {hbl_or_bk}({index}) 'Container list' datas and save it")
def step_impl(context, hbl_or_bk, index):
    if hbl_or_bk == "BK":
        page_class_name = f"Pages.OEVSBasicTab.BK({ index }).ContainerList"
        input_dynamic_datas(context.table, page_class_name)
    elif hbl_or_bk == "HBL":
        page_class_name = f"Pages.OEVSBasicTab.HBL({ index }).ContainerList"
        input_dynamic_datas(context.table, page_class_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@When("the user switch to BK({index}) in OEVS")
def step_impl(context, index):
    index_int = int(index)
    if Pages.OEVSSidePanel.booking_button.is_visible():
        Pages.OEVSSidePanel.booking_button.click()
    Pages.OEVSSidePanel.booking_select_button(index_int).click()
    Pages.Common.spin_bar.gone()
    sleep(3)


@When("the user switch to HBL({index}) in OEVS")
def step_impl(context, index):
    index_int = int(index)
    if Pages.OEVSSidePanel.hbl_select_button(index_int).is_invisible:
        Pages.OEVSSidePanel.hb_l_button.click()
    Pages.OEVSSidePanel.hbl_select_button(index_int).click()
    Pages.Common.spin_bar.gone()
    sleep(3)


@When("the user add continers to OEVS VS 'Container list'")
def step_impl(context):
    for row in context.table:
        Pages.OEVSBasicTab.VS.ContainerList.new_button.click()
        if "Container No." in context.table.headings:
            container_no = row["Container No."]
            Pages.OEVSBasicTab.VS.ContainerList.container(1).container_no_input.input(container_no)
        if "Handle Agent" in context.table.headings:
            input_data = transfer_data(row["Handle Agent"])
            Pages.OEVSBasicTab.VS.ContainerList.container(1).handle_agent_autocomplete.input(input_data)
        # Gofreight will sort the container according to 'TP/SZ' fileds, so it should be filled lastly
        if "TP/SZ" in context.table.headings:
            Pages.OEVSBasicTab.VS.ContainerList.container(1).tp_sz_select.select(row["TP/SZ"])


@Then("'Handle Agent' field should be visible in OEVS Container List")
def step_impl(context):
    assert Pages.OEVSBasicTab.VS.ContainerList.handle_agent_title_label.is_visible()


@When("the user load {hbl_or_bk}s' information to the container({index_str}) in OEVS")
def step_impl(context, hbl_or_bk, index_str):
    index = int(index_str)
    Pages.OEVSBasicTab.VS.ContainerList.container(index).action_button.click()
    Pages.OEVSBasicTab.VS.ContainerList.container(index).action_modify_button.click()

    # Tick all checkboxs of the booking we want to select
    for row in context.table:
        if hbl_or_bk == "HBL":
            booking_index = int(row["HBL No."])
        elif hbl_or_bk == "BK":
            booking_index = int(row["Booking No."])
        Pages.OEVSBasicTab.LoadPlanPopup.Booking(booking_index).select_checkbox.tick(True)

    Pages.OEVSBasicTab.LoadPlanPopup.save_button.click()
    Pages.Common.spin_bar.gone()


@When("the user creates 1 MBL as '{name}' from containers in OEVS")
def step_impl(context, name):
    # Tick all containers we want to be used to create HBL
    if "No." in context.table.headings:
        container_indices_list = []
        for row in context.table:
            container_indices_list.append(int(row["No."]))
        for index in container_indices_list:
            Pages.OEVSBasicTab.VS.ContainerList.container(index).select_checkbox.tick(True)
    if "Container No." in context.table.headings:
        container_no_list = []
        for row in context.table:
            container_no_list.append(row["Container No."])
        for container_no in container_no_list:
            Pages.OEVSBasicTab.VS.ContainerList.container(container_no=container_no).select_checkbox.tick(True)

    Pages.OEVSBasicTab.VS.ContainerList.create_mbl_button.click()
    Pages.OEVSBasicTab.VS.ContainerList.create_mbl_create_1_mb_l_button.click()
    sleep(1)

    Pages.OEVSBasicTab.TransmitToMBLConfirmPopup.ok_button.click()
    sleep(3)
    assert Pages.OEVSBasicTab.MBLIsCreatedPopup.created_mbl_link.is_visible()

    model = VerifiedModel("Pages.OEBookingBasicTab")
    mbl_no = Pages.OEVSBasicTab.MBLIsCreatedPopup.created_mbl_link.get_value()
    model.add("File No.", "input", mbl_no)

    # Click the link that links to created MBL, click ok to dismiss the popup, then switch to window of created MBL
    window_title = f"{ mbl_no } - OE"
    Pages.OEVSBasicTab.MBLIsCreatedPopup.created_mbl_link.click()
    Pages.OEVSBasicTab.MBLIsCreatedPopup.ok_button.click()
    Driver.switch_to(window_name=window_title)
    Pages.Common.spin_bar.gone()

    # Save the url of the OE shipment
    shipment_url = Driver.get_url()
    shipment_url_dict = {name: shipment_url}
    context._vp.add_dict(dict_name="shipment_url", value=shipment_url_dict)
    context._vp.add_dict(dict_name="mbl_model", value={name: model})


@When("the user enter OEVS HBL 'Container List' datas")
def step_impl(context):
    input_dynamic_datas(context.table, "Pages.OEVSBasicTab.HBL.ContainerList")


@When("the user inputs containers information to OEVS VS")
def step_impl(context):
    for row in context.table:
        if "Handle Agent" in context.table.headings:
            container_no = row["Container No."]
            input_data = row["Handle Agent"]
            Pages.OEVSBasicTab.VS.ContainerList.container(container_no=container_no).handle_agent_autocomplete.input(
                input_data
            )
