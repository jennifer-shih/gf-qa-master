import random
import re
from decimal import Decimal
from time import sleep

from behave import Given, Then, When

import src.pages as Pages  # noqa
from config import globalparameter as gl
from src.api.gofreight_config import GBy
from src.drivers.driver import Driver
from src.helper.executor import exec_act_cmd
from src.helper.script import input_dynamic_datas
from src.helper.transfer import transfer_to_feature_table
from src.models import VerifiedModel


@When("the user click AI MAWB 'More' button")
def step_impl(context):
    # 如果沒展開再click more button
    if not Pages.AIBasicTab.MAWB.e_commerce_checkbox.is_interactable():
        Pages.AIBasicTab.MAWB.more_button.click()


@When("the user tick AI 'Direct Master' checkbox")
def step_impl(context):
    Pages.AIBasicTab.MAWB.direct_master_checkbox.tick(True)
    Pages.Common.spin_bar.gone()


@When("the user click AI HAWB({hbl_index}) 'More' button")
def step_impl(context, hbl_index):
    hbl_index = int(hbl_index)
    # 如果沒展開再click more button
    if not Pages.AIBasicTab.HAWB(hbl_index).e_commerce_checkbox.is_interactable():
        Pages.AIBasicTab.HAWB(hbl_index).more_button.click()


@Then("the AI shipment '{name}' 'Volume Weight' won't change")
def step_impl(context, name):
    # the user is very cautios so she click cancel to see what will happen
    models = context._vp.get("mawb_volume_weight_model")[name]
    Pages.AIBasicTab.MAWB.set_dimensions_button.click()
    for model in models:
        model.verify()
    Pages.AIBasicTab.Dimension.dimension_cancel_button.click()


@Then("the AI shipment '{name}' 'Route' won't change")
def step_impl(context, name):
    # the user is very cautios so she click cancel to see what will happen
    model = context._vp.get("mawb_route_model")[name]
    Pages.AIBasicTab.MAWB.connecting_flight_button.click()
    model.verify()
    Pages.AIBasicTab.MAWB.route_cancel_button.click()


@When("the user select '{value}' for field '{field}' in AI 'new shipment' page for MAWB")
def step_impl(context, value, field):
    exec_act_cmd(field, "autocomplete", "input", [value], "Pages.AIBasicTab.MAWB")


@When("the user select '{value}' for field '{field}' in AI 'new shipment' page for HAWB")
def step_impl(context, value, field):
    exec_act_cmd(field, "autocomplete", "input", [value], "Pages.AIBasicTab.HAWB")


@Then("the AI MAWB '{name}' '{data_type}' data is saved")
def step_impl(context, name, data_type):
    # go to the shipment which just created
    Driver.open(context._vp.get("url"))
    Pages.Common.spin_bar.gone()
    Pages.AIBasicTab.MAWB.more_button.click()

    if data_type == "Volume Weight":
        models = context._vp.get("mawb_volume_weight_model")[name]
        Pages.AIBasicTab.MAWB.set_dimensions_button.click()
        for model in models:
            model.verify()

    elif data_type == "Route":
        model = context._vp.get("mawb_route_model")[name]
        Pages.AIBasicTab.MAWB.connecting_flight_button.click()
        model.verify()


@Then("the AI shipment '{name}' HAWB({hbl_index}) '{data_type}' data is saved")
def step_impl(context, name, hbl_index, data_type):
    # go to the shipment which just created
    Driver.open(context._vp.get("url"))
    Pages.Common.spin_bar.gone()
    Pages.AIBasicTab.HAWB(hbl_index).more_button.click()

    if data_type == "Volume Weight":
        Pages.AIBasicTab.HAWB(hbl_index).set_dimensions_button.click()

    data_type = data_type.replace(" ", "_").lower()
    models = context._vp.get("hawb_{}_model".format(data_type))["{}_{}".format(name, hbl_index)]
    for model in models:
        model.verify()


@Then("'Departure' value should be the same as 'Departure' value in 'Connecting Flight'")
def step_impl(context):
    exp_value = Pages.AIBasicTab.MAWB.departure_autocomplete.get_value()
    Pages.AIBasicTab.MAWB.connecting_flight_button.click()
    sleep(2)
    value = Pages.AIBasicTab.MAWB.departure_autocomplete.get_value()
    Pages.AIBasicTab.MAWB.route_save_button.click()
    sleep(2)
    assert exp_value == value, "Expect [{0}]. but get [{1}]".format(exp_value, value)


@Then("'Destination' value should be the same as 'Destination' value in 'Connecting Flight'")
def step_impl(context):
    exp_value = Pages.AIBasicTab.MAWB.destination_autocomplete.get_value()
    Pages.AIBasicTab.MAWB.connecting_flight_button.click()
    sleep(2)
    value = Pages.AIBasicTab.MAWB.route_final_destination_autocomplete.get_value()
    Pages.AIBasicTab.MAWB.route_save_button.click()
    sleep(2)
    assert exp_value == value, "Expect [{0}]. but get [{1}]".format(exp_value, value)


@Then("the AI MAWB '{name}' 'Volume Weight' data are correct")
@Then("the AI shipment '{name}' HAWB({hbl_index}) 'Volume Weight' data are correct")
def step_impl(context, name, hbl_index=None):
    if hbl_index:
        dimensions = context._vp.get("hawb_dimension_model")["{}_{}".format(name, hbl_index)]
    else:
        dimensions = context._vp.get("mawb_dimension_model")[name]
    for index in range(len(dimensions)):
        kgs = Pages.AIBasicTab.Dimension(index + 1).kgs_label.get_value().replace(",", "")
        lbs = Pages.AIBasicTab.Dimension(index + 1).lbs_label.get_value().replace(",", "")
        cbm = Pages.AIBasicTab.Dimension(index + 1).cbm_label.get_value().replace(",", "")
        cft = Pages.AIBasicTab.Dimension(index + 1).cft_label.get_value().replace(",", "")

        # ? KNOWN ISSUE
        assert (
            abs(Decimal(dimensions[index]["volume_kgs"]) - Decimal(kgs)) <= 0.05
        ), "Expect kgs({0}) to be [{1}]. but get [{2}]".format(index + 1, dimensions[index]["volume_kgs"], Decimal(kgs))
        assert (
            abs(Decimal(dimensions[index]["volume_lbs"]) - Decimal(lbs)) <= 0.05
        ), "Expect lbs({0}) to be [{1}]. but get [{2}]".format(index + 1, dimensions[index]["volume_lbs"], Decimal(lbs))
        assert (
            abs(Decimal(dimensions[index]["measure_cbm"]) - Decimal(cbm)) <= 0.05
        ), "Expect cbm({0}) to be [{1}]. but get [{2}]".format(
            index + 1, dimensions[index]["measure_cbm"], Decimal(cbm)
        )
        assert (
            abs(Decimal(dimensions[index]["measure_cft"]) - Decimal(cft)) <= 1
        ), "Expect cft({0}) to be [{1}]. but get [{2}]".format(
            index + 1, dimensions[index]["measure_cft"], Decimal(cft)
        )
        # ?


