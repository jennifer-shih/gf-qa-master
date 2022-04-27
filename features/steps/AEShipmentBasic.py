import random
from decimal import Decimal
from time import sleep

from behave import Given, Then, When

from config import globalparameter as gl
from src.api.gofreight_config import GBy
from src.drivers.driver import Driver
from src.exception.exception import StepParaNotDefinedError
from src.helper.script import input_dynamic_datas
from src.helper.transfer import transfer_data, transfer_to_feature_table
from src.pages import AEBasicTab, Common


@Then("the default issuing carrier agent is correct")
def step_impl(context):
    default_issue_carrier = gl.bill_to_nick_name[gl.company]
    assert (
        AEBasicTab.MAWB.issuing_carrier_agent_autocomplete.get_value() == default_issue_carrier
    ), "Wrong default issuing carrier/agent. Expect [{0}]".format(default_issue_carrier)


@Then("the default MAWB NO. has correct prefix")
def step_impl(context):
    default_mawb_no_prefix = "911-"
    assert (
        AEBasicTab.MAWB.mawb_no_input.get_value() == default_mawb_no_prefix
    ), "Wrong default MAWB NO. Expect [{0}]".format(default_mawb_no_prefix)


@Then("the default ITN NO. is correct")
def step_impl(context):
    if gl.company == "OLC":
        default_ito_no = ""
    else:
        default_ito_no = "NO EEI 30.37(a)"
    assert AEBasicTab.MAWB.itn_no_input.get_value() == default_ito_no, "Wrong default ITN NO. Expect [{0}]".format(
        default_ito_no
    )


@Then("the default shipper is correct")
def step_impl(context):
    default_shipper = gl.bill_to_nick_name[gl.company]
    assert (
        AEBasicTab.MAWB.shipper_shipping_agent_autocomplete.get_value() == default_shipper
    ), "Wrong default shipper (shipping agent). Expect [{0}]".format(default_shipper)


@Then("the default D.V. carriage is correct")
def step_impl(context):
    default_dv_carriage = "NVD"
    assert (
        AEBasicTab.MAWB.dv_carriage_input.get_value() == default_dv_carriage
    ), "Wrong default D.V. carriage Expect [{0}]".format(default_dv_carriage)


@Then("the default D.V. customs is correct")
def step_impl(context):
    default_dv_customs = "NCV"
    assert (
        AEBasicTab.MAWB.dv_customs_input.get_value() == default_dv_customs
    ), "Wrong default D.V. customs Expect [{0}]".format(default_dv_customs)


@Then("the default insurance is correct")
def step_impl(context):
    default_insurance = "XXX"
    assert (
        AEBasicTab.MAWB.insurance_input.get_value() == default_insurance
    ), "Wrong default insurance Expect [{0}]".format(default_insurance)


@Then("the default carrier agent in Other Charge({oc_index}) is correct")
def step_impl(context, oc_index):
    oc_index = int(oc_index)
    default_carrier_agent = "AGENT"
    if oc_index == 1 or oc_index == 2:
        default_carrier_agent = "CARRIER"
    assert (
        AEBasicTab.MAWB.OtherCharges(oc_index).carrier_agent_select.get_value() == default_carrier_agent
    ), "Wrong default carrier agent Expect [{0}]".format(default_carrier_agent)


@Then("the default collect prepaid in Other Charge({oc_index}) is correct")
def step_impl(context, oc_index):
    oc_index = int(oc_index)
    default_collect_prepaid = "COLLECT"
    if oc_index == 1 or oc_index == 2:
        default_collect_prepaid = "PREPAID"
    assert (
        AEBasicTab.MAWB.OtherCharges(oc_index).collect_prepaid_select.get_value() == default_collect_prepaid
    ), "Wrong default collect prepaid Expect [{0}]".format(default_collect_prepaid)


@Then("the default charge item in Other Charge({oc_index}) is correct")
def step_impl(context, oc_index):
    oc_index = int(oc_index)
    default_charge_item = "AWB Cancellation"
    if oc_index == 1:
        default_charge_item = "Fuel Surcharge — Due Issuing Carrier"
    elif oc_index == 2:
        default_charge_item = "Security (Surcharge/premiums)"
    assert (
        AEBasicTab.MAWB.OtherCharges(oc_index).charge_item_select.get_value() == default_charge_item
    ), "Wrong default charge item Expect [{0}]".format(default_charge_item)


@Then("the default description in Other Charge({oc_index}) is correct")
def step_impl(context, oc_index):
    oc_index = int(oc_index)
    default_description = ""
    if oc_index == 1:
        default_description = "Fuel Surcharge — Due Issuing Carrier"
    elif oc_index == 2:
        default_description = "Security (Surcharge/premiums)"
    assert (
        AEBasicTab.MAWB.OtherCharges(oc_index).description_input.get_value() == default_description
    ), "Wrong default description Expect [{0}]".format(default_description)


@When("the user click AE MAWB 'More' button")
def step_impl(context):
    # 如果沒展開再click more button
    if not AEBasicTab.MAWB.e_commerce_checkbox.is_interactable():
        AEBasicTab.MAWB.more_button.click()


@When("the user tick AE 'Direct Master' checkbox")
def step_impl(context):
    AEBasicTab.MAWB.direct_master_checkbox.tick(True)
    Common.spin_bar.gone()


@When("the user click AE HAWB({hbl_index}) 'More' button")
def step_impl(context, hbl_index):
    hbl_index = int(hbl_index)
    # 如果沒展開再click more button
    if not AEBasicTab.HAWB(hbl_index).e_commerce_checkbox.is_interactable():
        AEBasicTab.HAWB(hbl_index).more_button.click()


@When("the user input information for AE MAWB '{name}' 'Other Charge'")
def step_impl(context, name):
    models = []
    current_page_class_name = "AEBasicTab.MAWB.OtherCharges"
    for index in range(len(context.table.rows)):
        action_table = [
            {
                "field": "Charge Amount",
                "attribute": "input",
                "action": "input",
                "data": context.table[index]["Charge Amount"],
            }
        ]
        models.append(input_dynamic_datas(action_table, current_page_class_name + "(" + str(index + 1) + ")"))
    context._vp.add_dict(dict_name="mawb_other_charge_model", value={"{}".format(name): models})


@When("the user input information for AE shipment '{name}' HAWB({hbl_index}) 'Other Charge'")
def step_impl(context, name, hbl_index):
    hbl_index = int(hbl_index)
    models = []
    current_page_class_name = "AEBasicTab.HAWB(" + str(hbl_index) + ").OtherCharges"
    for _ in context.table:
        AEBasicTab.HAWB(hbl_index).other_charge_add_button.click()
    for index in range(len(context.table.rows)):
        action_table = [
            {
                "field": "Carrier/Agent",
                "attribute": "select",
                "action": "select",
                "data": context.table[index]["Carrier/Agent"],
            }
        ]
        action_table.append(
            {
                "field": "Collect/Prepaid",
                "attribute": "select",
                "action": "select",
                "data": context.table[index]["Collect/Prepaid"],
            }
        )
        action_table.append(
            {
                "field": "Charge Item",
                "attribute": "select",
                "action": "random select",
                "data": "",
            }
        )
        action_table.append(
            {
                "field": "Charge Amount",
                "attribute": "input",
                "action": "input",
                "data": context.table[index]["Charge Amount"],
            }
        )

        models.append(
            input_dynamic_datas(
                action_table,
                current_page_class_name + "(" + str(hbl_index) + "," + str(index + 1) + ")",
            )
        )
    context._vp.add_dict(
        dict_name="hawb_other_charge_model",
        value={"{}_{}".format(name, hbl_index): models},
    )


@When("the user input information for AE MAWB '{name}' 'Commodity'")
def step_impl(context, name):
    models = []
    current_page_class_name = "AEBasicTab.MAWB.Commodity"
    for index in range(len(context.table.rows)):
        po_no_options = AEBasicTab.MAWB.po_no_tag_input.get_value().split(";")
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

        AEBasicTab.MAWB.commodity_add_button.click()
        models.append(input_dynamic_datas(action_table, current_page_class_name + "(" + str(index + 1) + ")"))
    context._vp.add_dict(dict_name="mawb_commodity_model", value={"{}".format(name): models})


