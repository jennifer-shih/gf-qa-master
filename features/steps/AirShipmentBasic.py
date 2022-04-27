import re
from decimal import Decimal

from behave import Then, When

import src.pages as Pages  # noqa
from config import globalparameter as gl
from src.api.gofreight_config import GBy
from src.drivers.driver import Driver
from src.helper.executor import exec_act_cmd
from src.helper.script import input_dynamic_datas


@When("the user enter '{value}' for field '{field}' in {AI_or_AE} 'new shipment' page for {mbl_or_hbl}")
def step_impl(context, value, field, AI_or_AE, mbl_or_hbl):
    if mbl_or_hbl == "MAWB":
        pass
    elif re.match(r"HAWB\((\d+)\)", mbl_or_hbl) != None:
        index = re.match(r"HAWB\((\d+)\)", mbl_or_hbl).group(1)
        if AI_or_AE == "AI":
            Pages.AIBasicTab.HAWB(index).hbl_side_panel_button.click()
            if not Pages.AIBasicTab.HAWB(index).e_commerce_checkbox.is_interactable():
                Pages.AIBasicTab.HAWB(index).more_button.click()
        elif AI_or_AE == "AE":
            Pages.AEBasicTab.HAWB(index).hbl_side_panel_button.click()
            if not Pages.AEBasicTab.HAWB(index).e_commerce_checkbox.is_interactable():
                Pages.AEBasicTab.HAWB(index).more_button.click()
        else:
            raise Exception(f"AI_or_AE: [{AI_or_AE}] is not valid")
    else:
        raise Exception(f"mbl_or_hbl: [{mbl_or_hbl}] is not valid")

    exec_act_cmd(field, "input", "input", [value], "Pages." + AI_or_AE + "BasicTab." + mbl_or_hbl)


@When("the user click Air 'Save' button")
def step_impl(context):
    Pages.Common.save_button.click()
    assert Pages.Common.save_msg.is_visible(timeout=30)

    context._vp.add_v(v_name="url", value=Driver.get_url())
    Driver.refresh()


@Then("the shipment '{name}' of 'Air {import_or_export}' will be created")
def step_impl(context, name, import_or_export):
    model = context._vp.get("mawb_model")[name]

    # go to the shipment which just created
    Driver.open(context._vp.get("url"))
    Pages.Common.spin_bar.gone()
    if import_or_export == "Import":
        Pages.AIBasicTab.MAWB.more_button.click()
    elif import_or_export == "Export":
        Pages.AEBasicTab.MAWB.more_button.click()

    # url should be https://fms-stage-qa-5.gofreight.co/air/import/shipment/{File_No}/
    # or https://fms-stage-qa-5.gofreight.co/air/export/shipment/{File_No}/
    file_no = Driver.get_url().split("/")[-2]
    model.add(field="file_no", attribute="input", data=file_no)

    # direct master
    if import_or_export == "Import":
        # 如果有填 Consignee, 且 Notify, Customer, Bill To都沒有另外輸入value，這些欄位會與Consignee相同
        if (
            Pages.AIBasicTab.MAWB.direct_master_checkbox.get_value() == True
            and model.has_key("Consignee")
            and not model.has_key("Notify")
            and not model.has_key("Customer")
            and not model.has_key("Bill To")
        ):
            consignee = model.get_data("Consignee")
            model.add(field="Notify", attribute="autocomplete", data=consignee)
            model.add(field="Customer", attribute="autocomplete", data=consignee)
            model.add(field="Bill To", attribute="autocomplete", data=consignee)
    elif import_or_export == "Export":
        # 如果有填 Customer, 且 Bill To 沒有另外輸入value，這些欄位會與Customer相同
        if (
            Pages.AEBasicTab.MAWB.direct_master_checkbox.get_value() == True
            and model.has_key("Customer")
            and not model.has_key("Bill To")
        ):
            customer = model.get_data("Customer")
            model.add(field="Bill To", attribute="autocomplete", data=customer)

    model.verify()


@When("the user input Length, Width, Height and PCS for {AI_or_AE} MAWB '{name}' 'Volume Weight'")
@When("the user input Length, Width, Height and PCS for {AI_or_AE} shipment '{name}' HAWB({hbl_index}) 'Volume Weight'")
def step_impl(context, AI_or_AE, name, hbl_index=None):
    current_page_class_name = "Pages." + AI_or_AE + "BasicTab.Dimension"

    models = []
    dimensions = []
    for index in range(len(context.table.rows)):
        action_table = [
            {
                "field": "Length",
                "attribute": "input",
                "action": "input",
                "data": context.table[index]["Length"],
            }
        ]
        action_table.append(
            {
                "field": "Width",
                "attribute": "input",
                "action": "input",
                "data": context.table[index]["Width"],
            }
        )
        action_table.append(
            {
                "field": "Height",
                "attribute": "input",
                "action": "input",
                "data": context.table[index]["Height"],
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

        eval("Pages." + AI_or_AE + "BasicTab.Dimension.dimension_add_button.click()")
        models.append(input_dynamic_datas(action_table, current_page_class_name + "(" + str(index + 1) + ")"))

        length = eval("Pages." + AI_or_AE + "BasicTab.Dimension(" + str(index + 1) + ").length_input.get_value()")
        width = eval("Pages." + AI_or_AE + "BasicTab.Dimension(" + str(index + 1) + ").width_input.get_value()")
        height = eval("Pages." + AI_or_AE + "BasicTab.Dimension(" + str(index + 1) + ").height_input.get_value()")
        pcs = eval("Pages." + AI_or_AE + "BasicTab.Dimension(" + str(index + 1) + ").pcs_input.get_value()")

        weight_places = Decimal(10) ** -(
            Decimal(gl.gofreight_config.get_ai_weight_decimal(gl.user_info.office, GBy.OID))
        )
        measure_places = Decimal(10) ** -(
            Decimal(gl.gofreight_config.get_measurement_decimal(gl.user_info.office, GBy.OID))
        )
        measure_cbm = (int(length) * int(width) * int(height) * int(pcs)) / 1000000.00

        volume_kgs = str(Decimal(str(measure_cbm * 1000 / 6)).quantize(Decimal(weight_places)))
        volume_lbs = str(Decimal(str(Decimal(volume_kgs) * Decimal(str(gl.KG2LB)))).quantize(Decimal(weight_places)))
        measure_cbm = str(Decimal(measure_cbm).quantize(Decimal(measure_places)))
        measure_cft = str(
            Decimal(str(Decimal(measure_cbm) * Decimal(str(gl.CBM2CFT)))).quantize(Decimal(measure_places))
        )
        dimensions.append(
            {
                "pcs": pcs,
                "volume_kgs": volume_kgs,
                "volume_lbs": volume_lbs,
                "measure_cbm": measure_cbm,
                "measure_cft": measure_cft,
            }
        )

    if hbl_index:
        context._vp.add_dict(
            dict_name="hawb_volume_weight_model",
            value={"{}_{}".format(name, hbl_index): models},
        )
        context._vp.add_dict(
            dict_name="hawb_dimension_model",
            value={"{}_{}".format(name, hbl_index): dimensions},
        )
    else:
        context._vp.add_dict(dict_name="mawb_volume_weight_model", value={name: models})
        context._vp.add_dict(dict_name="mawb_dimension_model", value={name: dimensions})
