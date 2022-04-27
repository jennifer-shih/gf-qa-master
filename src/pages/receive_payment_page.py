from selenium.webdriver.common.by import By

from src.elements import *


class ReceivePayment:
    received_from_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.pay.data.customer']"), (By.XPATH, "//*[@ng-model='vm.pay.data.customer']//input[@type='search']"))
    post_date_datepicker = Datepicker((By.XPATH, "//input[@ng-model='vm.pay.data.post_date']"))

    save_button = Button((By.XPATH, "//button[@ng-click='vm.save()']"))

    class InvoiceSearch:
        customer_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.invoiceSearch.filter.input.trade_partner']"), (By.XPATH, "//*[@ng-model='vm.invoiceSearch.filter.input.trade_partner']//input[@type='search']"))
        search_button = Button((By.XPATH, "//button[@ng-click='vm.progressiveSearch()']"))

    class InvoiceList:
        _rows = {}

        new_payment_by_g_l_button = Button((By.XPATH, "//button[@ng-click='vm.addSimpleInvoice()']"))
        show_more_invoices_button = Button((By.XPATH, "//a[@ng-click='vm.invoiceSearch.toggleFilter()']"))
        empty_info_element = Element((By.XPATH, "//td[contains(@class, 'col-empty')]"))

        def __new__(cls, index=1):
            index = int(index)
            if index not in cls._rows:
                cls._rows[index] = super().__new__(cls)
            return cls._rows[index]

        def __init__(self, index=1):
            index = int(index)
            def ROW_XPATH(xpath):
                return "//hcgridcontainer//div[contains(@class, 'ag-center-cols-container')]/div[{0}]{1}".format(index, xpath)

            self.g_l_autocompelete = Autocomplete((By.XPATH, ROW_XPATH("/div[@col-id='glCode']//hcglselect")), (By.XPATH, "//ng-dropdown-panel//input"))
            self.select_checkbox = Checkbox((By.XPATH, ROW_XPATH("/div[contains(@col-id, '__checked')]//input")), click_locator=(By.XPATH, ROW_XPATH("/div[contains(@col-id, '__checked')]//span")))

    class PopupMessage:
        message_element = Element((By.XPATH, "//div[@uib-modal-transclude]//*[@ng-bind-html='msg']"))
        cancel_button = Button((By.XPATH, "//div[@uib-modal-transclude]//button[@ng-click='cancel()'][@ng-bind='config.cancelBtnWording']"))
        proceed_button = Button((By.XPATH, "//div[@uib-modal-transclude]//button[@ng-click='ok()']"))
