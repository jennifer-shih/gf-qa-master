import re
from time import sleep

from behave import *

import src.pages as Pages  # noqa
from config import globalparameter as gl
from src.drivers.driver import Driver
from src.helper.executor import exec_act_cmd
from src.helper.filters import ExceptedFilter
from src.helper.function import wday
from src.helper.script import input_dynamic_datas
from src.helper.transfer import transfer_to_feature_table
from src.models import VerifiedModel


@When("the user click OI MBL 'More' button")
def step_impl(context):
    # 如果沒展開再click more button
    if Pages.OIBasicTab.MBL.it_date_datepicker.is_disable():  # TODO GQT-423 如果眼睛看到的話（不論看不看得到，都會在 dom 上）
        Pages.OIBasicTab.MBL.more_button.click()


@When("the user tick OI 'Direct Master' checkbox")
def step_impl(context):
    Pages.OIBasicTab.MBL.direct_master_checkbox.tick(True)
    Pages.Common.spin_bar.gone()


@When("the user click OI HBL({index}) 'More' button")
def step_impl(context, index):
    # 如果沒展開再click more button
    if Pages.OIBasicTab.HBL(index).ship_type_select.is_disable():  # TODO GQT-423 如果眼睛看到的話（不論看不看得到，都會在 dom 上）
        Pages.OIBasicTab.HBL(index).more_button.click()


@Then("the shipment '{name}' of 'Ocean Import' will be created")
def step_impl(context, name):
    model = context._vp.get("mbl_model")[name]

    # go to the shipment which just created
    Driver.open(context._vp.get("url"))
    Pages.Common.spin_bar.gone()
    Pages.OIBasicTab.MBL.more_button.click()

    # url should be https://fms-stage-qa-5.gofreight.co/truck/shipment/{File_No}/
    file_no = Driver.get_url().split("/")[-2]
    model.add(field="file_no", attribute="input", data=file_no)

    # direct master
    # 如果有填 Consignee, 且 Notify, Customer, Bill To都沒有另外輸入value，這些欄位會與Consignee相同
    if (
        Pages.OIBasicTab.MBL.direct_master_checkbox.get_value() == True
        and model.has_key("Consignee")
        and not model.has_key("Notify")
        and not model.has_key("Customer")
        and not model.has_key("Bill To")
    ):
        consignee = model.get_data("Consignee")
        model.add(field="Notify", attribute="autocomplete", data=consignee)
        model.add(field="Customer", attribute="autocomplete", data=consignee)
        model.add(field="Bill To", attribute="autocomplete", data=consignee)

    # ? KNOWN ISSUE
    it_iss_loc_field = "IT Issued Location"
    if model.has_key(it_iss_loc_field):
        v = model.pop(it_iss_loc_field)
        exp = v[VerifiedModel.DATA]
        value = exec_act_cmd(it_iss_loc_field, v[VerifiedModel.ATTRIBUTE], "get_value", page=model.page_class_name)
        regex = r"\((\d+)\) " + exp
        assert re.match(regex, value) != None, "{0}: [{1}] must be [{2}]".format(it_iss_loc_field, value, regex)
    # ?

    model.verify()


