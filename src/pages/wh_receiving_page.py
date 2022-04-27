from selenium.webdriver.common.by import By

from src.elements import *
from src.pages.base_components.accounting_billing_base_component import *
from src.pages.base_components.accounting_invoice_base_component import *


class WHReceivingTab:
    basic_tab = Link((By.XPATH, "//a[@ng-bind='tab.name'][contains(.,'Basic')]"))
    accounting_tab = Link((By.XPATH, "//a[@ng-bind='tab.name'][contains(.,'Accounting')]"))
    doc_center_tab = Link((By.XPATH, "//a[@ng-bind='tab.name'][contains(.,'Doc Center')]"))
    status_tab = Link((By.XPATH, "//a[@ng-bind='tab.name'][contains(.,'Status')]"))

class WHReceivingBasicTab:

    file_no_input = Input((By.XPATH, "//input[@ng-value='vm.wh.data.filing_no']"))
    post_date_datepicker = Datepicker((By.XPATH, "//*[@ng-model='vm.wh.data.post_date']"))
    office_autocomplete = Autocomplete((By.XPATH, "//hc-department-select[@*[name()='[(office-model)]']='vm.wh.data.office']/ng-select"), (By.XPATH, "//hc-department-select[@*[name()='[(office-model)]']='vm.wh.data.office']//ng-dropdown-panel//input"))
    customer_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.wh.data.customer']"), (By.XPATH, "//*[@ng-model='vm.wh.data.customer']//input[@type='search']"))
    in_date_datepicker = Datepicker((By.XPATH, "//*[@ng-model='vm.wh.data.shipment_date']"))

class WHReceivingAccountingBillingBasedTab:
    save_button = Button((By.XPATH, "//button[@type='submit'][contains(@class,'btn green')]"))

    class Common:
        class copy_to_dropdown:
            # TODO Waiting for improvement
            MBL_revenue_checkbox = Checkbox((By.XPATH, "(//div[@ngbdropdownmenu]//label[contains(., 'Revenue')]//input[@type='checkbox'])[2]"))
            MBL_cost_checkbox = Checkbox((By.XPATH, "(//div[@ngbdropdownmenu]//label[contains(., 'Cost')]//input[@type='checkbox'])[2]"))
            copy_button = Button((By.XPATH, "(//button[contains(text(), 'Copy')])[2]"))

    tool_button = Button((By.XPATH, "//hcslidecontainer[contains(@containerclass, 'mbl_board')]//hctools"))
    class revenue(BaseAccountingBillingBasedMBLRevenue):
        pass

    class cost(BaseAccountingBillingBasedMBLCost):
        pass

    class Memo:
        memo_title_button = Button((By.XPATH, "//hcmemo//*[contains(text(), 'Memo')]"))

class WHReceivingAccountingInvoiceBasedTab:
    create_ar_button = Button((By.XPATH, "//a[@name='mbl-create-ar']"))
    create_dc_button = Button((By.XPATH, "//a[@name='mbl-create-dc']"))
    create_ap_button = Button((By.XPATH, "//a[@name='mbl-create-ap']"))
    include_draft_amount_checkbox = Checkbox((By.XPATH, "//input[contains(@ng-model, 'vm.isIncludeDraft')]"))

    class ar(BaseAccountingInvoiceBasedMblAr):
        pass

    class dc(BaseAccountingInvoiceBasedMblDc):
        pass

    class ap(BaseAccountingInvoiceBasedMblAp):
        pass

    total_revenue_label = Label((By.XPATH, "//div[contains(@class, 'mbl_board')]//strong[@ng-bind='vm.totalAmounts.totalRevenue | number:2']"))
    total_cost_label = Label((By.XPATH, "//div[contains(@class, 'mbl_board')]//strong[@ng-bind='vm.totalAmounts.totalCost | number:2']"))
    total_balance_label = Label((By.XPATH, "//div[contains(@class, 'mbl_board')]//strong[@ng-bind='vm.getTotalBalance(vm.invList) | number:2']"))
