from datetime import datetime
from decimal import Decimal
from time import sleep

from behave import Given, Then, When

import src.pages as Pages
from config import globalparameter as gl
from src.api.gofreight_config import GBy
from src.drivers.driver import Driver
from src.helper.function import get_wh_receipt_no, wday
from src.helper.script import input_dynamic_datas
from src.helper.transfer import transfer_to_feature_table


@When("the user enter 'others' receipt basic datas as '{name}'")
def step_impl(context, name):
    current_page_class_name = "Pages.WHReceiptBasicTab"
    model = input_dynamic_datas(context.table, current_page_class_name)
    receipt_no = get_wh_receipt_no(gl.user_info.office, GBy.OID)
    model.add(field="Warehouse Receipt No.", attribute="input", data=receipt_no)
    context._vp.add_dict(dict_name="receipt_model", value={name: model})


@When("the user enter 'automobile' receipt basic datas as '{name}'")
def step_impl(context, name):
    current_page_class_name = "Pages.WHReceiptBasicTab"
    model = input_dynamic_datas(context.table, current_page_class_name)

    # If 'Title Received' is checked and we didn't fill in date value, add default value (today) into verified_model
    if model.has_key("AM Title Received Status") and not model.has_key("AM Title Received"):
        data = wday(0) if model.get_data(field="AM Title Received Status") else ""
        model.add(field="AM Title Received", attribute="datepicker", data=data)
    # 'Shipper' will have the same value as 'Customer', so the 'Shipper' value in verified_model should be modified or add.
    if model.has_key("AM Customer"):
        model.pop(field="Shipper", not_exist_ok=True)
        data = model.get_data(field="AM Customer")
        model.add(field="Shipper", attribute="autocomplete", data=data)
    # The original 'Maker' will be blocked once we change this receipt into an automobile one.
    if model.has_key("Maker"):
        model.add(field="Maker", attribute="autocomplete", data="")

    receipt_no = get_wh_receipt_no(gl.user_info.office, GBy.OID)
    model.add(field="Warehouse Receipt No.", attribute="input", data=receipt_no)
    context._vp.add_dict(dict_name="receipt_model", value={name: model})


@When("the user input receipt '{name}' dimension datas")
def step_impl(context, name):
    models = []
    current_page_class_name = "Pages.WHReceiptBasicTab.Dimension"
    for index in range(len(context.table.rows)):
        action_table = []
        for heading in context.table.headings:
            if heading == "Dimension" or heading == "Unit":
                value = context.table[index][heading]
                if value == "random select":
                    action = {
                        "field": heading,
                        "attribute": "select",
                        "action": "random select",
                        "data": "",
                    }
                else:
                    action = {
                        "field": heading,
                        "attribute": "select",
                        "action": "select",
                        "data": context.table[index][heading],
                    }
            else:
                action = {
                    "field": heading,
                    "attribute": "input",
                    "action": "input",
                    "data": context.table[index][heading],
                }
            action_table.append(action)

        Pages.WHReceiptBasicTab.Dimension.dimension_add_button.click()
        model = input_dynamic_datas(action_table, current_page_class_name + "(" + str(index + 1) + ")")
        # ? KNOWN ISSUE
        model.add(
            field="volume_kgs",
            attribute="label",
            data=Pages.WHReceiptBasicTab.Dimension(index + 1).volume_kgs_label.get_value(),
        )
        model.add(
            field="volume_lbs",
            attribute="label",
            data=Pages.WHReceiptBasicTab.Dimension(index + 1).volume_lbs_label.get_value(),
        )
        model.add(
            field="measurement_cbm",
            attribute="input",
            data=Pages.WHReceiptBasicTab.Dimension(index + 1).measurement_cbm_input.get_value(),
        )
        model.add(
            field="measurement_cft",
            attribute="input",
            data=Pages.WHReceiptBasicTab.Dimension(index + 1).measurement_cft_input.get_value(),
        )
        model.add(
            field="act_weight_lbs",
            attribute="input",
            data=Pages.WHReceiptBasicTab.Dimension(index + 1).act_weight_lbs_input.get_value(),
        )
        # ?
        models.append(model)
    context._vp.add_dict(dict_name="receipt_dimension_model", value={name: models})


@When("the user click WH 'Save' button")
def step_impl(context):
    Pages.Common.save_button.click()
    assert Pages.Common.save_msg.is_visible(timeout=30) is True

    context._vp.add_v(v_name="url", value=Driver.get_url())
    Driver.refresh()


@Then("the storage day is correct")
def step_impl(context):
    received_date = Pages.WHReceiptBasicTab.received_date_time_datepicker.get_value()
    Pages.WHReceiptBasicTab.storage_day_icon_label.hover()
    loaded_date = Pages.WHReceiptBasicTab.loaded_date_time_datepicker.get_value()

    date_time_format = gl.user_info.date_time_format
    received_date = datetime.strptime(received_date, date_time_format)
    loaded_date = datetime.strptime(loaded_date, date_time_format)
    delta = loaded_date - received_date
    exp_day = "Storage: " + str(delta.days) + " days"

    day = Pages.WHReceiptBasicTab.storage_day_tips_label.get_value()

    assert exp_day == day, "Expect [{0}], but get [{1}]".format(exp_day, day)