@Then("the AI MAWB '{name}' summarized 'Volume Weight' data are correct")
@Then("the AI shipment '{name}' HAWB({hbl_index}) summarized 'Volume Weight' data are correct")
def step_impl(context, name, hbl_index=None):
    exp_total_pcs, exp_total_kgs, exp_total_lbs, exp_total_cbm, exp_total_cft = (
        Decimal(0),
        Decimal(0),
        Decimal(0),
        Decimal(0),
        Decimal(0),
    )
    if hbl_index:
        dimensions = context._vp.get("hawb_dimension_model")["{}_{}".format(name, hbl_index)]
    else:
        dimensions = context._vp.get("mawb_dimension_model")[name]
    for index in range(len(dimensions)):
        exp_total_pcs += Decimal(Pages.AIBasicTab.Dimension(index + 1).pcs_input.get_value())
        exp_total_kgs += Decimal(Pages.AIBasicTab.Dimension(index + 1).kgs_label.get_value().replace(",", ""))
        exp_total_lbs += Decimal(Pages.AIBasicTab.Dimension(index + 1).lbs_label.get_value().replace(",", ""))
        exp_total_cbm += Decimal(Pages.AIBasicTab.Dimension(index + 1).cbm_label.get_value().replace(",", ""))
        exp_total_cft += Decimal(Pages.AIBasicTab.Dimension(index + 1).cft_label.get_value().replace(",", ""))

    pcs_sum = Decimal(Pages.AIBasicTab.Dimension.dimension_pcs_sum_label.get_value().replace(",", ""))
    kgs_sum = Decimal(Pages.AIBasicTab.Dimension.dimension_kgs_sum_label.get_value().replace(",", ""))
    lbs_sum = Decimal(Pages.AIBasicTab.Dimension.dimension_lbs_sum_label.get_value().replace(",", ""))
    cbm_sum = Decimal(Pages.AIBasicTab.Dimension.dimension_cbm_sum_label.get_value().replace(",", ""))
    cft_sum = Decimal(Pages.AIBasicTab.Dimension.dimension_cft_sum_label.get_value().replace(",", ""))

    # ? KNOWN ISSUE
    assert abs(exp_total_pcs - pcs_sum) <= 0.05, "Expect pcs sum to be [{0}]. but get [{1}]".format(
        exp_total_pcs, pcs_sum
    )
    assert abs(exp_total_kgs - kgs_sum) <= 0.05, "Expect kgs sum to be [{0}]. but get [{1}]".format(
        exp_total_kgs, kgs_sum
    )
    assert abs(exp_total_lbs - lbs_sum) <= 0.05, "Expect lbs sum to be [{0}]. but get [{1}]".format(
        exp_total_lbs, lbs_sum
    )
    assert abs(exp_total_cbm - cbm_sum) <= 0.05, "Expect cbm sum to be [{0}]. but get [{1}]".format(
        exp_total_cbm, cbm_sum
    )
    assert abs(exp_total_cft - cft_sum) <= 1, "Expect cft sum to be [{0}]. but get [{1}]".format(exp_total_cft, cft_sum)
    # ?
    context._vp.add_v(v_name="dimension_sum", value={"kgs_sum": str(kgs_sum), "cbm_sum": str(cbm_sum)})


@Given("the user has an AI Shipment without any HAWB")
def step_impl(context):
    create_ai_mawb_table = transfer_to_feature_table(
        """
        | field              | attribute    | action | data                 |
        | MAWB No.           | input        | input  | 911-{randomNo(7)}    |
        | Arrival Date/Time  | datepicker   | input  | {today+2}            |
        | Freight Location   | autocomplete | input  | {randomTradePartner} |
        | Storage Start Date | datepicker   | input  | {today+3}            |
    """
    )

    Driver.open(gl.URL.AI_NEW_SHIPMENT)
    Pages.AIBasicTab.MAWB.more_button.click()
    input_dynamic_datas(create_ai_mawb_table, "Pages.AIBasicTab.MAWB")
    Pages.Common.save_button.click()
    assert Pages.Common.save_msg.is_visible(timeout=30) is True


@Then("the freight location for AI HAWB({hbl_index}) is the same as in MAWB")
def step_impl(context, hbl_index):
    # 如果沒展開再click expand button
    if Pages.AIBasicTab.MAWB.file_no_input.is_invisible():
        Pages.AIBasicTab.MAWB.expand_button.click()
        sleep(3)
    exp_freight_loc = Pages.AIBasicTab.MAWB.freight_location_autocomplete.get_value()
    freight_loc = Pages.AIBasicTab.HAWB(hbl_index).freight_location_autocomplete.get_value()

    assert exp_freight_loc == freight_loc, "Expect [{0}]. but get [{1}]".format(exp_freight_loc, freight_loc)


@Then("the storage start date for AI HAWB({hbl_index}) is the same as in MAWB")
def step_impl(context, hbl_index):
    # 如果沒展開再click expand button
    if Pages.AIBasicTab.MAWB.more_button.is_disable():  # TODO GQT-423 如果眼睛看不到 more button 的話（理論上會在 dom 上，但不重要）
        Pages.AIBasicTab.MAWB.expand_button.click()
    exp_stge_sd = Pages.AIBasicTab.MAWB.storage_start_date_datepicker.get_value()
    stge_sd = Pages.AIBasicTab.HAWB(hbl_index).storage_start_date_datepicker.get_value()

    assert exp_stge_sd == stge_sd, "Expect [{0}]. but get [{1}]".format(exp_stge_sd, stge_sd)