@Given("the user has a OI MBL with {count} HBL as '{name}'")
def step_impl(context, count, name):
    create_oi_mbl_table = transfer_to_feature_table(
        """
        | field                  | attribute    | action        | data                            |
        | MB/L No.               | input        | input         | HACO-{randN(6)}                 |
        | ETA                    | datepicker   | input         | {today+2}                       |
    """
    )

    create_oi_hbl_table = transfer_to_feature_table(
        """
        | field                   | attribute        | action               | data                            |
        | HB/L No.                | input            | input                | 111-{randomNo(6)}               |
        | AMS No.                 | input            | input                | AMS{randN(6)}                   |
        | ISF No.                 | input            | input                | ISF{randN(6)}                   |
        | ISF Filing by 3rd Party | checkbox         | tick                 | {on}                            |
        | Shipper                 | autocomplete     | input                | {randomTradePartner}            |
        | Consignee               | autocomplete     | input and close memo | {randomTradePartner}            |
        | Sub B/L No.             | input            | input                | SBL{randomNo(6)}                |
        | Forwarding Agent        | autocomplete     | input                | {randomTradePartner}            |
        | Customs Broker          | autocomplete     | input                | {randomTradePartner}            |
        | Trucker                 | autocomplete     | input                | {randomTradePartner}            |
        | CY/CFS Location         | autocomplete     | input                | {randomTradePartner}            |
        | Available               | datepicker       | input                | {today+5}                       |
        | Place of Delivery       | autocomplete     | input                | {randomPort}                    |
        | Place of Delivery ETA   | datepicker       | input                | {today+3}                       |
        | Final Destination       | autocomplete     | input                | {randomPort}                    |
        | Final ETA               | datepicker       | input                | {today+4}                       |
        | Ship Mode               | select           | random select        |                                 |
        | Freight                 | select           | random select        |                                 |
        | LFD                     | datepicker       | input                | {today+6}                       |
        | Rail                    | check select     | random select        |                                 |
        | IT No.                  | input            | input                | IT{randomNo(4)}                 |
        | IT Date                 | datepicker       | input                | {today+9}                       |
        | IT Issued Location      | autocomplete     | input                | 3074                            |
        | G.O Date                | datepicker       | input                | {today+7}                       |
        | Expiry Date             | datepicker       | input                | {today+9}                       |
        | Express B/L             | radio group      | click                | No                              |
        | Sales Type              | select           | random select        |                                 |
        | Incoterms               | select           | random select        |                                 |
        | Cargo Type              | select           | random select        |                                 |
        | Door Move               | checkbox         | tick                 | {on}                            |
        | C.Clearance             | checkbox         | tick                 | {on}                            |
        | C.Hold                  | checkbox         | tick                 | {on}                            |
        | C. Released Date        | datepicker       | input                | {today+8}                       |
        | Service Term From       | select           | random select        |                                 |
        | Service Term To         | select           | random select        |                                 |
        | Business Referred By    | autocomplete     | input                | {randomTradePartner}            |
        | OB/L Received           | check datepicker | tick                 | {on}                            |
        | Telex release received  | check datepicker | tick                 | {on}                            |
        | ROR                     | checkbox         | tick                 | {on}                            |
        | Frt. Released           | check datepicker | tick and close memo  |                                 |
        | Door Delivered          | datepicker       | input                | {today+10}                      |
        | L/C No.                 | input            | input                | LC{randN(6)}                    |
        | Ship Type               | select           | random select        |                                 |
        | S/C No.                 | input            | input                | SCNO{randN(6)}                  |
        | Name Account            | input            | input                | NA{randN(6)}                    |
        | Group Comm              | input            | input                | GC{randN(6)}                    |
        | Line Code               | input            | input                | LC{randN(6)}                    |
        | E-Commerce              | checkbox         | tick                 | {on}                            |
    """
    )

    # create a new MBL
    Driver.open(gl.URL.OI_NEW_SHIPMENT)
    Pages.Common.spin_bar.gone()
    Pages.OIBasicTab.MBL.more_button.click()
    mbl_model = input_dynamic_datas(create_oi_mbl_table, "Pages.OIBasicTab.MBL", ExceptedFilter.oi_mbl_filter)
    Pages.Common.save_button.click()
    assert Pages.Common.save_msg.is_visible(timeout=30) is True

    # add additional field
    mbl_model.add(
        field="File No.",
        attribute="input",
        data=Pages.OIBasicTab.MBL.file_no_input.get_value(),
    )
    mbl_model.add(
        field="Office",
        attribute="autocomplete",
        data=Pages.OIBasicTab.MBL.office_autocomplete.get_value(),
    )

    context._vp.add_dict(dict_name="mbl_model", value={name: mbl_model})

    # create new HBLs
    for i in range(1, int(count) + 1):
        Pages.OIBasicTab.add_hb_l_button.click()
        sleep(2)

        # Expand the MBL board to prevent it's folded by default when swithing tab
        Pages.OIBasicTab.MBL.expand_button.click()
        sleep(2)

        Pages.OIBasicTab.HBL(i).more_button.click()
        hbl_model = input_dynamic_datas(
            create_oi_hbl_table,
            "Pages.OIBasicTab.HBL({})".format(i),
            ExceptedFilter.oi_hbl_filter,
        )

        Pages.Common.save_button.click()
        Pages.Common.spin_bar.gone()
        assert Pages.Common.save_msg.is_visible(timeout=10) is True

        hbl_model.add(
            field="Notify",
            attribute="autocomplete",
            data=Pages.OIBasicTab.HBL(i).notify_autocomplete.get_value(),
        )
        hbl_model.add(
            field="Customer",
            attribute="autocomplete",
            data=Pages.OIBasicTab.HBL(i).customer_autocomplete.get_value(),
        )
        hbl_model.add(
            field="Bill To",
            attribute="autocomplete",
            data=Pages.OIBasicTab.HBL(i).bill_to_autocomplete.get_value(),
        )
        hbl_model.add(
            field="Delivery Location",
            attribute="autocomplete",
            data=Pages.OIBasicTab.HBL(i).delivery_location_autocomplete.get_value(),
        )
        hbl_model.add(
            field="OP",
            attribute="autocomplete",
            data=Pages.OIBasicTab.HBL(i).op_autocomplete.get_value(),
        )

        context._vp.add_dict(dict_name="hbl_model", value={"{}_{}".format(name, i): hbl_model})

    context._vp.add_dict(dict_name="shipment_url", value={name: Driver.get_url()})


