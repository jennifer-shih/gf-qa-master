from selenium.webdriver.common.by import By

from src.elements import *
from src.pages.base_components.accounting_billing_base_component import *
from src.pages.base_components.accounting_invoice_base_component import *


class AETab:
    basic_tab = Link((By.XPATH, "//a[@ng-bind='tab.name'][contains(.,'Basic')]"))
    accounting_tab = Link((By.XPATH, "//a[@ng-bind='tab.name'][contains(.,'Accounting')]"))
    doc_center_tab = Link((By.XPATH, "//a[@ng-bind='tab.name'][contains(.,'Doc Center')]"))
    status_tab = Link((By.XPATH, "//a[@ng-bind='tab.name'][contains(.,'Status')]"))


class AESidePanel:
    def hawb_select_button(index):
        xpath = f"//div[@id='hbl_side_{ index - 1 }'] | //div[contains(@class, 'hbl_sm')][contains(@class, 'ng-star-inserted')][{ index }]"
        return Button((By.XPATH, xpath))


class AEBasicTab:
    add_hawb_button = Button((By.XPATH, "//*[normalize-space(text())='+ Add HAWB']"))

    class MAWB:
        tools_button = Button((By.XPATH, "//div[@tool-items='vm.mblTools']"))
        expand_button = Button((By.XPATH, "//a[@ng-click='vm.toggleMblDisplayStatus();']"))
        file_no_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.filing_no']"))
        issuing_carrier_agent_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.ae_info.issue_carrier']"), (By.XPATH, "//*[@ng-model='vm.mbl.ae_info.issue_carrier']//input[@type='search']"))
        awb_type_select = Select((By.XPATH, "//select[contains(@ng-model,'vm.mbl.bl_type')]"))
        mawb_no_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.MBL_NO']"))
        mawb_no_invalid_mark_button = Button((By.XPATH, "//input[@ng-model='vm.mbl.MBL_NO']/../span"))
        mawb_no_invalid_message_label = Label((By.XPATH, "//div[contains(@class, 'qtip-content')]"))
        mawb_no_system_generate_button = Button((By.XPATH, "//button[@ng-click='vm.assignAwbNo()']"))
        mawb_auto_gen_button = Button((By.XPATH, "//button[@ng-click='vm.assignAwbNo()']"))
        mawb_auto_gen_confirm_label = Label((By.XPATH, "//div[contains(@class, 'modal-dialog')]//h4[@ng-bind-html='msg']"))
        mawb_auto_gen_confirm_button = Button((By.XPATH, "//button[@ng-click='ok()']"))
        awb_date_datepicker = Datepicker((By.XPATH, "//*[@ng-model='vm.mbl.ae_info.bl_date']"))
        itn_no_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ae_info.itn_no']"))
        shipper_shipping_agent_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.shipping_agent']"), (By.XPATH, "//*[@ng-model='vm.mbl.shipping_agent']//input[@type='search']"))
        consignee_oversea_agent_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.oversea_agent']"), (By.XPATH, "//*[@ng-model='vm.mbl.oversea_agent']//input[@type='search']"))
        notify_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.ae_info.notify']"), (By.XPATH, "//*[@ng-model='vm.mbl.ae_info.notify']//input[@type='search']"))
        # post_date_input = Input((By.NAME, "mbl_post_date"))
        office_autocomplete = Autocomplete((By.XPATH, '//hc-department-select/ng-select'), (By.XPATH, "//hc-department-select/ng-select//ng-dropdown-panel//input"))
        carrier_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.carrier']"), (By.XPATH, "//*[@ng-model='vm.mbl.carrier']//input[@type='search']"))
        co_loader_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.co_loader']"), (By.XPATH, "//*[@ng-model='vm.mbl.co_loader']//input[@type='search']"))

        # direct master
        direct_master_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.mbl.ae_info.is_direct']"))
        customer_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.ae_info.customer']"), (By.XPATH, "//*[@ng-model='vm.mbl.ae_info.customer']//ng-dropdown-panel//input"))
        bill_to_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.ae_info.bill_to']"), (By.XPATH, "//*[@ng-model='vm.mbl.ae_info.bill_to']//ng-dropdown-panel//input"))
        consignee_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.ae_info.consignee']"), (By.XPATH, "//*[@ng-model='vm.mbl.ae_info.consignee']//ng-dropdown-panel//input"))
        cargo_type_select = Select((By.XPATH, "//input[@ng-model='vm.mbl.ae_info.cargo_type']"))
        sales_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.sales_person']"), (By.XPATH, "//*[@ng-model='vm.mbl.sales_person']//ng-dropdown-panel//input"))

        departure_autocomplete = Autocomplete((By.XPATH, "//*[@model='vm.mbl.APOL']"), (By.XPATH, "//*[@model='vm.mbl.APOL']//input[@type='search']"))
        departure_date_time_datepicker = Datepicker((By.XPATH, "//*[@ng-model='vm.mbl.ETD']"))
        flight_no_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ae_info.flight_no']"))
        connecting_flight_button = Button((By.XPATH, "//button[@ng-click='vm.openConnectFlight()']"))
        destination_autocomplete = Autocomplete((By.XPATH, "//*[@model='vm.mbl.APOD']"), (By.XPATH, "//*[@model='vm.mbl.APOD']//input[@type='search']"))
        arrival_date_time_datepicker = Datepicker((By.XPATH, "//*[@ng-model='vm.mbl.ETA']"))
        dv_carriage_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ae_info.dv_carriage']"))
        dv_customs_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ae_info.dv_customs']"))
        insurance_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ae_info.insurance']"))
        carriers_spot_no_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ae_info.carrier_spot_no']"))
        wt_val_radio_group = RadioGroup({'PPD': (By.XPATH, "//input[@ng-model='vm.mbl.freight_term' and @value='P']"),
                                        'COLL': (By.XPATH, "//input[@ng-model='vm.mbl.freight_term' and @value='C']")})
        other_radio_group = RadioGroup({'PPD': (By.XPATH, "//input[@ng-model='vm.mbl.ae_info.other_charge_term' and @value='P']"),
                                        'COLL': (By.XPATH, "//input[@ng-model='vm.mbl.ae_info.other_charge_term' and @value='C']")})
        delivery_to_pier_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.ae_info.delivery_to']"), (By.XPATH, "//*[@ng-model='vm.mbl.ae_info.delivery_to']//input[@type='search']"))

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

        package_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ae_info.package']"))
        package_unit_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.package_unit']"), (By.XPATH, "//*[@ng-model='vm.mbl.package_unit']//input[@type='search']"))
        gross_weight_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ae_info.gross_weight']"))
        gross_weight_lb_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ae_info.gross_weight_lb']"))
        gross_weight_amount_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ae_info.gross_weight_amount']"))
        buying_rate_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ae_info.buying_rate']"))
        awb_gross_weight_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ae_info.bl_gross_weight']"))
        awb_gross_weight_lb_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ae_info.bl_gross_weight_lb']"))
        awb_gross_weight_amount_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ae_info.bl_gross_weight_amount']"))
        selling_rate_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ae_info.rate']"))
        chargeable_weight_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ae_info.chargeable_weight']"))
        chargeable_weight_lb_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ae_info.chargeable_weight_lb']"))
        chargeable_weight_amount_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ae_info.chargeable_weight_amount']"))
        volume_weight_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ae_info.volume_weight']"))
        volume_measure_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ae_info.volume_measure']"))
        awb_chargeable_weight_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ae_info.bl_chargeable_weight']"))
        awb_chargeable_weight_lb_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ae_info.bl_chargeable_weight_lb']"))
        awb_chargeable_weight_amount_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ae_info.bl_chargeable_weight_amount']"))
        set_dimensions_button = Button((By.XPATH, "//button[@ng-click=\"vm.openVolumeWeightCalculation('mbl')\"]"))
        sum_package_and_weight_button = Button((By.XPATH, "//button[contains(@ng-click, 'handleSumPackageAndWeightClick')]"))

        freight_select = Select((By.XPATH, "//select[contains(@ng-model,'vm.mbl.freight_term')]"))
        incoterms_select = Select((By.XPATH, "//select[contains(@ng-model,'vm.mbl.ae_info.incoterms')]"))
        service_term_from_select = Select((By.XPATH, "//select[contains(@ng-model,'vm.mbl.svc_term_from')]"))
        service_term_to_select = Select((By.XPATH, "//select[contains(@ng-model,'vm.mbl.svc_term_to')]"))
        business_referred_by_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.referral_by']"), (By.XPATH, "//*[@ng-model='vm.mbl.referral_by']//input[@type='search']"))
        more_button = Button((By.XPATH, "//*[@id='advance-mbl-btn']"))
        e_commerce_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.mbl.is_e_commerce']"))

        other_charge_add_button = Button((By.XPATH, "//*[@charge-list='vm.mbl.ae_info.other_charge_list']//button[@ng-click='vm.listAdd()']"))

        more_expand_button = Button((By.XPATH, "//a[@id='mblMoreInfoBtn']"))
        prepaid_valuation_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ae_info.valuation_p']"))
        prepaid_tax_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ae_info.tax_p']"))
        prepaid_currency_conversion_rates_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ae_info.currency_conversion_rate']"))
        collect_valuation_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ae_info.valuation_c']"))
        collect_tax_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ae_info.tax_c']"))
        collect_cc_charges_in_dest_currency_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ae_info.cc_charge_in_dest_currency']"))
        collect_charges_at_destination_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.ae_info.charge_at_destination']"))
        po_no_tag_input = TagInput((By.XPATH, "//tags-input[@ng-model='vm.mbl.ae_info.__po_num_list']//ul[@class='tag-list']"), (By.XPATH, "//tags-input[@ng-model='vm.mbl.ae_info.__po_num_list']//input[@ng-model='newTag.text']"))
        commodity_add_button = Button((By.XPATH, "//button[@ng-click=\"vm.addCommodity(vm.mbl.ae_info, 'mbl')\"]"))
        mark_input = Input((By.XPATH, "//textarea[@ng-model='vm.mbl.mark']"))
        nature_and_quantity_of_goods_input = Input((By.XPATH, "//textarea[@ng-model='vm.mbl.description']"))
        copy_po_button = Button((By.XPATH, "//button[@ng-click='vm.copyPONoToDescription(vm.mbl.ae_info, vm.mbl, mblForm)']"))
        copy_commodity_button = Button((By.XPATH, "//button[@ng-click='vm.copyCommodityToDescription(vm.mbl.ae_info, vm.mbl, mblForm)']"))
        copy_commodity_and_hts_button = Button((By.XPATH, "//button[@ng-click='vm.copyCommodityToDescription(vm.mbl.ae_info, vm.mbl, mblForm, { withHtsCode: true })']"))
        handling_information_input = Input((By.XPATH, "//textarea[@ng-model='vm.mbl.ae_info.handling_information']"))

        class Tools:
            delete_button = Button((By.XPATH, "//a[contains(., 'Delete')]"))
            copy_button = Button((By.XPATH, "//a[contains(., 'Copy') and not(contains(., 'Copy to AI'))]"))

        class OtherCharges:
            _instances = {}

            def __new__(cls, index=1):
                index = int(index)
                if index not in cls._instances:
                    cls._instances[index] = super().__new__(cls)
                return cls._instances[index]

            def __init__(self, index=1):
                index = int(index)
                def OC_XPATH(xpath):
                    return "//tr[@ng-repeat='charge in vm.chargeList'][{0}]{1}".format(index, xpath)

                self.carrier_agent_select = Select((By.XPATH, OC_XPATH("//select[@ng-model='charge.party_term']")))
                self.collect_prepaid_select = Select((By.XPATH, OC_XPATH("//select[@ng-model='charge.freight_term']")))
                self.charge_item_select = Select((By.XPATH, OC_XPATH("//select[@ng-model='charge.code']")))
                self.description_input = Input((By.XPATH, OC_XPATH("//input[@ng-model='charge.description']")))
                self.charge_amount_input = Input((By.XPATH, OC_XPATH("//input[@ng-model='charge.amount']")))

        class Commodity:
            _instances = {}

            def __new__(cls, index=1):
                index = int(index)
                if index not in cls._instances:
                    cls._instances[index] = super().__new__(cls)
                return cls._instances[index]

            def __init__(self, index=1):
                index = int(index)
                def ROW_XPATH(xpath):
                    return "//tr[@ng-repeat='item in vm.mbl.ae_info.__its'][{0}]{1}".format(index, xpath)

                self.commodity_description_input = Input((By.XPATH, ROW_XPATH("//input[@ng-model='item.description']")))
                self.hts_code_input = Input((By.XPATH, ROW_XPATH("//input[@ng-model='item.hts_code']")))
                self.po_no_tag_input = TagInput((By.XPATH, "//tags-input[@ng-model='item.__po_num_list']//ul[@class='tag-list']"), (By.XPATH, "//tags-input[@ng-model='item.__po_num_list']//input[@ng-model='newTag.text']"))

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
            self.booking_date_datepicker = Datepicker((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ae_info.booking_date']")))
            self.itn_no_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ae_info.itn_no']")))
            self.quotation_no_autocomplete = Autocomplete((By.XPATH, HAWB_XPATH("//*[@model='hbl.quotation']")), (By.XPATH, HAWB_XPATH("//*[@model='hbl.quotation']//input[@type='search']")))
            self.actual_shipper_autocomplete = Autocomplete((By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.shipper']")), (By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.shipper']//input[@type='search']")))
            self.customer_autocomplete = Autocomplete((By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.customer']")), (By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.customer']//input[@type='search']")))
            self.bill_to_autocomplete = Autocomplete((By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.bill_to']")), (By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.bill_to']//input[@type='search']")))
            self.consignee_autocomplete = Autocomplete((By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.consignee']")), (By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.consignee']//input[@type='search']")))
            self.notify_autocomplete = Autocomplete((By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.notify']")), (By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.notify']//input[@type='search']")))
            self.oversea_agent_autocomplete = Autocomplete((By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.ae_info.oversea_agent']")), (By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.ae_info.oversea_agent']//input[@type='search']")))
            self.issuing_carrier_agent_autocomplete = Autocomplete((By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.ae_info.issue_carrier']")), (By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.ae_info.issue_carrier']//input[@type='search']")))
            self.trucker_autocomplete = Autocomplete((By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.trucker']")), (By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.trucker']//input[@type='search']")))
            self.sales_autocomplete = Autocomplete((By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.sales_person']")), (By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.sales_person']//ng-dropdown-panel//input[@type='text']")))
            self.op_autocomplete = Autocomplete((By.XPATH, HAWB_XPATH("//hcoperatorselect")), (By.XPATH, HAWB_XPATH("//hcoperatorselect//ng-dropdown-panel//input")))
            self.sub_agent_awb_checkbox = Checkbox((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ae_info.is_sub_agent_bl']")))
            self.departure_input = Input((By.XPATH, HAWB_XPATH("//*[@ng-value='displayAirport(vm.mbl.APOL)']")))
            self.destination_input = Input((By.XPATH, HAWB_XPATH("//*[@ng-value='displayAirport(vm.mbl.APOD)']")))
            self.cargo_pickup_autocomplete = Autocomplete((By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.ae_info.cargo_pickup']")), (By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.ae_info.cargo_pickup']//input[@type='search']")))
            self.delivery_to_pier_autocomplete = Autocomplete((By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.ae_info.delivery_to']")), (By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.ae_info.delivery_to']//input[@type='search']")))
            self.cargo_type_select = Select((By.XPATH, HAWB_XPATH("//select[@ng-model='hbl.ae_info.cargo_type']")))
            self.sales_type_select = Select((By.XPATH, HAWB_XPATH("//select[@ng-model='hbl.sales_type']")))
            self.ship_type_select = Select((By.XPATH, HAWB_XPATH("//select[@ng-model='hbl.ship_type']")))
            self.dv_carriage_input = Input((By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.ae_info.dv_carriage']")))
            self.dv_customs_input = Input((By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.ae_info.dv_customs']")))
            self.insurance_input = Input((By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.ae_info.insurance']")))
            self.wt_val_radio_group = RadioGroup({'PPD': (By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.freight_term' and @value='P']")),
                                        'COLL': (By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.freight_term' and @value='C']"))})
            self.other_radio_group = RadioGroup({'PPD': (By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ae_info.other_charge_term' and @value='P']")),
                                        'COLL': (By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ae_info.other_charge_term' and @value='C']"))})

            self.package_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ae_info.package']")))
            self.package_unit_autocomplete = Autocomplete((By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.package_unit']")), (By.XPATH, HAWB_XPATH("//*[@ng-model='hbl.package_unit']//div[contains(@class, 'search')]//input")))
            self.gross_weight_shpr_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ae_info.shipper_gross_weight']")))
            self.gross_weight_shpr_lb_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ae_info.shipper_gross_weight_lb']")))
            self.gross_weight_shpr_amount_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ae_info.shipper_gross_weight_amount']")))
            self.buying_rate_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ae_info.buying_rate']")))
            self.buying_rate_unit_select = Select((By.XPATH, HAWB_XPATH("//select[@ng-model='hbl.ae_info.buying_rate_unit']")))
            self.gross_weight_cnee_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ae_info.consignee_gross_weight']")))
            self.gross_weight_cnee_lb_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ae_info.consignee_gross_weight_lb']")))
            self.gross_weight_cnee_amount_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ae_info.consignee_gross_weight_amount']")))
            self.selling_rate_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ae_info.selling_rate']")))
            self.selling_rate_unit_select = Select((By.XPATH, HAWB_XPATH("//select[@ng-model='hbl.ae_info.selling_rate_unit']")))
            self.chargeable_weight_shpr_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ae_info.shipper_chargeable_weight']")))
            self.chargeable_weight_shpr_lb_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ae_info.shipper_chargeable_weight_lb']")))
            self.chargeable_weight_shpr_amount_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ae_info.shipper_chargeable_weight_amount']")))
            self.volume_weight_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ae_info.volume_weight']")))
            self.volume_measure_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ae_info.volume_measure']")))
            self.chargeable_weight_cnee_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ae_info.consignee_chargeable_weight']")))
            self.chargeable_weight_cnee_lb_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ae_info.consignee_chargeable_weight_lb']")))
            self.chargeable_weight_cnee_amount_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ae_info.consignee_chargeable_weight_amount']")))
            self.set_dimensions_button = Button((By.XPATH, HAWB_XPATH("//button[@ng-click=\"vm.openVolumeWeightCalculation('hbl', hbl)\"]")))

            self.incoterms_select = Select((By.XPATH, HAWB_XPATH("//select[@ng-model='hbl.incoterms']")))
            self.service_term_from_select = Select((By.XPATH, HAWB_XPATH("//select[@ng-model='hbl.svc_term_from']")))
            self.service_term_to_select = Select((By.XPATH, HAWB_XPATH("//select[@ng-model='hbl.svc_term_to']")))

            self.display_unit_select = Select((By.XPATH, HAWB_XPATH("//select[@ng-model='hbl.display_unit']")))

            self.l_c_no_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.LC_NO']")))
            self.l_c_issue_bank_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ae_info.lc_issue_bank']")))
            self.l_c_issue_date_datepicker = Datepicker((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ae_info.lc_issue_date']")))
            self.customer_ref_no_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.customer_ref_no']")))
            self.agent_ref_no_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ae_info.agent_ref_no']")))
            self.export_ref_no_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ae_info.export_ref_no']")))
            self.rate_select = Select((By.XPATH, HAWB_XPATH("//select[@ng-model='hbl.ae_info.rate']")))
            self.more_button = Button((By.XPATH, HAWB_XPATH("//a[@ng-click='vm.toggleHblAdvanced($index)']")))
            self.e_commerce_checkbox = Checkbox((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.is_e_commerce']")))

            self.po_no_tag_input = TagInput((By.XPATH, HAWB_XPATH("//tags-input[@ng-model='hbl.__po_num_list']//ul[@class='tag-list']")), (By.XPATH, HAWB_XPATH("//tags-input[@ng-model='hbl.__po_num_list']//input[@ng-model='newTag.text']")))
            self.commodity_add_button = Button((By.XPATH, HAWB_XPATH("//button[@ng-click=\"vm.addCommodity(hbl, 'hbl')\"]")))
            self.mark_input = Input((By.XPATH, HAWB_XPATH("//textarea[@ng-model='hbl.mark']")))
            self.nature_and_quantity_of_goods_input = Input((By.XPATH, HAWB_XPATH("//textarea[@ng-model='hbl.description']")))
            self.copy_po_button = Button((By.XPATH, HAWB_XPATH("//button[@ng-click='vm.copyPONoToDescription(hbl, hbl, hbl.__form)']")))
            self.copy_commodity_button = Button((By.XPATH, HAWB_XPATH("//button[@ng-click='vm.copyCommodityToDescription(hbl, hbl, hbl.__form)']")))
            self.copy_commodity_and_hts_button = Button((By.XPATH, HAWB_XPATH("//button[@ng-click='vm.copyCommodityToDescription(hbl, hbl, hbl.__form, { withHtsCode: true })']")))
            self.manifest_nature_and_quantity_of_goods_input = Input((By.XPATH, HAWB_XPATH("//textarea[@ng-model='hbl.ae_info.manifest_description']")))
            self.handling_information_input = Input((By.XPATH, HAWB_XPATH("//textarea[@ng-model='hbl.ae_info.handling_information']")))

            self.other_charge_add_button = Button((By.XPATH, HAWB_XPATH("//*[@charge-list='hbl.other_charge_list']//button[@ng-click='vm.listAdd()']")))

            self.more_expand_button = Button((By.XPATH, HAWB_XPATH("//a[../../div[.='More'] and ../../div[contains(@class, 'tools')]]")))
            self.prepaid_valuation_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ae_info.valuation_p']")))
            self.prepaid_tax_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ae_info.tax_p']")))
            self.prepaid_currency_conversion_rates_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ae_info.currency_conversion_rate']")))
            self.collect_valuation_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ae_info.valuation_c']")))
            self.collect_tax_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ae_info.tax_c']")))
            self.collect_cc_charges_in_dest_currency_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ae_info.cc_charge_in_dest_currency']")))
            self.collect_charges_at_destination_input = Input((By.XPATH, HAWB_XPATH("//input[@ng-model='hbl.ae_info.charge_at_destination']")))

        class OtherCharges:
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
                def OC_XPATH(xpath):
                    return "//tr[@ng-repeat='charge in vm.chargeList'][{0}]{1}".format(index, xpath)

                self.carrier_agent_select = Select((By.XPATH, HAWB_XPATH(OC_XPATH("//select[@ng-model='charge.party_term']"))))
                self.collect_prepaid_select = Select((By.XPATH, HAWB_XPATH(OC_XPATH("//select[@ng-model='charge.freight_term']"))))
                self.charge_item_select = Select((By.XPATH, HAWB_XPATH(OC_XPATH("//select[@ng-model='charge.code']"))))
                self.description_input = Input((By.XPATH, HAWB_XPATH(OC_XPATH("//input[@ng-model='charge.description']"))))
                self.charge_amount_input = Input((By.XPATH, HAWB_XPATH(OC_XPATH("//input[@ng-model='charge.amount']"))))

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

class AEAccountingBillingBasedTab:
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


class AEAccountingInvoiceBasedTab:
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
