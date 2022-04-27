from time import sleep

from behave.model import Row, Table

import src.pages as Pages
from src.elements import Element
from src.exception.exception import StepParaNotDefinedError
from src.models import VerifiedModel


def get_awb_no_range_mapping(index: int) -> dict[str, Element]:
    return {
        "Checked": Pages.AWBNoMngPage.AWBRanges(index).checked_checkbox,
        "Carrier": Pages.AWBNoMngPage.AWBRanges(index).carrier_autocomplete,
        "Prefix": Pages.AWBNoMngPage.AWBRanges(index).prefix_label,
        "Begin No.": Pages.AWBNoMngPage.AWBRanges(index).begin_no_input,
        "End No.": Pages.AWBNoMngPage.AWBRanges(index).end_no_input,
        "Latest Assigned No.": Pages.AWBNoMngPage.AWBRanges(index).latest_assigned_no_label,
        "Remark": Pages.AWBNoMngPage.AWBRanges(index).remark_input,
    }


def _input_awb_no_range(awb_no_range: dict, index: int) -> VerifiedModel:
    vm = VerifiedModel(f"Pages.AWBNoMngPage.AWBRanges({index})")
    checked = carrier = prefix = begin_no = end_no = remark = None

    if "Checked" in awb_no_range:
        checked = awb_no_range["Checked"]
        Pages.AWBNoMngPage.AWBRanges(index).checked_checkbox.tick(checked)
        vm.add("Checked", "checkbox", checked)
    if "Carrier" in awb_no_range:
        carrier = awb_no_range["Carrier"]
        Pages.AWBNoMngPage.AWBRanges(index).carrier_autocomplete.input(carrier)
        vm.add("Carrier", "autocomplete", carrier)
    if "Prefix" in awb_no_range:
        prefix = awb_no_range["Prefix"]
        if Pages.AWBNoMngPage.SetupAirCarrierPrefixModal.prefix_input.is_visible(2.5):
            Pages.AWBNoMngPage.SetupAirCarrierPrefixModal.prefix_input.input(prefix)
            Pages.AWBNoMngPage.SetupAirCarrierPrefixModal.save_button.click()
            Pages.Common.save_msg.is_visible()
        vm.add("Prefix", "label", prefix)
    if "Begin No." in awb_no_range:
        begin_no = awb_no_range["Begin No."]
        Pages.AWBNoMngPage.AWBRanges(index).begin_no_input.input(begin_no)
        vm.add("Begin No.", "input", begin_no)
    if "End No." in awb_no_range:
        end_no = awb_no_range["End No."]
        Pages.AWBNoMngPage.AWBRanges(index).end_no_input.input(end_no)
        vm.add("End No.", "input", end_no)
    if "Remark" in awb_no_range:
        remark = awb_no_range["Remark"]
        Pages.AWBNoMngPage.AWBRanges(index).remark_input.input(remark)
        vm.add("Remark", "input", remark)

    return vm


def add_awb_no_range(data_table: Table) -> list[VerifiedModel]:
    """
    add a new awb no. range, and return verified model.
    """
    vms = []
    freight_index = len(data_table.rows)

    # 一次 add 完需要的數量，verified model 的 xpath 才不會因為 add 下一筆導致 index 必須加 1
    for _ in range(freight_index):
        Pages.AWBNoMngPage.new_awb_no_range_button.click()

    for awb_no_range in data_table:
        vm = _input_awb_no_range(awb_no_range.as_dict(), freight_index)
        vms.append(vm)
        freight_index -= 1

    Pages.Common.save_button.click()
    sleep(2)

    return vms


def edit_awb_no_range(awb_no_range: Row, carrier: str) -> list[VerifiedModel]:
    """
    edit a existd awb no. range, and return verified model.
    """
    curr_awb_no_range = {"Carrier": carrier}
    idx = get_awb_no_range_index(curr_awb_no_range)
    vm = _input_awb_no_range(awb_no_range.as_dict(), idx)
    Pages.Common.save_button.click()
    sleep(2)

    return vm


def get_awb_no_range_index(awb_no_range: dict) -> int:
    """
    return the row index of target awb no range
    """
    num_awb_no_range = Pages.AWBNoMngPage.AWBRanges.get_len()

    for i in range(1, num_awb_no_range + 1):
        matched = True
        mapping = get_awb_no_range_mapping(i)
        for field, value in awb_no_range.items():
            if value != mapping[field].get_value():
                matched = False
                break

        if matched:
            return i
    return None


def verify_col_enable(carrier: str, enabled_list: Row):
    """
    verify columns are enabled/disabled
    """
    index = get_awb_no_range_index({"Carrier": carrier})
    mapping = get_awb_no_range_mapping(index)

    for col, is_enable_text in enabled_list.items():
        ele = mapping[col]
        if is_enable_text == "enabled":
            result = ele.is_enable()
        elif is_enable_text == "disabled":
            result = ele.is_disabled()
        else:
            raise StepParaNotDefinedError(is_enable_text)
        assert result, f"Expect {carrier}'s [{col}] is {is_enable_text}"