@When("the user input information for AE shipment '{name}' HAWB({hbl_index}) 'Commodity'")
def step_impl(context, name, hbl_index):
    hbl_index = int(hbl_index)
    models = []
    current_page_class_name = "AEBasicTab.HAWB(" + str(hbl_index) + ").Commodity"
    for index in range(len(context.table.rows)):
        po_no_options = AEBasicTab.HAWB(hbl_index).po_no_tag_input.get_value().split(";")
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

        AEBasicTab.HAWB(hbl_index).commodity_add_button.click()
        models.append(
            input_dynamic_datas(
                action_table,
                current_page_class_name + "(" + str(hbl_index) + "," + str(index + 1) + ")",
            )
        )
    context._vp.add_dict(
        dict_name="hawb_commodity_model",
        value={"{}_{}".format(name, hbl_index): models},
    )


@When("the user expand MAWB 'More' block")
def step_impl(context):
    # 如果沒展開再click more expand button
    if not AEBasicTab.MAWB.commodity_add_button.is_interactable():
        AEBasicTab.MAWB.more_expand_button.click()


@When("the user expand HAWB({hbl_index}) 'More' block")
def step_impl(context, hbl_index):
    hbl_index = int(hbl_index)
    # 如果沒展開再click more expand button
    if not AEBasicTab.HAWB(hbl_index).prepaid_valuation_input.is_interactable():
        AEBasicTab.HAWB(hbl_index).more_expand_button.click()


@Then("the AE MAWB '{name}' '{data_type}' data is saved")
def step_impl(context, name, data_type):
    # go to the shipment which just created
    Driver.open(context._vp.get("url"))
    Common.spin_bar.gone()
    AEBasicTab.MAWB.more_button.click()

    if data_type == "Volume Weight" or data_type == "Other Charge" or data_type == "Commodity":
        if data_type == "Volume Weight":
            AEBasicTab.MAWB.set_dimensions_button.click()
        else:
            AEBasicTab.MAWB.more_expand_button.click()
        data_type = data_type.replace(" ", "_").lower()
        models = context._vp.get("mawb_{}_model".format(data_type))[name]
        sleep(0.5)
        for model in models:
            model.verify()

    elif data_type == "Route":
        model = context._vp.get("mawb_route_model")[name]
        AEBasicTab.MAWB.connecting_flight_button.click()
        model.verify()


@Then("the AE shipment '{name}' HAWB({hbl_index}) '{data_type}' data is saved")
def step_impl(context, name, hbl_index, data_type):
    # go to the shipment which just created
    Driver.open(context._vp.get("url"))
    Common.spin_bar.gone()
    AEBasicTab.HAWB(hbl_index).more_button.click()

    if data_type == "Volume Weight":
        AEBasicTab.HAWB(hbl_index).set_dimensions_button.click()

    data_type = data_type.replace(" ", "_").lower()
    models = context._vp.get("hawb_{}_model".format(data_type))["{}_{}".format(name, hbl_index)]
    for model in models:
        model.verify()


@Then("'HAWB NO.' should be autofilled with '{prefix}'")
def step_impl(context, prefix):
    assert AEBasicTab.MAWB.mawb_no_input.get_value() == prefix, "Wrong HAWB NO. Expect [{0}]".format(prefix)


@Then("amount should be autofilled with right numbers")
def step_impl(context):
    sleep(1)

    exp_gross_amount = Decimal(AEBasicTab.MAWB.gross_weight_input.get_value()) * Decimal(
        AEBasicTab.MAWB.buying_rate_input.get_value()
    )
    gross_amount = Decimal(AEBasicTab.MAWB.gross_weight_amount_input.get_value())

    exp_chargeable_amount = Decimal(AEBasicTab.MAWB.chargeable_weight_input.get_value()) * Decimal(
        AEBasicTab.MAWB.selling_rate_input.get_value()
    )
    chargeable_amount = Decimal(AEBasicTab.MAWB.chargeable_weight_amount_input.get_value())

    # ? KNOWN ISSUEs
    assert abs(exp_gross_amount - gross_amount) <= 0.05, "Expect gross amount to be [{0}]. but get [{1}]".format(
        exp_gross_amount, gross_amount
    )
    assert (
        abs(exp_chargeable_amount - chargeable_amount) <= 0.05
    ), "Expect chargeableamount to be [{0}]. but get [{1}]".format(exp_chargeable_amount, chargeable_amount)
    # ?


@Then("the 'Nature and Quantity of Goods' field are correct")
def step_impl(context):
    description = AEBasicTab.MAWB.nature_and_quantity_of_goods_input.get_value()
    exp_description = context._vp.get("description")
    assert exp_description == description, "Expect [{0}]. but get [{1}]".format(exp_description, description)


@Then("the AE '{name}' 'Volume Weight' won't change")
def step_impl(context, name):
    # the user is very cautios so she click cancel to see what will happen
    models = context._vp.get("mawb_volume_weight_model")[name]
    AEBasicTab.MAWB.set_dimensions_button.click()
    for model in models:
        model.verify()
    AEBasicTab.Dimension.dimension_cancel_button.click()


@Then("the AE '{name}' 'Route' won't change")
def step_impl(context, name):
    # the user is very cautios so she click cancel to see what will happen
    model = context._vp.get("mawb_route_model")[name]
    AEBasicTab.MAWB.connecting_flight_button.click()
    model.verify()
    AEBasicTab.MAWB.route_cancel_button.click()


@Then("the AE MAWB '{name}' 'Volume Weight' data are correct")
@Then("the AE shipment '{name}' HAWB({hbl_index}) 'Volume Weight' data are correct")
def step_impl(context, name, hbl_index=None):
    if hbl_index:
        dimensions = context._vp.get("hawb_dimension_model")["{}_{}".format(name, hbl_index)]
    else:
        dimensions = context._vp.get("mawb_dimension_model")[name]
    for index in range(len(dimensions)):
        kgs = AEBasicTab.Dimension(index + 1).kgs_label.get_value().replace(",", "")
        lbs = AEBasicTab.Dimension(index + 1).lbs_label.get_value().replace(",", "")
        cbm = AEBasicTab.Dimension(index + 1).cbm_label.get_value().replace(",", "")
        cft = AEBasicTab.Dimension(index + 1).cft_label.get_value().replace(",", "")

        # ? KNOWN ISSUE
        assert (
            abs(Decimal(dimensions[index]["volume_kgs"]) - Decimal(kgs)) <= 0.05
        ), "Expect volume kgs to be [{0}]. but get [{1}]".format(dimensions[index]["volume_kgs"], Decimal(kgs))
        assert (
            abs(Decimal(dimensions[index]["volume_lbs"]) - Decimal(lbs)) <= 0.05
        ), "Expect volume lbs to be [{0}]. but get [{1}]".format(dimensions[index]["volume_lbs"], Decimal(lbs))
        assert (
            abs(Decimal(dimensions[index]["measure_cbm"]) - Decimal(cbm)) <= 0.05
        ), "Expect measure cbm to be [{0}]. but get [{1}]".format(dimensions[index]["measure_cbm"], Decimal(cbm))
        assert (
            abs(Decimal(dimensions[index]["measure_cft"]) - Decimal(cft)) <= 1
        ), "Expect measure cft to be [{0}]. but get [{1}]".format(dimensions[index]["measure_cft"], Decimal(cft))
        # ?