@Then("the receipt '{name}' total dimension is correct")
def step_impl(context, name):
    (
        exp_pkg,
        exp_pallet,
        exp_total_pcs,
        exp_volume_kgs,
        exp_volume_lbs,
        exp_mea_cbm,
        exp_mea_cft,
        exp_act_kgs,
        exp_act_lbs,
    ) = (
        Decimal(0),
        Decimal(0),
        Decimal(0),
        Decimal(0),
        Decimal(0),
        Decimal(0),
        Decimal(0),
        Decimal(0),
        Decimal(0),
    )
    models = context._vp.get(dict_name="receipt_dimension_model")[name]
    for index in range(len(models)):
        exp_pkg += Decimal(Pages.WHReceiptBasicTab.Dimension(index + 1).pkg_input.get_value().replace(",", ""))
        exp_pallet += Decimal(Pages.WHReceiptBasicTab.Dimension(index + 1).pallet_input.get_value().replace(",", ""))
        exp_total_pcs += Decimal(
            Pages.WHReceiptBasicTab.Dimension(index + 1).total_pcs_input.get_value().replace(",", "")
        )
        exp_volume_kgs += Decimal(
            Pages.WHReceiptBasicTab.Dimension(index + 1).volume_kgs_label.get_value().replace(",", "")
        )
        exp_volume_lbs += Decimal(
            Pages.WHReceiptBasicTab.Dimension(index + 1).volume_lbs_label.get_value().replace(",", "")
        )
        exp_mea_cbm += Decimal(
            Pages.WHReceiptBasicTab.Dimension(index + 1).measurement_cbm_input.get_value().replace(",", "")
        )
        exp_mea_cft += Decimal(
            Pages.WHReceiptBasicTab.Dimension(index + 1).measurement_cft_input.get_value().replace(",", "")
        )
        exp_act_kgs += Decimal(
            Pages.WHReceiptBasicTab.Dimension(index + 1).act_weight_kgs_input.get_value().replace(",", "")
        )
        exp_act_lbs += Decimal(
            Pages.WHReceiptBasicTab.Dimension(index + 1).act_weight_lbs_input.get_value().replace(",", "")
        )
    pkg = Decimal(Pages.WHReceiptBasicTab.Dimension.dimension_total_pkg_label.get_value().replace(",", ""))
    pallet = Decimal(Pages.WHReceiptBasicTab.Dimension.dimension_total_pallet_label.get_value().replace(",", ""))
    total_pcs = Decimal(Pages.WHReceiptBasicTab.Dimension.dimension_total_pcs_label.get_value().replace(",", ""))
    volume_kgs = Decimal(Pages.WHReceiptBasicTab.Dimension.dimension_total_vol_kgs_label.get_value().replace(",", ""))
    volume_lbs = Decimal(Pages.WHReceiptBasicTab.Dimension.dimension_total_vol_lbs_label.get_value().replace(",", ""))
    mea_cbm = Decimal(Pages.WHReceiptBasicTab.Dimension.dimension_total_measure_cbm_label.get_value().replace(",", ""))
    mea_cft = Decimal(Pages.WHReceiptBasicTab.Dimension.dimension_total_measure_cft_label.get_value().replace(",", ""))
    act_kgs = Decimal(Pages.WHReceiptBasicTab.Dimension.dimension_total_act_kgs_label.get_value().replace(",", ""))
    act_lbs = Decimal(Pages.WHReceiptBasicTab.Dimension.dimension_total_act_lbs_label.get_value().replace(",", ""))

    # ? KNOWN ISSUE
    assert abs(exp_pkg - pkg) < 0.05, "Expect pkg is [{0}], but get [{1}]".format(exp_pkg, pkg)
    assert abs(exp_pallet - pallet) < 0.05, "Expect pallet is [{0}], but get [{1}]".format(exp_pallet, pallet)
    assert abs(exp_total_pcs - total_pcs) < 0.05, "Expect total pcs is [{0}], but get [{1}]".format(
        exp_total_pcs, total_pcs
    )
    assert abs(exp_volume_kgs - volume_kgs) < 0.05, "Expect volume kgs is [{0}], but get [{1}]".format(
        exp_volume_kgs, volume_kgs
    )
    assert abs(exp_volume_lbs - volume_lbs) < 0.05, "Expect volume lbs is [{0}], but get [{1}]".format(
        exp_volume_lbs, volume_lbs
    )
    assert abs(exp_mea_cbm - mea_cbm) < 0.05, "Expect measurement cbm is [{0}], but get [{1}]".format(
        exp_mea_cbm, mea_cbm
    )
    assert abs(exp_mea_cft - mea_cft) < 0.05, "Expect measurement cft is [{0}], but get [{1}]".format(
        exp_mea_cft, mea_cft
    )
    assert abs(exp_act_kgs - act_kgs) < 0.05, "Expect actual kgs is [{0}], but get [{1}]".format(exp_act_kgs, act_kgs)
    assert abs(exp_act_lbs - act_lbs) < 0.05, "Expect actual lbs is [{0}], but get [{1}]".format(exp_act_lbs, act_lbs)
    # ?


@Then("the '{cargo_type}' receipt '{name}' will be created")
def step_impl(context, cargo_type, name):
    model = context._vp.get(dict_name="receipt_model")[name]

    # go to the receipt which just created
    Driver.open(context._vp.get("url"))
    Pages.Common.spin_bar.gone()

    model.verify()


@Then("the '{cargo_type}' receipt '{name}' dimension data will be saved")
def step_impl(context, cargo_type, name):
    models = context._vp.get(dict_name="receipt_dimension_model")[name]
    Driver.open(context._vp.get("url"))
    Pages.Common.spin_bar.gone()
    for index in range(len(models)):
        model = models[index]
        model.verify()


