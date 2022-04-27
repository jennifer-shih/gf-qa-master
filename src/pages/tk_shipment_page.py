from selenium.webdriver.common.by import By

from src.drivers.driver import Driver
from src.elements import *
from src.pages.base_components.accounting_billing_base_component import *
from src.pages.base_components.accounting_invoice_base_component import *


class TKTab:
    basic_tab = Link((By.XPATH, "//a[@ng-bind='tab.name'][contains(.,'Basic')]"))
    container_and_item_tab = Link((By.XPATH, "//a[@ng-bind='tab.name'][contains(.,'Container & Item')]"))
    accounting_tab = Link((By.XPATH, "//a[@ng-bind='tab.name'][contains(.,'Accounting')]"))
    doc_center_tab = Link((By.XPATH, "//a[@ng-bind='tab.name'][contains(.,'Doc Center')]"))
    work_order_tab = Link((By.XPATH, "//a[@ng-bind='tab.name'][contains(.,'Work Order')]"))
    status_tab = Link((By.XPATH, "//a[@ng-bind='tab.name'][contains(.,'Status')]"))

class TKBasicTab:
    class MBL:
        tools_button = Button((By.XPATH, "//a[@ng-class='{disabled: toolDisabled}']"))
        file_no_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.filing_no']"))
        post_date_datepicker = Datepicker((By.NAME, "post_date"))
        office_autocomplete = Autocomplete((By.XPATH, "//ng2-form-dispatcher[@name='office']/preceding-sibling::hc-department-select"), (By.XPATH, "//ng-dropdown-panel/div/div/input"))
        type_select = Select((By.XPATH, "//select[contains(@class,'select value-sm form-control')]"))
        mb_l_no_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.MBL_NO']"))
        hb_l_no_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.tk_info.HBL_NO']"))
        vessel_flight_no_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.tk_info.vessel_flight_no']"))
        carrier_bkg_no_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.tk_info.carrier_bkg_no']"))
        quotation_no_autocomplete = Autocomplete((By.XPATH, "//*[@model='vm.mbl.quotation']"), (By.XPATH, "//*[@model='vm.mbl.quotation']//input[@type='search']"))
        customer_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.tk_info.customer']"), (By.XPATH, "//*[@ng-model='vm.mbl.tk_info.customer']//input[@type='search']"))
        customer_ref_no_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.tk_info.customer_ref_no']"))
        shipper_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.tk_info.shipper']"), (By.XPATH, "(//input[@type='search'])[2]"))
        consignee_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.tk_info.consignee']"), (By.XPATH, "(//input[@type='search'])[2]"))
        trucker_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.tk_info.trucker']"), (By.XPATH, "(//input[@type='search'])[2]"))
        bill_to_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.tk_info.bill_to']"), (By.XPATH, "(//input[@type='search'])[2]"))
        sales_autocomplete = Autocomplete((By.XPATH, "//hc-sales-select[@ng-model='vm.mbl.tk_info.sales_person']"), (By.XPATH, "//hc-sales-select[@ng-model='vm.mbl.tk_info.sales_person']//ng-dropdown-panel//input"))
        ship_type_select = Select((By.XPATH, "//select[@ng-model='vm.mbl.tk_info.type']"))
        port_of_loading_autocomplete = Autocomplete((By.XPATH, "//*[@model='vm.mbl.POL']"), (By.XPATH, "(//input[@type='search'])[2]"))
        departure_autocomplete = Autocomplete((By.XPATH, "//*[@model='vm.mbl.APOL']"), (By.XPATH, "(//input[@type='search'])[2]"))
        etd_datepicker = Datepicker((By.XPATH, "//input[@ng-model='vm.mbl.ETD']"))
        port_of_discharge_autocomplete = Autocomplete((By.XPATH, "//*[@model='vm.mbl.POD']"), (By.XPATH, "(//input[@type='search'])[3]"))
        destination_autocomplete = Autocomplete((By.XPATH, "//*[@model='vm.mbl.APOD']"), (By.XPATH, "(//input[@type='search'])[3]"))
        eta_datepicker = Datepicker((By.XPATH, "//input[@ng-model='vm.mbl.ETA']"))
        final_destination_autocomplete = Autocomplete((By.XPATH, "//*[@model='vm.mbl.FDEST']"), (By.XPATH, "(//input[@type='search'])[4]"))
        final_eta_datepicker = Datepicker((By.NAME, "FETA"))
        empty_pickup_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.tk_info.empty_pickup']"), (By.XPATH, "(//input[@type='search'])[5]"))
        freight_pickup_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.tk_info.freight_pickup']"), (By.XPATH, "(//input[@type='search'])[5]"))
        delivery_to_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.tk_info.delivery_to']"), (By.XPATH, "(//input[@type='search'])[5]"))
        empty_return_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.tk_info.empty_return']"), (By.XPATH, "(//input[@type='search'])[5]"))
        package_input = Input((By.NAME, "package"))
        package_unit_autocomplete = Autocomplete((By.XPATH, '//*[@ng-model="vm.mbl.package_unit"]'), (By.XPATH, "xpath=(//input[@type='text'])[29]"))
        weight_kg_input = Input((By.NAME, "weight"))
        weight_lb_input = Input((By.XPATH, "//input[@ng-model='vm.mbl_weight_lb']"))
        measurement_cbm_input = Input((By.NAME, "measure"))
        measurement_cft_input = Input((By.XPATH, "//input[@ng-model='vm.mbl_measure_cft']"))
        estimated_delivery_date_datepicker = Datepicker((By.XPATH, "//input[@ng-model='vm.mbl.tk_info.EDD']"))
        delivered_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.mbl.tk_info.is_delivered']"))
        delivered_date_datepicker = Datepicker((By.XPATH, "//input[@ng-model='vm.mbl.tk_info.delivered_date']"))
        more_button = Button((By.XPATH, "//*[@id='advance-mbl-btn']"))
        e_commerce_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.mbl.is_e_commerce']"))