@When("the user input information for AI shipment '{name}' HAWB({hbl_index}) 'Sub HAWB'")
def step_impl(context, name, hbl_index):
    models = []
    current_page_class_name = "Pages.AIBasicTab.HAWB.Sub_HAWB"
    for index in range(len(context.table.rows)):
        action_table = [
            {
                "field": "Sub HAWB",
                "attribute": "input",
                "action": "input",
                "data": context.table[index]["Sub HAWB"],
            }
        ]
        action_table.append(
            {
                "field": "Description / IT No.",
                "attribute": "input",
                "action": "input",
                "data": context.table[index]["Description / IT No."],
            }
        )
        action_table.append(
            {
                "field": "PCS",
                "attribute": "input",
                "action": "input",
                "data": context.table[index]["PCS"],
            }
        )
        action_table.append(
            {
                "field": "PKG Unit",
                "attribute": "autocomplete",
                "action": "input",
                "data": context.table[index]["PKG Unit"],
            }
        )
        action_table.append(
            {
                "field": "Amount",
                "attribute": "input",
                "action": "input",
                "data": context.table[index]["Amount"],
            }
        )

        Pages.AIBasicTab.HAWB(hbl_index).sub_hawb_add_button.click()
        models.append(
            input_dynamic_datas(
                action_table,
                current_page_class_name + "(" + hbl_index + "," + str(index + 1) + ")",
            )
        )
    context._vp.add_dict(dict_name="hawb_sub_hawb_model", value={"{}_{}".format(name, hbl_index): models})


@When("the user input information for AI shipment '{name}' HAWB({hbl_index}) 'Commodity'")
def step_impl(context, name, hbl_index):
    models = []
    current_page_class_name = "Pages.AIBasicTab.HAWB.Commodity"
    for index in range(len(context.table.rows)):
        po_no_options = Pages.AIBasicTab.HAWB(hbl_index).customer_reference___po_no_tag_input.get_value().split(";")
        po_no = random.choice(po_no_options)
        action_table = [
            {
                "field": "Commodity Description",
                "attribute": "input",
                "action": "input",
                "data": context.table[index]["Commodity Description"],
            }
        ]
        action_table.append(
            {
                "field": "HTS Code",
                "attribute": "input",
                "action": "input",
                "data": context.table[index]["HTS Code"],
            }
        )
        action_table.append(
            {
                "field": "P.O. No.",
                "attribute": "tag input",
                "action": "input",
                "data": po_no,
            }
        )

        Pages.AIBasicTab.HAWB(hbl_index).commodity_add_button.click()
        models.append(
            input_dynamic_datas(
                action_table,
                current_page_class_name + "(" + hbl_index + "," + str(index + 1) + ")",
            )
        )
    context._vp.add_dict(
        dict_name="hawb_commodity_model",
        value={"{}_{}".format(name, hbl_index): models},
    )


@Then("the shipment '{name}' HAWB({hbl_index}) in 'Air Import' will be created")
def step_impl(context, name, hbl_index):
    model = context._vp.get("hawb_model")["{}_{}".format(name, hbl_index)]

    # go to the shipment which just created
    Driver.open(context._vp.get("url"))
    Pages.Common.spin_bar.gone()
    Pages.AIBasicTab.HAWB(hbl_index).more_button.click()

    # ? KNOWN ISSUE
    it_iss_loc_field = "IT Issued Location"
    if it_iss_loc_field in model.get_all_fields():
        v = model.pop(it_iss_loc_field)
        exp = v[VerifiedModel.DATA]
        value = exec_act_cmd(it_iss_loc_field, v[VerifiedModel.ATTRIBUTE], "get_value", page=model.page_class_name)
        regex = r"\((\d+)\) " + exp
        assert re.match(regex, value) != None, "{0}: [{1}] must be [{2}]".format(it_iss_loc_field, value, regex)
    # ?

    model.verify()


@Then("the 'Description' field for AI HAWB({hbl_index}) are correct")
def step_impl(context, hbl_index):
    description = Pages.AIBasicTab.HAWB(hbl_index).description_input.get_value()
    exp_description = context._vp.get("description")
    assert exp_description == description, "Expect [{0}]. but get [{1}]".format(exp_description, description)


@Then(
    "'Notify', 'Customer', 'Bill To', 'Delivery Location' should be the same values as 'Consignee' for HAWB({hbl_index})"
)
def step_impl(context, hbl_index):
    consignee = Pages.AIBasicTab.HAWB(hbl_index).consignee_autocomplete.get_value()
    notify = Pages.AIBasicTab.HAWB(hbl_index).notify_autocomplete.get_value()
    customer = Pages.AIBasicTab.HAWB(hbl_index).customer_autocomplete.get_value()
    bill_to = Pages.AIBasicTab.HAWB(hbl_index).bill_to_autocomplete.get_value()
    delivery_location = Pages.AIBasicTab.HAWB(hbl_index).delivery_location_autocomplete.get_value()

    assert consignee == notify, "Expect notify to be [{0}]. but get [{1}]".format(consignee, notify)
    assert consignee == customer, "Expect customer to be [{0}]. but get [{1}]".format(consignee, customer)
    assert consignee == bill_to, "Expect 'bill to' to be [{0}]. but get [{1}]".format(consignee, bill_to)
    assert consignee == delivery_location, "Expect delivery location to be [{0}]. but get [{1}]".format(
        consignee, delivery_location
    )


