from selenium.webdriver.common.by import By

from src.elements import *
from src.pages.base_components.accounting_billing_base_component import *
from src.pages.base_components.accounting_invoice_base_component import *


class OEVSSidePanel:
    booking_button = Button((By.XPATH, "//a[normalize-space(text())='Booking']"))
    hb_l_button = Button((By.XPATH, "//a[normalize-space(text())='HB/L']"))

    def booking_select_button(index):
        return Button((By.XPATH, f"//div[@id='hbl_side_{ index - 1 }'] | //div[contains(@class, 'hbl_sm')][contains(@class, 'ng-star-inserted')][{ index }]"))

    def hbl_select_button(index):
        return Button((By.XPATH, f"//div[@class='hbl_sm_area']//div[contains(@class, 'hbl_sm')][not(contains(@class, 'ng-hide'))][{ index }] | //div[contains(@class, 'hbl_sm')][contains(@class, 'ng-star-inserted')][not(@hidden)][{ index }]"))

class OEVSBasicTab:
    add_booking_button = Button((By.XPATH, "//button[@id='add_hbl']"))

    class VS:
        vessel_schedule_no_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.data.reference_no']"))
        office_autocomplete = Autocomplete((By.XPATH, '//hc-department-select[contains(.,vm.mbl.data.office)]/ng-select'), (By.XPATH, "//hc-department-select[contains(.,vm.mbl.data.office)]//ng-dropdown-panel//input"))
        b_l_type_select = Select((By.XPATH, "//select[contains(@ng-model,'vm.mbl.data.bl_type')]"))
        post_date_input = Input((By.XPATH, "//input[@name='post_date']"))
        carrier_bkg_no_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.data.oe_info.carrier_bkg_no']"))
        itn_no_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.data.oe_info.itn_no']"))
        carrier_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.data.carrier']"), (By.XPATH, "//*[@ng-model='vm.mbl.data.carrier']//ng-dropdown-panel//input"))
        b_l_acct_carrier_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.data.oe_info.bl_acct_carrier']"), (By.XPATH, "//*[@ng-model='vm.mbl.data.oe_info.bl_acct_carrier']//ng-dropdown-panel//input"))
        shipping_agent_autocomplete = Autocomplete((By.XPATH, "//hc-tp-select[@ng-model='vm.mbl.data.shipping_agent']"), (By.XPATH, "//hc-tp-select[@ng-model='vm.mbl.data.shipping_agent']//ng-dropdown-panel//input"))
        oversea_agent_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.data.oversea_agent']"), (By.XPATH, "//*[@ng-model='vm.mbl.data.oversea_agent']//ng-dropdown-panel//input"))
        notify_autocomplete = Autocomplete((By.XPATH, "//hc-tp-select[@name='notify']"), (By.XPATH, "//hc-tp-select[@name='notify']//ng-dropdown-panel//input"))
        forwarding_agent_autocomplete = Autocomplete((By.XPATH, "//hc-tp-select[@ng-model='vm.mbl.data.oe_info.forwarding_agent']"), (By.XPATH, "//hc-tp-select[@ng-model='vm.mbl.data.oe_info.forwarding_agent']//ng-dropdown-panel//input"))
        co_loader_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.data.co_loader']"), (By.XPATH, "//*[@ng-model='vm.mbl.data.co_loader']//ng-dropdown-panel//input"))
        op_autocomplete = Autocomplete((By.XPATH, "//hc-operator-select[@name='mbl_operator']"), (By.XPATH, "//hc-operator-select[@name='mbl_operator']//ng-dropdown-panel//input"))

        multiple_pol_pod_checkbox = Checkbox((By.XPATH, "//label[@on-click='vm.onClickEnableMultiPolPod()']//input"), click_locator=(By.XPATH, "//label[@on-click='vm.onClickEnableMultiPolPod()']//span"))
        vessel_autocomplete = Autocomplete((By.XPATH, "//*[@model='vm.mbl.data.vessel_name']"), (By.XPATH, "//*[@model='vm.mbl.data.vessel_name']//div[@class='search-container select2-search']/input"))
        voyage_input = Input((By.XPATH, "//input[@ng-model='vm.mbl.data.voyage']"))
        delivery_to_pier_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.data.oe_info.delivery_to']"), (By.XPATH, "//*[@ng-model='vm.mbl.data.oe_info.delivery_to']//ng-dropdown-panel//input"))
        empty_pickup_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.mbl.data.oe_info.empty_pickup']"), (By.XPATH, "//*[@ng-model='vm.mbl.data.oe_info.empty_pickup']//ng-dropdown-panel//input"))
        port_of_loading_autocomplete = Autocomplete((By.XPATH, "//*[@model='vm.mbl.data.POL']"), (By.XPATH, "//*[@model='vm.mbl.data.POL']//input[@type='search']"))
        etd_datepicker = Datepicker((By.XPATH, "//input[@ng-model='vm.mbl.data.ETD']"))
        place_of_receipt_autocomplete = Autocomplete((By.XPATH, "//*[@model='vm.mbl.data.POR']"), (By.XPATH, "//*[@model='vm.mbl.data.POR']//input[@type='search']"))
        place_of_receipt_etd_datepicker = Datepicker((By.XPATH, "//input[@ng-model='vm.mbl.data.POR_ETD']"))
        port_of_discharge_autocomplete = Autocomplete((By.XPATH, "//*[@model='vm.mbl.data.POD']"), (By.XPATH, "//*[@model='vm.mbl.data.POD']//input[@type='search']"))
        eta_datepicker = Datepicker((By.XPATH, "//input[@ng-model='vm.mbl.data.ETA']"))
        place_of_delivery_autocomplete = Autocomplete((By.XPATH, "//*[@model='vm.mbl.data.DEL']"), (By.XPATH, "//*[@model='vm.mbl.data.DEL']//input[@type='search']"))
        place_of_delivery_etd_datepicker = Datepicker((By.XPATH, "//input[@ng-model='vm.mbl.data.DETA']"))
        freight_select = Select((By.XPATH, "//*[@ng-model='vm.mbl.data.freight_term']"))
        ship_mode_select = Select((By.XPATH, "//*[@ng-model='vm.mbl.data.ship_mode']"))
        svc_term_from_select = Select((By.XPATH, "//*[@ng-model='vm.mbl.data.svc_term_from']"))
        svc_term_to_select = Select((By.XPATH, "//*[@ng-model='vm.mbl.data.svc_term_to']"))
        ov_l_type_select = Select((By.XPATH, "//*[@ng-model='vm.mbl.data.oe_info.obl_type']"))
        doc_cut_off_date_datepicker = Datepicker((By.XPATH, "//*[@ng-model='vm.mbl.data.oe_info.doc_cut_off_time']"))
        port_cut_off_date_datepicker = Datepicker((By.XPATH, "//*[@ng-model='vm.mbl.data.oe_info.port_cut_off_time']"))
        rail_cut_off_date_datepicker = Datepicker((By.XPATH, "//*[@ng-model='vm.mbl.data.oe_info.rail_cut_off_time']"))
        more_button = Button((By.XPATH, "//a[@id='advance-mbl-btn']"))

        class MultiplePortCutOffDates:
            pass

        class MultiplePOLPOD:
            pass

        class ContainerList:
            new_button = Button((By.XPATH, "//button[@ng-click='vm.mbl.addNewContainer()']"))
            delete_button = Button((By.XPATH, "//button[@ng-click='vm.deleteSelectedContainers()']"))
            create_mbl_button = Button((By.XPATH, "//button[@ng-disabled='!vm.canCreateMBL()']"))
            create_mbl_create_1_mb_l_button = Button((By.XPATH, "//a[contains(., 'Create 1 MB/L')][not(contains(.,'for each booking'))]"))
            create_mbl_create_1_mb_l_for_eack_booking_button = Button((By.XPATH, "//a[contains(., 'Create 1 MB/L for each booking')]"))
            handle_agent_title_label = Label((By.XPATH, "//th[@ng-if='vm.isEnableHandleAgent()']"))



            class container:
                _row = {}
                def __new__(cls, index=None, container_no=None):
                    index = cls.transfer_into_index(index, container_no)

                    if index not in cls._row:
                        cls._row[index] = super().__new__(cls)
                    return cls._row[index]

                def __init__(self, index=None, container_no=None):
                    index = self.transfer_into_index(index, container_no)

                    def ROW_XPATH(xpath):
                        return "//tr[contains(@ng-repeat, 'vm.sortedContainerInfoSet')][{0}]{1}".format(index, xpath)

                    self.select_checkbox = Checkbox((By.XPATH, ROW_XPATH("//input[@type='checkbox']")))
                    self.container_no_input = Input((By.XPATH, ROW_XPATH("//input[@ng-model='ct.container_no']")))
                    self.tp_sz_select = Select((By.XPATH, ROW_XPATH("//select[@ng-model='ct.container_size']")))
                    self.handle_agent_autocomplete = Autocomplete((By.XPATH, ROW_XPATH("//hc-tp-select")), (By.XPATH, ROW_XPATH("//hc-tp-select//ng-dropdown-panel//input")))
                    self.seal_no_input = Input((By.XPATH, ROW_XPATH("//input[@ng-model='ct.seal_no']")))
                    self.action_button = Button((By.XPATH, ROW_XPATH("//button")))
                    self.action_modify_button = Button((By.XPATH, ROW_XPATH("//button/..//a[.='Modify']")))
                    self.action_print_button = Button((By.XPATH, ROW_XPATH("//button/..//a[.='Print']")))

                @classmethod
                def transfer_into_index(cls, index, container_no):
                    if index:
                        return index
                    elif container_no:
                        return cls.search_container_index(container_no)
                    else:
                        raise AttributeError

                @staticmethod
                def search_container_index(container_no):
                    sleep(3)
                    container_no_inputs = Driver.get_driver().find_elements_by_xpath("//input[@ng-model='ct.container_no']")
                    for element in container_no_inputs:
                        element_value = element.get_attribute("value")
                        element_no = element_value if element_value != None else element.text
                        if element_no == container_no:
                            return container_no_inputs.index(element) + 1
                    return None


        class ShipmentStatus:
            pass

        class Memo:
            pass

    class BK:
        _instances = {}
        def __new__(cls, index=1):
            index = int(index)
            if index not in cls._instances:
                cls._instances[index] = super().__new__(cls)
            return cls._instances[index]

        def __init__(self, index=1):
            index = int(index)
            def Booking_XPATH(xpath):
                return "//hc-booking-hbl-board[{0}]{1}".format(index-1, xpath)

            # right side hbl panel
            self.booking_side_panel = Button((By.XPATH, "//div[@id='hbl_side_{0}']".format(index-1)))

            # Booking Title
            self.title = Label((By.XPATH, "//hc-booking-hbl-board//div[@class='portlet-title']/div[@class ='caption ng-binding']"))
            self.tools_button = Button((By.XPATH, "//hc-booking-hbl-board//hc-tools"))
            self.tools_create_hbl_1to1_button = Button((By.XPATH, "//hc-booking-hbl-board//hc-tools//a[contains(., 'Create HB/L - 1 to 1')]"))
            self.tools_create_hbl_split_button = Button((By.XPATH, "//hc-booking-hbl-board//hc-tools//a[contains(., 'Create HB/L - Split')]"))
            self.tools_create_hbl_merge_button = Button((By.XPATH, "//hc-booking-hbl-board//hc-tools//a[contains(., 'Create HB/L - Merge')]"))

            # Input datas
            self.booking_no_input = Input((By.XPATH, Booking_XPATH("//input[@ng-model='vm.hbl.data.oe_info.booking_no']")))
            self.booking_date_datepicker = Datepicker((By.XPATH, Booking_XPATH("//input[@name='booking_date']")))

        @staticmethod
        def get_len():
            return Driver.num_of_element("//div[contains(@id ,'hbl_side_')]")

        class ContainerList:
            pkg_unit_autocomplete = Autocomplete((By.XPATH, "//hc-choice-select[@ng-model='vm.hbl.data.package_unit']//ng-select"), (By.XPATH, "//hc-choice-select[@ng-model='vm.hbl.data.package_unit']//ng-dropdown-panel//input"))
            weight_unit_select = Select((By.XPATH, "//select[@ng-model='vm.hbl.data.weight_unit']"))
            measurement_unit_select = Select((By.XPATH, "//select[@ng-model='vm.hbl.data.measure_unit']"))

            pkg_input = Input((By.XPATH, "//input[@ng-model='vm.hbl.data.booking_info.total_package']"))
            weight_input = Input((By.XPATH, "//input[@ng-model='vm.hbl.data.booking_info.total_weight_kg']"))
            measurement_input = Input((By.XPATH, "//input[@ng-model='vm.hbl.data.booking_info.total_measure_cbm']"))

        class Commodity:
            pass

    class HBL:
        class ContainerList:
            pkg_unit_autocomplete = Autocomplete((By.XPATH, "//hc-choice-select[@ng-model='vm.hbl.data.package_unit']//ng-select"), (By.XPATH, "//hc-choice-select[@ng-model='vm.hbl.data.package_unit']//ng-dropdown-panel//input"))
            weight_unit_select = Select((By.XPATH, "//select[@ng-model='vm.hbl.data.weight_unit']"))
            measurement_unit_select = Select((By.XPATH, "//select[@ng-model='vm.hbl.data.measure_unit']"))

            manual_input_pkg_input = Input((By.XPATH, "//input[@ng-model='vm.hbl.data.total_package']"))
            manual_input_weight_input = Input((By.XPATH, "//input[@ng-model='vm.hbl.data.total_weight_kg']"))
            manual_input_measurement_input = Input((By.XPATH, "//input[@ng-model='vm.hbl.data.total_measure_cbm']"))


    class LoadPlanPopup:
        select_all_checkbox = Checkbox((By.XPATH, "//div[@uib-modal-transclude]//div[contains(@class, 'table-scroll-head')]//input[@type='checkbox']"))
        cancel_button = Button((By.XPATH, "//div[@uib-modal-transclude]//button[@ng-click='vm.cancel()']"))
        save_button = Button((By.XPATH, "//div[@uib-modal-transclude]//button[@ng-click='vm.save()']"))

        class Booking:
            _instances = {}
            def __new__(cls, index=1):
                index = int(index)
                if index not in cls._instances:
                    cls._instances[index] = super().__new__(cls)
                return cls._instances[index]

            def __init__(self, index=1):
                index = int(index)
                def Booking_XPATH(xpath):
                    return "//div[@uib-modal-transclude]//div[contains(@class, 'table-scroll-body')]//tr[{0}]{1}".format(index, xpath)

                self.select_checkbox = Checkbox((By.XPATH, Booking_XPATH("//input[@type='checkbox']")))


    class CreateHBL1to1Popup:
        hbl_no_input = Input((By.XPATH, "//input[@ng-model='vm.hblData.hblNo']"))
        create_button = Button((By.XPATH, "//button[@ng-click='vm.ok()']"))


    class CreateHBLSplitPopop:
        hb_l_no_input = Input((By.XPATH, "//input[@name='splitHblNo']"))
        copy_input = Input((By.XPATH, "//input[@name='splitCount']"))
        cancel_button = Button((By.XPATH, "//button[@ng-click='vm.cancel()']"))
        split_button = Button((By.XPATH, "//button[@ng-click='vm.ok()']"))

    class CreateHBLMergePopup:
        def bk_not_yet_converted_select_button(bk_no):
            return Button((By.XPATH, f"//div[@class='modal-content']//div[h5/text()='Bookings have not yet converted to HB/Ls']//table[contains(@class, 'table-data')]//tr[contains(., '{ bk_no }')]"))

        move_to_to_be_merged_list_button = Button((By.XPATH, "//button[@ng-click='vm.addSelected()']"))

        hbl_no_input = Input((By.XPATH, "//input[@name='mergeHblNo']"))
        cancel_button = Button((By.XPATH, "//button[@ng-click='vm.cancel()']"))
        merge_button = Button((By.XPATH, "//button[@ng-click='vm.ok()']"))

    class TransmitToMBLConfirmPopup:
        ok_button = Button((By.XPATH, "//button[@ng-click='ok()']"))
        cancel_button = Button((By.XPATH, "//button[@ng-click='cancel()']"))

    class MBLIsCreatedPopup:
        created_mbl_link = Link((By.XPATH, "//div[@class='modal-content']//span/a"))
        ok_button = Button((By.XPATH, "//button[@ng-click='ok()']"))


