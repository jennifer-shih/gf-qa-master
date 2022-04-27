from selenium.webdriver.common.by import By

from src.elements import *
from src.pages.base_components.accounting_billing_base_component import *
from src.pages.base_components.accounting_invoice_base_component import *


class AITab:
    basic_tab = Link((By.XPATH, "//a[@ng-bind='tab.name'][contains(.,'Basic')]"))
    accounting_tab = Link((By.XPATH, "//a[@ng-bind='tab.name'][contains(.,'Accounting')]"))
    doc_center_tab = Link((By.XPATH, "//a[@ng-bind='tab.name'][contains(.,'Doc Center')]"))
    status_tab = Link((By.XPATH, "//a[@ng-bind='tab.name'][contains(.,'Status')]"))


class AISidePanel:
    def hawb_select_button(index):
        xpath = f"//div[@id='hbl_side_{ index - 1 }'] | //div[contains(@class, 'hbl_sm')][contains(@class, 'ng-star-inserted')][{ index }]"
        return Button((By.XPATH, xpath))


class AIBasicTab:
    add_hawb_button = Button((By.XPATH, "//button[normalize-space(text())='+ Add HAWB']"))

    class MAWB:
        expand_button = Button((By.XPATH, "//a[@ng-click='vm.toggleMblDisplayStatus();']"))
        file_no_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.filing_no']"))
        mawb_no_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.MBL_NO']"))
        office_autocomplete = Autocomplete((By.XPATH, '//*[@id="mblForm"]/div[2]/div/div[1]/div[3]/div/hc-department-select/ng-select'), (By.XPATH, "(//div[@class='search-container select2-search'])[1]/input"))
        awb_type_select = Select((By.XPATH, "//select[contains(@ng-model,'vm.mbl.bl_type')]"))
        post_date_input = Input((By.NAME, "post_date"))
        oversea_agent_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.oversea_agent']"), (By.XPATH, "//*[@ng-model='vm.mbl.oversea_agent']//input[@type='search']"))
        carrier_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.carrier']"), (By.XPATH, "//*[@ng-model='vm.mbl.carrier']//input[@type='search']"))
        co_loader_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.co_loader']"), (By.XPATH, "//*[@ng-model='vm.mbl.co_loader']//input[@type='search']"))
        direct_master_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.mbl.ai_info.is_direct']"))

        # direct master
        shipper_autocomplete = Autocomplete((By.XPATH, "//*[@name='mbl_shipper']"), (By.XPATH, "//*[@name='mbl_shipper']//ng-dropdown-panel//input"))
        consignee_autocomplete = Autocomplete((By.XPATH, "//*[@name='mbl_consignee']"), (By.XPATH, "//*[@name='mbl_consignee']//ng-dropdown-panel//input"))
        notify_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.ai_info.notify']"), (By.XPATH, "//*[@ng-model='vm.mbl.ai_info.notify']//input[@type='search']"))
        customer_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.ai_info.customer']"), (By.XPATH, "//*[@ng-model='vm.mbl.ai_info.customer']//input[@type='search']"))
        bill_to_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.ai_info.bill_to']"), (By.XPATH, "//*[@ng-model='vm.mbl.ai_info.bill_to']//input[@type='search']"))
        sales_autocomplete = Autocomplete((By.XPATH, "//*[@name='mbl_sales']"), (By.XPATH, "//*[@name='mbl_sales']//ng-dropdown-panel//input"))

        departure_autocomplete = Autocomplete((By.XPATH, "//*[@model='vm.mbl.APOL']"), (By.XPATH, "//*[@model='vm.mbl.APOL']//input[@type='search']"))
        departure_date_time_datepicker = Datepicker((By.XPATH, "//*[@ng-model='vm.mbl.ETD']"))
        flight_no_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ai_info.flight_no']"))
        destination_autocomplete = Autocomplete((By.XPATH, "//*[@model='vm.mbl.APOD']"), (By.XPATH, "//*[@model='vm.mbl.APOD']//input[@type='search']"))
        arrival_date_time_datepicker = Datepicker((By.XPATH, "//*[@ng-model='vm.mbl.ETA']"))
        freight_location_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.ai_info.freight_location']"), (By.XPATH, "//*[@ng-model='vm.mbl.ai_info.freight_location']//input[@type='search']"))
        storage_start_date_datepicker = Datepicker((By.XPATH, "//*[@ng-model='vm.mbl.ai_info.storage_start_date']"))
        connecting_flight_button = Button((By.XPATH, "//button[@ng-click='vm.openConnectFlight()']"))

        route_departure_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='mblData.APOL']"), (By.XPATH, "//*[@ng-model='mblData.APOL']//input[@type='search']"))
        route_departure_departure_date_time_datepicker = Datepicker((By.XPATH, "//input[@ng-model='mblData.ETD']"))
        route_trans_1_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='mblInfoData.trans_port1']"), (By.XPATH, "//*[@ng-model='mblInfoData.trans_port1']//input[@type='search']"))
        route_trans_1_arrival_date_time_datepicker = Datepicker((By.NAME, "ETA_trans1"))
        route_trans_1_departure_date_time_datepicker = Datepicker((By.NAME, "ETD_trans1"))
        route_trans_1_flight_no_input = Input((By.NAME, "flight_no_trans1"))
        route_trans_1_carrier_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='mblInfoData.carrier_trans1']"), (By.XPATH, "(//input[@type='search'])[last()]"))
        route_trans_2_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='mblInfoData.trans_port2']"), (By.XPATH, "//*[@ng-model='mblInfoData.trans_port2']//input[@type='search']"))
        route_trans_2_arrival_date_time_datepicker = Datepicker((By.NAME, "ETA_trans2"))
        route_trans_2_departure_date_time_datepicker = Datepicker((By.NAME, "ETD_trans2"))
        route_trans_2_flight_no_input = Input((By.NAME, "flight_no_trans2"))
        route_trans_2_carrier_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='mblInfoData.carrier_trans2']"), (By.XPATH, "(//input[@type='search'])[last()]"))
        route_trans_3_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='mblInfoData.trans_port3']"), (By.XPATH, "//*[@ng-model='mblInfoData.trans_port3']//input[@type='search']"))
        route_trans_3_arrival_date_time_datepicker = Datepicker((By.NAME, "ETA_trans3"))
        route_trans_3_departure_date_time_datepicker = Datepicker((By.NAME, "ETD_trans3"))
        route_trans_3_flight_no_input = Input((By.NAME, "flight_no_trans3"))
        route_trans_3_carrier_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='mblInfoData.carrier_trans3']"), (By.XPATH, "(//input[@type='search'])[last()]"))
        route_final_destination_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='mblData.APOD']"), (By.XPATH, "//*[@ng-model='mblData.APOD']//input[@type='search']"))
        route_final_destination_arrival_date_time_datepicker = Datepicker((By.XPATH, "//input[@ng-model='mblData.ETA']"))
        route_save_button = Button((By.XPATH, "//button[@ng-click='ok()']"))
        route_cancel_button = Button((By.XPATH, "//button[@ng-click='cancel()']"))

        sum_package_and_weight_button = Button((By.XPATH, "//button[contains(@ng-click, 'handleSumPackageAndWeightClick')]"))
        package_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ai_info.package']"))
        package_unit_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.package_unit']"), (By.XPATH, "//*[@ng-model='vm.mbl.package_unit']//input[@type='search']"))
        gross_weight_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ai_info.gross_weight']"))
        gross_weight_lb_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ai_info.gross_weight_lb']"))
        chargeable_weight_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ai_info.chargeable_weight']"))
        chargeable_weight_lb_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ai_info.chargeable_weight_lb']"))
        set_dimensions_button = Button((By.XPATH, "//a[.='Set Dimensions']"))
        volume_weight_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ai_info.volume_weight']"))
        volume_measure_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ai_info.volume_measure']"))

        freight_select = Select((By.XPATH, "//select[contains(@ng-model,'vm.mbl.freight_term')]"))
        incoterms_select = Select((By.XPATH, "//select[contains(@ng-model,'vm.mbl.ai_info.incoterms')]"))
        service_term_from_select = Select((By.XPATH, "//select[contains(@ng-model,'vm.mbl.svc_term_from')]"))
        service_term_to_select = Select((By.XPATH, "//select[contains(@ng-model,'vm.mbl.svc_term_to')]"))
        business_referred_by_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.referral_by']"), (By.XPATH, "//*[@ng-model='vm.mbl.referral_by']//input[@type='search']"))
        more_button = Button((By.XPATH, "//*[@id='advance-mbl-btn']"))
        e_commerce_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.mbl.is_e_commerce']"))

    class HAWB:
        _instances = {}

        def __new__(cls, index=1):
            index = int(index)
            if index not in cls._instances:
                cls._instances[index] = super().__new__(cls)
            return cls._instances[index]

        def __init__(self, index=1):
            index = int(index)
            def HAWB_XPATH(xpath):
                return "//div[@id='hbl_{0}']{1}".format(index-1, xpath)

            self.hbl_side_panel_button = Button((By.XPATH, "//div[@id='hbl_side_{0}']".format(index-1)))
            self.tools_button = Button((By.XPATH, HAWB_XPATH("//div[@tool-btn='tools']")))
            self.tools_copy_to_button = Button((By.XPATH, HAWB_XPATH("//a[contains(.,'Copy To')]")))

            self.hawb_no_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.HBL_NO']")))
            self.hsn_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ai_info.hsn']")))
            self.quotation_no_autocomplete = Autocomplete((By.XPATH, HAWB_XPATH("//*[@model='hbl.quotation']")), (By.XPATH, HAWB_XPATH("//*[@model='hbl.quotation']//input[@type='search']")))
            self.shipper_autocomplete = Autocomplete((By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.shipper']")), (By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.shipper']//input[@type='search']")))
            self.consignee_autocomplete = Autocomplete((By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.consignee']")), (By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.consignee']//input[@type='search']")))
            self.notify_autocomplete = Autocomplete((By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.notify']")), (By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.notify']//input[@type='search']")))
            self.customer_autocomplete = Autocomplete((By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.customer']")), (By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.customer']//input[@type='search']")))
            self.bill_to_autocomplete = Autocomplete((By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.bill_to']")), (By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.bill_to']//input[@type='search']")))
            self.customs_broker_autocomplete = Autocomplete((By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.customs_broker']")), (By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.customs_broker']//input[@type='search']")))
            self.sales_autocomplete = Autocomplete((By.XPATH, HAWB_XPATH("//hcsalesselect")), (By.XPATH, HAWB_XPATH("//hcsalesselect//ng-dropdown-panel//input")))
            self.op_autocomplete = Autocomplete((By.XPATH, HAWB_XPATH("//hcoperatorselect")), (By.XPATH, HAWB_XPATH("//hcoperatorselect//ng-dropdown-panel//input")))

            self.freight_location_autocomplete = Autocomplete((By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.ai_info.freight_location']")), (By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.ai_info.freight_location']//input[@type='search']")))
            self.final_destination_autocomplete = Autocomplete((By.XPATH, HAWB_XPATH("//*[@model='hbl.FDEST']")), (By.XPATH, HAWB_XPATH("//*[@model='hbl.FDEST']//input[@type='search']")))
            self.final_eta_datepicker = Datepicker((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.FETA']")))
            self.delivery_location_autocomplete = Autocomplete((By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.delivery_location']")), (By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.delivery_location']//input[@type='search']")))
            self.trucker_autocomplete = Autocomplete((By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.trucker']")), (By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.trucker']//input[@type='search']")))
            self.last_free_day_datepicker = Datepicker((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.last_free_date']")))
            self.storage_start_date_datepicker = Datepicker((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ai_info.storage_start_date']")))
            self.freight_select = Select((By.XPATH, HAWB_XPATH("//select[@ng-model='hbl.freight_term']")))
            self.sales_type_select = Select((By.XPATH, HAWB_XPATH("//select[@ng-model='hbl.sales_type']")))

            self.package_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ai_info.package']")))
            self.package_unit_autocomplete = Autocomplete((By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.package_unit']")), (By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.package_unit']//div[contains(@class, 'search')]//input")))
            self.gross_weight_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ai_info.gross_weight']")))
            self.gross_weight_lb_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ai_info.gross_weight_lb']")))
            self.chargeable_weight_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ai_info.chargeable_weight']")))
            self.chargeable_weight_lb_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ai_info.chargeable_weight_lb']")))
            self.set_dimensions_button = Button((By.XPATH, HAWB_XPATH("//a[.='Set Dimensions']")))
            self.volume_weight_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ai_info.volume_weight']")))
            self.volume_measure_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ai_info.volume_measure']")))

            self.it_no_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.it_no']")))
            self.class_of_entry_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ai_info.it_class_no']")))
            self.it_date_datepicker = Datepicker((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.it_date']")))
            self.it_issued_location_autocomplete = Autocomplete((By.XPATH, HAWB_XPATH("//*[@model='hbl.it_issue_location']")), (By.XPATH, HAWB_XPATH("//*[@model='hbl.it_issue_location']//input[@type='search']")))
            self.cargo_released_to_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ai_info.cargo_release_to']")))
            self.c_released_date_datepicker = Datepicker((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ai_info.customs_release_date']")))
            self.door_delivered_datepicker = Datepicker((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ai_info.door_delivered']")))
            self.ship_type_select = Select((By.XPATH, HAWB_XPATH("//select[@ng-model='hbl.ship_type']")))
            self.incoterms_select = Select((By.XPATH, HAWB_XPATH("//select[@ng-model='hbl.incoterms']")))
            self.service_term_from_select = Select((By.XPATH, HAWB_XPATH("//select[@ng-model='hbl.svc_term_from']")))
            self.service_term_to_select = Select((By.XPATH, HAWB_XPATH("//select[@ng-model='hbl.svc_term_to']")))

            self.more_button = Button((By.XPATH, HAWB_XPATH("//a[@ng-click='vm.toggleHblAdvanced($index)']")))
            self.e_commerce_checkbox = Checkbox((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.is_e_commerce']")))

            self.display_unit_select = Select((By.XPATH, HAWB_XPATH("//select[@ng-model='hbl.display_unit']")))

            self.sub_hawb_add_button = Button((By.XPATH, HAWB_XPATH("//button[@ng-click='vm.addSubHawb(hbl)']")))
            self.customer_reference___po_no_tag_input = TagInput((By.XPATH, HAWB_XPATH("//tags-input[@ng-model='hbl.__po_num_list']//ul[@class='tag-list']")), (By.XPATH, HAWB_XPATH("//tags-input[@ng-model='hbl.__po_num_list']//input[@ng-model='newTag.text']")))
            self.commodity_add_button = Button((By.XPATH, HAWB_XPATH("//button[@ng-click=\"vm.addCommodity(hbl, 'hbl')\"]")))
            self.load_from_warehouse_button = Button((By.XPATH, HAWB_XPATH("//button[@ng-click='vm.openWarehouseLoader()']")))
            self.mark_input = Input((By.XPATH, HAWB_XPATH("//textarea[@ng-model='hbl.mark']")))
            self.description_input = Input((By.XPATH, HAWB_XPATH("//textarea[@ng-model='hbl.description']")))
            self.copy_po_button = Button((By.XPATH, HAWB_XPATH("//button[@ng-click='vm.copyPONoToDescription(hbl, hbl, hbl.__form)']")))
            self.copy_commodity_button = Button((By.XPATH, HAWB_XPATH("//button[@ng-click='vm.copyCommodityToDescription(hbl, hbl, hbl.__form)']")))
            self.copy_commodity_and_hts_button = Button((By.XPATH, HAWB_XPATH("//button[@ng-click='vm.copyCommodityToDescription(hbl, hbl, hbl.__form, { withHtsCode: true })']")))
            self.remark_input = Input((By.XPATH, HAWB_XPATH("//textarea[@ng-model='hbl.remark']")))

        @staticmethod
        def get_len():
            return Driver.num_of_element("//div[contains(@ng-repeat, 'hbl in vm.hblList')]")

        class Sub_HAWB:
            _rows = {}

            def __new__(cls, hbl_index=1, index=1):
                hbl_index = int(hbl_index)
                index = int(index)
                if hbl_index not in cls._rows:
                    cls._rows[hbl_index] = {}
                if index not in cls._rows[hbl_index]:
                    cls._rows[hbl_index][index] = super().__new__(cls)
                return cls._rows[hbl_index][index]

            def __init__(self, hbl_index=1, index=1):
                hbl_index = int(hbl_index)
                index = int(index)
                def HAWB_XPATH(xpath):
                    return "//div[@id='hbl_{0}']{1}".format(hbl_index-1, xpath)
                def ROW_XPATH(xpath):
                    return "//tr[@ng-repeat='subhawb in hbl.__subhawb'][{0}]{1}".format(index, xpath)
                self.sub_hawb_input = Input((By.XPATH, HAWB_XPATH(ROW_XPATH("//input[@ng-model='subhawb.sub_hawb']"))))
                self.description___it_no_input = Input((By.XPATH, HAWB_XPATH(ROW_XPATH("//input[@ng-model='subhawb.description']"))))
                self.pcs_input = Input((By.XPATH, HAWB_XPATH(ROW_XPATH("//input[@ng-model='subhawb.pcs']"))))
                self.pkg_unit_autocomplete = Autocomplete((By.XPATH, HAWB_XPATH("//*[@ng-model='subhawb.package_unit']/..")), (By.XPATH, HAWB_XPATH("//*[@ng-model='subhawb.package_unit']//div[contains(@class, 'search')]//input")))
                self.amount_input = Input((By.XPATH, HAWB_XPATH(ROW_XPATH("//input[@ng-model='subhawb.amount']"))))

        class Commodity:
            _rows = {}

            def __new__(cls, hbl_index=1, index=1):
                hbl_index = int(hbl_index)
                index = int(index)
                if hbl_index not in cls._rows:
                    cls._rows[hbl_index] = {}
                if index not in cls._rows[hbl_index]:
                    cls._rows[hbl_index][index] = super().__new__(cls)
                return cls._rows[hbl_index][index]

            def __init__(self, hbl_index=1, index=1):
                hbl_index = int(hbl_index)
                index = int(index)
                def HAWB_XPATH(xpath):
                    return "//div[@id='hbl_{0}']{1}".format(hbl_index-1, xpath)
                def ROW_XPATH(xpath):
                    return "//tr[@ng-repeat='item in hbl.__its'][{0}]{1}".format(index, xpath)

                self.commodity_description_input = Input((By.XPATH, HAWB_XPATH(ROW_XPATH("//input[@ng-model='item.description']"))))
                self.hts_code_input = Input((By.XPATH, HAWB_XPATH(ROW_XPATH("//input[@ng-model='item.hts_code']"))))
                self.po_no_tag_input = TagInput((By.XPATH, HAWB_XPATH("//tags-input[@ng-model='item.__po_num_list']//ul[@class='tag-list']")), (By.XPATH, HAWB_XPATH("//tags-input[@ng-model='item.__po_num_list']//input[@ng-model='newTag.text']")))

    class Dimension:
        _rows = {}
        dimension_add_button = Button((By.XPATH, "//button[@ng-click='vm.addItem()']"))
        dimension_length_unit_radio_group = RadioGroup(
            {"CM": (By.XPATH, "//input[@value='CM']"),
            "Inch": (By.XPATH, '//input[@value="IN"]'),
            "Feet": (By.XPATH, "//input[@value='FEET']")}
        )
        dimension_pcs_sum_label = Label((By.XPATH, "//td[contains(@ng-bind,'vm.calcPCSSum(vm.data.items)')]"))
        dimension_kgs_sum_label = Label((By.XPATH, "//td[contains(@ng-bind,'vm.calcKGSSum(vm.data.items)')]"))
        dimension_lbs_sum_label = Label((By.XPATH, "//td[contains(@ng-bind,'vm.calcLBSSum(vm.data.items)')]"))
        dimension_cbm_sum_label = Label((By.XPATH, "//td[contains(@ng-bind,'vm.calcCBMSum(vm.data.items)')]"))
        dimension_cft_sum_label = Label((By.XPATH, "//td[contains(@ng-bind,'vm.calcCFTSum(vm.data.items)')]"))
        dimension_apply_button = Button((By.XPATH, "//button[contains(.,'Apply')]"))
        dimension_cancel_button = Button((By.XPATH, "//button[contains(.,'Cancel')]"))

        def __new__(cls, index=1):
            index = int(index)
            if index not in cls._rows:
                cls._rows[index] = super().__new__(cls)
            return cls._rows[index]

        def __init__(self, index=1):
            index = int(index)
            def ROW_XPATH(xpath):
                return "//tr[@ng-repeat='item in vm.data.items'][{0}]{1}".format(index, xpath)

            self.length_input = Input((By.XPATH, ROW_XPATH("//input[@ng-model='item.length']")))
            self.width_input = Input((By.XPATH, ROW_XPATH("//input[@ng-model='item.width']")))
            self.height_input = Input((By.XPATH, ROW_XPATH("//input[@ng-model='item.height']")))
            self.pcs_input = Input((By.XPATH, ROW_XPATH("//input[@ng-model='item.pcs']")))
            self.kgs_label = Label((By.XPATH, ROW_XPATH("//td[contains(@ng-bind,'vm.calcKGS(item)')]")))
            self.lbs_label = Label((By.XPATH, ROW_XPATH("//td[contains(@ng-bind,'vm.calcLBS(item)')]")))
            self.cbm_label = Label((By.XPATH, ROW_XPATH("//td[contains(@ng-bind,'vm.calcCBM(item)')]")))
            self.cft_label = Label((By.XPATH, ROW_XPATH("//td[contains(@ng-bind,'vm.calcCFT(item)')]")))

    class CopyHBLToMBL:
        select_mbl_autocomplete = Autocomplete((By.XPATH, "//hc-mbl-select[@ng-model='vm.selectedMbl']"), (By.XPATH, "//hc-mbl-select[@ng-model='vm.selectedMbl']//ng-dropdown-panel//input"))
        copy_accouting_info_checkbox = Checkbox((By.XPATH, "//div[@class='checker']/span/input[@name='acct'][@type='checkbox']"))
        a_p_checkbox = Checkbox((By.XPATH, "//copy-inv-types-choice//div[@class='checker']/parent::label[contains(.,'A/P')]"))
        a_r_checkbox = Checkbox((By.XPATH, "//copy-inv-types-choice//div[@class='checker']/parent::label[contains(.,'A/R')]"))
        d_c_checkbox = Checkbox((By.XPATH, "//copy-inv-types-choice//div[@class='checker']/parent::label[contains(.,'D/C')]"))
        ok_button = Button((By.XPATH, "//button[@data-dismiss='modal'][@ng-click='vm.confirm()']"))
        close_button = Button((By.XPATH, "//button[@data-dismiss='modal'][@ng-click='vm.cancel()']"))
        mbl_link = Link((By.XPATH, "//a[@ng-if='link.url']"))

class AIAccountingBillingBasedTab:
    save_button = Button((By.XPATH, "//button[@type='submit'][contains(@class,'btn green')]"))

    class Common:
        class copy_to_dropdown:
            MAWB_revenue_checkbox = Checkbox((By.XPATH, "(//div[@ngbdropdownmenu]//div[contains(., 'MAWB')]//input[@binduniform][@type='checkbox'])[7]"))
            MAWB_cost_checkbox = Checkbox((By.XPATH, "(//div[@ngbdropdownmenu]//div[contains(., 'MAWB')]//input[@binduniform][@type='checkbox'])[8]"))
            HAWB_revenue_checkbox = Checkbox((By.XPATH, "(//div[@ngbdropdownmenu]//div[contains(., 'HAWB')]//input[@binduniform][@type='checkbox'])[7]"))
            HAWB_cost_checkbox = Checkbox((By.XPATH, "(//div[@ngbdropdownmenu]//div[contains(., 'HAWB')]//input[@binduniform][@type='checkbox'])[8]"))
            copy_button = Button((By.XPATH, "//body/div[@class='dropdown']//div[contains(@class, 'dropdown-checkboxes-block')][4]//button"))

    class MAWB:
        tool_button = Button((By.XPATH, "//*[contains(@class, 'mbl_board')]//hctools"))

        class revenue(BaseAccountingBillingBasedMBLRevenue):
            pass

        class cost(BaseAccountingBillingBasedMBLCost):
            pass

        class MAWBAmount(BaseMAWBAmount):
            pass

        class ShipmentProfit(BaseMBLShipmentProfit):
            pass

        class Memo:
            memo_title_button = Button((By.XPATH, "//hcmemo[@type='mbl']//div[contains(text(), 'Memo')]"))

    class HAWB:
        tool_button = Button((By.XPATH, "//*[contains(@class, 'hbl_board')]//hctools"))

        class revenue(BaseAccountingBillingBasedHBLRevenue):
            pass

        class cost(BaseAccountingBillingBasedHBLCost):
            pass

        class HAWBAmount(BaseHAWBAmount):
            pass

        class ShipmentProfit(BaseHBLShipmentProfit):
            pass

        class Memo:
            memo_title_button = Button((By.XPATH, "//hcmemo[@type='hbl']//div[contains(text(), 'Memo')]"))

class AIAccountingInvoiceBasedTab:
    class MAWB:
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

    class HAWB:
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
        hawb_profit_amount_label = Label((By.XPATH, "//div[contains(@class, 'hbl_board')]//table[@ng-if='vm.invoiceProfit']//td[2]"))
        hawb_profit_profit_percentage_label = Label((By.XPATH, "//div[contains(@class, 'hbl_board')]//table[@ng-if='vm.invoiceProfit']//td[3]"))
        hawb_profit_profit_margin_label = Label((By.XPATH, "//div[contains(@class, 'hbl_board')]//table[@ng-if='vm.invoiceProfit']//td[4]"))