@Then("the HAWBs weight should be sumed up in AI MAWB block")
def step_impl(context):
    exp_total_vol_kgs, exp_total_vol_cbm = Decimal(0), Decimal(0)
    exp_total_gross_kgs, exp_total_gross_lb = Decimal(0), Decimal(0)
    if not Pages.AIBasicTab.MAWB.more_button.is_disable():  # TODO GQT-423 如果眼睛看到 more button 的話（不論看不看得到，都會在 dom 上）
        Pages.AIBasicTab.MAWB.expand_button.click()

    for index in range(1, Pages.AIBasicTab.HAWB.get_len() + 1):
        Pages.AIBasicTab.HAWB(index).hbl_side_panel_button.click()
        exp_total_gross_kgs += Decimal(Pages.AIBasicTab.HAWB(index).gross_weight_input.get_value())
        exp_total_gross_lb += Decimal(Pages.AIBasicTab.HAWB(index).gross_weight_lb_input.get_value())
        exp_total_vol_kgs += Decimal(Pages.AIBasicTab.HAWB(index).volume_weight_input.get_value())
        exp_total_vol_cbm += Decimal(Pages.AIBasicTab.HAWB(index).volume_measure_input.get_value())

    if Pages.AIBasicTab.MAWB.more_button.is_disable():  # TODO GQT-423 如果眼睛看不到 more button 的話（理論上會在 dom 上，但不重要）
        Pages.AIBasicTab.MAWB.expand_button.click()
    gross_kg = Decimal(Pages.AIBasicTab.MAWB.gross_weight_input.get_value())
    gross_lb = Decimal(Pages.AIBasicTab.MAWB.gross_weight_lb_input.get_value())
    vol_kg = Decimal(Pages.AIBasicTab.MAWB.volume_weight_input.get_value())
    vol_cbm = Decimal(Pages.AIBasicTab.MAWB.volume_measure_input.get_value())

    # ? KNOWN ISSUE
    assert abs(exp_total_gross_kgs - gross_kg) <= 0.05, "Expect gross kg to be [{0}]. but get [{1}]".format(
        exp_total_gross_kgs, gross_kg
    )
    assert abs(exp_total_gross_lb - gross_lb) <= 0.05, "Expect gross lb to be [{0}]. but get [{1}]".format(
        exp_total_gross_lb, gross_lb
    )
    assert abs(exp_total_vol_kgs - vol_kg) <= 0.05, "Expect volume kg to be [{0}]. but get [{1}]".format(
        exp_total_vol_kgs, vol_kg
    )
    assert abs(exp_total_vol_cbm - vol_cbm) <= 0.05, "Expect volume cbm to be [{0}]. but get [{1}]".format(
        exp_total_vol_cbm, vol_cbm
    )
    # ?


@Given("the user created an AI Shipment with {count} of HAWB")
def step_impl(context, count):
    create_ai_mawb_table = transfer_to_feature_table(
        """
        | field              | attribute    | action | data                 |
        | MAWB No.           | input        | input  | 911-{randomNo(7)}    |
    """
    )
    create_ai_hawb_table = transfer_to_feature_table(
        """
        | field              | attribute    | action | data                 |
        | HAWB No.           | input        | input  | 911-{randomNo(7)}    |
    """
    )

    Driver.open(gl.URL.AI_NEW_SHIPMENT)
    Pages.AIBasicTab.MAWB.more_button.click()
    input_dynamic_datas(create_ai_mawb_table, "Pages.AIBasicTab.MAWB")
    Pages.Common.save_button.click()
    assert Pages.Common.save_msg.is_visible(timeout=30) is True

    # create new HAWBs
    for i in range(1, int(count) + 1):
        Pages.AIBasicTab.add_hawb_button.click()
        sleep(2)
        Pages.AIBasicTab.HAWB(i).more_button.click()
        hawb_model = input_dynamic_datas(create_ai_hawb_table, "Pages.AIBasicTab.HAWB({})".format(i))
        Pages.Common.save_button.click()
        Pages.Common.spin_bar.gone()
        assert Pages.Common.save_msg.is_visible(timeout=10) is True
        context._vp.add_dict(dict_name="hawb_model", value={"{}".format(i): hawb_model})

    context._vp.add_v("shipment_url", Driver.get_url())


@Then("the default pakage unit for AI MAWB is correct")
def step_impl(context):
    default_package_unit = gl.gofreight_config.get_default_package(gl.user_info.office, GBy.OID)
    package_unit = Pages.AIBasicTab.MAWB.package_unit_autocomplete.get_value()
    assert package_unit == default_package_unit, "Wrong default package unit. Expect [{0}]".format(default_package_unit)


@Then("the default pakage unit for AI HAWB({hbl_index}) is correct")
def step_impl(context, hbl_index):
    default_package_unit = gl.gofreight_config.get_default_package(gl.user_info.office, GBy.OID)
    package_unit = Pages.AIBasicTab.HAWB(int(hbl_index)).package_unit_autocomplete.get_value()
    assert package_unit == default_package_unit, "Wrong default package unit. Expect [{0}]".format(default_package_unit)


@When("the user enter AI MAWB 'Shipment' datas as '{name}'")
def step_impl(context, name):
    current_page_class_name = "Pages.AIBasicTab.MAWB"
    mawb_model = input_dynamic_datas(context.table, current_page_class_name)
    context._vp.add_dict(dict_name="mawb_model", value={name: mawb_model})


@When("the user enter AI MAWB '{name}' 'Route' datas")
def step_impl(context, name):
    current_page_class_name = "Pages.AIBasicTab.MAWB"
    model = input_dynamic_datas(context.table, current_page_class_name)
    context._vp.add_dict(dict_name="mawb_route_model", value={name: model})


@When("the user enter AI MAWB '{name}' 'More' datas")
def step_impl(context, name):
    current_page_class_name = "Pages.AIBasicTab.MAWB"
    model = input_dynamic_datas(context.table, current_page_class_name)
    context._vp.add_dict(dict_name="mawb_route_model", value={name: model})


@When("the user enter AI shipment '{name}' HAWB({hbl_index}) datas")
def step_impl(context, name, hbl_index):
    current_page_class_name = f"Pages.AIBasicTab.HAWB({ hbl_index })"
    model = input_dynamic_datas(context.table, current_page_class_name)
    context._vp.add_dict(dict_name="hawb_model", value={"{}_{}".format(name, hbl_index): model})


@When("the user click AI 'Add HAWB' button")
def step_impl(context):
    Pages.AIBasicTab.add_hawb_button.click()
    sleep(5)


@When("the user expand AI MAWB block")
def step_impl(context):
    # 如果沒展開再click expand button
    if Pages.AIBasicTab.MAWB.more_button.is_disable():  # TODO GQT-423 如果眼睛看不到 more button 的話（理論上會在 dom 上，但不重要）
        Pages.AIBasicTab.MAWB.expand_button.click()


@When("the user close AI MAWB block")
def step_impl(context):
    # 如果沒展開再click expand button
    if not Pages.AIBasicTab.MAWB.more_button.is_disable():  # TODO GQT-423 如果眼睛看不到 more button 的話（理論上會在 dom 上，但不重要）
        Pages.AIBasicTab.MAWB.expand_button.click()


@When("the user click AI MAWB 'Set Dimensions' button")
def step_impl(context):
    Pages.AIBasicTab.MAWB.set_dimensions_button.click()
    sleep(2)


