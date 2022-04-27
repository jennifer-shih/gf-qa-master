from selenium.webdriver.common.by import By

from src.elements import *
from src.pages.base_components.list_filter_base_component import BaseListFilter


class MAWBStockListPage:
    title_label = Label((By.XPATH, "//div[@class='portlet-title']/div[contains(@class,'caption')]/span"))
    reserve_button = Button((By.XPATH, "//button[contains(text(),'Reserve')]"))
    unreserve_button = Button((By.XPATH, "//button[contains(text(),'Unreserve')]"))
    create_mawb_button = Button((By.XPATH, "//button[contains(text(),'Create MAWB')]"))
    paging_label = Label((By.XPATH, "//div[@class='data-num']"))
    filter_button = Button((By.XPATH, "//hcfilteractionbutton//a"))
    class StockList:
        _rows = {}
        def __new__(cls, index=1):
                index = int(index) - 1
                if index not in cls._rows:
                    cls._rows[index] = super().__new__(cls)
                return cls._rows[index]

        def __init__(self, index=1):
            index = int(index) - 1
            def ROW_XPATH(xpath):
                return f"//div[contains(@class, 'ag-center-cols-container')]//div[@row-id='{index}']{xpath}"

            self.check_checkbox = Checkbox((By.XPATH, ROW_XPATH("//div[@col-id=(//div[contains(@class, 'ag-header-cell') and descendant::span[@class='customchk']]/@col-id)]//input")), (By.XPATH, ROW_XPATH("//div[@col-id=(//div[contains(@class, 'ag-header-cell') and descendant::span[@class='customchk']]/@col-id)]//span")))
            self.status_label = Label((By.XPATH, ROW_XPATH("//div[@col-id=(//div[contains(@class, 'ag-header-cell') and descendant::span[text()='Status']]/@col-id)]")))
            self.prefix_label = Label((By.XPATH, ROW_XPATH("//div[@col-id=(//div[contains(@class, 'ag-header-cell') and descendant::span[text()='Prefix']]/@col-id)]")))
            self.carrier_label = Label((By.XPATH, ROW_XPATH("//div[@col-id=(//div[contains(@class, 'ag-header-cell') and descendant::span[text()='Carrier']]/@col-id)]")))
            self.mawb_no_label = Label((By.XPATH, ROW_XPATH("//div[@col-id=(//div[contains(@class, 'ag-header-cell') and descendant::span[text()='MAWB No.']]/@col-id)]")))
            self.reserverd_by_label = Label((By.XPATH, ROW_XPATH("//div[@col-id=(//div[contains(@class, 'ag-header-cell') and descendant::span[text()='Reserved By']]/@col-id)]")))
            self.file_no_link = Link((By.XPATH, ROW_XPATH("//div[@col-id=(//div[contains(@class, 'ag-header-cell') and descendant::span[text()='File No.']]/@col-id)]/descendant::*[last()]")))
            self.office_label = Label((By.XPATH, ROW_XPATH("//div[@col-id=(//div[contains(@class, 'ag-header-cell') and descendant::span[text()='Office']]/@col-id)]")))
            self.created_date_label = Label((By.XPATH, ROW_XPATH("//div[@col-id=(//div[contains(@class, 'ag-header-cell') and descendant::span[text()='Created Date']]/@col-id)]")))
            self.remark_input = Input((By.XPATH, ROW_XPATH("//div[@col-id=(//div[contains(@class, 'ag-header-cell') and descendant::span[text()='Remark']]/@col-id)]//input")))

    class Filter(BaseListFilter):
        reserved_by_autocomplete = Autocomplete((By.XPATH, "//hcuserselect//ng-select"), (By.XPATH, "//ng-dropdown-panel//input"))
        status_select = Select((By.XPATH, "//hcfilteroption[@formcontrolname='status']//select"))
        prefix_input = Input((By.XPATH, "//hcfiltertext[@formcontrolname='prefix']//input"))
        carrier_autocomplete = Autocomplete((By.XPATH, "//hctpselect//ng-select"), (By.XPATH, "//ng-dropdown-panel//input"))

        def is_invisible(timeout=5):
            return Element((By.XPATH, "//mawb-no-stock-list-filter//form")).is_invisible(timeout)