@Then("the AE MAWB '{name}' summarized 'Volume Weight' data are correct")
@Then("the AE shipment '{name}' HAWB({hbl_index}) summarized 'Volume Weight' data are correct")
def step_impl(context, name, hbl_index=None):
    if hbl_index:
        dimensions = context._vp.get("hawb_dimension_model")["{}_{}".format(name, hbl_index)]
    else:
        dimensions = context._vp.get("mawb_dimension_model")[name]
    exp_total_pcs, exp_total_kgs, exp_total_lbs, exp_total_cbm, exp_total_cft = (
        Decimal(0),
        Decimal(0),
        Decimal(0),
        Decimal(0),
        Decimal(0),
    )
    for index in range(len(dimensions)):
        exp_total_pcs += Decimal(AEBasicTab.Dimension(index + 1).pcs_input.get_value())
        exp_total_kgs += Decimal(AEBasicTab.Dimension(index + 1).kgs_label.get_value().replace(",", ""))
        exp_total_lbs += Decimal(AEBasicTab.Dimension(index + 1).lbs_label.get_value().replace(",", ""))
        exp_total_cbm += Decimal(AEBasicTab.Dimension(index + 1).cbm_label.get_value().replace(",", ""))
        exp_total_cft += Decimal(AEBasicTab.Dimension(index + 1).cft_label.get_value().replace(",", ""))

    pcs_sum = Decimal(AEBasicTab.Dimension.dimension_pcs_sum_label.get_value().replace(",", ""))
    kgs_sum = Decimal(AEBasicTab.Dimension.dimension_kgs_sum_label.get_value().replace(",", ""))
    lbs_sum = Decimal(AEBasicTab.Dimension.dimension_lbs_sum_label.get_value().replace(",", ""))
    cbm_sum = Decimal(AEBasicTab.Dimension.dimension_cbm_sum_label.get_value().replace(",", ""))
    cft_sum = Decimal(AEBasicTab.Dimension.dimension_cft_sum_label.get_value().replace(",", ""))

    # ? KNOWN ISSUE
    assert abs(exp_total_pcs - pcs_sum) <= 0.05, "Expect pcs sum to be [{0}]. but get [{1}]".format(
        exp_total_pcs, pcs_sum
    )
    assert abs(exp_total_kgs - kgs_sum) <= 0.05, "Expect kgs sum to be [{0}]. but get [{1}]".format(
        exp_total_kgs, kgs_sum
    )
    assert abs(exp_total_lbs - lbs_sum) <= 0.05, "Expect pclbss sum to be [{0}]. but get [{1}]".format(
        exp_total_lbs, lbs_sum
    )
    assert abs(exp_total_cbm - cbm_sum) <= 0.05, "Expect cbm sum to be [{0}]. but get [{1}]".format(
        exp_total_cbm, cbm_sum
    )
    assert abs(exp_total_cft - cft_sum) <= 1, "Expect cft sum to be [{0}]. but get [{1}]".format(exp_total_cft, cft_sum)
    # ?
    context._vp.add_v(v_name="dimension_sum", value={"kgs_sum": str(kgs_sum), "cbm_sum": str(cbm_sum)})


@Given("the user has an AE Shipment without any HAWB")
def step_impl(context):
    create_ae_mawb_table = transfer_to_feature_table(
        """
        | field               | attribute  | action | data      |
        | Departure Date/Time | datepicker | input  | {today+1} |
    """
    )

    Driver.open(gl.URL.AE_NEW_SHIPMENT)
    AEBasicTab.MAWB.more_button.click()
    input_dynamic_datas(create_ae_mawb_table, "AEBasicTab.MAWB")
    Common.save_button.click()
    assert Common.save_msg.is_visible(timeout=30) is True


@Then("the default ITN NO. for AE HAWB({hbl_index}) is correct")
def step_impl(context, hbl_index):
    # 如果沒展開再click expand button
    if not AEBasicTab.MAWB.more_button.is_interactable():
        AEBasicTab.MAWB.expand_button.click()

    default_itn_no = AEBasicTab.MAWB.itn_no_input.get_value()
    assert (
        AEBasicTab.HAWB(hbl_index).itn_no_input.get_value() == default_itn_no
    ), "Wrong default ITN NO. Expect [{0}]".format(default_itn_no)


@Then("AE HAWB({hbl_idx}) fileds should be same as MAWB")
def step_impl(context, hbl_idx):
    hbl_idx = int(hbl_idx)
    if not AEBasicTab.MAWB.more_button.is_interactable():
        AEBasicTab.MAWB.expand_button.click()
    if not AEBasicTab.HAWB(hbl_idx).more_button.is_interactable():
        AEBasicTab.HAWB(1).hbl_side_panel_button.click()

    for row in context.table:
        mbl_field = row["MAWB"]
        hbl_field = row["HAWB"]

        if hbl_field == "Booking Date" and mbl_field == "AWB Date":
            exp_val = AEBasicTab.MAWB.awb_date_datepicker.get_value()
            val = AEBasicTab.HAWB(hbl_idx).booking_date_datepicker.get_value()
        elif hbl_field == mbl_field == "Oversea Agent":
            exp_val = AEBasicTab.MAWB.consignee_oversea_agent_autocomplete.get_value()
            val = AEBasicTab.HAWB(hbl_idx).oversea_agent_autocomplete.get_value()
        elif hbl_field == mbl_field == "Insurance":
            exp_val = AEBasicTab.MAWB.insurance_input.get_value()
            val = AEBasicTab.HAWB(hbl_idx).insurance_input.get_value()
        elif hbl_field == mbl_field == "Departure":
            exp_val = AEBasicTab.MAWB.departure_autocomplete.get_value()
            val = AEBasicTab.HAWB(hbl_idx).departure_input.get_value()
        elif hbl_field == mbl_field == "Destination":
            exp_val = AEBasicTab.MAWB.destination_autocomplete.get_value()
            val = AEBasicTab.HAWB(hbl_idx).destination_input.get_value()
        elif hbl_field == mbl_field == "D.V. Carriage":
            exp_val = AEBasicTab.MAWB.dv_carriage_input.get_value()
            val = AEBasicTab.HAWB(hbl_idx).dv_carriage_input.get_value()
        elif hbl_field == mbl_field == "D.V. Customs":
            exp_val = AEBasicTab.MAWB.dv_customs_input.get_value()
            val = AEBasicTab.HAWB(hbl_idx).dv_customs_input.get_value()
        else:
            raise StepParaNotDefinedError(mbl_field, hbl_field)
        assert exp_val == val, f"HBL({hbl_idx}) field expect to be [{exp_val}], but get [{val}]"


@Then("AE HAWB({hbl_idx}) fields should be")
def step_impl(context, hbl_idx):
    hbl_idx = int(hbl_idx)
    if not AEBasicTab.MAWB.more_button.is_interactable():
        AEBasicTab.MAWB.expand_button.click()
    if not AEBasicTab.HAWB(hbl_idx).more_button.is_interactable():
        AEBasicTab.HAWB(1).hbl_side_panel_button.click()

    for row in context.table:
        field = row["field"]

        if field == "ITN NO.":
            exp_val = AEBasicTab.MAWB.itn_no_input.get_value()
            val = AEBasicTab.HAWB(hbl_idx).itn_no_input.get_value()
        elif field == "Issuing Carrier":
            exp_val = AEBasicTab.MAWB.issuing_carrier_agent_autocomplete.get_value()
            val = AEBasicTab.HAWB(hbl_idx).issuing_carrier_agent_autocomplete.get_value()
        elif field == "WT/VAL":
            exp_val = "PPD"
            val = AEBasicTab.HAWB(hbl_idx).wt_val_radio_group.get_value()
        elif field == "Other":
            exp_val = "PPD"
            val = AEBasicTab.HAWB(hbl_idx).other_radio_group.get_value()
        else:
            raise StepParaNotDefinedError(field)
        assert exp_val == val, f"HBL({hbl_idx}) field expect to be [{exp_val}], but get [{val}]"


@Then("the shipment '{name}' HAWB({hbl_index}) in 'Air Export' will be created")
def step_impl(context, name, hbl_index):
    model = context._vp.get("hawb_model")["{}_{}".format(name, hbl_index)]

    # go to the shipment which just created
    Driver.open(context._vp.get("url"))
    Common.spin_bar.gone()
    AEBasicTab.HAWB(hbl_index).more_button.click()

    model.verify()