@Given("the user has a WH 'automobile' receipt as '{name}' having {dim_cnt} dimensions")
def step_impl(context, name, dim_cnt):
    create_wh_receipt_table = transfer_to_feature_table(
        """
        | field                    | attribute    | action               | data                                                               |
        | Received Date/Time       | datepicker   | input                | {today+1} 13:00                                                    |
        | Received By              | select       | random select        |                                                                    |
        | Truck B/L No.            | input        | input                | TK-{randomNo(6)}                                                   |
        | Location                 | input        | input                | {randomCity}                                                       |
        | Loaded Date/Time         | datepicker   | input                | {today+6} 16:00                                                    |
        | Maker                    | autocomplete | input                | {randomTradePartner}                                               |
        | Shipper                  | autocomplete | input and close memo | {randomTradePartner}                                               |
        | Consignee                | autocomplete | input                | {randomTradePartner}                                               |
        | Delivered Carrier        | input        | input                | {randomTradePartner}                                               |
        | Delivered By             | input        | input                | {randomTradePartner}                                               |
        | Amount                   | input        | input                | {randN(6)}                                                         |
        | Check No.                | input        | input                | CHK-{randN(4)}                                                     |
        | Cargo Type               | radio group  | click                | Automobile                                                         |
        | Hazardous Goods          | checkbox     | tick                 | {randomOnOff}                                                      |
        | Heat Treated Pallets     | checkbox     | tick                 | {randomOnOff}                                                      |
        | P.O. No.                 | input        | input                | PO-{randomNo(6)}                                                   |
        | Remark                   | input        | input                | This is Warehouse Receipt on remark textarea for Automobile script |
    """
    )

    create_wh_receipt_am_table = transfer_to_feature_table(
        """
        | field                    | attribute    | action               | data                                                               |
        | AM Vin No.               | autocomplete | input                | {randomVin}                                                        |
        | AM Tag No.               | input        | input                | tag{randN(6)}                                                      |
        | AM Customer              | autocomplete | input                | {randomTradePartner}                                               |
        | AM Maker                 | input        | input                | {randomTradePartner}                                               |
        | AM Year                  | input        | input                | 20{randN(2)}                                                       |
        | AM Model                 | input        | input                | {randomModel}                                                      |
        | AM Color                 | input        | input                | {randomColor}                                                      |
        | AM Engine No.            | input        | input                | EN-{randN(8)}                                                      |
        | AM Manufacture Year      | autocomplete | input                | {randInt(1900,2019)}                                               |
        | AM Manufacture Month     | autocomplete | input                | {randInt(1,12)}                                                    |
        | AM Title Received Status | checkbox     | tick                 | {randomOnOff}                                                      |
        | AM Condition             | input        | input                | CND-{randN(8)}                                                     |
        | AM Key                   | input        | input                | {randInt(0,10)}                                                    |
        | AM Fuel                  | input        | input                | F-{randN(2)}%                                                      |
        | AM Tire Size (Front)     | input        | input                | {randN(3)} / {randN(2)} / R{randN(2)}                              |
        | AM Tire Size (Rear)      | input        | input                | {randN(3)} / {randN(2)} / R{randN(2)}                              |
        | AM Mileage               | input        | input                | {randN(4)}                                                         |
        | AM W.STICKER             | radio group  | random click         |                                                                    |
        | AM Remote Control        | radio group  | random click         |                                                                    |
        | AM Headphone             | radio group  | random click         |                                                                    |
        | AM Owner's Manual        | radio group  | random click         |                                                                    |
        | AM CD Player             | radio group  | random click         |                                                                    |
        | AM CD Changer            | radio group  | random click         |                                                                    |
        | AM First Aid Kit         | radio group  | random click         |                                                                    |
        | AM Floor Mat             | radio group  | random click         |                                                                    |
        | AM Cigarette Lighter     | radio group  | random click         |                                                                    |
        | AM Cargo Net             | radio group  | random click         |                                                                    |
        | AM Ashtray               | radio group  | random click         |                                                                    |
        | AM Tools                 | radio group  | random click         |                                                                    |
        | AM Spare Tire            | radio group  | random click         |                                                                    |
        | AM Sun Roof              | radio group  | random click         |                                                                    |
    """
    )

    create_wh_receipt_dimension_table = transfer_to_feature_table(
        """
        | field           | attribute | action        | data          |
        | Length          | input     | input         | {randN(2)}    |
        | Width           | input     | input         | {randN(2)}    |
        | Height          | input     | input         | {randN(2)}    |
        | Dimension       | select    | random select |               |
        | PKG             | input     | input         | {randN(2)}    |
        | Unit            | select    | random select |               |
        | Sku PO          | input     | input         | SKU{randN(6)} |
        | Pallet          | input     | input         | {randN(2)}    |
        | Total PCS       | input     | input         | {randN(1)}    |
        | Act. Weight KGS | input     | input         | {randN(3)}    |
    """
    )

    # create a new receipt
    Driver.open(gl.URL.WH_NEW_RECEIPTS)
    receipt_model = input_dynamic_datas(create_wh_receipt_table, "Pages.WHReceiptBasicTab")
    receipt_am_model = input_dynamic_datas(create_wh_receipt_am_table, "Pages.WHReceiptBasicTab")
    Pages.Common.save_button.click()
    assert Pages.Common.save_msg.is_visible(timeout=30) is True

    # add additional field
    receipt_no = get_wh_receipt_no(gl.user_info.office, GBy.OID)
    receipt_am_model.add(field="Warehouse Receipt No.", attribute="input", data=receipt_no)
    receipt_model.add(
        field="Office",
        attribute="autocomplete",
        data=Pages.WHReceiptBasicTab.office_autocomplete.get_value(),
    )
    # If 'Title Received' is checked and we didn't fill in date value, add default value (today) into verified_model
    if receipt_am_model.has_key("AM Title Received Status") and not receipt_am_model.has_key("AM Title Received"):
        data = wday(0) if receipt_am_model.get_data(field="AM Title Received Status") else ""
        receipt_am_model.add(field="AM Title Received", attribute="datepicker", data=data)
    # 'Shipper' will have the same value as 'Customer', so the 'Shipper' value in verified_model should be modified or add.
    if receipt_am_model.has_key("AM Customer"):
        receipt_model.pop(field="Shipper", not_exist_ok=True)
        data = receipt_am_model.get_data(field="AM Customer")
        receipt_model.add(field="Shipper", attribute="autocomplete", data=data)
    # The original 'Maker' will be blocked once we change this receipt into an automobile one.
    f_dict = receipt_model.pop("Maker")
    receipt_model.add(field="Maker", attribute=f_dict[receipt_model.ATTRIBUTE], data="")

    context._vp.add_dict(dict_name="receipt_model", value={name: receipt_model})
    context._vp.add_dict(dict_name="receipt_am_model", value={name: receipt_am_model})

    # add receipt dimension
    for i in range(1, int(dim_cnt) + 1):
        Pages.WHReceiptBasicTab.Dimension.dimension_add_button.click()
        dimension_model = input_dynamic_datas(
            create_wh_receipt_dimension_table,
            "Pages.WHReceiptBasicTab.Dimension({})".format(i),
        )

        dimension_model.add(
            field="Volume KGS",
            attribute="label",
            data=Pages.WHReceiptBasicTab.Dimension(i).volume_kgs_label.get_value(),
        )
        dimension_model.add(
            field="Volume LBS",
            attribute="label",
            data=Pages.WHReceiptBasicTab.Dimension(i).volume_lbs_label.get_value(),
        )
        dimension_model.add(
            field="Measurement CFT",
            attribute="input",
            data=Pages.WHReceiptBasicTab.Dimension(i).measurement_cft_input.get_value(),
        )
        dimension_model.add(
            field="Act. Weight LBS",
            attribute="input",
            data=Pages.WHReceiptBasicTab.Dimension(i).act_weight_lbs_input.get_value(),
        )
        dimension_model.add(field="Lnkd", attribute="checkbox", data=False)
        dimension_model.add(field="Shpd", attribute="checkbox", data=False)
        dimension_model.add(field="M", attribute="select", data="")
        dimension_model.add(field="Date", attribute="datepicker", data="")
        dimension_model.add(field="B/L Bkg. No.", attribute="input", data="")

        context._vp.add_dict(
            dict_name="receipt_dimension_model",
            value={"{}_{}".format(name, i): dimension_model},
        )

    Pages.Common.save_button.click()
    assert Pages.Common.save_msg.is_visible(timeout=30) is True
    context._vp.add_dict(dict_name="receipt_url", value={name: Driver.get_url()})


