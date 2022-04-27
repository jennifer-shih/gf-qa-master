from behave import Then, When

import src.pages as Pages
from config import globalparameter as gl
from src.exception.exception import StepParaNotDefinedError
from src.helper.timer import DownloadTimer


@When("the user click 'Doc Center' tab of Truck")
def step_impl(context):
    Pages.TKTab.doc_center_tab.click()
    Pages.Common.spin_bar.gone()


@When("the user click 'Tools' -> 'Pickup / Delivery Order'")
def step_impl(context):
    Pages.TKDocTab.MBL.tools_button.click()
    Pages.TKDocTab.MBL.pickup_delivery_order_button.click()
    Pages.Common.spin_bar.gone(30)


@Then("TK {doc} file should be saved in download folder ({timeout} sec)")
def step_impl(context, doc, timeout):
    if doc == "PICKUP & DELIVERY ORDER":
        model_dict = context._vp.get("mbl_model")
        model = list(model_dict.values())[0]
        file_no = model.get_data("File No.")
        file_name = f"PICKUP & DELIVERY ORDER - { file_no }.pdf"
    elif doc == "Pickup Delivery Order":
        file_name = "Pickup Delivery Order.pdf"
    else:
        raise StepParaNotDefinedError(doc)

    dt = DownloadTimer(str(gl.download_path_tk / file_name), int(timeout))
    dt.start()


@Then("{doc} should shows up on 'Document List'")
def step_impl(context, doc):
    if doc == "PICKUP & DELIVERY ORDER":
        model_dict = context._vp.get("mbl_model")
        model = list(model_dict.values())[0]
        file_no = model.get_data("File No.")
        file_name = f"PICKUP & DELIVERY ORDER - {file_no}.pdf"
        names = []
        for i in range(1, Pages.TKDocTab.MBL.document_list.get_len() + 1):
            names.append(Pages.TKDocTab.MBL.document_list(i).name_edit_input.get_value())
    elif doc == "Pickup Delivery Order":
        names = []
        file_name = "Pickup Delivery Order.pdf"
        for i in range(1, Pages.TKDocTab.MBL.document_list.get_len() + 1):
            names.append(Pages.TKDocTab.MBL.document_list(i).name_edit_input.get_value())
    else:
        raise StepParaNotDefinedError(doc)

    assert file_name in names, "Not found the file '{}' in Document List".format(file_name)