@When("the user click AI HAWB({hbl_index}) 'Set Dimensions' button")
def step_impl(context, hbl_index):
    Pages.AIBasicTab.HAWB(int(hbl_index)).set_dimensions_button.click()
    sleep(2)


@When("the user click AI 'Sum Package & Weight' button")
def step_impl(context):
    Pages.AIBasicTab.MAWB.sum_package_and_weight_button.click()


@When("the user save AI 'Dimensions' settings")
def step_impl(context):
    Pages.AIBasicTab.Dimension.dimension_apply_button.click()
    sleep(2)


@When("the user cancel AI 'Dimensions' settings")
def step_impl(context):
    Pages.AIBasicTab.Dimension.dimension_cancel_button.click()
    sleep(2)


@When("the user cancel AI MAWB 'Route' settings")
def step_impl(context):
    Pages.AIBasicTab.MAWB.route_cancel_button.click()
    sleep(2)


@Then("field 'Chargeable Weight' for AI MAWB should be autofilled with right numbers")
def step_impl(context):
    gr_weight = Pages.AIBasicTab.MAWB.gross_weight_input.get_value()
    chargable_weight = Pages.AIBasicTab.MAWB.chargeable_weight_input.get_value()
    vol_weight = Pages.AIBasicTab.MAWB.volume_weight_input.get_value()

    # The value of 'Chargable Weight' should be equal to 'Volume Weight' or 'Gross Weight' if one and only one of
    # them are filled. If both of them are filled, the value of 'Chargable Weight' should be equal to the larger one
    if vol_weight == "" and gr_weight != "":
        assert gr_weight == chargable_weight, "Expect [{0}]. but get [{1}]".format(gr_weight, chargable_weight)
    elif vol_weight != "" and gr_weight == "":
        assert vol_weight == chargable_weight, "Expect [{0}]. but get [{1}]".format(vol_weight, chargable_weight)
    elif float(gr_weight) > float(vol_weight):
        assert gr_weight == chargable_weight, "Expect [{0}]. but get [{1}]".format(gr_weight, chargable_weight)
    else:
        assert vol_weight == chargable_weight, "Expect [{0}]. but get [{1}]".format(vol_weight, chargable_weight)


@Then("field 'Chargeable Weight' for AI HAWB({hbl_index}) should be autofilled with right numbers")
def step_impl(context, hbl_index):
    hbl_index = int(hbl_index)
    gr_weight = Pages.AIBasicTab.HAWB(hbl_index).gross_weight_input.get_value()
    chargable_weight = Pages.AIBasicTab.HAWB(hbl_index).chargeable_weight_input.get_value()
    vol_weight = Pages.AIBasicTab.HAWB(hbl_index).volume_weight_input.get_value()

    if (vol_weight == "" and gr_weight != "") or float(gr_weight) > float(vol_weight):
        assert gr_weight == chargable_weight, "Expect [{0}]. but get [{1}]".format(gr_weight, chargable_weight)
    else:
        assert vol_weight == chargable_weight, "Expect [{0}]. but get [{1}]".format(vol_weight, chargable_weight)


@When("the user click AI MAWB 'Connecting Flight' button")
def step_impl(context):
    Pages.AIBasicTab.MAWB.connecting_flight_button.click()
    sleep(2)


@When("the user save AI MAWB 'Route' settings")
def step_impl(context):
    Pages.AIBasicTab.MAWB.route_save_button.click()
    sleep(2)


@When("the user click 'Gross Weight LB' for AI MAWB")
def step_impl(context):
    Pages.AIBasicTab.MAWB.gross_weight_lb_input.click()


@When("the user click 'Gross Weight LB' for AI HAWB({hbl_index})")
def step_impl(context, hbl_index):
    Pages.AIBasicTab.HAWB(int(hbl_index)).gross_weight_lb_input.click()


@Then("'Chargeable Weight' value should be the same as 'Gross Weight' value for AI MAWB")
def step_impl(context):
    value_1 = Pages.AIBasicTab.MAWB.chargeable_weight_input.click()
    value_2 = Pages.AIBasicTab.MAWB.gross_weight_input.click()
    lb_value_1 = Pages.AIBasicTab.MAWB.chargeable_weight_lb_input.click()
    lb_value_2 = Pages.AIBasicTab.MAWB.gross_weight_lb_input.click()

    assert value_1 == value_2, "Expect chargeable weight to be [{0}]. but get [{1}]".format(value_2, value_1)
    assert lb_value_1 == lb_value_2, "Expect chargeable weight lb to be [{0}]. but get [{1}]".format(
        lb_value_2, lb_value_1
    )


@Then("'Chargeable Weight' value should be the same as 'Gross Weight' value for AI HAWB({hbl_index})")
def step_impl(context, hbl_index):
    hbl_index = int(hbl_index)
    value_1 = Pages.AIBasicTab.HAWB(hbl_index).chargeable_weight_input.click()
    value_2 = Pages.AIBasicTab.HAWB(hbl_index).gross_weight_input.click()
    lb_value_1 = Pages.AIBasicTab.HAWB(hbl_index).chargeable_weight_lb_input.click()
    lb_value_2 = Pages.AIBasicTab.HAWB(hbl_index).gross_weight_lb_input.click()

    assert value_1 == value_2, "Expect chargeable weight to be [{0}]. but get [{1}]".format(value_2, value_1)
    assert lb_value_1 == lb_value_2, "Expect chargeable weight lb to be [{0}]. but get [{1}]".format(
        lb_value_2, lb_value_1
    )


@Then("'Volume Weight' data in the 'New Shipment' page for AI MAWB are correct")
def step_impl(context):

    volume_weight = Pages.AIBasicTab.MAWB.volume_weight_input.get_value()
    volume_measure = Pages.AIBasicTab.MAWB.volume_measure_input.get_value()
    dimension_sum = context._vp.get("dimension_sum")

    # ? KNOWN ISSUE
    assert (
        Decimal(dimension_sum["kgs_sum"]) - Decimal(volume_weight) <= 0.05
    ), "Expect volume weight to be [{0}]. but get [{1}]".format(dimension_sum["kgs_sum"], Decimal(volume_weight))
    assert (
        Decimal(dimension_sum["cbm_sum"]) - Decimal(volume_measure) <= 1
    ), "Expect volume measure to be [{0}]. but get [{1}]".format(dimension_sum["cbm_sum"], Decimal(volume_measure))
    # ?