@Given("the user has a OI MBL with {count} HBL as '{name}' with only required fields filled")
def step_impl(context, count, name):
    create_oi_mbl_table = transfer_to_feature_table(
        """
        | field                  | attribute    | action        | data                            |
        | MB/L No.               | input        | input         | HACO-{randN(6)}                 |
        | ETA                    | datepicker   | input         | {today+2}                       |
    """
    )

    create_oi_hbl_table = transfer_to_feature_table(
        """
        | field                   | attribute        | action               | data                            |
        | HB/L No.                | input            | input                | 111-{randomNo(6)}               |
        | Sales                   | autocomplete     | input                | {randomSales}                   |
    """
    )

    # create a new MBL
    Driver.open(gl.URL.OI_NEW_SHIPMENT)
    Pages.Common.spin_bar.gone()
    Pages.OIBasicTab.MBL.more_button.click()
    mbl_model = input_dynamic_datas(create_oi_mbl_table, "Pages.OIBasicTab.MBL", ExceptedFilter.oi_mbl_filter)
    Pages.Common.save_button.click()
    assert Pages.Common.save_msg.is_visible(timeout=30) is True

    # add additional field
    mbl_model.add(
        field="File No.",
        attribute="input",
        data=Pages.OIBasicTab.MBL.file_no_input.get_value(),
    )
    mbl_model.add(
        field="Office",
        attribute="autocomplete",
        data=Pages.OIBasicTab.MBL.office_autocomplete.get_value(),
    )

    context._vp.add_dict(dict_name="mbl_model", value={name: mbl_model})

    # create new HBLs
    for i in range(1, int(count) + 1):
        Pages.OIBasicTab.add_hb_l_button.click()
        sleep(2)

        # Expand the MBL board to prevent it's folded by default when swithing tab
        Pages.OIBasicTab.MBL.expand_button.click()
        sleep(2)

        Pages.OIBasicTab.HBL(i).more_button.click()
        hbl_model = input_dynamic_datas(
            create_oi_hbl_table,
            "Pages.OIBasicTab.HBL({})".format(i),
            ExceptedFilter.oi_hbl_filter,
        )

        Pages.Common.save_button.click()
        Pages.Common.spin_bar.gone()
        assert Pages.Common.save_msg.is_visible(timeout=10) is True

        hbl_model.add(
            field="Notify",
            attribute="autocomplete",
            data=Pages.OIBasicTab.HBL(i).notify_autocomplete.get_value(),
        )
        hbl_model.add(
            field="Customer",
            attribute="autocomplete",
            data=Pages.OIBasicTab.HBL(i).customer_autocomplete.get_value(),
        )
        hbl_model.add(
            field="Bill To",
            attribute="autocomplete",
            data=Pages.OIBasicTab.HBL(i).bill_to_autocomplete.get_value(),
        )
        hbl_model.add(
            field="Delivery Location",
            attribute="autocomplete",
            data=Pages.OIBasicTab.HBL(i).delivery_location_autocomplete.get_value(),
        )
        hbl_model.add(
            field="OP",
            attribute="autocomplete",
            data=Pages.OIBasicTab.HBL(i).op_autocomplete.get_value(),
        )

        context._vp.add_dict(dict_name="hbl_model", value={"{}_{}".format(name, i): hbl_model})

    context._vp.add_dict(dict_name="shipment_url", value={name: Driver.get_url()})