@Then("'Customer', 'Bill To' should be the same values as 'Actual Shipper' for HAWB({hbl_index})")
def step_impl(context, hbl_index):
    actual_shipper = AEBasicTab.HAWB(hbl_index).actual_shipper_autocomplete.get_value()
    customer = AEBasicTab.HAWB(hbl_index).customer_autocomplete.get_value()
    bill_to = AEBasicTab.HAWB(hbl_index).bill_to_autocomplete.get_value()

    assert actual_shipper == bill_to, "Expect 'bill to' to be [{0}]. but get [{1}]".format(actual_shipper, bill_to)
    assert actual_shipper == customer, "Expect customer to be [{0}]. but get [{1}]".format(actual_shipper, customer)


@When("the user click 'Gross Weight (SHPR) LB' for AE HAWB({hbl_index})")
def step_impl(context, hbl_index):
    AEBasicTab.HAWB(hbl_index).gross_weight_shpr_lb_input.click()


@Then("all 'Weight' fields for AE HAWB({hbl_index}) should be autofilled with right numbers")
def step_impl(context, hbl_index):
    gr_weight_shpr = AEBasicTab.HAWB(hbl_index).gross_weight_shpr_input.get_value()
    gr_weight_cnee = AEBasicTab.HAWB(hbl_index).gross_weight_cnee_input.get_value()
    chargable_weight_shpr = AEBasicTab.HAWB(hbl_index).chargeable_weight_shpr_input.get_value()
    chargable_weight_cnee = AEBasicTab.HAWB(hbl_index).chargeable_weight_cnee_input.get_value()
    vol_weight = AEBasicTab.HAWB(hbl_index).volume_weight_input.get_value()

    if (vol_weight == "" and gr_weight_shpr != "") or float(gr_weight_shpr) > float(vol_weight):
        assert gr_weight_shpr == gr_weight_cnee, "Expect gross weight consignee to be [{0}]. but get [{1}]".format(
            gr_weight_shpr, gr_weight_cnee
        )
        assert (
            gr_weight_shpr == chargable_weight_shpr
        ), "Expect chargeable weight shipper to be [{0}]. but get [{1}]".format(gr_weight_shpr, chargable_weight_shpr)
        assert (
            gr_weight_shpr == chargable_weight_cnee
        ), "Expect chargeable weight consignee to be [{0}]. but get [{1}]".format(gr_weight_shpr, chargable_weight_cnee)
    else:
        assert gr_weight_shpr == gr_weight_cnee, "Expect gross weight consignee to be [{0}]. but get [{1}]".format(
            gr_weight_shpr, gr_weight_cnee
        )
        assert (
            vol_weight == chargable_weight_shpr
        ), "Expect chargeable weight shipper to be [{0}]. but get [{1}]".format(vol_weight, chargable_weight_shpr)
        assert (
            vol_weight == chargable_weight_cnee
        ), "Expect chargeable weight consignee to be [{0}]. but get [{1}]".format(vol_weight, chargable_weight_cnee)


@Then("the 'Nature and Quantitfy of Goods' field for AE HAWB({hbl_index}) are correct")
def step_impl(context, hbl_index):
    description = AEBasicTab.HAWB(hbl_index).nature_and_quantity_of_goods_input.get_value()
    exp_description = context._vp.get("description")
    assert exp_description == description, "Expect [{0}]. but get [{1}]".format(exp_description, description)


@Then("the HAWBs weight should be sumed up in AE MAWB block")
def step_impl(context):
    exp_total_vol_kgs, exp_total_vol_cbm = Decimal(0), Decimal(0)
    exp_total_gross_kgs, exp_total_gross_lb = Decimal(0), Decimal(0)
    if AEBasicTab.MAWB.more_button.is_interactable():
        AEBasicTab.MAWB.expand_button.click()
    for index in range(1, 3):
        AEBasicTab.HAWB(index).hbl_side_panel_button.click()
        gross_weight_shpr_input = AEBasicTab.HAWB(index).gross_weight_shpr_input.get_value()
        gross_weight_shpr_lb_input = AEBasicTab.HAWB(index).gross_weight_shpr_lb_input.get_value()
        volume_weight_input = AEBasicTab.HAWB(index).volume_weight_input.get_value()
        volume_measure_input = AEBasicTab.HAWB(index).volume_measure_input.get_value()
        exp_total_gross_kgs += Decimal(gross_weight_shpr_input) if gross_weight_shpr_input != "" else 0
        exp_total_gross_lb += Decimal(gross_weight_shpr_lb_input) if gross_weight_shpr_lb_input != "" else 0
        exp_total_vol_kgs += Decimal(volume_weight_input) if volume_weight_input != "" else 0
        exp_total_vol_cbm += Decimal(volume_measure_input) if volume_measure_input != "" else 0

    if not AEBasicTab.MAWB.more_button.is_interactable():
        AEBasicTab.MAWB.expand_button.click()
    gross_kg = Decimal(AEBasicTab.MAWB.gross_weight_input.get_value())
    gross_lb = Decimal(AEBasicTab.MAWB.gross_weight_lb_input.get_value())
    vol_kg = Decimal(AEBasicTab.MAWB.volume_weight_input.get_value())
    vol_cbm = Decimal(AEBasicTab.MAWB.volume_measure_input.get_value())

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


@Then("the default pakage unit for AE {mbl_or_hbl} is correct")
def step_impl(context, mbl_or_hbl):
    default_package_unit = gl.gofreight_config.get_default_package(gl.user_info.office, GBy.OID)
    if mbl_or_hbl == "MAWB":
        package_unit = AEBasicTab.MAWB.package_unit_autocomplete.get_value()
    elif mbl_or_hbl == "HAWB":
        package_unit = AEBasicTab.HAWB.package_unit_autocomplete.get_value()
    assert package_unit == default_package_unit, "Wrong default package unit. Expect [{0}]".format(default_package_unit)


@When("the user enter AE MAWB 'Shipment' datas as '{name}'")  #! Deprecated
@When("the user fills in AE MAWB 'Basic' data as '{name}'")
def step_impl(context, name):
    current_page_class_name = "AEBasicTab.MAWB"
    model = input_dynamic_datas(context.table, current_page_class_name)
    context._vp.add_dict(dict_name="mawb_model", value={name: model})


@When("the user enter AE MAWB '{name}' 'Route' datas")
def step_impl(context, name):
    current_page_class_name = "AEBasicTab.MAWB"
    model = input_dynamic_datas(context.table, current_page_class_name)
    context._vp.add_dict(dict_name="mawb_route_model", value={name: model})


@When("the user enter AE MAWB '{name}' 'More' datas")
def step_impl(context, name):
    current_page_class_name = "AEBasicTab.MAWB"
    model = input_dynamic_datas(context.table, current_page_class_name)
    context._vp.add_dict(dict_name="mawb_more_model", value={name: model})


@When("the user enter AE shipment '{name}' HAWB({hbl_index}) '{datatype}' datas")
def step_impl(context, name, hbl_index, datatype):
    # datatype could be Shipment, More
    current_page_class_name = "AEBasicTab.HAWB(" + hbl_index + ")"
    model = input_dynamic_datas(context.table, current_page_class_name)
    datatype = datatype.replace(" ", "_").lower()
    if datatype == "more":
        context._vp.add_dict(dict_name="hawb_more_model", value={"{}_{}".format(name, hbl_index): model})
    else:
        context._vp.add_dict(dict_name="hawb_model", value={"{}_{}".format(name, hbl_index): model})


@When("the user click AE 'Add HAWB' button")
def step_impl(context):
    AEBasicTab.add_hawb_button.click()
    sleep(5)


@When("the user expand AE MAWB block")
def step_impl(context):
    # 如果沒展開再click expand button
    if not AEBasicTab.MAWB.more_button.is_interactable():  # TODO GQT-423 如果眼睛看不到 more button 的話（理論上會在 dom 上，但不重要）
        AEBasicTab.MAWB.expand_button.click()


@When("the user close AE MAWB block")
def step_impl(context):
    # 如果沒展開再click expand button
    if AEBasicTab.MAWB.more_button.is_interactable():  # TODO GQT-423 如果眼睛看不到 more button 的話（理論上會在 dom 上，但不重要）
        AEBasicTab.MAWB.expand_button.click()


@When("the user click AE MAWB 'Set Dimensions' button")
def step_impl(context):
    AEBasicTab.MAWB.set_dimensions_button.click()
    sleep(2)


