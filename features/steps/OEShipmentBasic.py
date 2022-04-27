import json
from time import sleep

from behave import Given, Then, When

import src.pages as Pages
from config import globalparameter as gl
from src.drivers.driver import Driver
from src.helper.filters import ExceptedFilter
from src.helper.function import randN, wday
from src.helper.script import input_dynamic_datas
from src.helper.transfer import transfer_to_feature_table


@Given("the user has a OE Shipment with one HBL({hbl_no})")
def step_impl(context, hbl_no):
    Driver.open(gl.URL.OE_NEW_SHIPMENT)
    Pages.Common.spin_bar.gone()
    Pages.OEBasicTab.MBL.mb_l_no_input.input(hbl_no)
    Pages.OEBasicTab.MBL.etd_datepicker.input(wday(1))
    Pages.OEBasicTab.add_hb_l_button.click()
    Pages.Common.spin_bar.gone()
    Pages.Common.save_button.click()
    Pages.Common.save_msg.is_visible(timeout=10)


@When("the user tick OE 'Direct Master' checkbox")
def step_impl(context):
    Pages.OEBasicTab.MBL.direct_master_checkbox.tick(True)
    Pages.Common.spin_bar.gone()


@When("the user click OE MBL 'More' button")
def step_impl(context):
    # 如果沒展開再click more button
    if not Pages.OEBasicTab.MBL.e_commerce_checkbox.is_interactable():
        Pages.OEBasicTab.MBL.more_button.click()


@Then("the shipment '{name}' of 'Ocean Export' will be created")
def step_impl(context, name):
    model = context._vp.get("mbl_model")[name]

    # go to the shipment which just created
    Driver.open(context._vp.get("url"))
    Pages.Common.spin_bar.gone()
    Pages.OEBasicTab.MBL.more_button.click()

    # url should be https://fms-stage-qa-5.gofreight.co/truck/shipment/{File_No}/
    file_no = Driver.get_url().split("/")[-2]
    model.add(field="file_no", attribute="input", data=file_no)

    # direct master
    # 如果有填 Customer, 且 Bill To都沒有另外輸入value，這些欄位會與Customer相同
    if (
        Pages.OEBasicTab.MBL.direct_master_checkbox.get_value() == True
        and model.has_key("Customer")
        and not model.has_key("Bill To")
    ):
        customer = model.get_data("Customer")
        model.add(field="Bill To", attribute="autocomplete", data=customer)

    model.verify()


@Given("the user already has a OE shipment")
def step_impl(context):
    with gl.oe_info_file.open(mode="r") as data_file:
        info = json.load(data_file)
    Driver.open(info["shipment_url"])
    Pages.Common.spin_bar.gone()


@Given("the user has a OE Shipment")
def step_impl(context):
    Driver.open(gl.URL.OE_NEW_SHIPMENT)
    Pages.OEBasicTab.MBL.mb_l_no_input.input("HACO-" + str(randN(6)))
    Pages.OEBasicTab.MBL.etd_datepicker.input(wday(3))
    Pages.Common.save_button.click()
    Pages.Common.spin_bar.gone()