@Then("'Volume Weight' data in the 'New Shipment' page for AI HAWB({hbl_index}) are correct")
def step_impl(context, hbl_index):
    hbl_index = int(hbl_index)
    volume_weight = Pages.AIBasicTab.HAWB(hbl_index).volume_weight_input.get_value()
    volume_measure = Pages.AIBasicTab.HAWB(hbl_index).volume_measure_input.get_value()
    dimension_sum = context._vp.get("dimension_sum")

    # ? KNOWN ISSUE
    assert (
        Decimal(dimension_sum["kgs_sum"]) - Decimal(volume_weight) <= 0.05
    ), "Expect volume weight to be [{0}]. but get [{1}]".format(dimension_sum["kgs_sum"], Decimal(volume_weight))
    assert (
        Decimal(dimension_sum["cbm_sum"]) - Decimal(volume_measure) <= 1
    ), "Expect volume measure to be [{0}]. but get [{1}]".format(dimension_sum["cbm_sum"], Decimal(volume_measure))
    # ?


@When("the user click 'Copy P.O.' button for AI HAWB({hbl_index})")
def step_impl(context, hbl_index):
    hbl_index = int(hbl_index)
    description = (
        context._vp.get("description")
        if context._vp.has_v("description")
        else Pages.AIBasicTab.HAWB(hbl_index).description_input.get_value()
    )
    Pages.AIBasicTab.HAWB(hbl_index).copy_po_button.click()
    description += "\n\nP.O. NO.\n"
    description += ", ".join(
        Pages.AIBasicTab.HAWB(hbl_index).customer_reference___po_no_tag_input.get_value().split(";")
    )
    context._vp.add_v(v_name="description", value=description)


@When("the user click 'Copy Commodity' button for AI HAWB({hbl_index})")
def step_impl(context, hbl_index):
    hbl_index = int(hbl_index)
    description = (
        context._vp.get("description")
        if context._vp.has_v("description")
        else Pages.AIBasicTab.HAWB(hbl_index).description_input.get_value()
    )
    Pages.AIBasicTab.HAWB(hbl_index).copy_commodity_button.click()
    description += "\n\n" + Pages.AIBasicTab.HAWB(hbl_index).Commodity(1).commodity_description_input.get_value()
    context._vp.add_v(v_name="description", value=description)


@When("the user click 'Copy Commodity & HTS' button for AI HAWB({hbl_index})")
def step_impl(context, hbl_index):
    hbl_index = int(hbl_index)
    description = (
        context._vp.get("description")
        if context._vp.has_v("description")
        else Pages.AIBasicTab.HAWB(hbl_index).description_input.get_value()
    )
    Pages.AIBasicTab.HAWB(hbl_index).copy_commodity_and_hts_button.click()
    description += (
        "\n\n"
        + Pages.AIBasicTab.HAWB(hbl_index).Commodity(1).commodity_description_input.get_value()
        + " "
        + Pages.AIBasicTab.HAWB(hbl_index).Commodity(1).hts_code_input.get_value()
    )
    context._vp.add_v(v_name="description", value=description)