@When("the user click AE HAWB({hbl_index}) 'Set Dimensions' button")
def step_impl(context, hbl_index):
    AEBasicTab.HAWB(int(hbl_index)).set_dimensions_button.click()
    sleep(2)


@When("the user click AE 'Sum Package & Weight' button")
def step_impl(context):
    AEBasicTab.MAWB.sum_package_and_weight_button.click()


@When("the user save AE 'Dimensions' settings")
def step_impl(context):
    AEBasicTab.Dimension.dimension_apply_button.click()
    sleep(2)


@When("the user cancel AE 'Dimensions' settings")
def step_impl(context):
    AEBasicTab.Dimension.dimension_cancel_button.click()
    sleep(2)


@When("the user cancel AE MAWB 'Route' settings")
def step_impl(context):
    AEBasicTab.MAWB.route_cancel_button.click()
    sleep(2)


@Then("field 'Chargeable Weight' for AE MAWB should be autofilled with right numbers")
def step_impl(context):
    gr_weight = AEBasicTab.MAWB.gross_weight_input.get_value()
    chargable_weight = AEBasicTab.MAWB.chargeable_weight_input.get_value()
    vol_weight = AEBasicTab.MAWB.volume_weight_input.get_value()

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


@Then("field 'Chargeable Weight' for AE HAWB({hbl_index}) should be autofilled with right numbers")
def step_impl(context, hbl_index):
    hbl_index = int(hbl_index)
    gr_weight = AEBasicTab.HAWB(hbl_index).gross_weight_input.get_value()
    chargable_weight = AEBasicTab.HAWB(hbl_index).chargeable_weight_input.get_value()
    vol_weight = AEBasicTab.HAWB(hbl_index).volume_weight_input.get_value()

    if (vol_weight == "" and gr_weight != "") or float(gr_weight) > float(vol_weight):
        assert gr_weight == chargable_weight, "Expect [{0}]. but get [{1}]".format(gr_weight, chargable_weight)
    else:
        assert vol_weight == chargable_weight, "Expect [{0}]. but get [{1}]".format(vol_weight, chargable_weight)


@When("the user click AE MAWB 'Connecting Flight' button")
def step_impl(context):
    AEBasicTab.MAWB.connecting_flight_button.click()
    sleep(2)


@When("the user save AE MAWB 'Route' settings")
def step_impl(context):
    AEBasicTab.MAWB.route_save_button.click()
    sleep(2)


@When("the user click 'Gross Weight LB' for AE MAWB")
def step_impl(context):
    AEBasicTab.MAWB.gross_weight_lb_input.click()


@When("the user click 'Gross Weight LB' for AE HAWB({hbl_index})")
def step_impl(context, hbl_index):
    AEBasicTab.HAWB(int(hbl_index)).gross_weight_lb_input.click()


@Then("'Chargeable Weight' value should be the same as 'Gross Weight' value for AE MAWB")
def step_impl(context):
    value_1 = AEBasicTab.MAWB.chargeable_weight_input.click()
    value_2 = AEBasicTab.MAWB.gross_weight_input.click()
    lb_value_1 = AEBasicTab.MAWB.chargeable_weight_lb_input.click()
    lb_value_2 = AEBasicTab.MAWB.gross_weight_lb_input.click()

    assert value_1 == value_2, "Expect chargeable weight to be [{0}]. but get [{1}]".format(value_2, value_1)
    assert lb_value_1 == lb_value_2, "Expect chargeable weight lb to be [{0}]. but get [{1}]".format(
        lb_value_2, lb_value_1
    )


@Then("'Volume Weight' data in the 'New Shipment' page for AE MAWB '{name}' are correct")
def step_impl(context, name):

    volume_weight = AEBasicTab.MAWB.volume_weight_input.get_value()
    volume_measure = AEBasicTab.MAWB.volume_measure_input.get_value()
    dimension_sum = context._vp.get("dimension_sum")

    # ? KNOWN ISSUE
    assert (
        Decimal(dimension_sum["kgs_sum"]) - Decimal(volume_weight) <= 0.05
    ), "Expect volume weight to be [{0}]. but get [{1}]".format(dimension_sum["kgs_sum"], Decimal(volume_weight))
    assert (
        Decimal(dimension_sum["cbm_sum"]) - Decimal(volume_measure) <= 1
    ), "Expect volume measure to be [{0}]. but get [{1}]".format(dimension_sum["cbm_sum"], Decimal(volume_measure))
    # ?


@Then("'Volume Weight' data in the 'New Shipment' page for AE shipment '{name}' HAWB({hbl_index}) are correct")
def step_impl(context, name, hbl_index):
    hbl_index = int(hbl_index)
    volume_weight = AEBasicTab.HAWB(hbl_index).volume_weight_input.get_value()
    volume_measure = AEBasicTab.HAWB(hbl_index).volume_measure_input.get_value()
    dimension_sum = context._vp.get("dimension_sum")

    # ? KNOWN ISSUE
    assert (
        Decimal(dimension_sum["kgs_sum"]) - Decimal(volume_weight) <= 0.05
    ), "Expect volume weight to be [{0}]. but get [{1}]".format(dimension_sum["kgs_sum"], Decimal(volume_weight))
    assert (
        Decimal(dimension_sum["cbm_sum"]) - Decimal(volume_measure) <= 1
    ), "Expect volume measure to be [{0}]. but get [{1}]".format(dimension_sum["cbm_sum"], Decimal(volume_measure))
    # ?


@When("the user click 'Copy P.O.' button for AE MAWB")
def step_impl(context):
    description = (
        context._vp.get("description")
        if context._vp.has_v("description")
        else AEBasicTab.MAWB.nature_and_quantity_of_goods_input.get_value()
    )
    AEBasicTab.MAWB.copy_po_button.click()
    description += "\n\nP.O. NO.\n"
    description += ", ".join(AEBasicTab.MAWB.po_no_tag_input.get_value().split(";"))
    context._vp.add_v(v_name="description", value=description)


@When("the user click 'Copy P.O.' button for AE HAWB({hbl_index})")
def step_impl(context, hbl_index):
    hbl_index = int(hbl_index)
    description = (
        context._vp.get("description")
        if context._vp.has_v("description")
        else AEBasicTab.HAWB(hbl_index).nature_and_quantity_of_goods_input.get_value()
    )
    AEBasicTab.HAWB(hbl_index).copy_po_button.click()
    description += "\n\nP.O. NO.\n"
    description += ", ".join(AEBasicTab.HAWB(hbl_index).po_no_tag_input.get_value().split(";"))
    context._vp.add_v(v_name="description", value=description)


@When("the user click 'Copy Commodity' button for AE MAWB")
def step_impl(context):
    description = (
        context._vp.get("description")
        if context._vp.has_v("description")
        else AEBasicTab.MAWB.nature_and_quantity_of_goods_input.get_value()
    )
    AEBasicTab.MAWB.copy_commodity_button.click()
    description += "\n\n" + AEBasicTab.MAWB.Commodity(1).commodity_description_input.get_value()
    context._vp.add_v(v_name="description", value=description)


@When("the user click 'Copy Commodity' button for AE HAWB({hbl_index})")
def step_impl(context, hbl_index):
    hbl_index = int(hbl_index)
    description = (
        context._vp.get("description")
        if context._vp.has_v("description")
        else AEBasicTab.HAWB(hbl_index).nature_and_quantity_of_goods_input.get_value()
    )
    AEBasicTab.HAWB(hbl_index).copy_commodity_button.click()
    description += "\n\n" + AEBasicTab.HAWB(hbl_index).Commodity(1).commodity_description_input.get_value()
    context._vp.add_v(v_name="description", value=description)


@When("the user click 'Copy Commodity & HTS' button for AE MAWB")
def step_impl(context):
    description = (
        context._vp.get("description")
        if context._vp.has_v("description")
        else AEBasicTab.MAWB.nature_and_quantity_of_goods_input.get_value()
    )
    AEBasicTab.MAWB.copy_commodity_and_hts_button.click()
    description += (
        "\n\n"
        + AEBasicTab.MAWB.Commodity(1).commodity_description_input.get_value()
        + " "
        + AEBasicTab.MAWB.Commodity(1).hts_code_input.get_value()
    )
    context._vp.add_v(v_name="description", value=description)


