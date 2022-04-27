from selenium.webdriver.common.by import By

from src.elements import *
from src.pages.base_components.accounting_billing_base_component import *
from src.pages.base_components.accounting_invoice_base_component import *


class OESidePanel:
    def hbl_select_button(index):
        return Button((By.XPATH, f"//div[@id='hbl_side_{ index - 1 }'] | //div[contains(@class, 'hbl_sm')][contains(@class, 'ng-star-inserted')][{ index }]"))


class OEBasicTab:
    add_hb_l_button = Button((By.XPATH, "//button[normalize-space(text())='+ Add HB/L']"))

    class MBL:
        expand_button = Button((By.XPATH, "//a[@ng-click='vm.toggleMblDisplayStatus();']"))
        mbl_body_element = Element((By.XPATH, "//div[@id='mblForm']//div[contains(@class, 'portlet-body')][@style='display: block;']"))

        file_no_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.filing_no']"))
        mb_l_no_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.MBL_NO']"))
        office_autocomplete = Autocomplete((By.XPATH, '//*[@id="mblForm"]/div[2]/div/div[1]/div[3]/div/hc-department-select/ng-select'), (By.XPATH, "(//div[@class='search-container select2-search'])[1]/input"))
        b_l_type_select = Select((By.XPATH, "//select[contains(@ng-model,'vm.mbl.bl_type')]"))
        post_date_input = Input((By.XPATH, "//input[@name='post_date']"))
        carrier_bkg_no_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.oe_info.carrier_bkg_no']"))
        itn_no_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.oe_info.itn_no']"))
        carrier_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.carrier']"), (By.XPATH, "(//input[@type='search'])[1]"))
        b_l_acct_carrier_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.oe_info.bl_acct_carrier']"), (By.XPATH, "(//input[@type='search'])[1]"))
        shipping_agent_autocomplete = Autocomplete((By.XPATH, "//hc-tp-select[@name='shipping_agent']"), (By.XPATH, "(//input[@type='search'])[1]"))
        oversea_agent_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.oversea_agent']"), (By.XPATH, "(//input[@type='search'])[1]"))
        notify_autocomplete = Autocomplete((By.XPATH, "//hc-tp-select[@name='mbl_notify']"), (By.XPATH, "(//input[@type='search'])[1]"))
        forwarding_agent_autocomplete = Autocomplete((By.XPATH, "//hc-tp-select[@ng-model='vm.mbl.oe_info.forwarding_agent']"), (By.XPATH, "(//input[@type='search'])[1]"))
        co_loader_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.co_loader']"), (By.XPATH, "(//input[@type='search'])[1]"))
        c_o_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.mbl.oe_info.use_care_of']"))
        c_o_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.oe_info.care_of'"), (By.XPATH, "(//input[@type='search'])[1]"))
        op_autocomplete = Autocomplete((By.XPATH, "(//hcoperatorselect)[1]/ng-select[1]/div/div/div[@class='ng-value']"), (By.XPATH, "(//div[@class='search-container select2-search'])[1]/input"))

        direct_master_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.mbl.oe_info.is_direct']"))
        customer_ref_no_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.oe_info.customer_ref_no']"))
        customer_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.oe_info.customer']"), (By.XPATH, "//*[@ng-model='vm.mbl.oe_info.customer']//ng-dropdown-panel//input"))
        bill_to_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.oe_info.bill_to']"), (By.XPATH, "//*[@ng-model='vm.mbl.oe_info.bill_to']//ng-dropdown-panel//input"))
        consignee_autocomplete = Autocomplete((By.XPATH, "//*[@name='mbl_consignee']"), (By.XPATH, "//*[@name='mbl_consignee']//ng-dropdown-panel//input"))
        sales_type_select = Select((By.XPATH, "//select[@name='mbl_sales_type']"))
        cargo_type_select = Select((By.XPATH, "//select[@ng-model='vm.mbl.oe_info.cargo_type']"))
        sales_autocomplete = Autocomplete((By.XPATH, "//*[@name='mbl_sales']"), (By.XPATH, "//*[@name='mbl_sales']//ng-dropdown-panel//input"))

        vessel_autocomplete = Autocomplete((By.XPATH, "//*[@model='vm.mbl.vessel_name']"), (By.XPATH, "(//input[@type='search'])[1]"))
        voyage_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.voyage']"))
        place_of_receipt_autocomplete = Autocomplete((By.XPATH, "//*[@model='vm.mbl.POR']"), (By.XPATH, "//*[@model='vm.mbl.POR']//input[@type='search']"))
        place_of_receipt_etd_datepicker = Datepicker((By.XPATH, "//input[@ng-model='vm.mbl.POR_ETD']"))
        port_of_loading_autocomplete = Autocomplete((By.XPATH, "//*[@model='vm.mbl.POL']"), (By.XPATH, "//*[@model='vm.mbl.POL']//input[@type='search']"))
        etd_datepicker = Datepicker((By.XPATH, "//input[contains(@ng-model,'vm.mbl.ETD')]"))
        port_of_discharge_autocomplete = Autocomplete((By.XPATH, "//*[@model='vm.mbl.POD']"), (By.XPATH, "//*[@model='vm.mbl.POD']//input[@type='search']"))
        eta_datepicker = Datepicker((By.XPATH, "//input[@ng-model='vm.mbl.ETA']"))
        more_button = Button((By.XPATH, "//a[@id='advance-mbl-btn']"))
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
            self.title = Label((By.XPATH, "//div[@class='portlet-title ng-scope']//div[@class ='caption ng-binding']['hc-toggle-caption']"))

            self.hb_l_no_autogen_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.autoGenHBLNO']"))
            self.hb_l_no_input = Input((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.HBL_NO']")))
            self.booking_no_input = Input((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.oe_info.booking_no']")))
            self.itn_no_input = Input((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.oe_info.itn_no']")))
            self.customer_ref_no_input = Input((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.customer_ref_no']")))
            self.actual_shipper_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.shipper']")), (By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.shipper']//ng-dropdown-panel//input[@type='search']")))
            self.customer_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.customer']")), (By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.customer']//ng-dropdown-panel//input[@type='search']")))
            self.bill_to_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.bill_to']")), (By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.bill_to']//ng-dropdown-panel//input[@type='search']")))
            self.consignee_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.consignee']")), (By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.consignee']//ng-dropdown-panel//input[@type='search']")))
            self.notify_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.notify']")), (By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.notify']//ng-dropdown-panel//input[@type='search']")))
            self.customs_broker_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.customs_broker']")), (By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.customs_broker']//ng-dropdown-panel//input[@type='search']")))
            self.trucker_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.trucker']")), (By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.trucker']//ng-dropdown-panel//input[@type='search']")))
            self.sales_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hcsalesselect")), (By.XPATH, HBL_XPATH("//hcsalesselect//ng-dropdown-panel//input")))
            self.hb_l_agent_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.oe_info.agent']")), (By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.oe_info.agent']//ng-dropdown-panel//input[@type='search']")))
            self.forwarding_agent_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.oe_info.forwarding_agent']")), (By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.oe_info.forwarding_agent']//ng-dropdown-panel//input[@type='search']")))
            self.op_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hcoperatorselect")), (By.XPATH, HBL_XPATH("//hcoperatorselect//ng-dropdown-panel//input")))
            self.sub_agent_b_l_checkbox = Checkbox((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.oe_info.is_sub_agent_bl']")))
            self.receiving_agent_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.oe_info.receiving_agent']")), (By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.oe_info.receiving_agent']//ng-dropdown-panel//input[@type='search']")))
            self.place_of_receipt_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-location-select[@model='hbl.oe_info.POR']")), (By.XPATH, HBL_XPATH("//hc-location-select[@model='hbl.oe_info.POR']//div[contains(@class, 'ui-select-dropdown')]//input")))
            self.place_of_receipt_etd_datepicker = Datepicker((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.oe_info.POR_ETD']")))
            self.port_of_discharge_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-location-select[@model='hbl.oe_info.POD']")), (By.XPATH, HBL_XPATH("//hc-location-select[@model='hbl.oe_info.POD']//div[contains(@class, 'ui-select-dropdown')]//input")))
            self.eta_datepicker = Datepicker((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.oe_info.ETA']")))
            self.place_of_delivery_del_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-location-select[@model='hbl.DEL']")), (By.XPATH, HBL_XPATH("//hc-location-select[@model='hbl.DEL']//input[@type='search']")))
            self.place_of_delivery_eta_datepicker = Datepicker((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.DETA']")))
            self.final_destination_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-location-select[@model='hbl.FDEST']")), (By.XPATH, HBL_XPATH("//hc-location-select[@model='hbl.FDEST']//input[@type='search']")))
            self.final_eta_datepicker = Datepicker((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.FETA']")))
            self.fba_fc_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.oe_info.fba_fc']")), (By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.oe_info.fba_fc']//ng-dropdown-panel//input[@type='search']")))
            self.empty_pickup_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.oe_info.empty_pickup']")), (By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.oe_info.empty_pickup']//ng-dropdown-panel//input[@type='search']")))
            self.delivery_to_pier_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.oe_info.delivery_to']")), (By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.oe_info.delivery_to']//ng-dropdown-panel//input[@type='search']")))
            self.cargo_ready_date_datepicker = Datepicker((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.oe_info.cargo_arrival_date']")))
            self.cargo_pickup_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.oe_info.cargo_pickup']")), (By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.oe_info.cargo_pickup']//ng-dropdown-panel//input[@type='search']")))
            self.ship_mode_select = Select((By.XPATH, HBL_XPATH("//select[@ng-model='hbl.ship_mode']")))
            self.buying_freight_select = Select((By.XPATH, HBL_XPATH("//select[@ng-model='hbl.oe_info.buying_freight']")))
            self.selling_freight_select = Select((By.XPATH, HBL_XPATH("//select[@ng-model='hbl.oe_info.selling_freight']")))
            self.service_term_from_select = Select((By.XPATH, HBL_XPATH("//select[@ng-model='hbl.svc_term_from']")))
            self.service_term_to_select = Select((By.XPATH, HBL_XPATH("//select[@ng-model='hbl.svc_term_to']")))
            self.express_b_l_radio_group = RadioGroup({'Yes': (By.XPATH, HBL_XPATH("//input[@ng-model='hbl.is_express'][@ng-value='true']")),
                                                       'No': (By.XPATH, HBL_XPATH("//input[@ng-model='hbl.is_express'][@ng-value='false']"))})
            self.cargo_type_select = Select((By.XPATH, HBL_XPATH("//select[@ng-model='hbl.oe_info.cargo_type']")))
            self.sales_type_select = Select((By.XPATH, HBL_XPATH("//select[@ng-model='hbl.sales_type']")))
            self.w_h_cut_off_date_datepicker = Datepicker((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.oe_info.wh_cut_off_time']")))
            self.early_return_date_datepicker = Datepicker((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.oe_info.early_return_datetime']")))
            self.l_c_no_input = Input((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.LC_NO']")))
            self.l_c_issue_bank_input = Input((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.oe_info.lc_issue_bank']")))
            self.l_c_issue_date_datepicker = Datepicker((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.oe_info.lc_issue_date']")))
            self.onboard_datepicker = Datepicker((By.XPATH, HBL_XPATH("//input[@name='hbl_on_board_date']")))
            self.stackable_radio_group = RadioGroup({'Yes': (By.XPATH, HBL_XPATH("//input[@ng-model='hbl.oe_info.is_stackable'][@ng-value='true']")),
                                                     'No': (By.XPATH, HBL_XPATH("//input[@ng-model='hbl.oe_info.is_stackable'][@ng-value='false']"))})
            self.business_referred_by_autocomplete = Autocomplete((By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.oe_info.referral_by']")), (By.XPATH, HBL_XPATH("//hc-tp-select[@ng-model='hbl.oe_info.referral_by']//ng-dropdown-panel//input[@type='search']")))
            self.more_button = Button((By.XPATH, HBL_XPATH("//a[@ng-click='vm.toggleHblAdvanced($index)']")))
            self.w_o_no_input = Input((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.oe_info.wo_no']")))
            self.ship_type_select = Select((By.XPATH, HBL_XPATH("//select[@ng-model='hbl.ship_type']")))
            self.incoterms_select = Select((By.XPATH, HBL_XPATH("//select[@ng-model='hbl.incoterms']")))
            self.nar_no_input = Input((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.oe_info.nra_no']")))
            self.e_commerce_checkbox = Checkbox((By.XPATH, HBL_XPATH("//input[@ng-model='hbl.is_e_commerce']")))

    class CopyHBLToMBL:
        select_mbl_autocomplete = Autocomplete((By.XPATH, "//hc-mbl-select[@ng-model='vm.selectedMbl']"), (By.XPATH, "//hc-mbl-select[@ng-model='vm.selectedMbl']//ng-dropdown-panel//input"))
        copy_accouting_info_checkbox = Checkbox((By.XPATH, "//div[@class='checker']/span/input[@name='acct'][@type='checkbox']"))
        a_p_checkbox = Checkbox((By.XPATH, "//copy-inv-types-choice//div[@class='checker']/parent::label[contains(.,'A/P')]"))
        a_r_checkbox = Checkbox((By.XPATH, "//copy-inv-types-choice//div[@class='checker']/parent::label[contains(.,'A/R')]"))
        d_c_checkbox = Checkbox((By.XPATH, "//copy-inv-types-choice//div[@class='checker']/parent::label[contains(.,'D/C')]"))
        ok_button = Button((By.XPATH, "//button[@data-dismiss='modal'][@ng-click='vm.confirm()']"))
        close_button = Button((By.XPATH, "//button[@data-dismiss='modal'][@ng-click='vm.cancel()']"))
        mbl_link = Link((By.XPATH, "//a[@ng-if='link.url']"))


class OEContainerTab:
    class MBL:
        add_button = Button((By.XPATH, "//button[@ng-click='vm.addContainer()']"))
        add_five_button = Button((By.XPATH, "//button[@ng-click='vm.addMultipleContainer(5)']"))
        add_multiple_button = Button((By.XPATH, "//hc-add-multiple-container-btn/button"))
        delete_button = Button((By.XPATH, "//button[@ng-click='vm.delContainer()']"))

        assign_container_area_element = Element((By.XPATH, "//div[contains(@class, 'assign_area')]"))
        assign_container_button = Button((By.XPATH, "//button[@id='btn-assign-container']"))
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
                self.index = index

                self.select_checkbox = Checkbox((By.XPATH, self.ROW_XPATH("//input[@type='checkbox']")))
                self.container_no_input = Input((By.XPATH, self.ROW_XPATH("//input[@name='container_no']")))
                self.more_button = Button((By.XPATH, self.ROW_XPATH("//a[@class='btn-expand show-open']")))
                self.tp_sz_select = Select((By.XPATH, self.ROW_XPATH("//select[@ng-model='ct.container_size']")))
                self.seal_no_input = Input((By.XPATH, self.ROW_XPATH("//input[@ng-model='ct.seal_no']")))
                self.pkg_input = Input((By.XPATH, self.ROW_XPATH("//input[@name='package']")))
                # self.weight_input = Input((By.XPATH, self.ROW_XPATH("//input[@name='weight']")))
                self.weight_kg_input = Input((By.XPATH, self.ROW_XPATH("//input[@ng-model='ct.weight_kg']")))
                self.weight_lb_input = Input((By.XPATH, self.ROW_XPATH("//input[@ng-model='ct.weight_lb']")))
                self.measurement_cbm_input = Input((By.XPATH, self.ROW_XPATH("//input[@ng-model='ct.measure_cbm']")))
                self.measurement_cft_input = Input((By.XPATH, self.ROW_XPATH("//input[@ng-model='ct.measure_cft']")))
                self.assign_all_checkbox = Checkbox((By.XPATH, self.ROW_ASSIGN_CONTAINER_XPAHT("//td[1]//input")))

                # more
                self.seal_no_2_input = Input((By.XPATH, self.ROW_ADV_XPATH("//input[@ng-model='ct.seal_no2']")))
                self.lfd_datepicker = Datepicker((By.XPATH, self.ROW_ADV_XPATH("//input[@ng-model='ct.last_free_date']")))
                self.gate_out_datepicker = Datepicker((By.XPATH, self.ROW_ADV_XPATH("//input[@name='gate_out_date']")))
                self.storage_start_date_datepicker = Datepicker((By.XPATH, self.ROW_ADV_XPATH("//input[@name='storage_start_date']")))
                self.empty_return_datepicker = Datepicker((By.XPATH, self.ROW_ADV_XPATH("//input[@ng-model='ct.empty_return_date']")))
                self.unit_select = Select((By.XPATH, self.ROW_ADV_XPATH("//select[@ng-model='ct.temperature_unit']")))
                self.dg_select = Select((By.XPATH, self.ROW_ADV_XPATH("//select[@ng-model='ct.is_dangerous']")))

                self.pick_no_input = Input((By.XPATH, self.ROW_ADV_XPATH("//input[@ng-model='ct.pickup_no']")))
                self.fdd_datepicker = Datepicker((By.XPATH, self.ROW_ADV_XPATH("//input[@ng-model='ct.free_detention_date']")))
                self.delivered_datepicker = Datepicker((By.XPATH, self.ROW_ADV_XPATH("//input[@ng-model='ct.delivery_date']")))
                self.storage_end_date_datepicker = Datepicker((By.XPATH, self.ROW_ADV_XPATH("//input[@name='storage_end_date']")))
                self.temp_input = Input((By.XPATH, self.ROW_ADV_XPATH("//input[@name='temperature']")))
                self.vent_select = Select((By.XPATH, self.ROW_ADV_XPATH("//select[@ng-model='ct.vent']")))
                self.handle_agent_autocomplete = Autocomplete((By.XPATH, self.ROW_ADV_XPATH("//*[@ng-model='ct.handle_agent']")), (By.XPATH, self.ROW_ADV_XPATH("//*[@ng-model='ct.handle_agent']//ng-dropdown-panel//input")))
                self.remark_input = Input((By.XPATH, self.ROW_ADV_XPATH("//*[@ng-model='ct.remark']")))

            def ROW_XPATH(self, xpath):
                return "//div[@id='mblForm']//tr[@id='expand_row_{0}']/preceding-sibling::tr[1]{1}".format(self.index - 1, xpath)
            def ROW_ADV_XPATH(self, xpath):
                return "//div[@id='mblForm']//tr[@id='expand_row_{0}']{1}".format(self.index - 1, xpath)
            def ROW_ASSIGN_CONTAINER_XPAHT(self, xpath):
                return "//div[contains(@class, 'assign_area')]//tr[contains(@ng-repeat, 'vm.container_list')][{0}]{1}".format(self.index, xpath)

            def assign_to_hbl_checkbox(self, hbl_index):
                xpath = self.ROW_ASSIGN_CONTAINER_XPAHT(f"//td[contains(@ng-repeat, 'vm.hbl_list')][{ hbl_index }]//input")
                return Checkbox((By.XPATH, xpath))

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
        new_commodity_button = Button((By.XPATH, "//button[@ng-click='vm.addHblItem(hbl)']"))


        class ContainerList:
            total_amount_source_radio_group = RadioGroup({
                'Container Total': (By.XPATH, "//input[@ng-value='vm.TOTAL_AMOUNT_SOURCE.CONTAINER']"),
                'Manual Input Total': (By.XPATH, "//input[@ng-value='vm.TOTAL_AMOUNT_SOURCE.MANUAL']"),
                'Receiving Total': (By.XPATH, "//input[@ng-value='vm.TOTAL_AMOUNT_SOURCE.RECEIVING']")
            })
            manual_input_total_pkg_input = Input((By.XPATH, "//input[@ng-model='hbl.total_package']"))
            manual_input_total_weight_input = Input((By.XPATH, "//input[@ng-model='hbl.total_weight_kg']"))
            manual_input_total_measurement_input = Input((By.XPATH, "//input[@ng-model='hbl.total_measure_cbm']"))

            class container:
                pass

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

    class UnassignConfirmPopup:
        ok_button = Button((By.XPATH, "//div[contains(@class, 'modal-dialog')]//button[@ng-click='ok()']"))
        cancel_button = Button((By.XPATH, "//div[contains(@class, 'modal-dialog')]//button[@ng-click='cancel()']"))

    class DeleteConfirmPopup:
        ok_button = Button((By.XPATH, "//div[contains(@class, 'modal-dialog')]//button[@ng-click='ok()']"))
        cancel_button = Button((By.XPATH, "//div[contains(@class, 'modal-dialog')]//button[@ng-click='cancel()']"))


class OEAccountingBillingBasedTab:
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

class OEAccountingInvoiceBasedTab:
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