@Given("the user has a OE MBL with {count} HBL as '{name}'")
def step_impl(context, count, name):
    create_oe_mbl_table = transfer_to_feature_table(
        """
        | field                  | attribute    | action        | data                            |
        | MB/L No.               | input        | input         | HACO-{randN(6)}                 |
        | ETD                    | datepicker   | input         | {today+5}                       |
    """
    )

    # The 'Buying Freight' and 'Selling Freight' fields are connected in enterprise
    if gl.company == "OLC":
        create_oe_hbl_table = transfer_to_feature_table(
            """
            | field                   | attribute    | action               | data                 |
            | Customer Ref. No.       | input        | input                | CUS{randN(6)}        |
            | Actual Shipper          | autocomplete | input and close memo | {randomTradePartner} |
            | Consignee               | autocomplete | input and close memo | {randomTradePartner} |
            | Notify                  | autocomplete | input                | {randomTradePartner} |
            | Customs Broker          | autocomplete | input                | {randomTradePartner} |
            | Trucker                 | autocomplete | input                | {randomTradePartner} |
            | HB/L Agent              | autocomplete | input                | {randomTradePartner} |
            | Forwarding Agent        | autocomplete | input                | {randomTradePartner} |
            | Sub Agent B/L           | checkbox     | tick                 | {on}                 |
            | Receiving Agent         | autocomplete | input                | {randomTradePartner} |
            | Place of Receipt        | autocomplete | input                | {randomPort}         |
            | Place of Receipt ETD    | datepicker   | input                | {today+3}            |
            | Port of Discharge       | autocomplete | input                | {randomPort}         |
            | ETA                     | datepicker   | input                | {today+4}            |
            | Place of Delivery (DEL) | autocomplete | input                | {randomPort}         |
            | Place of Delivery ETA   | datepicker   | input                | {today+5}            |
            | Final Destination       | autocomplete | input                | {randomPort}         |
            | Final ETA               | datepicker   | input                | {today+6}            |
            | FBA FC                  | autocomplete | input                | {randomTradePartner} |
            | Empty Pickup            | autocomplete | input                | {randomTradePartner} |
            | Delivery To/Pier        | autocomplete | input                | {randomTradePartner} |
            | Cargo Ready Date        | datepicker   | input                | {today+10}           |
            | Cargo Pickup            | autocomplete | input                | {randomTradePartner} |
            | Ship Mode               | select       | random select        |                      |
            | Buying Freight          | select       | random select        |                      |
            | Service Term From       | select       | random select        |                      |
            | Service Term To         | select       | random select        |                      |
            | Express B/L             | radio group  | click                | No                   |
            | Cargo Type              | select       | random select        |                      |
            | Sales Type              | select       | random select        |                      |
            | W/H Cut-Off Date        | datepicker   | input                | {today+10} 00:00     |
            | Early Return Date       | datepicker   | input                | {today+12} 00:00     |
            | L/C No.                 | input        | input                | LC{randN(6)}         |
            | L/C Issue Bank          | input        | input                | LCBANK{randN(6)}     |
            | L/C Issue Date          | datepicker   | input                | {today+11}           |
            | Onboard                 | datepicker   | input                | {today+2}            |
            | Stackable               | radio group  | click                | Yes                  |
            | Business Referred By    | autocomplete | input                | {randomTradePartner} |
            | W/O No.                 | input        | input                | WO{randN(6)}         |
            | Ship Type               | select       | random select        |                      |
            | Incoterms               | select       | random select        |                      |
            | NAR No.                 | input        | input                | NAR{randN(6)}        |
            | E-Commerce              | checkbox     | tick                 | {on}                 |
        """
        )
    else:
        create_oe_hbl_table = transfer_to_feature_table(
            """
            | field                   | attribute    | action               | data                 |
            | Customer Ref. No.       | input        | input                | CUS{randN(6)}        |
            | Actual Shipper          | autocomplete | input and close memo | {randomTradePartner} |
            | Consignee               | autocomplete | input and close memo | {randomTradePartner} |
            | Notify                  | autocomplete | input                | {randomTradePartner} |
            | Customs Broker          | autocomplete | input                | {randomTradePartner} |
            | Trucker                 | autocomplete | input                | {randomTradePartner} |
            | HB/L Agent              | autocomplete | input                | {randomTradePartner} |
            | Forwarding Agent        | autocomplete | input                | {randomTradePartner} |
            | Sub Agent B/L           | checkbox     | tick                 | {on}                 |
            | Receiving Agent         | autocomplete | input                | {randomTradePartner} |
            | Place of Receipt        | autocomplete | input                | {randomPort}         |
            | Place of Receipt ETD    | datepicker   | input                | {today+3}            |
            | Port of Discharge       | autocomplete | input                | {randomPort}         |
            | ETA                     | datepicker   | input                | {today+4}            |
            | Place of Delivery (DEL) | autocomplete | input                | {randomPort}         |
            | Place of Delivery ETA   | datepicker   | input                | {today+5}            |
            | Final Destination       | autocomplete | input                | {randomPort}         |
            | Final ETA               | datepicker   | input                | {today+6}            |
            | FBA FC                  | autocomplete | input                | {randomTradePartner} |
            | Empty Pickup            | autocomplete | input                | {randomTradePartner} |
            | Delivery To/Pier        | autocomplete | input                | {randomTradePartner} |
            | Cargo Ready Date        | datepicker   | input                | {today+10}           |
            | Cargo Pickup            | autocomplete | input                | {randomTradePartner} |
            | Ship Mode               | select       | random select        |                      |
            | Buying Freight          | select       | random select        |                      |
            | Selling Freight         | select       | random select        |                      |
            | Service Term From       | select       | random select        |                      |
            | Service Term To         | select       | random select        |                      |
            | Express B/L             | radio group  | click                | No                   |
            | Cargo Type              | select       | random select        |                      |
            | Sales Type              | select       | random select        |                      |
            | W/H Cut-Off Date        | datepicker   | input                | {today+10} 00:00     |
            | Early Return Date       | datepicker   | input                | {today+12} 00:00     |
            | L/C No.                 | input        | input                | LC{randN(6)}         |
            | L/C Issue Bank          | input        | input                | LCBANK{randN(6)}     |
            | L/C Issue Date          | datepicker   | input                | {today+11}           |
            | Onboard                 | datepicker   | input                | {today+2}            |
            | Stackable               | radio group  | click                | Yes                  |
            | Business Referred By    | autocomplete | input                | {randomTradePartner} |
            | W/O No.                 | input        | input                | WO{randN(6)}         |
            | Ship Type               | select       | random select        |                      |
            | Incoterms               | select       | random select        |                      |
            | NAR No.                 | input        | input                | NAR{randN(6)}        |
            | E-Commerce              | checkbox     | tick                 | {on}                 |
        """
        )

    # create a new MBL
    Driver.open(gl.URL.OE_NEW_SHIPMENT)
    Pages.OEBasicTab.MBL.more_button.click()
    mbl_model = input_dynamic_datas(create_oe_mbl_table, "Pages.OEBasicTab.MBL", ExceptedFilter.oe_mbl_filter)
    Pages.Common.save_button.click()
    assert Pages.Common.save_msg.is_visible(timeout=30) is True

    # add additional field
    mbl_model.add(
        field="File No.",
        attribute="input",
        data=Pages.OEBasicTab.MBL.file_no_input.get_value(),
    )
    mbl_model.add(
        field="Office",
        attribute="autocomplete",
        data=Pages.OEBasicTab.MBL.office_autocomplete.get_value(),
    )

    context._vp.add_dict(dict_name="mbl_model", value={name: mbl_model})

    # create new HBLs
    for i in range(1, int(count) + 1):
        Pages.OEBasicTab.add_hb_l_button.click()
        sleep(4)
        Pages.OEBasicTab.HBL(i).hb_l_no_autogen_checkbox.tick(True)
        Pages.OEBasicTab.HBL(i).more_button.click()
        hbl_model = input_dynamic_datas(
            create_oe_hbl_table,
            "Pages.OEBasicTab.HBL({})".format(i),
            ExceptedFilter.oe_hbl_filter,
        )

        Pages.Common.save_button.click()
        Pages.Common.spin_bar.gone()
        assert Pages.Common.save_msg.is_visible(timeout=10) is True

        hbl_model.add(
            field="Customer",
            attribute="autocomplete",
            data=Pages.OEBasicTab.HBL(i).customer_autocomplete.get_value(),
        )
        hbl_model.add(
            field="Bill To",
            attribute="autocomplete",
            data=Pages.OEBasicTab.HBL(i).bill_to_autocomplete.get_value(),
        )
        hbl_model.add(
            field="Sales",
            attribute="autocomplete",
            data=Pages.OEBasicTab.HBL(i).sales_autocomplete.get_value(),
        )
        if gl.company == "OLC":
            buying_freighit_data = hbl_model.get_data("Buying Freight")
            hbl_model.add(field="Selling Freight", attribute="select", data=buying_freighit_data)

        context._vp.add_dict(dict_name="hbl_model", value={"{}_{}".format(name, i): hbl_model})

    context._vp.add_dict(dict_name="shipment_url", value={name: Driver.get_url()})