@When("the user click OI 'Add HBL' button")
def step_impl(context):
    Pages.OIBasicTab.add_hb_l_button.click()
    sleep(5)


@Then("the shipment '{name}' HBL({index}) of 'Ocean Import' will be created")
def step_impl(context, name, index):
    model = context._vp.get("hbl_model")["{}_{}".format(name, index)]

    # go to the shipment which just created
    Driver.open(context._vp.get("url"))
    Pages.Common.spin_bar.gone()
    Pages.OIBasicTab.HBL(index).hbl_side_panel.click()
    Pages.OIBasicTab.HBL(index).more_button.click()

    model.verify()


@When("the user select '{value}' for field 'Carrier'")
def step_impl(context, value):
    Pages.OIBasicTab.MBL.carrier_autocomplete.input(value)


@Then("'BL Acct. Carrier' should be autofilled with '{exp}'")
def step_impl(context, exp):
    sleep(2)
    result = Pages.OIBasicTab.MBL.b_l_acct_carrier_autocomplete.get_value()
    assert exp == result, "Expect [{0}]. but get [{1}]".format(exp, result)


@When("the user create a shipment that 'ETA' is 'today'")
def step_impl(context):
    context.execute_steps(
        """
        Given the user is on 'Ocean Import New Shipment' page
        When the user enter 'OI MBL' shipment datas as 'A' and save it
            | field    | attribute    | action | data            |
            | MB/L No. | input        | input  | HACO-{randN(6)} |
            | ETA      | datepicker   | input  | {today}         |
    """
    )


@Then("'Post Date' should be autofilled with 'today'")
def step_impl(context):
    result = Pages.OIBasicTab.MBL.post_date_input.get_value()
    exp = wday(0)
    assert exp == result, "Expect [{0}]. but get [{1}]".format(exp, result)


@When("the user switch 'Ship Mode' to {ship_mode}")
def step_impl(context, ship_mode):
    Pages.OIBasicTab.MBL.ship_mode_select.select(ship_mode)


@When("the user switch 'OBL Type' to {obl_type}")
def step_impl(context, obl_type):
    Pages.OIBasicTab.MBL.ob_l_type_select.select(obl_type)


@Then("'Service Term From' and 'Service Term To' should be change to 'CFS'")
def step_impl(context):
    from_val = Pages.OIBasicTab.MBL.service_term_from_select.get_value()
    to_val = Pages.OIBasicTab.MBL.service_term_to_select.get_value()
    assert "CFS" == from_val, "Expect [Service Term From] is [CFS], but get [{0}]".format(from_val)
    assert "CFS" == to_val, "Expect [Service Term To] is [CFS], but get [{0}]".format(to_val)
    # ship mode 只有切換到LCL or FAK才會強制變更service term，切換至FCL or BULK並不會有動作
    Driver.refresh()


@Then("'Received' field should change to {received}")
def step_impl(context, received):
    result = exec_act_cmd(received, "checkbox", "is_disabled", page="Pages.OIBasicTab.MBL")
    assert result == False, "Received field [{}] not show".format(received)
    # TODO GQT-423 應該要 checkbox 是不是 visible 或 enable 吧


@When("the user input '{value}' for MBL field 'Sub BL No.'")
def step_impl(context, value):
    Pages.OIBasicTab.MBL.sub_b_l_no_input.input(value)


@Then("new HBL field 'Sub BL No.' should be autofilled with '{exp}'")
def step_impl(context, exp):
    Pages.OIBasicTab.add_hb_l_button.click()
    result = Pages.OIBasicTab.HBL(1).sub_b_l_no_input.get_value()
    assert exp == result, "Expect [{0}]. but get [{1}]".format(exp, result)


@When("the user click OI '{name}' HBL({index}) 'Tools -> Copy To'")
def step_impl(context, name, index):
    Driver.open(context._vp.get("shipment_url")[name])
    Pages.Common.spin_bar.gone()
    Pages.OIBasicTab.HBL(index).hbl_side_panel.click()
    sleep(2)
    Pages.OIBasicTab.HBL(index).tools_button.click()
    Pages.OIBasicTab.HBL(index).tools_copy_to_button.click()