@Given("the user has a WH 'others' receipt as '{name}' having {dim_cnt} dimensions")
def step_impl(context, name, dim_cnt):
    create_wh_receipt_table = transfer_to_feature_table(
        """
        | field                    | attribute    | action               | data                                                               |
        | Received Date/Time       | datepicker   | input                | {today+1} 13:00                                                    |
        | Received By              | select       | random select        |                                                                    |
        | Truck B/L No.            | input        | input                | TK-{randomNo(6)}                                                   |
        | Location                 | input        | input                | {randomCity}                                                       |
        | Loaded Date/Time         | datepicker   | input                | {today+6} 16:00                                                    |
        | Maker                    | autocomplete | input                | {randomTradePartner}                                               |
        | Shipper                  | autocomplete | input and close memo | {randomTradePartner}                                               |
        | Consignee                | autocomplete | input                | {randomTradePartner}                                               |
        | Delivered Carrier        | input        | input                | {randomTradePartner}                                               |
        | Delivered By             | input        | input                | {randomTradePartner}                                               |
        | Amount                   | input        | input                | {randN(6)}                                                         |
        | Check No.                | input        | input                | CHK-{randN(4)}                                                     |
        | Cargo Type               | radio group  | click                | Others                                                         |
        | Hazardous Goods          | checkbox     | tick                 | {randomOnOff}                                                      |
        | Heat Treated Pallets     | checkbox     | tick                 | {randomOnOff}                                                      |
        | P.O. No.                 | input        | input                | PO-{randomNo(6)}                                                   |
        | Remark                   | input        | input                | This is Warehouse Receipt on remark textarea for Automobile script |
    """
    )

    create_wh_receipt_dimension_table = transfer_to_feature_table(
        """
        | field           | attribute | action        | data          |
        | Length          | input     | input         | {randN(2)}    |
        | Width           | input     | input         | {randN(2)}    |
        | Height          | input     | input         | {randN(2)}    |
        | Dimension       | select    | random select |               |
        | PKG             | input     | input         | {randN(2)}    |
        | Unit            | select    | random select |               |
        | Sku PO          | input     | input         | SKU{randN(6)} |
        | Pallet          | input     | input         | {randN(2)}    |
        | Total PCS       | input     | input         | {randN(1)}    |
        | Act. Weight KGS | input     | input         | {randN(3)}    |
    """
    )

    # create a new receipt
    Driver.open(gl.URL.WH_NEW_RECEIPTS)
    receipt_model = input_dynamic_datas(create_wh_receipt_table, "Pages.WHReceiptBasicTab")
    Pages.Common.save_button.click()
    assert Pages.Common.save_msg.is_visible(timeout=30) is True

    # add additional field
    receipt_no = get_wh_receipt_no(gl.user_info.office, GBy.OID)
    receipt_model.add(field="Warehouse Receipt No.", attribute="input", data=receipt_no)
    receipt_model.add(
        field="Office",
        attribute="autocomplete",
        data=Pages.WHReceiptBasicTab.office_autocomplete.get_value(),
    )

    context._vp.add_dict(dict_name="receipt_model", value={name: receipt_model})

    # add receipt dimension
    for i in range(1, int(dim_cnt) + 1):
        Pages.WHReceiptBasicTab.Dimension.dimension_add_button.click()
        dimension_model = input_dynamic_datas(
            create_wh_receipt_dimension_table,
            "Pages.WHReceiptBasicTab.Dimension({})".format(i),
        )

        dimension_model.add(
            field="Volume KGS",
            attribute="label",
            data=Pages.WHReceiptBasicTab.Dimension(i).volume_kgs_label.get_value(),
        )
        dimension_model.add(
            field="Volume LBS",
            attribute="label",
            data=Pages.WHReceiptBasicTab.Dimension(i).volume_lbs_label.get_value(),
        )
        dimension_model.add(
            field="Measurement CFT",
            attribute="input",
            data=Pages.WHReceiptBasicTab.Dimension(i).measurement_cft_input.get_value(),
        )
        dimension_model.add(
            field="Act. Weight LBS",
            attribute="input",
            data=Pages.WHReceiptBasicTab.Dimension(i).act_weight_lbs_input.get_value(),
        )
        dimension_model.add(field="Lnkd", attribute="checkbox", data=False)
        dimension_model.add(field="Shpd", attribute="checkbox", data=False)
        dimension_model.add(field="M", attribute="select", data="")
        dimension_model.add(field="Date", attribute="datepicker", data="")
        dimension_model.add(field="B/L Bkg. No.", attribute="input", data="")

        context._vp.add_dict(
            dict_name="receipt_dimension_model",
            value={"{}_{}".format(name, i): dimension_model},
        )

    Pages.Common.save_button.click()
    assert Pages.Common.save_msg.is_visible(timeout=30) is True
    context._vp.add_dict(dict_name="receipt_url", value={name: Driver.get_url()})


@Given("the dimension({dim_index}) in receipt is shipped")
@When("the user check dimension({dim_index}) Shpd field")
def step_impl(context, dim_index):
    create_wh_receipt_dimension_shipped_table = transfer_to_feature_table(
        """
        | field        | attribute  | action        | data          |
        | Shpd         | checkbox   | tick          | {on}          |
        | M            | select     | random select |               |
        | Date         | datepicker | input         | {today}       |
        | B/L Bkg. No. | input      | input         | Bkg{randN(6)} |
    """
    )
    input_dynamic_datas(
        create_wh_receipt_dimension_shipped_table,
        "Pages.WHReceiptBasicTab.Dimension({})".format(dim_index),
    )
    Pages.Common.save_button.click()
    Pages.Common.spin_bar.gone()


