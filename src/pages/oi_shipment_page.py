from time import sleep

from selenium.webdriver.common.by import By

from src.drivers.driver import Driver
from src.elements import *
from src.pages.base_components.accounting_billing_base_component import *
from src.pages.base_components.accounting_invoice_base_component import *


class OITab:
    basic_tab = Link((By.XPATH, "//a[@ng-bind='tab.name'][contains(.,'Basic')]"))
    container_and_item_tab = Link((By.XPATH, "//a[@ng-bind='tab.name'][contains(.,'Container & Item')]"))
    accounting_tab = Link((By.XPATH, "//a[@ng-bind='tab.name'][contains(.,'Accounting')]"))
    doc_center_tab = Link((By.XPATH, "//a[@ng-bind='tab.name'][contains(.,'Doc Center')]"))
    status_tab = Link((By.XPATH, "//a[@ng-bind='tab.name'][contains(.,'Status')]"))

class OIBasicTab:
    add_hb_l_button = Button((By.XPATH, "//button[normalize-space(text())='+ Add HB/L']"))

    class MBL:
        expand_button = Button((By.XPATH, "//a[@ng-click='vm.toggleMblDisplayStatus();']"))
        mbl_body_element = Element((By.XPATH, "//div[@id='mblForm']//div[contains(@class, 'form-body')]"))

        tools_button = Button((By.XPATH, "//div[@id='mblForm']//div[@tool-btn='tools']"))
        title = Label((By.XPATH, "//div[@class='caption ng-binding']"))
        file_no_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.filing_no']"))
        mb_l_no_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.MBL_NO']"))
        office_autocomplete = Autocomplete((By.XPATH, '//*[@id="mblForm"]/div[2]/div/div[1]/div[3]/div/hc-department-select/ng-select'), (By.XPATH, "(//div[@class='search-container select2-search'])[1]/input"))
        b_l_type_select = Select((By.XPATH, "//select[contains(@ng-model,'vm.mbl.bl_type')]"))
        post_date_input = Input((By.XPATH, "//input[@name='post_date']"))
        oversea_agent_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.oversea_agent']"), (By.XPATH, "(//input[@type='search'])[1]"))
        carrier_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.carrier']"), (By.XPATH, "(//input[@type='search'])[1]"))
        b_l_acct_carrier_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.oi_info.bl_acct_carrier']"), (By.XPATH, "(//input[@type='search'])[1]"))
        forwarding_agent_autocomplete = Autocomplete((By.XPATH, "//hc-tp-select[@ng-model='vm.mbl.oi_info.forwarding_agent']"), (By.XPATH, "//hc-tp-select[@ng-model='vm.mbl.oi_info.forwarding_agent']//input[@type='search']"))
        co_loader_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.co_loader']"), (By.XPATH, "(//input[@type='search'])[1]"))
        agent_ref_no_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.agent_ref_no']"))
        sub_b_l_no_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.sub_bl_no']"))
        op_autocomplete = Autocomplete((By.XPATH, "//hc-operator-select[@name='mbl_operator']"), (By.XPATH, "(//div[@class='search-container select2-search'])[1]/input"))

        direct_master_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.mbl.oi_info.is_direct']"))
        customer_ref_no_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.oi_info.customer_ref_no']"))
        shipper_autocomplete = Autocomplete((By.XPATH, "//*[@name='mbl_shipper']"), (By.XPATH, "//*[@name='mbl_shipper']//ng-dropdown-panel//input"))
        consignee_autocomplete = Autocomplete((By.XPATH, "//*[@name='mbl_consignee']"), (By.XPATH, "//*[@name='mbl_consignee']//ng-dropdown-panel//input"))
        notify_autocomplete = Autocomplete((By.XPATH, "//*[@name='mbl_notify']"), (By.XPATH, "//*[@name='mbl_notify']//ng-dropdown-panel//input"))
        customer_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.oi_info.customer']"), (By.XPATH, "//*[@ng-model='vm.mbl.oi_info.customer']//ng-dropdown-panel//input"))
        bill_to_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.oi_info.bill_to']"), (By.XPATH, "//*[@ng-model='vm.mbl.oi_info.bill_to']//ng-dropdown-panel//input"))
        sales_type_select = Select((By.XPATH, "//select[@name='mbl_sales_type']"))
        cargo_type_select = Select((By.XPATH, "//select[@ng-model='vm.mbl.oi_info.cargo_type']"))
        sales_autocomplete = Autocomplete((By.XPATH, "//*[@name='mbl_sales']"), (By.XPATH, "//*[@name='mbl_sales']//ng-dropdown-panel//input"))

        vessel_autocomplete = Autocomplete((By.XPATH, "//*[@model='vm.mbl.vessel_name']"), (By.XPATH, "(//input[@type='search'])[1]"))
        voyage_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.voyage']"))
        cy_location_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.cy_location']"), (By.XPATH, "(//input[@type='search'])[2]"))
        cfs_location_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.cfs_location']"), (By.XPATH, "(//input[@type='search'])[2]"))
        port_of_loading_autocomplete = Autocomplete((By.XPATH, "//*[@model='vm.mbl.POL']"), (By.XPATH, "(//input[@type='search'])[2]"))
        etd_datepicker = Datepicker((By.XPATH, "//input[contains(@ng-model,'vm.mbl.ETD')]"))
        port_of_discharge_autocomplete = Autocomplete((By.XPATH, "//*[@model='vm.mbl.POD']"), (By.XPATH, "(//input[@type='search'])[3]"))
        eta_datepicker = Datepicker((By.XPATH, "//input[@ng-model='vm.mbl.ETA']"))
        place_of_delivery_autocomplete = Autocomplete((By.XPATH, "//*[@model='vm.mbl.DEL']"), (By.XPATH, "//input[@aria-owns='ui-select-choices-3']"))
        place_of_delivery_eta_datepicker = Datepicker((By.XPATH, "//input[@ng-model='vm.mbl.DETA']"))
        final_destination_autocomplete = Autocomplete((By.XPATH, "//*[@model='vm.mbl.FDEST']"), (By.XPATH, "//input[@aria-owns='ui-select-choices-4']"))
        final_eta_datepicker = Datepicker((By.NAME, "FETA"))
        freight_select = Select((By.XPATH, "//select[@ng-model='vm.mbl.freight_term']"))
        ship_mode_select = Select((By.XPATH, "//select[@ng-model='vm.mbl.ship_mode']"))
        service_term_from_select = Select((By.XPATH, "//select[@ng-model='vm.mbl.svc_term_from']"))
        service_term_to_select = Select((By.XPATH, "//select[@ng-model='vm.mbl.svc_term_to']"))
        container_qty_input = Input((By.XPATH, "//input[@ng-value='vm.displayMblContainerSizeQtyInfo()']"))
        ob_l_type_select = Select((By.XPATH, "//select[@ng-model='vm.mbl.oi_info.obl_type']"))
        ob_l_received_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.mbl.oi_info.is_original_bl_received']"))
        ob_l_received_datepicker = Datepicker((By.XPATH, "//input[@ng-model='vm.mbl.oi_info.original_bl_received_date']"))
        telex_release_received_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.mbl.oi_info.is_telex_release_received']"))
        telex_release_received_datepicker = Datepicker((By.XPATH, "//input[@name='telex_release_received_date']"))
        released_date_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.mbl.is_released']"))
        released_date_datepicker = Datepicker((By.XPATH, "//input[@ng-model='vm.mbl.release_date']"))
        business_referred_by_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.referral_by']"), (By.XPATH, "(//input[@type='search'])[6]"))
        more_button = Button((By.XPATH, "//*[@id='advance-mbl-btn']"))
        place_of_receipt_autocomplete = Autocomplete((By.XPATH, "//*[@model='vm.mbl.POR']"), (By.XPATH, "(//input[@type='search'])[6]"))
        place_of_receipt_etd_datepicker = Datepicker((By.XPATH, "//input[@ng-model='vm.mbl.POR_ETD']"))
        return_location_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.return_location']"), (By.XPATH, "(//input[@type='search'])[7]"))
        it_no_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.it_no']"))
        it_date_datepicker = Datepicker((By.NAME, "it_date"))
        it_issued_location_autocomplete = Autocomplete((By.XPATH, "//*[@model='vm.mbl.it_issue_location']"), (By.XPATH, "(//input[@type='search'])[7]"))
        e_commerce_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.mbl.is_e_commerce']"))

    class HBL:
        _instances = {}
        def __new__(cls, index=1):
            index = int(index)
            if index not in cls._instances:
                cls._instances[index] = super().__new__(cls)
            return cls._instances[index]

        def __init__(self, index=1):
            index = int(index)
            def HBL_XPATH(xpath):
                return "//div[@id='hbl_{0}']{1}".format(index-1, xpath)

            # right side hbl panel
            self.hbl_side_panel = Button((By.XPATH, "//div[@id='hbl_side_{0}']".format(index-1)))

            self.tools_button = Button((By.XPATH, HBL_XPATH("//div[@tool-btn='tools']")))
            self.tools_copy_to_button = Button((By.XPATH, HBL_XPATH("//a[contains(.,'Copy To')]")))
            self.title = Label((By.XPATH, "//div[@class='caption _max-w22per text-hidden ng-binding']"))

            self.hb_l_no_input = Input((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.HBL_NO']")))
            self.ams_no_input = Input((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.AMS_NO']")))
            self.isf_no_input = Input((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.ISF_NO']")))
            self.isf_filing_by_3rd_party_checkbox = Checkbox((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.is_3rd_party_isf_filing']")))
            self.quotation_no_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-quotation-select[@model='hbl.quotation']")), (By.XPATH, HBL_XPATH("//hc-quotation-select[@model='hbl.quotation']//input[@type='search']")))
            self.shipper_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-tp-select[@name='hbl_shipper']")), (By.XPATH, HBL_XPATH("//ng-dropdown-panel//input[@type='search']")))
            self.consignee_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.consignee']")), (By.XPATH, HBL_XPATH("//ng-dropdown-panel//input[@type='search']")))
            self.notify_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-tp-select[@name='hbl_notify']")), (By.XPATH, HBL_XPATH("//hc-tp-select[@name='hbl_notify']//ng-dropdown-panel//input[@type='search']")))
            self.customer_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.customer']")), (By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.customer']//ng-dropdown-panel//input[@type='search']")))
            self.bill_to_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.bill_to']")), (By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.bill_to']//ng-dropdown-panel//input")))
            self.sub_b_l_no_input = Input((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.oi_info.sub_bl_no']")))
            self.op_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//*[@name='hbl_operator']")), (By.XPATH, HBL_XPATH("//hc-operator-select[@name='hbl_operator']//div[@class='ng-dropdown-header']//input")))
            self.sales_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-sales-select[@name='hbl_sales']")), (By.XPATH, HBL_XPATH("//hc-sales-select[@name='hbl_sales']//ng-dropdown-panel//input")))
            self.forwarding_agent_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-tp-select[@name='hbl_forwarding_agent']")), (By.XPATH, HBL_XPATH("//hc-tp-select[@name='hbl_forwarding_agent']//ng-dropdown-panel//input")))
            self.customs_broker_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.customs_broker']")), (By.XPATH, HBL_XPATH("//ng-dropdown-panel//input[@type='search']")))
            self.trucker_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.trucker']")), (By.XPATH, HBL_XPATH("//ng-dropdown-panel//input[@type='search']")))
            self.cy_cfs_location_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.cy_cfs_location']")), (By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.cy_cfs_location']//input[@type='search']")))
            self.available_datepicker = Datepicker((By.XPATH, HBL_XPATH("//input[@name='hbl_available_date']")))
            self.place_of_delivery_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-location-select[@model='hbl.DEL']")), (By.XPATH, HBL_XPATH("//hc-location-select[@model='hbl.DEL']//input[@type='search']")))
            self.place_of_delivery_eta_datepicker = Datepicker((By.XPATH, HBL_XPATH("//input[@name='hbl_DETA']")))
            self.final_destination_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-location-select[@model='hbl.FDEST']")), (By.XPATH, HBL_XPATH("//hc-location-select[@model='hbl.FDEST']//input[@type='search']")))
            self.final_eta_datepicker = Datepicker((By.XPATH, HBL_XPATH("//input[@name='hbl_FETA']")))
            self.delivery_location_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.delivery_location']")), (By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.delivery_location']//input[@type='search']")))
            self.ship_mode_select = Select((By.XPATH, HBL_XPATH("//select[@ng-model='hbl.ship_mode']")))
            self.freight_select = Select((By.XPATH, HBL_XPATH("//select[@ng-model='hbl.freight_term']")))
            self.lfd_datepicker = Datepicker((By.XPATH, HBL_XPATH("//input[@name='hbl_last_free_date']")))
            self.rail_check_select = CheckSelect((By.XPATH, HBL_XPATH("//input[@name='is_rail']")), (By.XPATH, HBL_XPATH("//select[@name='railway_code']")))
            self.it_no_input = Input((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.it_no']")))
            self.it_date_datepicker = Datepicker((By.XPATH, HBL_XPATH("//input[@name='hbl_it_date']")))
            self.it_issued_location_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-port-code-location-select[@model='hbl.it_issue_location']")), (By.XPATH, HBL_XPATH("//hc-port-code-location-select[@model='hbl.it_issue_location']//input[@type='search']")))
            self.go_date_datepicker = Datepicker((By.XPATH, HBL_XPATH("//input[@name='hbl_government_office_date']")))
            self.expiry_date_datepicker = Datepicker((By.XPATH, HBL_XPATH("//input[@name='hbl_expiry_date']")))
            self.express_b_l_radio_group = RadioGroup({'Yes': (By.XPATH, HBL_XPATH("//input[@ng-model='hbl.is_express'][@ng-value='true']")),
                                                       'No': (By.XPATH, HBL_XPATH("//input[@ng-model='hbl.is_express'][@ng-value='false']"))})
            self.sales_type_select = Select((By.XPATH, HBL_XPATH("//select[@ng-model='hbl.sales_type']")))
            self.incoterms_select = Select((By.XPATH, HBL_XPATH("//select[@ng-model='hbl.incoterms']")))
            self.cargo_type_select = Select((By.XPATH, HBL_XPATH("//select[@ng-model='hbl.oi_info.cargo_type']")))
            self.door_move_checkbox = Checkbox((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.oi_info.is_door_move']")))
            self.cclearance_checkbox = Checkbox((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.oi_info.is_customs_clearance']")))
            self.chold_checkbox = Checkbox((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.oi_info.is_customs_hold']")))
            self.c_released_date_datepicker =  Datepicker((By.XPATH, HBL_XPATH("//input[@name='hbl_customs_received_date']")))
            self.service_term_from_select = Select((By.XPATH, HBL_XPATH("//select[@ng-model='hbl.svc_term_from']")))
            self.service_term_to_select = Select((By.XPATH, HBL_XPATH("//select[@ng-model='hbl.svc_term_to']")))
            self.business_referred_by_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-tp-select[@name='hbl_referral_by']")), (By.XPATH, HBL_XPATH("//hc-tp-select[@name='hbl_referral_by'] //ng-dropdown-panel//input[@type='search']")))
            self.ob_l_received_check_datepicker = CheckDatepicker((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.is_original_bl_received']")), (By.XPATH, HBL_XPATH("//input[@name='hbl_original_bl_received_date']")))
            self.telex_release_received_check_datepicker = CheckDatepicker((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.oi_info.is_telex_release_received']")), (By.XPATH, HBL_XPATH("//input[@ng-model='hbl.oi_info.telex_release_received_date']")))
            self.ror_checkbox = Checkbox((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.is_release_order_required']")))
            self.frt_released_check_datepicker = CheckDatepicker((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.is_released']")), (By.XPATH, HBL_XPATH("//input[@name='hbl_release_date']")))
            self.door_delivered_datepicker =  Datepicker((By.XPATH, HBL_XPATH("//input[@name='door_delivered']")))
            self.l_c_no_input = Input((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.LC_NO']")))
            self.ship_type_select = Select((By.XPATH, HBL_XPATH("//select[@ng-model='hbl.ship_type']")))
            self.s_c_no_input = Input((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.oi_info.sc_no']")))
            self.name_account_input = Input((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.oi_info.name_account']")))
            self.group_comm_input = Input((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.oi_info.group_comm']")))
            self.line_code_input = Input((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.oi_info.line_code']")))
            self.e_commerce_checkbox = Checkbox((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.is_e_commerce']")))

            self.more_button = Button((By.XPATH, HBL_XPATH("//a[@ng-click='vm.toggleHblAdvanced($index)']")))

    class CopyHBLToMBL:
        select_mbl_autocomplete = Autocomplete((By.XPATH, "//hc-mbl-select[@ng-model='vm.selectedMbl']"), (By.XPATH, "//hc-mbl-select[@ng-model='vm.selectedMbl']//ng-dropdown-panel//input"))
        copy_accouting_info_checkbox = Checkbox((By.XPATH, "//span[@class='checked']/input[@name='acct'][@type='checkbox']"))
        a_p_checkbox = Checkbox((By.XPATH, "//copy-inv-types-choice//div[@class='checker']/parent::label[contains(.,'A/P')]"))
        a_r_checkbox = Checkbox((By.XPATH, "//copy-inv-types-choice//div[@class='checker']/parent::label[contains(.,'A/R')]"))
        d_c_checkbox = Checkbox((By.XPATH, "//copy-inv-types-choice//div[@class='checker']/parent::label[contains(.,'D/C')]"))
        ok_button = Button((By.XPATH, "//button[@data-dismiss='modal'][@ng-click='vm.confirm()']"))
        close_button = Button((By.XPATH, "//button[@data-dismiss='modal'][@ng-click='vm.cancel()']"))
        mbl_link = Link((By.XPATH, "//a[@ng-if='link.url']"))

class OIContainerTab:
    add_hb_l_button = Button((By.XPATH, "//button[normalize-space(text())='+ Add HB/L']"))

    class MBL:
        add_button = Button((By.XPATH, "//button[@ng-click='vm.addContainer()']"))
        add_five_button = Button((By.XPATH, "//button[@ng-click='vm.addMultipleContainer(5)']"))
        add_multiple_button = Button((By.XPATH, "//hc-add-multiple-container-btn/button"))
        pkg_unit_autocomplete = Autocomplete((By.XPATH, "//div[@id='mblForm']//div[@class='container_area']//thead//hc-choice-select[@ng-model='vm.mbl.package_unit']"), (By.XPATH, "//div[@id='mblForm']//div[@class='container_area']//thead//hc-choice-select[@ng-model='vm.mbl.package_unit']//ng-dropdown-panel//input[@type='text']"))
        weight_unit_select = Select((By.XPATH, "//select[@ng-model='vm.mbl.weight_unit']"))
        measurement_unit_select = Select((By.XPATH, "//select[@ng-model='vm.mbl.measure_unit']"))

        # Generic
        input_total_number_checkbox = Checkbox((By.XPATH, "//input[@type='checkbox'][@ng-model='vm.mbl.total_amount_type']"))
        # Enterprise
        total_amount_source_radio_group = RadioGroup({'Container Total': (By.XPATH, "//tr[@ng-form='vm.mblForm3']/td[@ng-if='vm.isEnableSyncTotalFromHbl()']//*[text()[contains(.,'Container Total')]]"),
                                                      'Manual Input': (By.XPATH, "//tr[@ng-form='vm.mblForm3']/td[@ng-if='vm.isEnableSyncTotalFromHbl()']//*[text()[contains(.,'Manual Input')]]"),
                                                      'Sync from HBL': (By.XPATH, "//tr[@ng-form='vm.mblForm3']/td[@ng-if='vm.isEnableSyncTotalFromHbl()']//*[text()[contains(.,'Sync from HBL')]]")})

        total_manual_pkg_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.total_package']"))
        total_manual_weight_kg_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.total_weight_kg']"))
        total_manual_weight_converter_label = Label((By.XPATH, "//span[@ng-show='vm.isMblTotalAmountManualInput() && vm.oeMbl.getTotalWeight(vm.mbl, (vm.mbl.weight_unit | versaUnit))']")) # if enable manual input will show this
        total_manual_measurement_converter_label = Label((By.XPATH, "ng-show='vm.isMblTotalAmountManualInput() && vm.oeMbl.getTotalMeasure(vm.mbl, (vm.mbl.measure_unit | versaUnit))'")) # if enable manual input will show this
        total_manual_weight_lb_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.total_weight_lb']"))
        total_manual_measurement_cbm_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.total_measure_cbm']"))
        total_manual_measurement_cft_input = Input((By.XPATH," //input[@ng-model='vm.mbl.total_measure_cft']"))


        # table of container list
        class container:
            _rows = {}
            def __new__(cls, index=1):
                index = int(index)
                if index not in cls._rows:
                    cls._rows[index] = super().__new__(cls)
                return cls._rows[index]

            def __init__(self, index=1):
                # index = len(self._rows) - int(index)
                index = int(index) - 1
                def ROW_XPATH(xpath):
                    return "//div[@id='mblForm']//tr[@id='expand_row_{0}']/preceding-sibling::tr[1]{1}".format(index, xpath)
                def ROW_ADV_XPATH(xpath): #
                    return "//div[@id='mblForm']//tr[@id='expand_row_{0}']{1}".format(index, xpath)

                self.container_no_input = Input((By.XPATH, ROW_XPATH("//input[@name='container_no']")))
                self.more_button = Button((By.XPATH, ROW_XPATH("//a[@class='btn-expand show-open']")))
                self.tp_sz_select = Select((By.XPATH, ROW_XPATH("//select[@ng-model='ct.container_size']")))
                self.seal_no_input = Input((By.XPATH, ROW_XPATH("//input[@ng-model='ct.seal_no']")))
                self.lfd_datepicker = Datepicker((By.XPATH, ROW_XPATH("//input[@name='last_free_date']")))
                self.fdd_datepicker = Datepicker((By.XPATH, ROW_XPATH("//input[@name='free_detention_date']")))
                self.pkg_input = Input((By.XPATH, ROW_XPATH("//input[@name='package']")))
                # self.weight_input = Input((By.XPATH, ROW_XPATH("//input[@name='weight']")))
                self.weight_kg_input = Input((By.XPATH, ROW_XPATH("//input[@ng-model='ct.weight_kg']")))
                self.weight_lb_input = Input((By.XPATH, ROW_XPATH("//input[@ng-model='ct.weight_lb']")))
                self.weight_converter_label = Label((By.XPATH, ROW_XPATH("//span[@ng-show='!vm.isDisablePkgWeightMeasurementInput(vm.mbl) && vm.oiMblContainer.getWeight(vm.mbl, ct, (vm.mbl.weight_unit | versaUnit)) !== null']")))
                self.measurement_cbm_input = Input((By.XPATH, ROW_XPATH("//input[@ng-model='ct.measure_cbm']")))
                self.measurement_cft_input = Input((By.XPATH, ROW_XPATH("//input[@ng-model='ct.measure_cft']")))
                self.measurement_converter_label = Label((By.XPATH, ROW_XPATH("//span[@ng-show='!vm.isDisablePkgWeightMeasurementInput(vm.mbl) && vm.oiMblContainer.getMeasure(vm.mbl, ct, (vm.mbl.measure_unit | versaUnit)) !== null']")))

                # more
                self.seal_no_2_input = Input((By.XPATH, ROW_ADV_XPATH("//input[@ng-model='ct.seal_no2']")))
                self.pick_no_input = Input((By.XPATH, ROW_ADV_XPATH("//input[@ng-model='ct.pickup_no']")))
                self.cprs_no_input = Input((By.XPATH, ROW_ADV_XPATH("//input[@ng-model='ct.cprs_no']")))
                self.cnru_no_input = Input((By.XPATH, ROW_ADV_XPATH("//input[@ng-model='ct.cnru_no']")))
                self.dg_select = Select((By.XPATH, ROW_ADV_XPATH("//select[@ng-model='ct.is_dangerous']")))
                self.storage_start_date_datepicker = Datepicker((By.XPATH, ROW_ADV_XPATH("//input[@name='storage_start_date']")))
                self.storage_end_date_datepicker = Datepicker((By.XPATH, ROW_ADV_XPATH("//input[@name='storage_end_date']")))
                self.rail_start_datepicker = Datepicker((By.XPATH, ROW_ADV_XPATH("//input[@name='rail_start_date']")))
                self.appt_datepicker = Datepicker((By.XPATH, ROW_ADV_XPATH("//input[@name='appt_date']")))
                self.pick_up_datepicker = Datepicker((By.XPATH, ROW_ADV_XPATH("//input[@name='pickup_date']")))
                self.gate_out_datepicker = Datepicker((By.XPATH, ROW_ADV_XPATH("//input[@name='gate_out_date']")))
                self.fdest_eta_datepicker = Datepicker((By.XPATH, ROW_ADV_XPATH("//input[@name='FETA']")))
                self.eta_door_datepicker = Datepicker((By.XPATH, ROW_ADV_XPATH("//input[@name='estimate_delivery_date']")))
                self.ata_door_datepicker = Datepicker((By.XPATH, ROW_ADV_XPATH("//input[@name='delivery_date']")))
                self.empty_return_datepicker = Datepicker((By.XPATH, ROW_ADV_XPATH("//input[@ng-model='ct.empty_return_date']")))
                self.remark_input = Input((By.XPATH, ROW_ADV_XPATH("//textarea[@ng-model='ct.remark']")))

            @staticmethod
            def search_container_index(container_no):
                sleep(3)
                container_no_inputs = Driver.get_driver().find_elements_by_xpath("//input[@name='container_no']")
                for element in container_no_inputs:
                    element_value = element.get_attribute("value")
                    element_no = element_value if element_value != None else element.text
                    if element_no == container_no:
                        return container_no_inputs.index(element) + 1
                return None


    class HBL:
        add_commodity_button = Button((By.XPATH, "//button[@ng-click='vm.addHblItem(hbl)']"))

        class commodity:
            _rows = {}
            def __new__(cls, index=1):
                index = int(index)
                if index not in cls._rows:
                    cls._rows[index] = super().__new__(cls)
                return cls._rows[index]

            def __init__(self, index=1):
                index = int(index)
                def ROW_XPATH(xpath):
                    return "//tr[@ng-form='item.__form'][{0}]{1}".format(index, xpath)

                self.commodity_description_input = Input((By.XPATH, ROW_XPATH("//input[@ng-model='item.description']")))
                self.hts_code_input = Input((By.XPATH, ROW_XPATH("//input[@ng-model='item.hts_code']")))
                self.container_tag_input = TagInput((By.XPATH, ROW_XPATH("//tags-input[@ng-model='item.__container_set']//ul[@class='tag-list']")), (By.XPATH, ROW_XPATH("//tags-input[@ng-model='item.__container_set']//input[@ng-model='newTag.text']")))

            @staticmethod
            def search_commodity_index(desc):
                sleep(3)
                commodity_description_inputs = Driver.get_driver().find_elements_by_xpath("//input[@ng-model='item.description']")
                for element in commodity_description_inputs:
                    element_value = element.get_attribute("value")
                    element_desc = element_value if element_value != None else element.text
                    if element_desc == desc:
                        return commodity_description_inputs.index(element) + 1
                return None


class OIAccountingBillingBasedTab:
    save_button = Button((By.XPATH, "//button[@type='submit'][contains(@class,'btn green')]"))

    class Common:
        class copy_to_dropdown:
            # TODO Waiting for improvement
            MBL_revenue_checkbox = Checkbox((By.XPATH, "(//div[@ngbdropdownmenu]//div[contains(., 'MB/L')]//input[@binduniform][@type='checkbox'])[7]"))
            MBL_cost_checkbox = Checkbox((By.XPATH, "(//div[@ngbdropdownmenu]//div[contains(., 'MB/L')]//input[@binduniform][@type='checkbox'])[8]"))
            HBL_revenue_checkbox = Checkbox((By.XPATH, "(//div[@ngbdropdownmenu]//div[contains(., 'HB/L')]//input[@binduniform][@type='checkbox'])[7]"))
            HBL_cost_checkbox = Checkbox((By.XPATH, "(//div[@ngbdropdownmenu]//div[contains(., 'HB/L')]//input[@binduniform][@type='checkbox'])[8]"))
            copy_button = Button((By.XPATH, "//body/div[@class='dropdown']//div[contains(@class, 'dropdown-checkboxes-block')][4]//button"))

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

    class HBL:
        tool_button = Button((By.XPATH, "//*[contains(@class, 'hbl_board')]//hctools"))

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

class OIAccountingInvoiceBasedTab:
    class MBL:
        invoice_ar_button = Button((By.XPATH, "//a[@name='mbl-create-ar']"))
        d_c_note_button = Button((By.XPATH, "//a[@name='mbl-create-dc']"))
        ap_button = Button((By.XPATH, "//a[@name='mbl-create-ap']"))
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

    class HBL:
        invoice_ar_button = Button((By.XPATH, "//a[@name='hbl-create-ar']"))
        d_c_note_button = Button((By.XPATH, "//a[@name='hbl-create-dc']"))
        ap_button = Button((By.XPATH, "//a[@name='hbl-create-ap']"))
        include_draft_amount_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.isIncludeDraftForHbl']"))

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
