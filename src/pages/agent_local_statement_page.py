from selenium.webdriver.common.by import By

from src.elements import *


class AgentLocalStatementPage:
    partner_type_radio_group = RadioGroup({"Agent/Customer": (By.XPATH, "//input[@name='radio_partner_customer']"),
                                           "Account Group": (By.XPATH, "//input[@name='radio_partner_account_group']")})
    partner_autocomplete = Autocomplete((By.XPATH, "//div[@name='account_group_name']"),
                                        (By.XPATH, "//div[@name='account_group_name']//input[@type='search']"))
    period_period_datepicker = PeriodDatepicker((By.XPATH, "//input[@model-date-start='vm.period_start'][@model-date-end='vm.period_end']"),
                                               (By.XPATH, "//input[@name='daterangepicker_start']"),
                                               (By.XPATH, "//input[@name='daterangepicker_end']"))
    filter_by_radio_group = RadioGroup({"All": (By.XPATH, "//input[@name='pay_status_all']"),
                                        "Open": (By.XPATH, "//input[@name='pay_status_open']"),
                                        "Paid": (By.XPATH, "//input[@name='pay_status_paid']")})
    search_button = Button((By.XPATH, "//button[@ng-click='vm.onClickSearch()']"))

    class invoice_table:
        check_all_checkbox = Checkbox(
            (By.XPATH, "//div[@role='columnheader']/div[@role='button']//label[@is-checked='grid.appScope.agentList.allChecked()']/input[@type='checkbox']"),
            click_locator=(By.XPATH, "//div[@role='columnheader']/div[@role='button']//label[@is-checked='grid.appScope.agentList.allChecked()']"))

        @staticmethod
        def get_len():
            #? This table is dynamic loading, the loading items number is between 14 to 18. So use get_len() is not a correctly method for counting all item in the table (if items > 14)
            sleep(1)
            return Driver.num_of_element("//div[@role='grid']//div[@class='ui-grid-canvas']//div[@ng-repeat='(rowRenderIndex, row) in rowContainer.renderedRows track by $index']")

    attach_original_invoices_checkbox = Checkbox((By.XPATH, "//input[@name='attachInvoices']"))
    view_button = Button((By.XPATH, "//button[@ng-click='vm.view()']"))
    downlaod_pdf_button = Button((By.XPATH, "//button[@ng-click='vm.downloadPDF()']"))
    downlaod_excel_button = Button((By.XPATH, "//button[@ng-click='vm.downloadExcel()']"))

    class generated_document_list:
        _instances = {}

        def __new__(cls, index=1):
            index = int(index)
            if index not in cls._instances:
                cls._instances[index] = super().__new__(cls)
            return cls._instances[index]

        def __init__(self, index=1):
            index = int(index)
            def ROW_XPATH(xpath):
                return "//hc-filter[@list='vm.logs']/following-sibling::div//tbody/tr[{0}]{1}".format(index, xpath)

            self.action_button = Button((By.XPATH, ROW_XPATH("//a[@ng-bind='::_T.ACTION.TITLE']")))
            self.reload_button = Input((By.XPATH, ROW_XPATH("//a[@ng-click='vm.onClickReloadReport(log)']")))

    #? 抓不到元素(page source 只有 call api 的 function)，應該跟網頁讀取資料的方式有關，待解...
    # class print:
    #     table_title_label = Label((By.XPATH, "//table/thead/tr"))
    #     @staticmethod
    #     def get_len():
    #         sleep(1)
    #         return Driver.num_of_element("//table/tbody/tr[@class='border-t-grey']")