@Given("the dimension({dim_index}) in receipt is linked to OI '{mbl_name}' HBL({hbl_index})")
@When("the user link dimension({dim_index}) in receipt to OI '{mbl_name}' HBL({hbl_index})")
def step_impl(context, dim_index, mbl_name, hbl_index):
    mbl_model = context._vp.get("mbl_model")["{}".format(mbl_name)]
    hbl_model = context._vp.get("hbl_model")["{}_{}".format(mbl_name, hbl_index)]
    bl_no = hbl_model.get_data("HB/L No.")
    date_format = gl.user_info.date_format
    exp_date = datetime.strptime(mbl_model.get_data("ETA"), date_format).strftime(
        "%Y-%m-%d"
    )  # when disable, become %Y-%m-%d format
    exp_lnkd, exp_shpd = True, True
    exp_m, exp_b_l_bkg_no = "O", bl_no

    Pages.WHReceiptBasicTab.Dimension(dim_index).checked_checkbox.tick(True)
    Pages.WHReceiptBasicTab.Dimension.dimension_link_hbl_to_receipt_autocomplete.input(bl_no, loading_timeout=10)
    Pages.WHReceiptBasicTab.Dimension.dimension_link_apply_button.click()
    sleep(0.5)

    lnkd = Pages.WHReceiptBasicTab.Dimension(dim_index).lnkd_checkbox.get_value()
    shpd = Pages.WHReceiptBasicTab.Dimension(dim_index).shpd_checkbox.get_value()
    m = Pages.WHReceiptBasicTab.Dimension(dim_index).m_select.get_value()
    date = Pages.WHReceiptBasicTab.Dimension(dim_index).date_datepicker.get_value()
    b_l_bkg_no = Pages.WHReceiptBasicTab.Dimension(dim_index).b_l_bkg_no_input.get_value()

    assert Pages.WHReceiptBasicTab.Dimension(dim_index).lnkd_checkbox.is_enable(), "Lnkd is not enabled"
    assert Pages.WHReceiptBasicTab.Dimension(dim_index).shpd_checkbox.is_disabled(), "Shpd is not disabled"
    # ? KNOWN ISSUE OLC-5040
    if Pages.WHReceiptBasicTab.Dimension(dim_index).shpd_checkbox.get_value() == True:
        assert Pages.WHReceiptBasicTab.Dimension(dim_index).m_select.is_enable(), "M is not enabled"
    # ?
    assert Pages.WHReceiptBasicTab.Dimension(dim_index).date_datepicker.is_disabled(), "Date is not disabled"

    assert exp_lnkd == lnkd, "Lnkd expect [{0}], but get [{1}]".format(exp_lnkd, lnkd)
    # ? KNOWN ISSUE OLC-5040
    assert shpd != None, "Shpd should have value [{0}]".format(shpd)
    # assert exp_shpd == shpd, 'Shpd expect [{0}], but get [{1}]'.format(exp_shpd, shpd)
    # ?
    assert exp_m == m, "M expect [{0}], but get [{1}]".format(exp_m, m)
    assert exp_date == date, "Date expect [{0}], but get [{1}]".format(exp_date, date)
    assert exp_b_l_bkg_no == b_l_bkg_no, "B/L Bkg. No. expect [{0}], but get [{1}]".format(exp_b_l_bkg_no, b_l_bkg_no)

    Pages.Common.save_button.click()
    Pages.Common.spin_bar.gone()

    lnkd = Pages.WHReceiptBasicTab.Dimension(dim_index).lnkd_checkbox.get_value()
    shpd = Pages.WHReceiptBasicTab.Dimension(dim_index).shpd_checkbox.get_value()
    m = Pages.WHReceiptBasicTab.Dimension(dim_index).m_select.get_value()
    date = Pages.WHReceiptBasicTab.Dimension(dim_index).date_datepicker.get_value()
    b_l_bkg_no = Pages.WHReceiptBasicTab.Dimension(dim_index).b_l_bkg_no_input.get_value()

    assert Pages.WHReceiptBasicTab.Dimension(dim_index).lnkd_checkbox.is_enable(), "Lnkd is not enabled"
    assert Pages.WHReceiptBasicTab.Dimension(dim_index).shpd_checkbox.is_disabled(), "Shpd is not disabled"
    assert Pages.WHReceiptBasicTab.Dimension(dim_index).m_select.is_enable(), "M is not enabled"
    assert Pages.WHReceiptBasicTab.Dimension(dim_index).date_datepicker.is_disabled(), "Date is not disabled"
    assert exp_lnkd == lnkd, "Lnkd expect [{0}], but get [{1}]".format(exp_lnkd, lnkd)
    assert exp_shpd == shpd, "Shpd expect [{0}], but get [{1}]".format(exp_shpd, shpd)
    assert exp_m == m, "M expect [{0}], but get [{1}]".format(exp_m, m)
    assert exp_date == date, "Date expect [{0}], but get [{1}]".format(exp_date, date)
    assert exp_b_l_bkg_no == b_l_bkg_no, "B/L Bkg. No. expect [{0}], but get [{1}]".format(exp_b_l_bkg_no, b_l_bkg_no)


@When("the user link dimension({dim_index}) in receipt to AE '{mawb_name}' HAWB({hawb_index})")
def step_impl(context, dim_index, mawb_name, hawb_index):
    mawb_model = context._vp.get("mawb_model")["{}".format(mawb_name)]
    hawb_model = context._vp.get("hawb_model")["{}_{}".format(mawb_name, hawb_index)]
    bl_no = hawb_model.get_data("HAWB No.")
    date_time_format = gl.user_info.date_time_format
    date_time = mawb_model.get_data("Departure Date/Time")
    exp_date = datetime.strptime(date_time, date_time_format).strftime(
        "%Y-%m-%d"
    )  # when disable, become %Y-%m-%d format
    exp_lnkd, exp_shpd = True, True
    exp_m, exp_b_l_bkg_no = "A", bl_no

    Pages.WHReceiptBasicTab.Dimension(dim_index).checked_checkbox.tick(True)
    Pages.WHReceiptBasicTab.Dimension.dimension_link_hbl_to_receipt_autocomplete.input(bl_no, loading_timeout=10)
    Pages.WHReceiptBasicTab.Dimension.dimension_link_apply_button.click()
    sleep(0.5)

    lnkd = Pages.WHReceiptBasicTab.Dimension(dim_index).lnkd_checkbox.get_value()
    shpd = Pages.WHReceiptBasicTab.Dimension(dim_index).shpd_checkbox.get_value()
    m = Pages.WHReceiptBasicTab.Dimension(dim_index).m_select.get_value()
    date_time = Pages.WHReceiptBasicTab.Dimension(dim_index).date_datepicker.get_value()
    b_l_bkg_no = Pages.WHReceiptBasicTab.Dimension(dim_index).b_l_bkg_no_input.get_value()

    assert Pages.WHReceiptBasicTab.Dimension(dim_index).lnkd_checkbox.is_enable(), "Lnkd is not enabled"
    assert Pages.WHReceiptBasicTab.Dimension(dim_index).shpd_checkbox.is_disabled(), "Shpd is not disabled"
    # ? KNOWN ISSUE OLC-5040
    if Pages.WHReceiptBasicTab.Dimension(dim_index).shpd_checkbox.get_value() == True:
        assert Pages.WHReceiptBasicTab.Dimension(dim_index).m_select.is_enable(), "M is not enabled"
    # ?
    assert Pages.WHReceiptBasicTab.Dimension(dim_index).date_datepicker.is_disabled(), "Date is not disabled"

    assert exp_lnkd == lnkd, "Lnkd expect [{0}], but get [{1}]".format(exp_lnkd, lnkd)
    # ? KNOWN ISSUE OLC-5040
    assert shpd != None, "Shpd should have value [{0}]".format(shpd)
    # assert exp_shpd == shpd, 'Shpd expect [{0}], but get [{1}]'.format(exp_shpd, shpd)
    # ?
    assert exp_m == m, "M expect [{0}], but get [{1}]".format(exp_m, m)
    assert exp_date == date_time, "Date expect [{0}], but get [{1}]".format(exp_date, date_time)
    assert exp_b_l_bkg_no == b_l_bkg_no, "B/L Bkg. No. expect [{0}], but get [{1}]".format(exp_b_l_bkg_no, b_l_bkg_no)

    Pages.Common.save_button.click()
    Pages.Common.spin_bar.gone()

    lnkd = Pages.WHReceiptBasicTab.Dimension(dim_index).lnkd_checkbox.get_value()
    shpd = Pages.WHReceiptBasicTab.Dimension(dim_index).shpd_checkbox.get_value()
    m = Pages.WHReceiptBasicTab.Dimension(dim_index).m_select.get_value()
    date_time = Pages.WHReceiptBasicTab.Dimension(dim_index).date_datepicker.get_value()
    b_l_bkg_no = Pages.WHReceiptBasicTab.Dimension(dim_index).b_l_bkg_no_input.get_value()

    assert Pages.WHReceiptBasicTab.Dimension(dim_index).lnkd_checkbox.is_enable(), "Lnkd is not enabled"
    assert Pages.WHReceiptBasicTab.Dimension(dim_index).shpd_checkbox.is_disabled(), "Shpd is not disabled"
    assert Pages.WHReceiptBasicTab.Dimension(dim_index).m_select.is_enable(), "M is not enabled"
    assert Pages.WHReceiptBasicTab.Dimension(dim_index).date_datepicker.is_disabled(), "Date is not disabled"
    assert exp_lnkd == lnkd, "Lnkd expect [{0}], but get [{1}]".format(exp_lnkd, lnkd)
    assert exp_shpd == shpd, "Shpd expect [{0}], but get [{1}]".format(exp_shpd, shpd)
    assert exp_m == m, "M expect [{0}], but get [{1}]".format(exp_m, m)
    assert exp_date == date_time, "Date expect [{0}], but get [{1}]".format(exp_date, date_time)
    assert exp_b_l_bkg_no == b_l_bkg_no, "B/L Bkg. No. expect [{0}], but get [{1}]".format(exp_b_l_bkg_no, b_l_bkg_no)