class TKContainerTab:
    class MBL:
        add_container_button = Button((By.XPATH, "//button[@ng-click='vm.addContainer()']"))
        po_no_tag_list = TagInput((By.XPATH, "//tags-input[@ng-model='vm.mbl.data.__po_num_list']//ul[@class='tag-list']"), (By.XPATH, "//div[@class='po_no_tag']//input[@ng-model='newTag.text']"))

        class container:
            _rows = {}
            def __new__(cls, index=1):
                index = int(index)
                if index not in cls._rows:
                    cls._rows[index] = super().__new__(cls)
                return cls._rows[index]

            def __init__(self, index=1):

                def ROW_XPATH(xpath):
                    return "//tr[@ng-repeat='ct in vm.container_list'][{0}]{1}".format(index, xpath)

                self.checker_checkbox = Checkbox((By.XPATH, "//input[@ng-click='vm.selCt(ct)']"))
                self.container_no_input = Input((By.XPATH, ROW_XPATH("//input[@name='container_no']")))
                self.tp_sz_select = Select((By.XPATH, ROW_XPATH("//select[@ng-model='ct.container_size']")))
                self.seal_no_input = Input((By.XPATH, ROW_XPATH("//input[@ng-model='ct.seal_no']")))
                self.pick_up_no_input = Input((By.XPATH, ROW_XPATH("//input[@ng-model='ct.pickup_no']")))
                self.pkg_input = Input((By.XPATH, ROW_XPATH("//input[@name='package']")))
                self.weight_input = Input((By.XPATH, ROW_XPATH("//input[@name='weight']")))
                self.measurement_input = Input((By.XPATH, ROW_XPATH("//input[@name='measure']")))
                self.storage_start_date_datepicker = Datepicker((By.XPATH, ROW_XPATH("//input[@name='storage_start_date']")))
                self.storage_end_date_datepicker = Datepicker((By.XPATH, ROW_XPATH("//input[@name='storage_end_date']")))
                self.lfd_datepicker = Datepicker((By.XPATH, ROW_XPATH("//input[@name='last_free_date']")))
                self.po_no_tag_input = TagInput((By.XPATH, ROW_XPATH("//ul[@class='tag-list']")), (By.XPATH, ROW_XPATH("//input[@ng-model='newTag.text']")))

        add_commodity_button = Button((By.XPATH, "//button[@ng-click='vm.addItem()']"))

        class commodity:
            _rows = {}
            def __new__(cls, index=1):
                index = int(index)
                if index not in cls._rows:
                    cls._rows[index] = super().__new__(cls)
                return cls._rows[index]

            def __init__(self, index=1):

                def ROW_XPATH(xpath):
                    return "//tr[@ng-repeat='item in vm.mbl.data.__its'][{0}]{1}".format(index, xpath)

                self.checker_checkbox = Checkbox((By.XPATH, ROW_XPATH("//input[@ng-click='vm.selItem(item)']")))
                self.commodity_description_input = Input((By.XPATH, ROW_XPATH("//input[@ng-model='item.description']")))
                self.hts_code_input = Input((By.XPATH, ROW_XPATH("//input[@ng-model='item.hts_code']")))
                self.container_tag_input = TagInput((By.XPATH, ROW_XPATH("//ul[@class='tag-list']")), (By.XPATH, ROW_XPATH("//auto-complete[@source='vm.ngTagsFilter(vm.getContainerSource(), $query)']/preceding-sibling::div[@class='tags']//input[@ng-model='newTag.text']")))

