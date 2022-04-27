from selenium.webdriver.common.by import By

from src.elements import *
from src.pages.base_components.accounting_billing_base_component import *
from src.pages.base_components.accounting_invoice_base_component import *


class OEBookingTab:
    basic_tab = Link((By.XPATH, "//ul[contains(@class, 'nav-tabs')]//a[contains(.,'Basic')]"))
    accounting_tab = Link((By.XPATH, "//ul[contains(@class, 'nav-tabs')]//a[contains(.,'Accounting')]"))
    doc_center_tab = Link((By.XPATH, "//ul[contains(@class, 'nav-tabs')]//a[contains(.,'Doc Center')]"))
class OEBookingBasicTab:
    tools_button = Button((By.XPATH, "//div[@tool-btn='tools']"))
    tools_copy_button = Button((By.XPATH, "//i[@class='fa fa-files-o']"))
    tools_copy_ok_button = Button((By.XPATH, "//button[@ng-click='vm.confirm()']"))

    # Col. 1
    booking_date_datepicker = Datepicker((By.XPATH, "//input[@name='booking_date']"))
    booking_no_input = Input((By.XPATH, "//input[@ng-model='vm.hbl.data.oe_info.booking_no']"))

    # Col. 2
    reference_no_autocomplete = Autocomplete((By.XPATH, "//hc-mbl-select[@ng-model='vm.hbl.mbl']"), (By.XPATH, "//hc-mbl-select[@ng-model='vm.hbl.mbl']//ng-dropdown-panel//input"))

    # Col. 4
    office_autocomplete = Autocomplete((By.XPATH, "//hc-department-select"), (By.XPATH, "//hc-department-select//ng-dropdown-panel//input"))

    save_button = Button((By.XPATH, "//button[@ng-click='vm.save()']"))

    class ContainerList:
        booking_pkg_input = Input((By.XPATH, "//input[@ng-model='vm.hbl.data.booking_info.total_package']"))
        booking_weight_input = Input((By.XPATH, "//input[@ng-model='vm.hbl.data.booking_info.total_weight_kg']"))
        booking_measurement_input = Input((By.XPATH, "//input[@ng-model='vm.hbl.data.booking_info.total_measure_cbm']"))


    class Commodity:
        pass


    class WarehouseReceiptList:
        pass


    class ApplyFromMBLToThisBookingPopup:
        """ Appears after input Reference No.
        """
        no_button = Button((By.XPATH, "//div[@class='modal-content']//button[@ng-click='vm.cancel()']"))
        yes_button = Button((By.XPATH, "//div[@class='modal-content']//button[@ng-click='vm.ok()']"))


class OEBookingAccountingBillingBasedTab:
    save_button = Button((By.XPATH, "//button[@type='submit'][contains(@class,'btn green')]"))
    tool_button = Button((By.XPATH, "//*[contains(@class, 'hbl_board')]//hctools"))

    class Common:
        class copy_to_dropdown:
            # TODO Waiting for improvement
            hbl_revenue_checkbox = Checkbox((By.XPATH, "(//div[@ngbdropdownmenu]//div[contains(., 'HB/L')]//input[@binduniform][@type='checkbox'])[3]"))
            hbl_cost_checkbox = Checkbox((By.XPATH, "(//div[@ngbdropdownmenu]//div[contains(., 'HB/L')]//input[@binduniform][@type='checkbox'])[4]"))
            copy_button = Button((By.XPATH, "//body/div[@class='dropdown']//div[contains(@class, 'dropdown-checkboxes-block')]//button"))

    class revenue(BaseAccountingBillingBasedHBLRevenue):
        pass

    class cost(BaseAccountingBillingBasedHBLCost):
        pass

    class HBLAmount(BaseHBLAmount):
        pass

    class ShipmentProfit(BaseHBLShipmentProfit):
        pass

    class Memo:
        memo_title_button = Button((By.XPATH, "//hcmemo[@type='hbl']//div[contains(text(), 'Memo')]"))


class OEBookingAccountingInvoiceBasedTab:
    invoice_ar_button = Button((By.XPATH, "//a[@name='hbl-create-ar']"))
    d_c_note_button = Button((By.XPATH, "//a[@name='hbl-create-dc']"))
    ap_button = Button((By.XPATH, "//a[@name='hbl-create-ap']"))
    include_draft_amount_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.isIncludeDraft']"))

    class ar(BaseAccountingInvoiceBasedHblAr):
        pass

    class dc(BaseAccountingInvoiceBasedHblDc):
        pass

    class ap(BaseAccountingInvoiceBasedHblAp):
        pass

    total_revenue_label = Label((By.XPATH, "//div[contains(@class, 'hbl_board')]//strong[@ng-bind='vm.totalAmounts.totalRevenue | number:2']"))
    total_cost_label = Label((By.XPATH, "//div[contains(@class, 'hbl_board')]//strong[@ng-bind='vm.totalAmounts.totalCost | number:2']"))
    total_balance_label = Label((By.XPATH, "//div[contains(@class, 'hbl_board')]//strong[@ng-bind='vm.getTotalBalance(vm.invList) | number:2']"))
    hbl_profit_amount_label = Label((By.XPATH, "//div[contains(@class, 'hbl_board')]//table[@ng-if='vm.invoiceProfit']//td[2]"))
    hbl_profit_profit_percentage_label = Label((By.XPATH, "//div[contains(@class, 'hbl_board')]//table[@ng-if='vm.invoiceProfit']//td[3]"))
    hbl_profit_profit_margin_label = Label((By.XPATH, "//div[contains(@class, 'hbl_board')]//table[@ng-if='vm.invoiceProfit']//td[4]"))