@When("the user link dimension({dim_index}) in receipt to TK '{mbl_name}' MBL")
def step_impl(context, dim_index, mbl_name):
    mbl_model = context._vp.get("mbl_model")["{}".format(mbl_name)]
    try:
        bl_no = mbl_model.get_data("MB/L No.")
    except KeyError:
        bl_no = mbl_model.get_data("File No.")
    date_format = gl.user_info.date_format
    date = mbl_model.get_data("Post Date")
    exp_date = datetime.strptime(date, date_format).strftime("%Y-%m-%d")  # when disable, become %Y-%m-%d format
    exp_lnkd, exp_shpd = True, True
    exp_m, exp_b_l_bkg_no = "T", bl_no

    Pages.WHReceiptBasicTab.Dimension(dim_index).checked_checkbox.tick(True)
    Pages.WHReceiptBasicTab.Dimension.dimension_link_hbl_to_receipt_autocomplete.input(bl_no, loading_timeout=10)
    Pages.WHReceiptBasicTab.Dimension.dimension_link_apply_button.click()
    sleep(0.5)

    lnkd = Pages.WHReceiptBasicTab.Dimension(dim_index).lnkd_checkbox.get_value()
    shpd = Pages.WHReceiptBasicTab.Dimension(dim_index).shpd_checkbox.get_value()
    m = Pages.WHReceiptBasicTab.Dimension(dim_index).m_select.get_value()
    date = Pages.WHReceiptBasicTab.Dimension(dim_index).date_datepicker.get_value()
    b_l_bkg_no = Pages.WHReceiptBasicTab.Dimension(dim_index).b_l_bkg_no_input.get_value()

    assert Pages.WHReceiptBasicTab.Dimension(dim_index).lnkd_checkbox.is_enable(), "Lnkd is not enabled"
    assert Pages.WHReceiptBasicTab.Dimension(dim_index).shpd_checkbox.is_disabled(), "Shpd is not disabled"
    # ? KNOWN ISSUE OLC-5040
    if Pages.WHReceiptBasicTab.Dimension(dim_index).shpd_checkbox.get_value() == True:
        assert Pages.WHReceiptBasicTab.Dimension(dim_index).m_select.is_enable(), "M is not enabled"
    # ?
    assert Pages.WHReceiptBasicTab.Dimension(dim_index).date_datepicker.is_disabled(), "Date is not disabled"

    assert exp_lnkd == lnkd, "Lnkd expect [{0}], but get [{1}]".format(exp_lnkd, lnkd)
    # ? KNOWN ISSUE OLC-5040
    assert shpd != None, "Shpd should have value [{0}]".format(shpd)
    # assert exp_shpd == shpd, 'Shpd expect [{0}], but get [{1}]'.format(exp_shpd, shpd)
    # ?
    assert exp_m == m, "M expect [{0}], but get [{1}]".format(exp_m, m)
    assert exp_date == date, "Date expect [{0}], but get [{1}]".format(exp_date, date)
    assert exp_b_l_bkg_no == b_l_bkg_no, "B/L Bkg. No. expect [{0}], but get [{1}]".format(exp_b_l_bkg_no, b_l_bkg_no)

    Pages.Common.save_button.click()
    Pages.Common.spin_bar.gone()

    lnkd = Pages.WHReceiptBasicTab.Dimension(dim_index).lnkd_checkbox.get_value()
    shpd = Pages.WHReceiptBasicTab.Dimension(dim_index).shpd_checkbox.get_value()
    m = Pages.WHReceiptBasicTab.Dimension(dim_index).m_select.get_value()
    date = Pages.WHReceiptBasicTab.Dimension(dim_index).date_datepicker.get_value()
    b_l_bkg_no = Pages.WHReceiptBasicTab.Dimension(dim_index).b_l_bkg_no_input.get_value()

    assert Pages.WHReceiptBasicTab.Dimension(dim_index).lnkd_checkbox.is_enable(), "Lnkd is not enabled"
    assert Pages.WHReceiptBasicTab.Dimension(dim_index).shpd_checkbox.is_disabled(), "Shpd is not disabled"
    assert Pages.WHReceiptBasicTab.Dimension(dim_index).m_select.is_enable(), "M is not enabled"
    assert Pages.WHReceiptBasicTab.Dimension(dim_index).date_datepicker.is_disabled(), "Date is not disabled"
    assert exp_lnkd == lnkd, "Lnkd expect [{0}], but get [{1}]".format(exp_lnkd, lnkd)
    assert exp_shpd == shpd, "Shpd expect [{0}], but get [{1}]".format(exp_shpd, shpd)
    assert exp_m == m, "M expect [{0}], but get [{1}]".format(exp_m, m)
    assert exp_date == date, "Date expect [{0}], but get [{1}]".format(exp_date, date)
    assert exp_b_l_bkg_no == b_l_bkg_no, "B/L Bkg. No. expect [{0}], but get [{1}]".format(exp_b_l_bkg_no, b_l_bkg_no)