@Given("the user has a OE MBL with {count} HBL as '{name}' with only required fields filled")
def step_impl(context, count, name):
    create_oe_mbl_table = transfer_to_feature_table(
        """
        | field                | attribute    | action        | data                         |
        | MB/L No.             | input        | input         | HACO-{randN(6)}              |
        | ETD                  | datepicker   | input         | {today+5}                    |
    """
    )

    create_oe_hbl_table = transfer_to_feature_table(
        """
        | field         | attribute     | action       | data             |
        | Sales         | autocomplete  | input        | {randomSales}    |
    """
    )

    # create a new MBL
    Driver.open(gl.URL.OE_NEW_SHIPMENT)
    Pages.OEBasicTab.MBL.more_button.click()
    mbl_model = input_dynamic_datas(create_oe_mbl_table, "Pages.OEBasicTab.MBL", ExceptedFilter.oe_mbl_filter)
    Pages.Common.save_button.click()
    assert Pages.Common.save_msg.is_visible(timeout=30) is True

    # add additional field
    mbl_model.add(
        field="File No.",
        attribute="input",
        data=Pages.OEBasicTab.MBL.file_no_input.get_value(),
    )
    mbl_model.add(
        field="Office",
        attribute="autocomplete",
        data=Pages.OEBasicTab.MBL.office_autocomplete.get_value(),
    )

    context._vp.add_dict(dict_name="mbl_model", value={name: mbl_model})

    # create new HBLs
    for i in range(1, int(count) + 1):
        Pages.OEBasicTab.add_hb_l_button.click()
        sleep(2)
        Pages.OEBasicTab.HBL(i).more_button.click()
        hbl_model = input_dynamic_datas(
            create_oe_hbl_table,
            "Pages.OEBasicTab.HBL({})".format(i),
            ExceptedFilter.oe_hbl_filter,
        )

        Pages.Common.save_button.click()
        Pages.Common.spin_bar.gone()
        assert Pages.Common.save_msg.is_visible(timeout=10) is True

        hbl_model.add(
            field="Customer",
            attribute="autocomplete",
            data=Pages.OEBasicTab.HBL(i).customer_autocomplete.get_value(),
        )
        hbl_model.add(
            field="Bill To",
            attribute="autocomplete",
            data=Pages.OEBasicTab.HBL(i).bill_to_autocomplete.get_value(),
        )
        hbl_model.add(
            field="Sales",
            attribute="autocomplete",
            data=Pages.OEBasicTab.HBL(i).sales_autocomplete.get_value(),
        )

        context._vp.add_dict(dict_name="hbl_model", value={"{}_{}".format(name, i): hbl_model})

    context._vp.add_dict(dict_name="shipment_url", value={name: Driver.get_url()})