@When("the user click 'Copy Commodity & HTS' button for AE HAWB({hbl_index})")
def step_impl(context, hbl_index):
    hbl_index = int(hbl_index)
    description = (
        context._vp.get("description")
        if context._vp.has_v("description")
        else AEBasicTab.HAWB(hbl_index).nature_and_quantity_of_goods_input.get_value()
    )
    AEBasicTab.HAWB(hbl_index).nature_and_quantity_of_goods_input.get_value()
    AEBasicTab.HAWB(hbl_index).copy_commodity_and_hts_button.click()
    description += (
        "\n\n"
        + AEBasicTab.HAWB(hbl_index).Commodity(1).commodity_description_input.get_value()
        + " "
        + AEBasicTab.HAWB(hbl_index).Commodity(1).hts_code_input.get_value()
    )
    context._vp.add_v(v_name="description", value=description)


@Given("the user has a AE MAWB with {count} HAWB as '{name}'")
def step_impl(context, count, name):
    create_ae_mawb_table = transfer_to_feature_table(
        """
        | field               | attribute  | action | data              |
        | MAWB No.            | input      | input  | 911-{randomNo(7)} |
        | Departure Date/Time | datepicker | input  | {today+1}         |
    """
    )

    if gl.company == "SFI":
        create_ae_hawb_table = transfer_to_feature_table(
            """
            | field                                 | attribute    | action               | data                                                            |
            | Actual Shipper                        | autocomplete | input and close memo | {randomTradePartner}                                            |
            | Consignee                             | autocomplete | input                | {randomTradePartner}                                            |
            | Notify                                | autocomplete | input                | {randomTradePartner}                                            |
            | Oversea Agent                         | autocomplete | input and close memo | {randomTradePartner}                                            |
            | Trucker                               | autocomplete | input                | {randomTradePartner}                                            |
            | Sub Agent AWB                         | checkbox     | tick                 | {on}                                                            |
            | Cargo Pickup                          | autocomplete | input                | {randomTradePartner}                                            |
            | Delivery To/Pier                      | autocomplete | input                | {randomTradePartner}                                            |
            | Cargo Type                            | select       | random select        |                                                                 |
            | Sales Type                            | select       | random select        |                                                                 |
            | Ship Type                             | select       | random select        |                                                                 |
            | WT/VAL                                | radio group  | random click         |                                                                 |
            | Other                                 | radio group  | random click         |                                                                 |
            | Incoterms                             | select       | random select        |                                                                 |
            | Service Term From                     | select       | random select        |                                                                 |
            | Service Term To                       | select       | random select        |                                                                 |
            | Package                               | input        | input                | {randInt(1,10)}                                                 |
            | Package Unit                          | autocomplete | input                | tank                                                            |
            | Buying Rate                           | input        | input                | {randInt(1,10)}                                                 |
            | Buying Rate Unit                      | select       | select               | LB                                                              |
            | Selling Rate                          | input        | input                | {randInt(1,10)}                                                 |
            | Selling Rate Unit                     | select       | select               | LB                                                              |
            | Gross Weight (SHPR)                   | input        | input                | {randInt(1,999)}                                                |
            | L/C NO.                               | input        | input                | LC{randN(6)}                                                    |
            | L/C Issue Bank                        | input        | input                | LCB{randN(6)}                                                   |
            | L/C Issue Date                        | datepicker   | input                | {today+10}                                                      |
            | Customer Ref. No.                     | input        | input                | CR{randN(6)}                                                    |
            | Agent Ref. No.                        | input        | input                | AN{randN(6)}                                                    |
            | Export Ref. No.                       | input        | input                | EX{randN(6)}                                                    |
            | Rate                                  | select       | random select        |                                                                 |
            | Display Unit                          | select       | select               | Show KG / CBM                                                   |
            | E-Commerce                            | checkbox     | tick                 | {randomOnOff}                                                   |
            | P.O. No.                              | tag input    | input                | {randomNo(6)}                                                   |
            | Mark                                  | input        | input                | THIS IS AIR EXPORT - HBL : MARK                                 |
            | Nature and Quantity of Goods          | input        | input                | THIS IS HAWB : NATURE AND QUANTITY OF GOODS                     |
            | Manifest Nature and Quantity of Goods | input        | input                | THIS IS AIR EXPORT - HAWB MENIFEST NATURE AND QUANTITY OF GOODS |
            | Handling Information                  | input        | input                | THIS IS AIR EXPORT - HAWB HANDLING INFORMATION                  |
        """
        )
    elif gl.company == "LOHAN" or gl.company == "OLC":
        create_ae_hawb_table = transfer_to_feature_table(
            """
            | field                                 | attribute    | action               | data                                                            |
            | Actual Shipper                        | autocomplete | input and close memo | {randomTradePartner}                                            |
            | Consignee                             | autocomplete | input                | {randomTradePartner}                                            |
            | Notify                                | autocomplete | input                | {randomTradePartner}                                            |
            | Oversea Agent                         | autocomplete | input and close memo | {randomTradePartner}                                            |
            | Trucker                               | autocomplete | input                | {randomTradePartner}                                            |
            | Sub Agent AWB                         | checkbox     | tick                 | {on}                                                            |
            | Cargo Pickup                          | autocomplete | input                | {randomTradePartner}                                            |
            | Delivery To/Pier                      | autocomplete | input                | {randomTradePartner}                                            |
            | Cargo Type                            | select       | random select        |                                                                 |
            | Sales Type                            | select       | random select        |                                                                 |
            | Ship Type                             | select       | random select        |                                                                 |
            | WT/VAL                                | radio group  | random click         |                                                                 |
            | Other                                 | radio group  | random click         |                                                                 |
            | Incoterms                             | select       | random select        |                                                                 |
            | Service Term From                     | select       | random select        |                                                                 |
            | Service Term To                       | select       | random select        |                                                                 |
            | Package                               | input        | input                | {randInt(1,10)}                                                 |
            | Package Unit                          | autocomplete | input                | tank                                                            |
            | Buying Rate                           | input        | input                | {randInt(1,10)}                                                 |
            | Buying Rate Unit                      | select       | select               | LB                                                              |
            | Selling Rate                          | input        | input                | {randInt(1,10)}                                                 |
            | Selling Rate Unit                     | select       | select               | LB                                                              |
            | Gross Weight (SHPR)                   | input        | input                | {randInt(1,999)}                                                |
            | L/C NO.                               | input        | input                | LC{randN(6)}                                                    |
            | L/C Issue Bank                        | input        | input                | LCB{randN(6)}                                                   |
            | L/C Issue Date                        | datepicker   | input                | {today+10}                                                      |
            | Customer Ref. No.                     | input        | input                | CR{randN(6)}                                                    |
            | Agent Ref. No.                        | input        | input                | AN{randN(6)}                                                    |
            | Export Ref. No.                       | input        | input                | EX{randN(6)}                                                    |
            | Rate                                  | select       | random select        |                                                                 |
            | Display Unit                          | select       | select               | Show KG / CBM                                                   |
            | E-Commerce                            | checkbox     | tick                 | {randomOnOff}                                                   |
            | P.O. No.                              | tag input    | input                | {randomNo(6)}                                                   |
            | Mark                                  | input        | input                | THIS IS AIR EXPORT - HBL : MARK                                 |
            | Nature and Quantity of Goods          | input        | input                | THIS IS HAWB : NATURE AND QUANTITY OF GOODS                     |
            | Handling Information                  | input        | input                | THIS IS AIR EXPORT - HAWB HANDLING INFORMATION                  |
        """
        )

    create_ae_hawb_dimension_table = transfer_to_feature_table(
        """
        | field  | attribute | action | data             |
        | Length | input     | input  | {randInt(1,200)} |
        | Width  | input     | input  | {randInt(1,200)} |
        | Height | input     | input  | {randInt(1,200)} |
        | PCS    | input     | input  | {randInt(1,99)}  |
    """
    )

    create_ae_hawb_commodity_table = transfer_to_feature_table(
        """
        | field                 | attribute    | action | data              |
        | Commodity Description | input        | input  | {randomCommodity} |
        | HTS Code              | input        | input  | HTS{randomNo(6)}  |
    """
    )

    create_ae_hawb_other_charge_table = transfer_to_feature_table(
        """
        | field           | attribute | action        | data             |
        | Carrier/Agent   | select    | select        | CARRIER          |
        | Collect/Prepaid | select    | select        | PREPAID          |
        | Charge Item     | select    | random select |                  |
        | Description     | input     | input         | Test             |
        | Charge Amount   | input     | input         | {randInt(1,999)} |
    """
    )

    create_ae_hawb_more_table = transfer_to_feature_table(
        """
        | field                                | attribute | action | data             |
        | Prepaid Valuation                    | input     | input  | {randInt(1,999)} |
        | Prepaid Tax                          | input     | input  | {randInt(1,999)} |
        | Prepaid Currency Conversion Rates    | input     | input  | {randInt(1,999)} |
        | Collect Valuation                    | input     | input  | {randInt(1,999)} |
        | Collect Tax                          | input     | input  | {randInt(1,999)} |
        | Collect CC Charges in Dest. Currency | input     | input  | {randInt(1,999)} |
        | Collect Charges at Destination       | input     | input  | {randInt(1,999)} |
    """
    )

    # create a new MAWB
    Driver.open(gl.URL.AE_NEW_SHIPMENT)
    AEBasicTab.MAWB.more_button.click()
    mawb_model = input_dynamic_datas(create_ae_mawb_table, "AEBasicTab.MAWB")
    Common.save_button.click()
    assert Common.save_msg.is_visible(timeout=30) is True

    # add additional field
    mawb_model.add(
        field="File No.",
        attribute="input",
        data=AEBasicTab.MAWB.file_no_input.get_value(),
    )
    mawb_model.add(
        field="Office",
        attribute="autocomplete",
        data=AEBasicTab.MAWB.office_autocomplete.get_value(),
    )

    context._vp.add_dict(dict_name="mawb_model", value={name: mawb_model})

    # create new HAWBs
    for i in range(1, int(count) + 1):
        AEBasicTab.add_hawb_button.click()
        sleep(4)
        AEBasicTab.HAWB(i).more_button.click()
        hawb_model = input_dynamic_datas(create_ae_hawb_table, "AEBasicTab.HAWB({})".format(i))

        # dimension
        AEBasicTab.HAWB(i).set_dimensions_button.click()
        AEBasicTab.Dimension.dimension_add_button.click()
        hawb_dimension_model = input_dynamic_datas(create_ae_hawb_dimension_table, "AEBasicTab.Dimension(1)")
        AEBasicTab.Dimension.dimension_apply_button.click()
        Common.spin_bar.gone()

        # commodity
        AEBasicTab.HAWB(i).commodity_add_button.click()
        hawb_commodity_model = input_dynamic_datas(
            create_ae_hawb_commodity_table,
            "AEBasicTab.HAWB({}).Commodity({}, 1)".format(i, i),
        )

        # TODO warehouse receipt

        # other charge
        AEBasicTab.HAWB(i).other_charge_add_button.click()
        hawb_other_charge_model = input_dynamic_datas(
            create_ae_hawb_other_charge_table,
            "AEBasicTab.HAWB({}).OtherCharges({}, 1)".format(i, i),
        )

        # more
        AEBasicTab.HAWB(i).more_expand_button.click()
        hawb_more_model = input_dynamic_datas(create_ae_hawb_more_table, "AEBasicTab.HAWB({})".format(i))

        Common.save_button.click()
        Common.spin_bar.gone()
        assert Common.save_msg.is_visible(timeout=10) is True

        hawb_model.add(
            field="Booking Date",
            attribute="datepicker",
            data=AEBasicTab.HAWB(i).booking_date_datepicker.get_value(),
        )
        hawb_model.add(
            field="ITN No.",
            attribute="input",
            data=AEBasicTab.HAWB(i).itn_no_input.get_value(),
        )
        hawb_model.add(
            field="Customer",
            attribute="autocomplete",
            data=AEBasicTab.HAWB(i).customer_autocomplete.get_value(),
        )
        hawb_model.add(
            field="Bill To",
            attribute="autocomplete",
            data=AEBasicTab.HAWB(i).bill_to_autocomplete.get_value(),
        )
        hawb_model.add(
            field="Issuing Carrier/Agent",
            attribute="autocomplete",
            data=AEBasicTab.HAWB(i).issuing_carrier_agent_autocomplete.get_value(),
        )
        hawb_model.add(
            field="Sales",
            attribute="autocomplete",
            data=AEBasicTab.HAWB(i).sales_autocomplete.get_value(),
        )
        hawb_model.add(
            field="D.V. Carriage",
            attribute="input",
            data=AEBasicTab.HAWB(i).dv_carriage_input.get_value(),
        )
        hawb_model.add(
            field="D.V. Customs",
            attribute="input",
            data=AEBasicTab.HAWB(i).dv_customs_input.get_value(),
        )
        hawb_model.add(
            field="Insurance",
            attribute="input",
            data=AEBasicTab.HAWB(i).insurance_input.get_value(),
        )
        hawb_model.add(
            field="Gross Weight (SHPR) LB",
            attribute="input",
            data=AEBasicTab.HAWB(i).gross_weight_shpr_lb_input.get_value(),
        )
        hawb_model.add(
            field="Gross Weight (SHPR) Amount",
            attribute="input",
            data=AEBasicTab.HAWB(i).gross_weight_shpr_amount_input.get_value(),
        )
        hawb_model.add(
            field="Gross Weight (CNEE)",
            attribute="input",
            data=AEBasicTab.HAWB(i).gross_weight_cnee_input.get_value(),
        )
        hawb_model.add(
            field="Gross Weight (CNEE) LB",
            attribute="input",
            data=AEBasicTab.HAWB(i).gross_weight_cnee_lb_input.get_value(),
        )
        hawb_model.add(
            field="Gross Weight (CNEE) Amount",
            attribute="input",
            data=AEBasicTab.HAWB(i).gross_weight_cnee_amount_input.get_value(),
        )
        hawb_model.add(
            field="Chargeable Weight (SHPR)",
            attribute="input",
            data=AEBasicTab.HAWB(i).chargeable_weight_shpr_input.get_value(),
        )
        hawb_model.add(
            field="Chargeable Weight (SHPR) LB",
            attribute="input",
            data=AEBasicTab.HAWB(i).chargeable_weight_shpr_lb_input.get_value(),
        )
        hawb_model.add(
            field="Chargeable Weight (SHPR) Amount",
            attribute="input",
            data=AEBasicTab.HAWB(i).chargeable_weight_shpr_amount_input.get_value(),
        )
        hawb_model.add(
            field="Chargeable Weight (CNEE)",
            attribute="input",
            data=AEBasicTab.HAWB(i).chargeable_weight_cnee_input.get_value(),
        )
        hawb_model.add(
            field="Chargeable Weight (CNEE) LB",
            attribute="input",
            data=AEBasicTab.HAWB(i).chargeable_weight_cnee_lb_input.get_value(),
        )
        hawb_model.add(
            field="Chargeable Weight (CNEE) Amount",
            attribute="input",
            data=AEBasicTab.HAWB(i).chargeable_weight_cnee_amount_input.get_value(),
        )
        hawb_model.add(
            field="Volume Weight",
            attribute="input",
            data=AEBasicTab.HAWB(i).volume_weight_input.get_value(),
        )
        hawb_model.add(
            field="Volume Measure",
            attribute="input",
            data=AEBasicTab.HAWB(i).volume_measure_input.get_value(),
        )

        context._vp.add_dict(dict_name="hawb_model", value={"{}_{}".format(name, i): hawb_model})
        context._vp.add_dict(
            dict_name="hawb_dimension_model",
            value={"{}_{}".format(name, i): hawb_dimension_model},
        )
        context._vp.add_dict(
            dict_name="hawb_commodity_model",
            value={"{}_{}".format(name, i): hawb_commodity_model},
        )
        context._vp.add_dict(
            dict_name="hawb_other_charge_model",
            value={"{}_{}".format(name, i): hawb_other_charge_model},
        )
        context._vp.add_dict(
            dict_name="hawb_more_model",
            value={"{}_{}".format(name, i): hawb_more_model},
        )

    context._vp.add_dict(dict_name="shipment_url", value={name: Driver.get_url()})


