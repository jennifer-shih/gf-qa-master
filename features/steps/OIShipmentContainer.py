from behave import *
from parse import parse

import src.pages as Pages
from config import globalparameter as gl
from src.helper.script import input_dynamic_datas


@When("the user click 'Container & Item' tab of OI")
def step_impl(context):
    Pages.OITab.container_and_item_tab.click()
    Pages.Common.spin_bar.gone()
    Pages.OIContainerTab.MBL.add_button.is_enable()


@When("the user click 'Add' for OI MBL Container List")
def step_impl(context):
    Pages.OIContainerTab.MBL.add_button.click()


@When("the user click 'More' button of OI MBL container({index})")
def step_impl(context, index):
    Pages.OIContainerTab.MBL.container(index).more_button.click()


@When("the user enters datas to OI container({index})")
def step_impl(context, index):
    verify_model = input_dynamic_datas(context.table, "Pages.OIContainerTab.MBL.container({0})".format(index))
    context._vp.add_v("verify_model", verify_model)


@Then("the container should be created")
def step_impl(context):
    model = context._vp.get("verify_model")
    page_class_name = model.get_page_class_name()
    index = parse("Pages.OIContainerTab.MBL.container({index})", page_class_name)["index"]
    Pages.OIContainerTab.MBL.container(index).more_button.click()
    model.get_page_class_name
    model.verify()


@When("the user click 'New' button for HBL Commodity")
def step_impl(context):
    Pages.OIContainerTab.HBL.add_commodity_button.click()


@When("the user add a new commodity #{index}")
def step_impl(context, index):
    verify_model = input_dynamic_datas(context.table, "Pages.OIContainerTab.HBL.commodity({0})".format(index))
    context._vp.add_v("verify_model", verify_model)


@Then("the commodity should be created")
def step_impl(context):
    model = context._vp.get("verify_model")
    model.verify()


@Then("PKG Unit = '{pkg_unit}'")
def step_impl(context, pkg_unit):
    value = Pages.OIContainerTab.MBL.pkg_unit_autocomplete.get_value()
    assert pkg_unit == value, "Expect to get [{0}], but [{1}]".format(pkg_unit, value)


@Then("Weight Unit = '{weight_unit}'")
def step_impl(context, weight_unit):
    value = Pages.OIContainerTab.MBL.weight_unit_select.get_value()
    assert weight_unit == value, "Expect to get [{0}], but [{1}]".format(weight_unit, value)


@Then("Measurement Unit = '{measurement_unit}'")
def step_impl(context, measurement_unit):
    value = Pages.OIContainerTab.MBL.measurement_unit_select.get_value()
    assert measurement_unit == value, "Expect to get [{0}], but [{1}]".format(measurement_unit, value)


@Then("weight unit converter should caculate with 1 KG = {n} LB")
def step_impl(context, n):
    weight_kg = float(Pages.OIContainerTab.MBL.container(1).weight_kg_input.get_value())
    value = float(
        Pages.OIContainerTab.MBL.container(1).weight_converter_label.get_value().strip().split()[0].replace(",", "")
    )
    unit = Pages.OIContainerTab.MBL.container(1).weight_converter_label.get_value().strip().split()[1]
    expected_value = weight_kg * float(n)
    expected_unit = "LB"

    assert abs(expected_value - value) < 0.02, "Expect get [{0}], but [{1}]".format(expected_value, value)
    assert expected_unit == unit, "Expect get [{0}], but [{1}]".format(expected_unit, unit)


@Then("measurement unit converter should caculate with 1 CBM = {n} CFT")
def step_impl(context, n):
    measurement_cbm = float(Pages.OIContainerTab.MBL.container(1).measurement_cbm_input.get_value())
    value = float(
        Pages.OIContainerTab.MBL.container(1)
        .measurement_converter_label.get_value()
        .strip()
        .split()[0]
        .replace(",", "")
    )
    unit = Pages.OIContainerTab.MBL.container(1).measurement_converter_label.get_value().strip().split()[1]
    expected_value = measurement_cbm * float(n)
    expected_unit = "CFT"

    assert abs(expected_value - value) < 0.02, "Expect get [{0}], but [{1}]".format(expected_value, value)
    assert expected_unit == unit, "Expect get [{0}], but [{1}]".format(expected_unit, unit)


@When("the user enable 'Input total number' of MBL")
def step_impl(context):
    if gl.company in ["SFI", "LOHAN"]:
        Pages.OIContainerTab.MBL.input_total_number_checkbox.tick(True)
    elif gl.company in ["OLC", "MASCOT"]:
        Pages.OIContainerTab.MBL.total_amount_source_radio_group.click("Manual Input")
    else:
        assert False, f"Company { gl.company } is not support in the step { context.step_name }"


@When("the user input total PKG, Weight, Measurement")
def step_impl(context):
    pkg = context.table[0]["PKG"]
    weight = context.table[0]["Weight"]
    measurement = context.table[0]["Measurement"]

    Pages.OIContainerTab.MBL.total_manual_pkg_input.input(pkg)
    Pages.OIContainerTab.MBL.total_manual_weight_kg_input.input(weight)
    Pages.OIContainerTab.MBL.total_manual_measurement_cbm_input.input(measurement)


@Then("Total PKG, Weight, Measurement should be")
def step_impl(context):
    expt_pkg = context.table[0]["PKG"]
    expt_weight = context.table[0]["Weight"]
    expt_measurement = context.table[0]["Measurement"]
    pkg = Pages.OIContainerTab.MBL.total_manual_pkg_input.get_value()
    weight = Pages.OIContainerTab.MBL.total_manual_weight_kg_input.get_value()
    measurement = Pages.OIContainerTab.MBL.total_manual_measurement_cbm_input.get_value()

    assert expt_pkg == pkg
    assert expt_weight == weight
    assert expt_measurement == measurement