@When("the user click OE 'Add HBL' button")
def step_impl(context):
    Pages.OEBasicTab.add_hb_l_button.click()
    sleep(5)


@When("the user click OE HBL({index}) 'More' button")
def step_impl(context, index):
    # 如果沒展開再click more button
    if Pages.OEBasicTab.HBL(index).ship_type_select.is_disable():  # TODO GQT-423 如果眼睛看到的話（不論看不看得到，都會在 dom 上）
        Pages.OEBasicTab.HBL(index).more_button.click()


@Then("the shipment '{name}' HBL({index}) of 'Ocean Export' will be created")
def step_impl(context, name, index):
    model = context._vp.get("hbl_model")["{}_{}".format(name, index)]

    # go to the shipment which just created
    Driver.open(context._vp.get("url"))
    Pages.Common.spin_bar.gone()
    Pages.OEBasicTab.HBL(index).hbl_side_panel.click()
    Pages.OEBasicTab.HBL(index).more_button.click()

    model.verify()


@When("the user click OE '{name}' HBL({index}) 'Tools -> Copy To'")
def step_impl(context, name, index):
    Driver.open(context._vp.get("shipment_url")[name])
    Pages.Common.spin_bar.gone()
    Pages.OEBasicTab.HBL(index).hbl_side_panel.click()
    sleep(2)
    Pages.OEBasicTab.HBL(index).tools_button.click()
    Pages.OEBasicTab.HBL(index).tools_copy_to_button.click()


@When("the user input '{name}' to OE copy HBL to")
def step_impl(context, name):
    mbl_no = context._vp.get("mbl_model")[name].get_data("MB/L No.")
    Pages.OEBasicTab.CopyHBLToMBL.select_mbl_autocomplete.input(mbl_no)


@When("the user click 'OK' button in OE 'Copy To' dialog")
def step_impl(context):
    Pages.OEBasicTab.CopyHBLToMBL.ok_button.click()


@Then("the link of '{name}' should show in OE 'Copy To' dialog")
def step_impl(context, name):
    exp = context._vp.get("mbl_model")[name].get_data("File No.")
    v = Pages.OEBasicTab.CopyHBLToMBL.mbl_link.get_value()
    assert exp == v, "Link shoud be [{0}], not [{1}]".format(exp, v)


@When("the user click the OE copied link")
def step_impl(context):
    Pages.OEBasicTab.CopyHBLToMBL.mbl_link.click()
    Driver.switch_to(window_index=1)
    Pages.Common.spin_bar.gone()


@Then("the HBL({index_1}) should copy from OE '{name}' HBL({index_2})")
def step_impl(context, index_1, name, index_2):
    Pages.OEBasicTab.HBL(index_1).hbl_side_panel.click()
    Pages.OEBasicTab.HBL(index_1).more_button.click()
    model = context._vp.get("hbl_model")["{}_{}".format(name, index_2)]
    model.set_page_class_name("Pages.OEBasicTab.HBL({})".format(index_1))

    # If the field in listed in the data table, the value should be same,
    # If not, then the value should be empty
    vm_fields = model.get_all_fields()
    copied_fields = [i["field"] for i in context.table]
    for f in vm_fields:
        if f not in copied_fields:
            f_dict = model.pop(f)
            model.add(field=f, attribute=f_dict[model.ATTRIBUTE], data="")

    # TODO check whether op is the current character
    model.verify()


@Then("the OE HBL({index}) should have 'COPY-1' as HBL NO.")
def step_impl(context, index):
    exp = "COPY-1"
    hbl_no = Pages.OEBasicTab.HBL(index).hb_l_no_input.get_value()
    assert hbl_no == exp, "HB/L No. should be [{0}], not [{1}]".format(exp, hbl_no)


@When("the user switch to HBL({index}) in OE")
def step_impl(context, index):
    index_int = int(index)
    Pages.OESidePanel.hbl_select_button(index_int).click()
    Pages.Common.spin_bar.gone()
    sleep(3)


@When("the user expand OE MBL block")
def step_impl(context):
    if Pages.OEBasicTab.MBL.mbl_body_element.is_invisible():
        Pages.OEBasicTab.MBL.expand_button.click()