@Given("the user has a AI MAWB with {count} HAWB as '{name}'")
def step_impl(context, count, name):
    create_ai_mawb_table = transfer_to_feature_table(
        """
        | field    | attribute  | action | data              |
        | MAWB No. | input      | input  | 911-{randomNo(7)} |
    """
    )

    create_ai_hawb_table = transfer_to_feature_table(
        """
        | field                         | attribute    | action               | data                                       |
        | HAWB No.                      | input        | input                | 333-{randomNo(7)}                          |
        | HSN                           | input        | input                | HSN{randomNo(6)}                           |
        | Shipper                       | autocomplete | input                | {randomTradePartner}                       |
        | Consignee                     | autocomplete | input and close memo | {randomTradePartner}                       |
        | Customs Broker                | autocomplete | input                | {randomTradePartner}                       |
        | Freight Location              | autocomplete | input                | {randomTradePartner}                       |
        | Final Destination             | autocomplete | input                | usdhd                                      |
        | Final ETA                     | datepicker   | input                | {today+4}                                  |
        | Trucker                       | autocomplete | input                | {randomTradePartner}                       |
        | Last Free Day                 | datepicker   | input                | {today+12}                                 |
        | Storage Start Date            | datepicker   | input                | {today+13}                                 |
        | Freight                       | select       | random select        |                                            |
        | Sales Type                    | select       | random select        |                                            |
        | Package                       | input        | input                | {randInt(1,999)}                           |
        | Package Unit                  | autocomplete | input                | tank                                       |
        | Gross Weight                  | input        | input                | {randInt(1,999)}                           |
        | IT NO.                        | input        | input                | ITN{randN(6)}                              |
        | Class of Entry                | input        | input                | CAI{randomNo(4)}                           |
        | IT Date                       | datepicker   | input                | {today+10}                                 |
        | IT Issued Location            | autocomplete | input                | 1901                                       |
        | Cargo Released To             | input        | input                | CARGO{randN(4)}                            |
        | C. Released Date              | datepicker   | input                | {today+11}                                 |
        | Door Delivered                | datepicker   | input                | {today+11}                                 |
        | Ship Type                     | select       | random select        |                                            |
        | Incoterms                     | select       | random select        |                                            |
        | Service Term From             | select       | random select        |                                            |
        | Service Term To               | select       | random select        |                                            |
        | E-Commerce                    | checkbox     | tick                 | {randomOnOff}                              |
        | Display Unit                  | select       | select               | Show KG / CBM                              |
        | Customer Reference / P.O. No. | tag input    | input                | {randomNo(6)}                              |
        | Mark                          | input        | input                | THis is Air Import - HAWB : MARK           |
        | Description                   | input        | input                | THis is Air Import - HAWB : DESCRIPTION    |
        | Remark                        | input        | input                | THis is Air Import - HAWB : REMARK SECTION |
    """
    )

    create_ai_hawb_dimension_table = transfer_to_feature_table(
        """
        | field  | attribute | action | data             |
        | Length | input     | input  | {randInt(1,200)} |
        | Width  | input     | input  | {randInt(1,200)} |
        | Height | input     | input  | {randInt(1,200)} |
        | PCS    | input     | input  | {randInt(1,99)}  |
    """
    )

    create_ai_hawb_sub_hawb_table = transfer_to_feature_table(
        """
        | field                | attribute    | action | data                     |
        | Sub HAWB             | input        | input  | SUBHAWB TEXT             |
        | Description / IT No. | input        | input  | SUBHAWB TEXT_DESCRIPTION |
        | PCS                  | input        | input  | {randN(2)}               |
        | PKG Unit             | autocomplete | input  | tank                     |
        | Amount               | input        | input  | {randN(3)}               |
    """
    )

    create_ai_hawb_commodity_table = transfer_to_feature_table(
        """
        | field                 | attribute    | action | data              |
        | Commodity Description | input        | input  | {randomCommodity} |
        | HTS Code              | input        | input  | HTS{randomNo(6)}  |
    """
    )

    # create a new MAWB
    Driver.open(gl.URL.AI_NEW_SHIPMENT)
    Pages.AIBasicTab.MAWB.more_button.click()
    mawb_model = input_dynamic_datas(create_ai_mawb_table, "Pages.AIBasicTab.MAWB")
    Pages.Common.save_button.click()
    assert Pages.Common.save_msg.is_visible(timeout=30) is True

    # add additional field
    mawb_model.add(
        field="File No.",
        attribute="input",
        data=Pages.AIBasicTab.MAWB.file_no_input.get_value(),
    )
    mawb_model.add(
        field="Office",
        attribute="autocomplete",
        data=Pages.AIBasicTab.MAWB.office_autocomplete.get_value(),
    )

    context._vp.add_dict(dict_name="mawb_model", value={name: mawb_model})

    # create new HAWBs
    for i in range(1, int(count) + 1):
        Pages.AIBasicTab.add_hawb_button.click()
        sleep(2)
        Pages.AIBasicTab.HAWB(i).more_button.click()
        hawb_model = input_dynamic_datas(create_ai_hawb_table, "Pages.AIBasicTab.HAWB({})".format(i))

        # dimension
        Pages.AIBasicTab.HAWB(i).set_dimensions_button.click()
        Pages.AIBasicTab.Dimension.dimension_add_button.click()
        hawb_dimension_model = input_dynamic_datas(create_ai_hawb_dimension_table, "Pages.AIBasicTab.Dimension(1)")
        Pages.AIBasicTab.Dimension.dimension_apply_button.click()
        Pages.Common.spin_bar.gone()

        # sub hawb
        Pages.AIBasicTab.HAWB(i).sub_hawb_add_button.click()
        hawb_sub_hawb_model = input_dynamic_datas(
            create_ai_hawb_sub_hawb_table,
            "Pages.AIBasicTab.HAWB({}).Sub_HAWB({}, 1)".format(i, i),
        )

        # commodity
        Pages.AIBasicTab.HAWB(i).commodity_add_button.click()
        hawb_commodity_model = input_dynamic_datas(
            create_ai_hawb_commodity_table,
            "Pages.AIBasicTab.HAWB({}).Commodity({}, 1)".format(i, i),
        )

        # TODO warehouse receipt

        Pages.Common.save_button.click()
        Pages.Common.spin_bar.gone()
        assert Pages.Common.save_msg.is_visible(timeout=10) is True

        hawb_model.add(
            field="Notify",
            attribute="autocomplete",
            data=Pages.AIBasicTab.HAWB(i).customer_autocomplete.get_value(),
        )
        hawb_model.add(
            field="Customer",
            attribute="autocomplete",
            data=Pages.AIBasicTab.HAWB(i).customer_autocomplete.get_value(),
        )
        hawb_model.add(
            field="Bill To",
            attribute="autocomplete",
            data=Pages.AIBasicTab.HAWB(i).bill_to_autocomplete.get_value(),
        )
        hawb_model.add(
            field="Sales",
            attribute="autocomplete",
            data=Pages.AIBasicTab.HAWB(i).sales_autocomplete.get_value(),
        )
        hawb_model.add(
            field="Delivery Location",
            attribute="autocomplete",
            data=Pages.AIBasicTab.HAWB(i).delivery_location_autocomplete.get_value(),
        )
        hawb_model.add(
            field="Gross Weight LB",
            attribute="input",
            data=Pages.AIBasicTab.HAWB(i).gross_weight_lb_input.get_value(),
        )
        hawb_model.add(
            field="Chargeable Weight",
            attribute="input",
            data=Pages.AIBasicTab.HAWB(i).chargeable_weight_input.get_value(),
        )
        hawb_model.add(
            field="Chargeable Weight LB",
            attribute="input",
            data=Pages.AIBasicTab.HAWB(i).chargeable_weight_lb_input.get_value(),
        )
        hawb_model.add(
            field="Volume Weight",
            attribute="input",
            data=Pages.AIBasicTab.HAWB(i).volume_weight_input.get_value(),
        )
        hawb_model.add(
            field="Volume Measure",
            attribute="input",
            data=Pages.AIBasicTab.HAWB(i).volume_measure_input.get_value(),
        )

        context._vp.add_dict(dict_name="hawb_model", value={"{}_{}".format(name, i): hawb_model})
        context._vp.add_dict(
            dict_name="hawb_dimension_model",
            value={"{}_{}".format(name, i): hawb_dimension_model},
        )
        context._vp.add_dict(
            dict_name="hawb_sub_hawb_model",
            value={"{}_{}".format(name, i): hawb_sub_hawb_model},
        )
        context._vp.add_dict(
            dict_name="hawb_commodity_model",
            value={"{}_{}".format(name, i): hawb_commodity_model},
        )

    context._vp.add_dict(dict_name="shipment_url", value={name: Driver.get_url()})