class TKAccountingBillingBasedTab:
    save_button = Button((By.XPATH, "//button[@type='submit'][contains(@class,'btn green')]"))

    class Common:
        class copy_to_dropdown:
            # TODO Waiting for improvement
            MBL_revenue_checkbox = Checkbox((By.XPATH, "(//div[@ngbdropdownmenu]//label[contains(., 'Revenue')]//input[@type='checkbox'])[2]"))
            MBL_cost_checkbox = Checkbox((By.XPATH, "(//div[@ngbdropdownmenu]//label[contains(., 'Cost')]//input[@type='checkbox'])[2]"))
            copy_button = Button((By.XPATH, "(//button[contains(text(), 'Copy')])[2]"))

    class MBL:
        tool_button = Button((By.XPATH, "//hcslidecontainer[contains(@containerclass, 'mbl_board')]//hctools"))
        class revenue(BaseAccountingBillingBasedMBLRevenue):
            pass

        class cost(BaseAccountingBillingBasedMBLCost):
            pass

        class MBLAmount(BaseMBLAmount):
            pass

        class ShipmentProfit(BaseMBLShipmentProfit):
            pass

        class Memo:
            memo_title_button = Button((By.XPATH, "//hcmemo[@type='mbl']//div[contains(text(), 'Memo')]"))

class TKAccountingInvoiceBasedTab:
    class MBL:
        create_ar_button = Button((By.XPATH, "//a[@name='mbl-create-ar']"))
        create_dc_button = Button((By.XPATH, "//a[@name='mbl-create-dc']"))
        create_ap_button = Button((By.XPATH, "//a[@name='mbl-create-ap']"))
        include_draft_amount_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.isIncludeDraftForMbl']"))

        class ar(BaseAccountingInvoiceBasedMblAr):
            pass

        class dc(BaseAccountingInvoiceBasedMblDc):
            pass

        class ap(BaseAccountingInvoiceBasedMblAp):
            pass

        total_revenue_label = Label((By.XPATH, "//div[contains(@class, 'mbl_board')]//strong[@ng-bind='vm.totalAmounts.totalRevenue | number:2']"))
        total_cost_label = Label((By.XPATH, "//div[contains(@class, 'mbl_board')]//strong[@ng-bind='vm.totalAmounts.totalCost | number:2']"))
        total_balance_label = Label((By.XPATH, "//div[contains(@class, 'mbl_board')]//strong[@ng-bind='vm.getTotalBalance(vm.invList) | number:2']"))
        total_profit_amount_label = Label((By.XPATH, "//div[contains(@class, 'mbl_board')]//table[@ng-if='vm.invoiceProfit']//td[2]"))
        total_profit_profit_percentage_label = Label((By.XPATH, "//div[contains(@class, 'mbl_board')]//table[@ng-if='vm.invoiceProfit']//td[3]"))
        total_profit_profit_margin_label = Label((By.XPATH, "//div[contains(@class, 'mbl_board')]//table[@ng-if='vm.invoiceProfit']//td[4]"))


class TKDocTab:

    class MBL:
        tools_button = Button((By.XPATH, "//div[@tool-items='vm.mbl_tools']"))
        pickup_delivery_order_button = Button((By.XPATH, "//a[contains(.,'Pickup / Delivery Order')]"))

        class document_list:
            _rows = {}
            def __new__(cls, index=1):
                index = int(index)
                if index not in cls._rows:
                    cls._rows[index] = super().__new__(cls)
                return cls._rows[index]

            def __init__(self, index=1):
                index = int(index)
                def ROW_XPATH(xpath):
                    return "//table[@hc-order='vm.docOrder']//tbody/tr[{0}]{1}".format(index, xpath)

                self.name_edit_input = EditInput((By.XPATH, ROW_XPATH("//hc-document-name[@model='item.file.name']//input[@ng-value='vm.model']")), (By.XPATH, ROW_XPATH("//hc-document-name[@model='item.file.name']//input[@ng-model='vm.nameInput']")), (By.XPATH, ROW_XPATH("//hc-document-name[@model='item.file.name']//button[@ng-click='vm.beginEditing()']")))

            @staticmethod
            def get_len():
                sleep(2)
                return Driver.num_of_element("//table[@hc-order='vm.docOrder']//tbody/tr")


class TKStatusTab:
    class MBL:
        op_select = Select((By.XPATH, "//select[@ng-model='vm.mbl.data.operator']"))
        sales_autocomplete = Autocomplete((By.XPATH, "//hc-sales-select[@ng-model='vm.mbl.data.tk_info.sales_person']"), ((By.XPATH, "//hc-sales-select[@ng-model='vm.mbl.data.tk_info.sales_person']//ng-dropdown-panel/div/div/input")))
