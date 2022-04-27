from datetime import datetime

from behave.model import Table
from parse import parse

import config.globalparameter as gl
import src.pages as Pages
from src.exception.exception import GfqaException
from src.helper.transfer import transfer_data
from src.models import MAWBStockModel, PagingInfo


def trans_mawb_stock_table(mawb_stock_list_table: Table) -> list[MAWBStockModel]:
    result = []
    for mawb_stock_row in mawb_stock_list_table:
        mawb_stock = MAWBStockModel()
        for field, val in mawb_stock_row.items():
            trans_val = transfer_data(val)
            if field == "MAWB No.":
                mawb_stock.mawb_no = trans_val
            elif field == "Prefix":
                mawb_stock.prefix = trans_val
            elif field == "Carrier":
                mawb_stock.carrier = trans_val
            elif field == "Status":
                mawb_stock.status = trans_val
            elif field == "Reserved By":
                mawb_stock.reserved_by = trans_val
            elif field == "File No":
                mawb_stock.file_no = trans_val
            elif field == "Office":
                mawb_stock.office = trans_val
            elif field == "Created Date":
                mawb_stock.created_date = trans_val
            elif field == "Remark":
                mawb_stock.remark = trans_val
        result.append(mawb_stock)
    return result


def get_stock_list_len() -> PagingInfo:
    """
    parse list paging info text and return it
    """
    paging_text = Pages.MAWBStockListPage.paging_label.get_value()
    parser = parse("Showing {start} to {end} of {all} records", paging_text.strip())
    paging_info = PagingInfo(int(parser["start"]), int(parser["end"]), int(parser["all"]))
    return paging_info


def get_mawb_stock_index_in_stock_list(mawb_stock: MAWBStockModel, endure_range_sec: int = 300) -> int:
    """
    use filter and find the row index of target awb no.
    endure_range_sec: 可接受的時間差？(sec)
    """
    if Pages.MAWBStockListPage.Filter.is_invisible():
        Pages.MAWBStockListPage.filter_button.click()
    Pages.MAWBStockListPage.Filter.carrier_autocomplete.input(mawb_stock.carrier)
    Pages.MAWBStockListPage.Filter.prefix_input.input(mawb_stock.prefix)
    if mawb_stock.remark != None:
        Pages.MAWBStockListPage.Filter.keyword_input.input(mawb_stock.remark)
    if mawb_stock.status != None:
        Pages.MAWBStockListPage.Filter.status_select.select(mawb_stock.status.capitalize())
    Pages.MAWBStockListPage.Filter.apply_filters_button.click()

    paging_info = get_stock_list_len()
    cnt = paging_info.get_cnt()
    for i in range(1, cnt + 1):
        curr_mawb_no = Pages.MAWBStockListPage.StockList(i).mawb_no_label.get_value()
        curr_prefix = Pages.MAWBStockListPage.StockList(i).prefix_label.get_value()
        curr_carrier = Pages.MAWBStockListPage.StockList(i).carrier_label.get_value()

        if mawb_stock.status != None:
            curr_status = Pages.MAWBStockListPage.StockList(i).status_label.get_value()
            if curr_status != mawb_stock.status:
                continue
        if mawb_stock.reserved_by != None:
            curr_reserved_by = Pages.MAWBStockListPage.StockList(i).reserverd_by_label.get_value()
            if curr_reserved_by != mawb_stock.reserved_by:
                continue
        if mawb_stock.file_no != None:
            curr_file_no = Pages.MAWBStockListPage.StockList(i).remark_input.get_value()
            if curr_file_no != mawb_stock.file_no:
                continue
        if mawb_stock.office != None:
            curr_office = Pages.MAWBStockListPage.StockList(i).office_label.get_value()
            if curr_office != mawb_stock.office:
                continue
        if mawb_stock.created_date != None:
            curr_created_date = Pages.MAWBStockListPage.StockList(i).created_date_label.get_value()
            t1 = datetime.strptime(curr_created_date, gl.user_info.date_time_format)
            t2 = datetime.strptime(mawb_stock.created_date, gl.user_info.date_time_format)
            delta_sec = (t2 - t1).total_seconds()
            if delta_sec > endure_range_sec:
                continue
        if mawb_stock.remark != None:
            curr_remark = Pages.MAWBStockListPage.StockList(i).remark_input.get_value()
            if curr_remark != mawb_stock.remark:
                continue

        if (
            curr_mawb_no == mawb_stock.mawb_no
            and curr_prefix == mawb_stock.prefix
            and curr_carrier == mawb_stock.carrier
        ):
            return i

    raise GfqaException("Not found any MAWB Stock is matched.")