@Given("the user has a AI MAWB with {count} HAWB as '{name}' with only required fields filled")
def step_impl(context, count, name):
    create_ai_mawb_table = transfer_to_feature_table(
        """
        | field    | attribute  | action | data              |
        | MAWB No. | input      | input  | 911-{randomNo(7)} |
    """
    )

    if gl.company in ["OLC", "MASCOT"]:
        create_ai_hawb_table = transfer_to_feature_table(
            """
            | field                         | attribute    | action               | data                                     |
            | HAWB No.                      | input        | input                | 333-{randomNo(7)}                        |
            | Sales                         | autocomplete | input                | {randomSales}                            |
        """
        )
    else:
        create_ai_hawb_table = transfer_to_feature_table(
            """
            | field                         | attribute    | action               | data                                     |
            | HAWB No.                      | input        | input                | 333-{randomNo(7)}                        |
        """
        )

    # create a new MAWB
    Driver.open(gl.URL.AI_NEW_SHIPMENT)
    Pages.AIBasicTab.MAWB.more_button.click()
    mawb_model = input_dynamic_datas(create_ai_mawb_table, "Pages.AIBasicTab.MAWB")
    Pages.Common.save_button.click()
    assert Pages.Common.save_msg.is_visible(timeout=30) is True

    # add additional field
    mawb_model.add(
        field="File No.",
        attribute="input",
        data=Pages.AIBasicTab.MAWB.file_no_input.get_value(),
    )
    mawb_model.add(
        field="Office",
        attribute="autocomplete",
        data=Pages.AIBasicTab.MAWB.office_autocomplete.get_value(),
    )

    context._vp.add_dict(dict_name="mawb_model", value={name: mawb_model})

    # create new HAWBs
    for i in range(1, int(count) + 1):
        Pages.AIBasicTab.add_hawb_button.click()
        sleep(2)
        Pages.AIBasicTab.HAWB(i).more_button.click()
        hawb_model = input_dynamic_datas(create_ai_hawb_table, "Pages.AIBasicTab.HAWB({})".format(i))

        Pages.Common.save_button.click()
        Pages.Common.spin_bar.gone()
        assert Pages.Common.save_msg.is_visible(timeout=10) is True

        hawb_model.add(
            field="Sales",
            attribute="autocomplete",
            data=Pages.AIBasicTab.HAWB(i).sales_autocomplete.get_value(),
        )

        context._vp.add_dict(dict_name="hawb_model", value={"{}_{}".format(name, i): hawb_model})

    context._vp.add_dict(dict_name="shipment_url", value={name: Driver.get_url()})


@When("the user click AI '{name}' HAWB({index}) 'Tools -> Copy To'")
def step_impl(context, name, index):
    Driver.open(context._vp.get("shipment_url")[name])
    Pages.Common.spin_bar.gone()
    Pages.AIBasicTab.HAWB(index).hbl_side_panel_button.click()
    sleep(2)
    Pages.AIBasicTab.HAWB(index).tools_button.click()
    Pages.AIBasicTab.HAWB(index).tools_copy_to_button.click()


@When("the user input '{name}' to AI copy HAWB to")
def step_impl(context, name):
    mbl_no = context._vp.get("mawb_model")[name].get_data("MAWB No.")
    Pages.AIBasicTab.CopyHBLToMBL.select_mbl_autocomplete.input(mbl_no)


@When("the user click 'OK' button in AI 'Copy To' dialog")
def step_impl(context):
    Pages.AIBasicTab.CopyHBLToMBL.ok_button.click()


@Then("the link of '{name}' should show in AI 'Copy To' dialog")
def step_impl(context, name):
    exp = context._vp.get("mawb_model")[name].get_data("File No.")
    v = Pages.AIBasicTab.CopyHBLToMBL.mbl_link.get_value()
    assert exp == v, "Link shoud be [{0}], not [{1}]".format(exp, v)


@When("the user click the AI copied link")
def step_impl(context):
    Pages.AIBasicTab.CopyHBLToMBL.mbl_link.click()
    Driver.switch_to(window_index=1)
    Pages.Common.spin_bar.gone()


@Then("the HAWB({index_1}) should copy from AI '{name}' HAWB({index_2})")
def step_impl(context, index_1, name, index_2):
    Pages.AIBasicTab.HAWB(index_1).hbl_side_panel_button.click()
    Pages.AIBasicTab.HAWB(index_1).more_button.click()
    model = context._vp.get("hawb_model")["{}_{}".format(name, index_2)]
    model.set_page_class_name("Pages.AIBasicTab.HAWB({})".format(index_1))
    vm_fields = model.get_all_fields()
    copied_fields = [i["field"] for i in context.table]
    for f in vm_fields:
        if f not in copied_fields:
            f_dict = model.pop(f)
            if f == "HAWB No.":
                data = "COPY-1"
            else:
                data = ""
            model.add(field=f, attribute=f_dict[model.ATTRIBUTE], data=data)
    # TODO check whether op is the current character
    model.verify()

    # dimension should be copied to
    Pages.AIBasicTab.HAWB(index_1).set_dimensions_button.click()
    dim_model = context._vp.get("hawb_dimension_model")["{}_{}".format(name, index_2)]
    dim_model.set_page_class_name("Pages.AIBasicTab.Dimension(1)")
    dim_model.verify()
    Pages.AIBasicTab.Dimension.dimension_cancel_button.click()

    # sub hawb should not be copied to
    assert Pages.AIBasicTab.HAWB(index_1).Sub_HAWB(1).sub_hawb_input.is_invisible(), "sub hawb should not be copied to"

    # commodity should not be copied to
    assert (
        Pages.AIBasicTab.HAWB(index_1).Commodity(1).commodity_description_input.is_invisible()
    ), "commodity should not be copied to"

    # TODO warehouse receipt


@Then("the AI HAWB({index}) should have 'COPY-1' as HAWB NO.")
def step_impl(context, index):
    exp = "COPY-1"
    hawb_no = Pages.AIBasicTab.HAWB(index).hawb_no_input.get_value()
    assert hawb_no == exp, "HAWB No. should be [{0}], not [{1}]".format(exp, hawb_no)


@When("the user click 'Accounting' tab of AI")
def step_impl(context):
    Pages.AITab.accounting_tab.click()
    Pages.Common.spin_bar.gone()


@When("the user add revenue freights to AI HAWB({index}) AR")
def step_impl(context, index):
    Pages.AISidePanel.hawb_select_button(int(index)).click()
    Pages.Common.spin_bar.gone()
    freight_index = 1
    for row in context.table:
        Pages.AIAccountingBillingBasedTab.HAWB.revenue.new_button.click()
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
        model = input_dynamic_datas(
            action_table,
            "Pages.AIAccountingBillingBasedTab.HAWB.revenue({})".format(freight_index),
        )

        context._vp.add_dict(
            dict_name="hawb_freight_model",
            value={"{}_{}".format(index, freight_index): model},
        )
        freight_index += 1


@When("the user click AI Accounting 'Save' Button")
def step_impl(context):
    Pages.AIAccountingBillingBasedTab.save_button.click()
    Pages.Common.spin_bar.gone()