@Given("the user has a AE MAWB with {count} HAWB as '{name}' with only required fields filled")
def step_impl(context, count, name):
    create_ae_mawb_table = transfer_to_feature_table(
        """
        | field               | attribute  | action | data              |
        | MAWB No.            | input      | input  | 911-{randomNo(7)} |
        | Departure Date/Time | datepicker | input  | {today+1}         |
    """
    )

    if gl.company in ["OLC", "MASCOT"]:
        create_ae_hawb_table = transfer_to_feature_table(
            """
            | field         | attribute    | action    | data                |
            | Sales         | autocomplete | input     | {randomSales}       |
        """
        )
    else:
        create_ae_hawb_table = transfer_to_feature_table(
            """
            | field         | attribute    | action    | data                |
        """
        )

    # create a new MAWB
    Driver.open(gl.URL.AE_NEW_SHIPMENT)
    AEBasicTab.MAWB.more_button.click()
    mawb_model = input_dynamic_datas(create_ae_mawb_table, "AEBasicTab.MAWB")
    Common.save_button.click()
    assert Common.save_msg.is_visible(timeout=30) is True

    # add additional field
    mawb_model.add(
        field="File No.",
        attribute="input",
        data=AEBasicTab.MAWB.file_no_input.get_value(),
    )
    mawb_model.add(
        field="Office",
        attribute="autocomplete",
        data=AEBasicTab.MAWB.office_autocomplete.get_value(),
    )

    context._vp.add_dict(dict_name="mawb_model", value={name: mawb_model})

    # create new HAWBs
    for i in range(1, int(count) + 1):
        AEBasicTab.add_hawb_button.click()
        sleep(4)
        AEBasicTab.HAWB(i).more_button.click()
        hawb_model = input_dynamic_datas(create_ae_hawb_table, "AEBasicTab.HAWB({})".format(i))

        Common.save_button.click()
        Common.spin_bar.gone()
        assert Common.save_msg.is_visible(timeout=10) is True

        hawb_no = AEBasicTab.HAWB(i).hawb_no_input.get_value()
        hawb_model.add(field="HAWB No.", attribute="input", data=hawb_no)
        hawb_model.add(
            field="Sales",
            attribute="autocomplete",
            data=AEBasicTab.HAWB(i).sales_autocomplete.get_value(),
        )

        context._vp.add_dict(dict_name="hawb_model", value={"{}_{}".format(name, i): hawb_model})

    context._vp.add_dict(dict_name="shipment_url", value={name: Driver.get_url()})


