from time import sleep

from behave import When

from src.helper.script import input_dynamic_datas
from src.pages import Common, OEContainerTab


@When("the user click 'Add' of OE MBL Container List")
def step_impl(context):
    OEContainerTab.MBL.add_button.click()


@When("the user click 'More' button of OE MBL container({index})")
def step_impl(context, index):
    index_int = int(index)
    OEContainerTab.MBL.container(index_int).more_button.click()


@When("the user enters datas to OE MBL container({index})")
def step_impl(context, index):
    input_dynamic_datas(context.table, "Pages.OEContainerTab.MBL.container({0})".format(index))


@When("the user enters datas to OE HBL 'Container List'")
def step_impl(context):
    input_dynamic_datas(context.table, "Pages.OEContainerTab.HBL.ContainerList")


@When("the user assign / unassign HBL to containers in OE shipment")
def step_impl(context):
    if OEContainerTab.MBL.assign_container_area_element.is_invisible():
        OEContainerTab.MBL.assign_container_button.click()
        sleep(3)

    need_click_save_button = False
    for row in context.table:
        container_index = int(row["Container No."])
        hbl_index = int(row["HBL No."])
        data = row["Assign"]
        if data == r"{on}":
            # only when the value changed, save button will be clickable by the user
            curr_state = OEContainerTab.MBL.container(container_index).assign_to_hbl_checkbox(hbl_index).get_value()
            if curr_state != True:
                need_click_save_button = True
            OEContainerTab.MBL.container(container_index).assign_to_hbl_checkbox(hbl_index).tick(True)
        elif data == r"{off}":
            OEContainerTab.MBL.container(container_index).assign_to_hbl_checkbox(hbl_index).tick(False)
            if OEContainerTab.UnassignConfirmPopup.ok_button.is_visible():
                OEContainerTab.UnassignConfirmPopup.ok_button.click()

    if need_click_save_button:
        Common.save_button.click()
        Common.spin_bar.gone()


@When("the user deletes containers in OE Container Tab")
def step_impl(context):
    for row in context.table:
        index = int(row["No."])
        OEContainerTab.MBL.container(index).select_checkbox.tick(True)

    OEContainerTab.MBL.delete_button.click()
    sleep(3)
    OEContainerTab.DeleteConfirmPopup.ok_button.click()
