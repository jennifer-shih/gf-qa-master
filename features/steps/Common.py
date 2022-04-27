import re
from time import sleep

from behave import Given, Then, When

import src.pages as Pages
from config import globalparameter as gl
from src.drivers.driver import Driver
from src.helper.filters import ExceptedFilter
from src.helper.script import input_dynamic_datas


@When("the user click save button")
def step_impl(context):
    Pages.Common.save_button.click()
    Pages.Common.spin_bar.gone()
    sleep(2)


@Then("'Save' button is diasbled")
def step_impl(context):
    assert Pages.Common.save_button.is_disabled() is True


@Then("the data is saved successfully")
def step_impl(context):
    assert Pages.Common.save_msg.is_visible(timeout=10) is True


@Then("save data successfully message will show")
def step_impl(context):
    assert Pages.Common.save_msg.is_visible(timeout=10) is True


@Then("save data fail message should show")
def step_impl(context):
    exp_fail_msg = context.text.replace(
        "\r", ""
    )  # Walkaround: in Windows OS, the newline escape character in doc string  will be regarded as '\r\n'
    fail_msg = Pages.Common.save_fail_msg.get_value(timeout=10)
    assert exp_fail_msg == fail_msg, f"Expect to fail by cause [{exp_fail_msg}], but get [{fail_msg}]"


@When("the user enter '{shipment_type}' shipment datas as '{name}' and save it")
def step_impl(context, shipment_type, name):
    """
    shipment_type: model.ShipmentType
    """
    dict_name = "model"
    if re.match(r"OI HBL\((\d+)\)", shipment_type) != None:
        index = re.match(r"OI HBL\((\d+)\)", shipment_type).group(1)
        current_page_class_name = "Pages.OIBasicTab.HBL({index})".format(index=index)
        excepted_filter = None
        dict_name = "hbl_model"
        name = "{}_{}".format(name, index)
    elif re.match(r"OE HBL\((\d+)\)", shipment_type) != None:
        index = re.match(r"OE HBL\((\d+)\)", shipment_type).group(1)
        current_page_class_name = "Pages.OEBasicTab.HBL({index})".format(index=index)
        excepted_filter = None
        dict_name = "hbl_model"
        name = "{}_{}".format(name, index)
    elif re.match(r"OEVS BK\((\d+)\)", shipment_type) != None:
        index = re.match(r"OEVS BK\((\d+)\)", shipment_type).group(1)
        current_page_class_name = "Pages.OEVSBasicTab.BK({index})".format(index=index)
        excepted_filter = None
        dict_name = "bk_model"
        name = "{}_{}".format(name, index)
    elif re.match(r"AI HAWB\((\d+)\)", shipment_type) != None:
        index = re.match(r"AI HAWB\((\d+)\)", shipment_type).group(1)
        current_page_class_name = "Pages.AIBasicTab.HAWB({index})".format(index=index)
        excepted_filter = None
        dict_name = "hawb_model"
        name = "{}_{}".format(name, index)
    elif re.match(r"AE HAWB\((\d+)\)", shipment_type) != None:
        index = re.match(r"AE HAWB\((\d+)\)", shipment_type).group(1)
        current_page_class_name = "Pages.AEBasicTab.HAWB({index})".format(index=index)
        excepted_filter = None
        dict_name = "hawb_model"
        name = "{}_{}".format(name, index)
    elif shipment_type == "OI MBL":
        current_page_class_name = "Pages.OIBasicTab.MBL"
        excepted_filter = ExceptedFilter.oi_mbl_filter
        dict_name = "mbl_model"
    elif shipment_type == "OE MBL":
        current_page_class_name = "Pages.OEBasicTab.MBL"
        excepted_filter = ExceptedFilter.oe_mbl_filter
        dict_name = "mbl_model"
    elif shipment_type == "OEVS VS":
        current_page_class_name = "Pages.OEVSBasicTab.VS"
        excepted_filter = None
        dict_name = "vs_model"
    elif shipment_type == "OEBK":
        current_page_class_name = "Pages.OEBookingBasicTab"
        excepted_filter = None
        dict_name = "bk_model"
    elif shipment_type == "AI MAWB":
        current_page_class_name = "Pages.AIBasicTab.MAWB"
        excepted_filter = None
        dict_name = "mawb_model"
    elif shipment_type == "AE MAWB":
        current_page_class_name = "Pages.AEBasicTab.MAWB"
        excepted_filter = None
        dict_name = "mawb_model"
    elif shipment_type == "TK MBL":
        current_page_class_name = "Pages.TKBasicTab.MBL"
        excepted_filter = ExceptedFilter.tk_mbl_filter
        dict_name = "mbl_model"
    elif shipment_type == "MS MBL":
        current_page_class_name = "Pages.MiscBasicTab.MBL"
        excepted_filter = ExceptedFilter.ms_mbl_filter
        dict_name = "mbl_model"
    elif shipment_type == "OE Vessel Schedule":
        current_page_class_name = "Pages.OENewVesselScheduleBasicTab.VesselSchedule"
        excepted_filter = None
        dict_name = "vs_model"
    elif shipment_type == "WH Shipping":
        current_page_class_name = "Pages.WHShippingBasicTab"
        excepted_filter = None
        dict_name = "mbl_model"
    elif shipment_type == "WH Receiving":
        current_page_class_name = "Pages.WHReceivingBasicTab"
        excepted_filter = None
        dict_name = "mbl_model"
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    model = input_dynamic_datas(context.table, current_page_class_name, excepted_filter)
    context._vp.add_dict(dict_name=dict_name, value={name: model})
    Pages.Common.save_button.click()
    assert Pages.Common.save_msg.is_visible(timeout=30) is True

    context._vp.add_v(v_name="url", value=Driver.get_url())


@Given("the download file folder is '{folder}'")
def step_impl(context, folder):
    if folder == "tk":
        context._vp.add_v(v_name="download_file_folder", value=gl.download_path_tk)
    elif folder == "download":
        context._vp.add_v(v_name="download_file_folder", value=gl.download_path)


@When("the user click 'Download PDF' button")
def step_impl(context):
    Driver.set_download_path(context._vp.get("download_file_folder"))
    Pages.DocPreviewToolBar.pdf_button.click()
    Pages.Common.spin_bar.gone(300)


@When("the user click 'Download Excel' button")
def step_impl(context):
    Driver.set_download_path(context._vp.get("download_file_folder"))
    Pages.DocPreviewToolBar.excel_button.hover()
    Pages.DocPreviewToolBar.excel_button.click()
    Pages.Common.spin_bar.gone(300)


@Then("there is no '{text}' text in the web page")
def step_impl(context, text):
    assert Driver.is_text_in_page_source(text) == False, f"There is text '{ text }' in the current web page"


@Then("'{v1}' should NOT be '{v2}'")
def step_impl(context, v1, v2):
    var_1 = context._vp.get(v1)
    var_2 = context._vp.get(v2)
    assert var_1 != var_2, f"[{var_1}] != [{var_2}]"


@When("the user clicks ok button")
def step_impl(context):
    Pages.Common.ok_button.click()