@When("the user click AE shipment '{name}' HAWB({index}) 'Tools -> Copy To'")
def step_impl(context, name, index):
    Driver.open(context._vp.get("shipment_url")[name])
    Common.spin_bar.gone()
    AEBasicTab.HAWB(index).hbl_side_panel_button.click()
    sleep(2)
    AEBasicTab.HAWB(index).tools_button.click()
    AEBasicTab.HAWB(index).tools_copy_to_button.click()


@When("the user input '{name}' to AE copy HAWB to")
def step_impl(context, name):
    mbl_no = context._vp.get("mawb_model")[name].get_data("MAWB No.")
    AEBasicTab.CopyHBLToMBL.select_mbl_autocomplete.input(mbl_no)


@When("the user click 'OK' button in AE 'Copy To' dialog")
def step_impl(context):
    AEBasicTab.CopyHBLToMBL.ok_button.click()


@Then("the link of '{name}' should show in AE 'Copy To' dialog")
def step_impl(context, name):
    exp = context._vp.get("mawb_model")[name].get_data("File No.")
    v = AEBasicTab.CopyHBLToMBL.mbl_link.get_value()
    assert exp == v, "Link shoud be [{0}], not [{1}]".format(exp, v)


@When("the user click the AE copied link")
def step_impl(context):
    AEBasicTab.CopyHBLToMBL.mbl_link.click()
    Driver.switch_to(window_index=1)
    Common.spin_bar.gone()


@Then("the HAWB({index_1}) should copy from AE shipment '{name}' HAWB({index_2})")
def step_impl(context, index_1, name, index_2):
    AEBasicTab.HAWB(index_1).hbl_side_panel_button.click()
    AEBasicTab.HAWB(index_1).more_button.click()
    model = context._vp.get("hawb_model")["{}_{}".format(name, index_2)]
    model.set_page_class_name("AEBasicTab.HAWB({})".format(index_1))
    vm_fields = model.get_all_fields()
    copied_fields = [i["field"] for i in context.table]
    for f in vm_fields:
        if f not in copied_fields:
            f_dict = model.pop(f)
            if f == "HAWB No.":
                continue
            else:
                data = ""
            model.add(field=f, attribute=f_dict[model.ATTRIBUTE], data=data)
    # TODO check whether op is the current character
    model.verify()

    # dimension should be copied to
    AEBasicTab.HAWB(index_1).set_dimensions_button.click()
    dim_model = context._vp.get("hawb_dimension_model")["{}_{}".format(name, index_2)]
    dim_model.set_page_class_name("AEBasicTab.Dimension(1)")
    dim_model.verify()
    AEBasicTab.Dimension.dimension_cancel_button.click()

    # commodity should not be copied to
    assert (
        AEBasicTab.HAWB(index_1).Commodity(1).commodity_description_input.is_invisible()
    ), "commodity should not be copied to"

    # TODO warehouse receipt

    # other charge
    assert (
        AEBasicTab.HAWB(index_1).OtherCharges(index_1, 1).carrier_agent_select.is_invisible()
    ), "other charge should not be copied to"

    # more should be copied to
    AEBasicTab.HAWB(index_1).more_expand_button.click()
    more_model = context._vp.get("hawb_more_model")["{}_{}".format(name, index_2)]
    more_model.set_page_class_name("AEBasicTab.HAWB({})".format(index_1))
    more_model.verify()


@Then("the AE HAWB({index}) should have 'COPY-1' as HAWB NO.")
def step_impl(context, index):
    exp = "COPY-1"
    hawb_no = AEBasicTab.HAWB(index).hawb_no_input.get_value()
    assert hawb_no == exp, "HAWB No. should be [{0}], not [{1}]".format(exp, hawb_no)


@When("the user deletes AE MAWB")
def step_impl(context):
    AEBasicTab.MAWB.tools_button.click()
    AEBasicTab.MAWB.Tools.delete_button.click()
    sleep(2)  # TODO: fix get_value() by pool -> ssuhung
    msg = Common.popup_modal_msg_label.get_value()
    assert (
        "Are you sure you want to delete? All corresponding information will be lost by doing this" == msg
    ), f"msg [{msg}] is not correct"
    Common.shipment_ok_button.click()
    Common.spin_bar.gone()


@When("the user copied AE MAWB")
def step_impl(context):
    AEBasicTab.MAWB.tools_button.click()
    AEBasicTab.MAWB.Tools.copy_button.click()
    sleep(2)  # TODO: fix get_value() by pool -> ssuhung
    msg = Common.popup_modal_msg_label.get_value()
    assert "Copy MAWB" == msg, f"msg [{msg}] is not correct"
    Common.shipment_ok_button.click()


@Then("AE MAWB '{field}' should be '{exp_val}'")
def step_impl(context, field, exp_val):
    exp_val = transfer_data(exp_val)
    if field == "MAWB No.":
        val = AEBasicTab.MAWB.mawb_no_input.get_value()
    elif field == "Carrier":
        val = AEBasicTab.MAWB.carrier_autocomplete.get_value()
    else:
        raise StepParaNotDefinedError(field)

    assert exp_val == val, f"{field} should be [{exp_val}], but now is [{val}]"
