from selenium.webdriver.common.by import By

from src.elements import *


class FrontDeskPortal:
    search_button = Button((By.XPATH, "//button[@data-hc-name='front-desk-list-search']"))

    keyword_input = Input((By.XPATH, "//input[@data-hc-name='front-desk-list-keyword-input']"))

    print_hbl_button = Button((By.XPATH, "//button[@data-hc-name='front-desk-list-print-hbl']"))
    receive_payment_button = Button((By.XPATH, "//button[@data-hc-name='front-desk-list-receive-payment']"))
    print_uniform_invoice_button = Button((By.XPATH, "//button[@data-hc-name='front-desk-list-print-uni-invoice']"))
    print_receipt_button = Button((By.XPATH, "//button[@data-hc-name='front-desk-list-print-receipt']"))

    class SearchResult:
        _rows = {}
        def __new__(cls, index=1):
                index = int(index) - 1
                if index not in cls._rows:
                    cls._rows[index] = super().__new__(cls)
                return cls._rows[index]

        def __init__(self, index=1):
            index = int(index) - 1
            def ROW_XPATH(xpath):
                return "//hcgridcontainer//div[@row-id='{0}']{1}".format(index, xpath)

            self.check_checkbox = Checkbox((By.XPATH, ROW_XPATH("//hcgridcontainer//div[@row-id='0']//div[@col-id='chk']//input")), (By.XPATH, ROW_XPATH("//hcgridcontainer//div[@row-id='0']//div[@col-id='chk']//span")))
            self.hbl_no_link = Link((By.XPATH, ROW_XPATH("//div[contains(@col-id,'bl_no')]//a")))
            self.party_name_label = Label((By.XPATH, ROW_XPATH("//div[contains(@col-id,'party_name')]//div")))

    class PrintUniformInvoiceModal:
        def MO_XPATH(xpath):
            return "//modal-container{0}".format(xpath)

        counter_label = Label((By.XPATH, MO_XPATH("//div[contains(@class, 'field-data') and ../label[.='Uniform Invoice No.']]")))
        cancel_button = Button((By.XPATH, MO_XPATH("//button[.='Cancel']")))

        class Freight:
            _rows = {}
            new_button = Button((By.XPATH, "//hcslidecontainer[contains(@class,'ng-tns-c407-7')]//i[@class='fa fa-plus']"))

            def __new__(cls, index=1):
                index = int(index)
                if index not in cls._rows:
                    cls._rows[index] = super().__new__(cls)
                return cls._rows[index]

            def __init__(self, index=1):
                index = int(index)
                def MO_XPATH(xpath):
                    return "//modal-container{0}".format(xpath)
                def ROW_XPATH(xpath):
                    return MO_XPATH("//uniforminvoicefreighttable//tr{0}".format(xpath))

                self.freight_code_autocomplete = Autocomplete((By.XPATH, '({})[{}]'.format(ROW_XPATH("//hcbillingselect"), index)), (By.XPATH, '({})[{}]'.format(ROW_XPATH("//ng-dropdown-panel//input[@type='search']"), index)))

    class PrintReceipt:
        print_button = Button((By.XPATH, "//div[@class='modal-footer']//button[contains(., 'Print')]"))
        class Freight:
            _rows = {}
            def __new__(cls, index=1):
                index = int(index)
                if index not in cls._rows:
                    cls._rows[index] = super().__new__(cls)
                return cls._rows[index]

            def __init__(self, index=1):
                index = int(index)
                def ROW_XPATH(xpath):
                    return "//tbody//tr[{0}]{1}".format(index, xpath)

                self.name_label = Label((By.XPATH, ROW_XPATH("//td[1]")))

    class ReceivePaymentModal:
        def MO_XPATH(xpath):
            return "//modal-container{0}".format(xpath)

        cash_button = Button((By.XPATH, MO_XPATH("//button[@data-hc-name='receive-payment-modal-cash-tab']")))
        check_button = Button((By.XPATH, MO_XPATH("//button[@data-hc-name='receive-payment-modal-check-tab']")))
        wire_button = Button((By.XPATH, MO_XPATH("//button[@data-hc-name='receive-payment-modal-wire-tab']")))
        temporary_receipt_button = Button((By.XPATH, MO_XPATH("//button[@data-hc-name='receive-payment-modal-temporary-receipt-tab']")))

    class ARDetailModal:
        def MO_XPATH(xpath):
            return "//div[contains(@class, 'page-quick-sidebar-wrapper')]{0}".format(xpath)
        spin_bar = SpinBar((By.XPATH, MO_XPATH("//hcloadingspin/div")))
        hbl_no_label = Label((By.XPATH, MO_XPATH("//ul/div/h4")))

    class ARSummaryDetailModal:
        def MO_XPATH(xpath):
            return "//div[contains(@class, 'page-quick-sidebar-wrapper')]{0}".format(xpath)
        spin_bar = SpinBar((By.XPATH, MO_XPATH("//hcloadingspin/div")))
        shipment_selected_label = Label((By.XPATH, MO_XPATH("/div/div/div")))