@When("the user link dimension({dim_index}) in receipt to MS '{mbl_name}' MBL")
def step_impl(context, dim_index, mbl_name):
    mbl_model = context._vp.get("mbl_model")["{}".format(mbl_name)]
    try:
        bl_no = mbl_model.get_data("MB/L No.")
    except KeyError:
        bl_no = mbl_model.get_data("File No.")
    date_format = gl.user_info.date_format
    date = mbl_model.get_data("Post Date")
    exp_date = datetime.strptime(date, date_format).strftime("%Y-%m-%d")  # when disable, become %Y-%m-%d format
    exp_lnkd, exp_shpd = True, True
    exp_m, exp_b_l_bkg_no = "M", bl_no

    Pages.WHReceiptBasicTab.Dimension(dim_index).checked_checkbox.tick(True)
    Pages.WHReceiptBasicTab.Dimension.dimension_link_hbl_to_receipt_autocomplete.input(bl_no, loading_timeout=10)
    Pages.WHReceiptBasicTab.Dimension.dimension_link_apply_button.click()
    sleep(0.5)

    lnkd = Pages.WHReceiptBasicTab.Dimension(dim_index).lnkd_checkbox.get_value()
    shpd = Pages.WHReceiptBasicTab.Dimension(dim_index).shpd_checkbox.get_value()
    m = Pages.WHReceiptBasicTab.Dimension(dim_index).m_select.get_value()
    date = Pages.WHReceiptBasicTab.Dimension(dim_index).date_datepicker.get_value()
    b_l_bkg_no = Pages.WHReceiptBasicTab.Dimension(dim_index).b_l_bkg_no_input.get_value()

    assert Pages.WHReceiptBasicTab.Dimension(dim_index).lnkd_checkbox.is_enable(), "Lnkd is not enabled"
    assert Pages.WHReceiptBasicTab.Dimension(dim_index).shpd_checkbox.is_disabled(), "Shpd is not disabled"
    # ? KNOWN ISSUE OLC-5040
    if Pages.WHReceiptBasicTab.Dimension(dim_index).shpd_checkbox.get_value() == True:
        assert Pages.WHReceiptBasicTab.Dimension(dim_index).m_select.is_enable(), "M is not enabled"
    # ?
    assert Pages.WHReceiptBasicTab.Dimension(dim_index).date_datepicker.is_disabled(), "Date is not disabled"

    assert exp_lnkd == lnkd, "Lnkd expect [{0}], but get [{1}]".format(exp_lnkd, lnkd)
    # ? KNOWN ISSUE OLC-5040
    assert shpd != None, "Shpd should have value [{0}]".format(shpd)
    # assert exp_shpd == shpd, 'Shpd expect [{0}], but get [{1}]'.format(exp_shpd, shpd)
    # ?
    assert exp_m == m, "M expect [{0}], but get [{1}]".format(exp_m, m)
    assert exp_date == date, "Date expect [{0}], but get [{1}]".format(exp_date, date)
    assert exp_b_l_bkg_no == b_l_bkg_no, "B/L Bkg. No. expect [{0}], but get [{1}]".format(exp_b_l_bkg_no, b_l_bkg_no)

    Pages.Common.save_button.click()
    Pages.Common.spin_bar.gone()

    lnkd = Pages.WHReceiptBasicTab.Dimension(dim_index).lnkd_checkbox.get_value()
    shpd = Pages.WHReceiptBasicTab.Dimension(dim_index).shpd_checkbox.get_value()
    m = Pages.WHReceiptBasicTab.Dimension(dim_index).m_select.get_value()
    date = Pages.WHReceiptBasicTab.Dimension(dim_index).date_datepicker.get_value()
    b_l_bkg_no = Pages.WHReceiptBasicTab.Dimension(dim_index).b_l_bkg_no_input.get_value()

    assert Pages.WHReceiptBasicTab.Dimension(dim_index).lnkd_checkbox.is_enable(), "Lnkd is not enabled"
    assert Pages.WHReceiptBasicTab.Dimension(dim_index).shpd_checkbox.is_disabled(), "Shpd is not disabled"
    assert Pages.WHReceiptBasicTab.Dimension(dim_index).m_select.is_enable(), "M is not enabled"
    assert Pages.WHReceiptBasicTab.Dimension(dim_index).date_datepicker.is_disabled(), "Date is not disabled"
    assert exp_lnkd == lnkd, "Lnkd expect [{0}], but get [{1}]".format(exp_lnkd, lnkd)
    assert exp_shpd == shpd, "Shpd expect [{0}], but get [{1}]".format(exp_shpd, shpd)
    assert exp_m == m, "M expect [{0}], but get [{1}]".format(exp_m, m)
    assert exp_date == date, "Date expect [{0}], but get [{1}]".format(exp_date, date)
    assert exp_b_l_bkg_no == b_l_bkg_no, "B/L Bkg. No. expect [{0}], but get [{1}]".format(exp_b_l_bkg_no, b_l_bkg_no)


@When("the user click WH receipt '{name}' 'Tools -> Copy'")
def step_impl(context, name):
    Driver.open(context._vp.get("receipt_url")[name])
    Pages.Common.spin_bar.gone()
    Pages.WHReceiptBasicTab.tools_button.click()
    Pages.WHReceiptBasicTab.tools_copy_button.click()
    Pages.Common.spin_bar.gone()


@Then("the 'automobile' receipt has empty Vin No. and Customer")
def step_impl(context):
    assert Pages.WHReceiptBasicTab.am_vin_no_autocomplete.get_value() == "", "Vin NO. should be empty field"
    assert Pages.WHReceiptBasicTab.am_customer_autocomplete.get_value() == "", "Customer should be empty field"


@Then("the receipt should be copied from receipt '{name}'")
def step_impl(context, name):
    model = context._vp.get("receipt_model")[name]
    model.set_page_class_name("Pages.WHReceiptBasicTab")
    vm_fields = model.get_all_fields()
    copied_fields = [i["field"] for i in context.table]
    for f in vm_fields:
        if f == "Warehouse Receipt No.":
            continue
        if f not in copied_fields:
            f_dict = model.pop(f)
            if f == "Received Date/Time":
                data = wday(0) + " 00:00"
            else:
                data = ""
            model.add(field=f, attribute=f_dict[model.ATTRIBUTE], data=data)
    model.verify()

    # dimension should be copied to
    for i in range(1, 5):
        dim_model = context._vp.get("receipt_dimension_model")["{}_{}".format(name, i)]
        dim_model.set_page_class_name("Pages.WHReceiptBasicTab.Dimension({})".format(i))
        dim_model.verify()


@Then("none of automobile feilds in receipt '{name}' should be copied from receipt '{copied_name}'")
def step_impl(context, name, copied_name):
    copied_model = context._vp.get("receipt_am_model")[copied_name].copy()
    model = context._vp.get("receipt_model")[name]
    copied_model.set_page_class_name("Pages.WHReceiptBasicTab")
    vm_fields = copied_model.get_all_fields()
    for f in vm_fields:
        if f == "Warehouse Receipt No.":
            continue
        if f == "AM Vin No.":
            data = model.get_data(field="AM Vin No.")
        elif f == "AM Customer":
            data = model.get_data(field="AM Customer")
        elif copied_model.get_attribute(f) == "radio group":
            data = None
        elif copied_model.get_attribute(f) == "checkbox":
            data = False
        else:
            data = ""
        f_dict = copied_model.pop(f)
        copied_model.add(field=f, attribute=f_dict[model.ATTRIBUTE], data=data)
    copied_model.verify()


@When("the user copy WH receipt dimension({index})")
def step_impl(context, index):
    Pages.WHReceiptBasicTab.Dimension(index).checked_checkbox.tick(True)
    Pages.WHReceiptBasicTab.Dimension.dimension_copy_button.click()