@When("the user input '{name}' to OI copy HBL to")
def step_impl(context, name):
    mbl_no = context._vp.get("mbl_model")[name].get_data("MB/L No.")
    Pages.OIBasicTab.CopyHBLToMBL.select_mbl_autocomplete.input(mbl_no)


@When("the user click 'OK' button in OI 'Copy To' dialog")
def step_impl(context):
    Pages.OIBasicTab.CopyHBLToMBL.ok_button.click()


@Then("the link of '{name}' should show in OI 'Copy To' dialog")
def step_impl(context, name):
    exp = context._vp.get("mbl_model")[name].get_data("File No.")
    v = Pages.OIBasicTab.CopyHBLToMBL.mbl_link.get_value()
    assert exp == v, "Link shoud be [{0}], not [{1}]".format(exp, v)


@When("the user click the OI copied link")
def step_impl(context):
    Pages.OIBasicTab.CopyHBLToMBL.mbl_link.click()
    Driver.switch_to(window_index=1)
    Pages.Common.spin_bar.gone()


@Then("the HBL({index_1}) should copy from OI '{name}' HBL({index_2})")
def step_impl(context, index_1, name, index_2):
    Pages.OIBasicTab.HBL(index_1).hbl_side_panel.click()
    Pages.OIBasicTab.HBL(index_1).more_button.click()
    model = context._vp.get("hbl_model")["{}_{}".format(name, index_2)]
    model.set_page_class_name("Pages.OIBasicTab.HBL({})".format(index_1))
    vm_fields = model.get_all_fields()
    copied_fields = [i["field"] for i in context.table]
    for f in vm_fields:
        if f not in copied_fields:
            f_dict = model.pop(f)
            if f_dict[model.ATTRIBUTE] == "checkbox":
                data = False
            elif f_dict[model.ATTRIBUTE] == "check datepicker":
                data = (False, None)
            else:
                data = ""
            model.add(field=f, attribute=f_dict[model.ATTRIBUTE], data=data)
    model.pop("HB/L No.")
    model.verify()


@Then("the OI HBL({index}) should have 'COPY-1' as HBL NO.")
def step_impl(context, index):
    exp = "COPY-1"
    hbl_no = Pages.OIBasicTab.HBL(index).hb_l_no_input.get_value()
    assert hbl_no == exp, "HB/L No. should be [{0}], not [{1}]".format(exp, hbl_no)


@When("the user click 'Accounting' tab of OI")
def step_impl(context):
    Pages.OITab.accounting_tab.click()
    Pages.Common.spin_bar.gone()


@When("the user without tax permission add freights to OI '{name}' HBL({index}) AR")
def step_impl(context, name, index):
    freight_index = 1
    sleep(0.5)
    for row in context.table:
        Pages.OIAccountingBillingBasedTab.HBL.revenue.new_button.click()
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
        ]
        hbl_freight_model = input_dynamic_datas(
            action_table,
            "Pages.OIAccountingBillingBasedTab.HBL.revenue({})".format(freight_index),
        )
        context._vp.add_dict(
            dict_name="hbl_freight_model",
            value={"{}_{}_{}".format(name, index, freight_index): hbl_freight_model},
        )
        freight_index += 1


@When("the user add freights to OI '{name}' HBL({index}) AR")
def step_impl(context, name, index):
    freight_index = 1
    sleep(0.5)
    for row in context.table:
        Pages.OIAccountingBillingBasedTab.HBL.revenue.new_button.click()
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
        hbl_freight_model = input_dynamic_datas(
            action_table,
            "Pages.OIAccountingBillingBasedTab.HBL.revenue({})".format(freight_index),
        )
        context._vp.add_dict(
            dict_name="hbl_freight_model",
            value={"{}_{}_{}".format(name, index, freight_index): hbl_freight_model},
        )
        freight_index += 1


@When("the user click OI Accounting 'Save' Button")
def step_impl(context):
    Pages.OIAccountingBillingBasedTab.save_button.click()
    Pages.Common.spin_bar.gone()