class OEVSAccountingBillingBasedTab:
    save_button = Button((By.XPATH, "//button[@type='submit'][contains(@class,'btn green')]"))

    class Common:
        class copy_to_dropdown:
            # TODO Waiting for improvement
            MBL_revenue_checkbox = Checkbox((By.XPATH, "(//div[@ngbdropdownmenu]//div[contains(., 'MB/L')]//input[@binduniform][@type='checkbox'])[3]"))
            MBL_cost_checkbox = Checkbox((By.XPATH, "(//div[@ngbdropdownmenu]//div[contains(., 'MB/L')]//input[@binduniform][@type='checkbox'])[4]"))
            HBL_revenue_checkbox = Checkbox((By.XPATH, "(//div[@ngbdropdownmenu]//div[contains(., 'HB/L')]//input[@binduniform][@type='checkbox'])[3]"))
            HBL_cost_checkbox = Checkbox((By.XPATH, "(//div[@ngbdropdownmenu]//div[contains(., 'HB/L')]//input[@binduniform][@type='checkbox'])[4]"))
            copy_button = Button((By.XPATH, "//body/div[@class='dropdown']//div[contains(@class, 'dropdown-checkboxes-block')][4]//button"))

    class VS:
        tool_button = Button((By.XPATH, "//*[contains(@class, 'mbl_board')]//hctools"))

    class BK:
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

class OEVSAccountingInvoiceBasedTab:
    class VS:
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

    class BK:
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