@Then(
    "the dimension({copy_index}) copied from dimension({index}) in receipt '{name}' should be the same except for field Lnkd, Date, BL BKG. No."
)
def step_impl(context, index, copy_index, name):
    model = context._vp.get("receipt_dimension_model")[name][int(index) - 1]
    model.set_page_class_name("Pages.WHReceiptBasicTab.Dimension({})".format(copy_index))
    model.add(field="Lnkd", attribute="checkbox", data=False)
    # ? KNOWN ISSUE OLC-5040
    model.add(field="Shpd", attribute="checkbox", data=True)
    model.add(
        field="M",
        attribute="select",
        data=Pages.WHReceiptBasicTab.Dimension(index).m_select.get_value(),
    )
    # model.add(field='Shpd', attribute='checkbox', data=False)
    # model.add(field='M', attribute='select', data='')
    # ?
    model.add(field="Date", attribute="datepicker", data="")
    model.add(field="B/L Bkg. No.", attribute="input", data="")
    model.verify()


@When("the user unlink WH receipt '{name}' dimension({index})")
def step_impl(context, name, index):
    # ? KNOWN ISSUE OLC-5040
    exp_m = Pages.WHReceiptBasicTab.Dimension(index).m_select.get_value()
    # ?
    Pages.WHReceiptBasicTab.Dimension(index).lnkd_checkbox.tick(False)
    sleep(3)
    models = context._vp.get("receipt_dimension_model")[name]
    model = models[int(index) - 1]

    shpd = Pages.WHReceiptBasicTab.Dimension(index).shpd_checkbox.get_value()
    m = Pages.WHReceiptBasicTab.Dimension(index).m_select.get_value()
    date = Pages.WHReceiptBasicTab.Dimension(index).date_datepicker.get_value()
    b_l_bkg_no = Pages.WHReceiptBasicTab.Dimension(index).b_l_bkg_no_input.get_value()

    # ? KNOWN ISSUE OLC-5040
    assert Pages.WHReceiptBasicTab.Dimension(index).shpd_checkbox.is_enable(), "Shpd is not enabled"
    assert Pages.WHReceiptBasicTab.Dimension(index).m_select.is_enable(), "M is not enabled"
    assert Pages.WHReceiptBasicTab.Dimension(index).date_datepicker.is_enable(), "Date is not enabled"
    assert Pages.WHReceiptBasicTab.Dimension(index).b_l_bkg_no_input.is_enable(), "B/L Bkg. No. is not enabled"
    assert shpd == True, "Shpd expect [{0}], but get [{1}]".format(True, shpd)
    assert m == exp_m, "M expect [{0}], but get [{1}]".format(exp_m, m)
    # assert Pages.WHReceiptBasicTab.Dimension(index).shpd_checkbox.is_disable(), 'Shpd is not disabled'
    # assert Pages.WHReceiptBasicTab.Dimension(index).m_select.is_disable(), 'M is not disabled'
    # assert Pages.WHReceiptBasicTab.Dimension(index).date_datepicker.is_disable(), 'Date is not disabled'
    # assert Pages.WHReceiptBasicTab.Dimension(index).b_l_bkg_no_input.is_disable(), 'B/L Bkg. No. is not disabled'
    # assert shpd == False, 'Shpd expect [{0}], but get [{1}]'.format(False, shpd)
    # assert m == '', 'M expect [{0}], but get [{1}]'.format('', m)
    # ?
    assert date == "", "Date expect [{0}], but get [{1}]".format("", date)
    assert b_l_bkg_no == "", "B/L Bkg. No. expect [{0}], but get [{1}]".format("", b_l_bkg_no)

    model.add(field="Lnkd", attribute="checkbox", data=False)
    # ? KNOWN ISSUE OLC-5040 (Updated 2021/12/8)
    if exp_m == "T" or exp_m == "M":
        model.add(field="Shpd", attribute="checkbox", data=True)
        model.add(field="M", attribute="select", data=exp_m)
    elif exp_m == "O" or exp_m == "A":
        model.add(field="Shpd", attribute="checkbox", data=False)
        model.add(field="M", attribute="select", data="")
    # ?
    model.add(field="Date", attribute="datepicker", data="")
    model.add(field="B/L Bkg. No.", attribute="input", data="")


@When("the user unshipped WH receipt '{name}' dimension({index})")
def step_impl(context, name, index):
    # ? KNOWN ISSUE OLC-5041
    exp_m = Pages.WHReceiptBasicTab.Dimension(index).m_select.get_value()
    exp_date = Pages.WHReceiptBasicTab.Dimension(index).date_datepicker.get_value()
    exp_bkg_no = Pages.WHReceiptBasicTab.Dimension(index).b_l_bkg_no_input.get_value()
    # ?
    Pages.WHReceiptBasicTab.Dimension(index).shpd_checkbox.tick(False)

    m = Pages.WHReceiptBasicTab.Dimension(index).m_select.get_value()
    date = Pages.WHReceiptBasicTab.Dimension(index).date_datepicker.get_value()
    b_l_bkg_no = Pages.WHReceiptBasicTab.Dimension(index).b_l_bkg_no_input.get_value()

    assert Pages.WHReceiptBasicTab.Dimension(index).m_select.is_disabled(), "M is not disabled"
    assert Pages.WHReceiptBasicTab.Dimension(index).date_datepicker.is_disabled(), "Date is not disabled"
    assert Pages.WHReceiptBasicTab.Dimension(index).b_l_bkg_no_input.is_disabled(), "B/L Bkg. No. is not disabled"
    # ? KNOWN ISSUE OLC-5041
    assert m == exp_m, "M expect [{0}], but get [{1}]".format(exp_m, m)
    assert date == exp_date, "Date expect [{0}], but get [{1}]".format(exp_date, date)
    assert b_l_bkg_no == exp_bkg_no, "B/L Bkg. No. expect [{0}], but get [{1}]".format(exp_bkg_no, b_l_bkg_no)
    # assert m == '', 'M expect [{0}], but get [{1}]'.format('', m)
    # assert date == '', 'Date expect [{0}], but get [{1}]'.format('', date)
    # assert b_l_bkg_no == '', 'B/L Bkg. No. expect [{0}], but get [{1}]'.format('', b_l_bkg_no)
    # ?

    models = context._vp.get("receipt_dimension_model")[name]
    model = models[int(index) - 1]
    model.add(field="Lnkd", attribute="checkbox", data=False)
    model.add(field="Shpd", attribute="checkbox", data=False)
    # ? KNOWN ISSUE OLC-5041
    model.add(field="M", attribute="select", data=exp_m)
    model.add(field="Date", attribute="datepicker", data=exp_date)
    model.add(field="B/L Bkg. No.", attribute="input", data=exp_bkg_no)
    # model.add(field='M', attribute='select', data='')
    # model.add(field='Date', attribute='datepicker', data='')
    # model.add(field='B/L Bkg. No.', attribute='input', data='')
    # ?
