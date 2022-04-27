from selenium.webdriver.common.by import By

from src.elements import *


class WHReceiptTab:
    basic_tab = Link((By.XPATH, "//a[@ng-bind='tab.name'][contains(.,'Basic')]"))
    doc_center_tab = Link((By.XPATH, "//a[@ng-bind='tab.name'][contains(.,'Doc Center')]"))

class WHReceiptBasicTab:

    tools_button = Button((By.XPATH, "//hc-tools"))
    tools_copy_button = Button((By.XPATH, "//a[contains(.,'Copy')]"))

    warehouse_receipt_no_input = Input((By.XPATH, "//input[@ng-model='vm.wh.data.receipt_no']"))
    received_date_time_datepicker = Datepicker((By.XPATH, "//*[@ng-model='vm.wh.data.receive_datetime']"))
    received_by_select = Select((By.XPATH, "//select[contains(@ng-model,'vm.wh.data.receive_by')]"))
    truck_b_l_no_input = Input((By.XPATH, "//input[@ng-model='vm.wh.data.truck_bl_no']"))
    location_input = Input((By.XPATH, "//input[@ng-model='vm.wh.data.location']"))
    loaded_date_time_datepicker = Datepicker((By.XPATH, "//input[@ng-model='vm.wh.data.loaded_datetime']"))
    storage_day_icon_label = Label((By.XPATH, "//i[@ng-show='vm.isShowStorageDays()']"))
    storage_day_tips_label = Label((By.CSS_SELECTOR, "div.tooltip-inner.ng-binding"))
    maker_autocomplete = Autocomplete((By.XPATH, "//hc-tp-select[@ng-model='vm.wh.data.maker']"),
                                      (By.XPATH, "//hc-tp-select[@ng-model='vm.wh.data.maker']//input[@type='search']"),
                                      disabled_locator = (By.XPATH, "//input[../label[.='Maker'] and @disabled]"))
    shipper_autocomplete = Autocomplete((By.XPATH, "//hc-tp-select[@ng-model='vm.wh.data.shipper']"), (By.XPATH, "//hc-tp-select[@ng-model='vm.wh.data.shipper']//input[@type='search']"))
    consignee_autocomplete = Autocomplete((By.XPATH, "//hc-tp-select[@ng-model='vm.wh.data.consignee']"), (By.XPATH, "//hc-tp-select[@ng-model='vm.wh.data.consignee']//input[@type='search']"))
    delivered_carrier_input = Input((By.XPATH, "//input[@ng-model='vm.wh.data.delivered_carrier']"))
    delivered_by_input = Input((By.XPATH, "//input[@ng-model='vm.wh.data.delivered_by']"))
    amount_input = Input((By.XPATH, "//input[@ng-model='vm.wh.data.amount']"))
    check_no_input = Input((By.XPATH, "//input[@ng-model='vm.wh.data.check_no']"))
    cargo_type_radio_group = RadioGroup({'Others': (By.XPATH, "//input[@ng-model='vm.wh.data.cargo_type' and @value='OTH']"),
                                        'Automobile': (By.XPATH, "//input[@ng-model='vm.wh.data.cargo_type' and @value='MOB']")})
    hazardous_goods_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.wh.data.is_hazardous']"))
    heat_treated_pallets_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.wh.data.is_heat_threat_pallet']"))
    commodity_input = Input((By.XPATH, "//textarea[@ng-model='vm.wh.data.commodity']"))
    po_no_input = Input((By.XPATH, "//input[@ng-model='vm.wh.data.po_no']"))
    remark_input = Input((By.XPATH, "//textarea[@ng-model='vm.wh.data.remark']"))
    office_autocomplete = Autocomplete((By.XPATH, "//hc-department-select[@*[name()='[office-model]']='vm.wh.data.office']/ng-select"), (By.XPATH, "//hc-department-select[@*[name()='[office-model]']='vm.wh.data.office']//ng-dropdown-panel//input"))

    am_vin_no_autocomplete = Autocomplete((By.XPATH, "//hc-warehouse-car-select[@model='vm.wh.data.car_info']"), (By.XPATH, "//hc-warehouse-car-select[@model='vm.wh.data.car_info']//input[@type='search']"))
    am_tag_no_input = Input((By.XPATH, "//input[@ng-model='vm.wh.data.car_info.tag_num']"))
    am_customer_autocomplete = Autocomplete((By.XPATH, "//hc-tp-select[@ng-model='vm.wh.data.car_info.customer']"), (By.XPATH, "//hc-tp-select[@ng-model='vm.wh.data.car_info.customer']//input[@type='search']"))
    am_maker_input = Input((By.XPATH, "//input[@ng-model='vm.wh.data.car_info.maker']"))
    am_year_input =  Input((By.XPATH, "//input[@ng-model='vm.wh.data.car_info.made_year']"))
    am_model_input = Input((By.XPATH, "//input[@ng-model='vm.wh.data.car_info.model']"))
    am_color_input = Input((By.XPATH, "//input[@ng-model='vm.wh.data.car_info.color']"))
    am_engine_no_input = Input((By.XPATH, "//input[@ng-model='vm.wh.data.car_info.engine_num']"))
    am_manufacture_year_autocomplete = Autocomplete((By.XPATH, "//hc-year-month-picker[@model='vm.wh.data.car_info.manufacture_date']//div[@ng-model='vm.year']"), (By.XPATH, "(//hc-year-month-picker[@model='vm.wh.data.car_info.manufacture_date']//input[@type='search'])[1]"))
    am_manufacture_month_autocomplete = Autocomplete((By.XPATH, "//hc-year-month-picker[@model='vm.wh.data.car_info.manufacture_date']//div[@ng-model='vm.month']"), (By.XPATH, "(//hc-year-month-picker[@model='vm.wh.data.car_info.manufacture_date']//input[@type='search'])[2]"))
    am_title_received_status_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.wh.data.car_info.is_title_received']"))
    am_title_received_datepicker = Datepicker((By.XPATH, "//input[@ng-model='vm.wh.data.car_info.title_receive_date']"))
    am_condition_input = Input((By.XPATH, "//input[@ng-model='vm.wh.data.car_info.condition']"))
    am_key_input = Input((By.XPATH, "//input[@ng-model='vm.wh.data.car_info.key_num']"))
    am_fuel_input = Input((By.XPATH, "//input[@ng-model='vm.wh.data.car_info.fuel']"))
    am_tire_size_front_input = Input((By.XPATH, "//input[@ng-model='vm.wh.data.car_info.tire_size_front']"))
    am_tire_size_rear_input = Input((By.XPATH, "//input[@ng-model='vm.wh.data.car_info.tire_size_rear']"))
    am_mileage_input = Input((By.XPATH, "//input[@ng-model='vm.wh.data.car_info.mileage']"))
    am_wsticker_radio_group = RadioGroup({'Yes': (By.XPATH, "//input[@ng-model='vm.wh.data.car_info.has_window_sticker' and @value='true']"),
                                        'No': (By.XPATH, "//input[@ng-model='vm.wh.data.car_info.has_window_sticker' and @value='false']")})
    am_remote_control_radio_group = RadioGroup({'Yes': (By.XPATH, "//input[@ng-model='vm.wh.data.car_info.has_remote_control' and @value='true']"),
                                        'No': (By.XPATH, "//input[@ng-model='vm.wh.data.car_info.has_remote_control' and @value='false']")})
    am_headphone_radio_group = RadioGroup({'Yes': (By.XPATH, "//input[@ng-model='vm.wh.data.car_info.has_headphone' and @value='true']"),
                                        'No': (By.XPATH, "//input[@ng-model='vm.wh.data.car_info.has_headphone' and @value='false']")})
    am_owners_manual_radio_group = RadioGroup({'Yes': (By.XPATH, "//input[@ng-model='vm.wh.data.car_info.has_owners_manual' and @value='true']"),
                                        'No': (By.XPATH, "//input[@ng-model='vm.wh.data.car_info.has_owners_manual' and @value='false']")})
    am_cd_player_radio_group = RadioGroup({'Yes': (By.XPATH, "//input[@ng-model='vm.wh.data.car_info.has_cd_player' and @value='true']"),
                                        'No': (By.XPATH, "//input[@ng-model='vm.wh.data.car_info.has_cd_player' and @value='false']")})
    am_cd_changer_radio_group = RadioGroup({'Yes': (By.XPATH, "//input[@ng-model='vm.wh.data.car_info.has_cd_changer' and @value='true']"),
                                        'No': (By.XPATH, "//input[@ng-model='vm.wh.data.car_info.has_cd_changer' and @value='false']")})
    am_first_aid_kit_radio_group = RadioGroup({'Yes': (By.XPATH, "//input[@ng-model='vm.wh.data.car_info.has_first_aid_kit' and @value='true']"),
                                        'No': (By.XPATH, "//input[@ng-model='vm.wh.data.car_info.has_first_aid_kit' and @value='false']")})
    am_floor_mat_radio_group = RadioGroup({'Yes': (By.XPATH, "//input[@ng-model='vm.wh.data.car_info.has_floor_mat' and @value='true']"),
                                        'No': (By.XPATH, "//input[@ng-model='vm.wh.data.car_info.has_floor_mat' and @value='false']")})
    am_cigarette_lighter_radio_group = RadioGroup({'Yes': (By.XPATH, "//input[@ng-model='vm.wh.data.car_info.has_cigarette_lighter' and @value='true']"),
                                        'No': (By.XPATH, "//input[@ng-model='vm.wh.data.car_info.has_cigarette_lighter' and @value='false']")})

    am_cargo_net_radio_group = RadioGroup({'Yes': (By.XPATH, "//input[@ng-model='vm.wh.data.car_info.has_cargo_net' and @value='true']"),
                                        'No': (By.XPATH, "//input[@ng-model='vm.wh.data.car_info.has_cargo_net' and @value='false']")})

    am_ashtray_radio_group = RadioGroup({'Yes': (By.XPATH, "//input[@ng-model='vm.wh.data.car_info.has_ashtray' and @value='true']"),
                                        'No': (By.XPATH, "//input[@ng-model='vm.wh.data.car_info.has_ashtray' and @value='false']")})
    am_tools_radio_group = RadioGroup({'Yes': (By.XPATH, "//input[@ng-model='vm.wh.data.car_info.has_tools' and @value='true']"),
                                        'No': (By.XPATH, "//input[@ng-model='vm.wh.data.car_info.has_tools' and @value='false']")})
    am_spare_tire_radio_group = RadioGroup({'Yes': (By.XPATH, "//input[@ng-model='vm.wh.data.car_info.has_spare_tire' and @value='true']"),
                                        'No': (By.XPATH, "//input[@ng-model='vm.wh.data.car_info.has_spare_tire' and @value='false']")})
    am_sun_roof_radio_group = RadioGroup({'Yes': (By.XPATH, "//input[@ng-model='vm.wh.data.car_info.has_sun_roof' and @value='true']"),
                                        'No': (By.XPATH, "//input[@ng-model='vm.wh.data.car_info.has_sun_roof' and @value='false']")})

    class Dimension:
        _rows = {}
        dimension_add_button = Button((By.XPATH, "//button[@ng-click='vm.addNewReceiptDetail()']"))
        dimension_copy_button = Button((By.XPATH, "//button[@ng-click='vm.copyReceiptDetail()']"))
        dimension_link_hbl_to_receipt_autocomplete = Autocomplete((By.XPATH, "//hc-bl-link-select[@ng-disabled='vm.isShipmentSelectDisabled()']"), (By.XPATH, "//hc-bl-link-select[@ng-disabled='vm.isShipmentSelectDisabled()']//input[@type='search']"))
        dimension_link_apply_button = Button((By.XPATH, "//button[@ng-click='vm.apply()']"))
        dimension_total_pkg_label = Label((By.XPATH, "//td[@ng-bind='vm.wh.data.detail_set | vcTotalPKG | number:0']"))
        dimension_total_pcs_label = Label((By.XPATH, "//td[@ng-bind='vm.wh.data.detail_set | vcTotalPCS']"))
        dimension_total_pallet_label = Label((By.XPATH, "//td[@ng-bind='vm.wh.data.detail_set | vcTotalPLT | number:0']"))
        dimension_total_vol_kgs_label = Label((By.XPATH, "//td[@ng-bind='vm.wh.data.detail_set | vcTotalVolumeKGS | weightNumber']"))
        dimension_total_vol_lbs_label = Label((By.XPATH, "//td[@ng-bind='vm.wh.data.detail_set | vcTotalVolumeLBS | weightNumber']"))
        dimension_total_measure_cbm_label = Label((By.XPATH, "//td[@ng-bind='vm.wh.data.detail_set | vcTotalMeasureCBM | measureNumber']"))
        dimension_total_measure_cft_label = Label((By.XPATH, "//td[@ng-bind='vm.wh.data.detail_set | vcTotalMeasureCFT | measureNumber']"))
        dimension_total_act_kgs_label = Label((By.XPATH, "//td[@ng-bind='vm.wh.data.detail_set | vcTotalActualWeightKGS | weightNumber']"))
        dimension_total_act_lbs_label = Label((By.XPATH, "//td[@ng-bind='vm.wh.data.detail_set | vcTotalActualWeightLBS | weightNumber']"))

        def __new__(cls, index=1):
            index = int(index)
            if index not in cls._rows:
                cls._rows[index] = super().__new__(cls)
            return cls._rows[index]

        def __init__(self, index=1):
            index = int(index)
            def ROW_XPATH(xpath):
                return "//tr[@ng-repeat-start='detail in vm.wh.data.detail_set'][{0}]{1}".format(index, xpath)

            self.checked_checkbox = Checkbox((By.XPATH, ROW_XPATH("//input[@ng-model='detail.__checked']")))
            self.length_input = Input((By.XPATH, ROW_XPATH("//input[@ng-model='detail.length']")))
            self.width_input = Input((By.XPATH, ROW_XPATH("//input[@ng-model='detail.width']")))
            self.height_input = Input((By.XPATH, ROW_XPATH("//input[@ng-model='detail.height']")))
            self.dimension_select = Select((By.XPATH, ROW_XPATH("//select[@ng-model='detail.dimension_unit']")))
            self.pkg_input = Input((By.XPATH, ROW_XPATH("//input[@ng-model='detail.package']")))
            self.unit_select = Select((By.XPATH, ROW_XPATH("//select[@ng-model='detail.unit']")))
            self.sku_po_input = Input((By.XPATH, ROW_XPATH("//input[@ng-model='detail.sku_po_no']")))
            self.pallet_input = Input((By.XPATH, ROW_XPATH("//input[@ng-model='detail.pallet']")))
            self.total_pcs_input = Input((By.XPATH, ROW_XPATH("//input[@ng-model='detail.pcs']")))
            self.volume_kgs_label = Label((By.XPATH, ROW_XPATH("//td[contains(@ng-bind,'vcVolumeKGS')]")))
            self.volume_lbs_label = Label((By.XPATH, ROW_XPATH("//td[contains(@ng-bind,'vcVolumeLBS')]")))
            self.measurement_cbm_input = Input((By.XPATH, ROW_XPATH("//input[@ng-model='detail.measure_cbm']")))
            self.measurement_cft_input = Input((By.XPATH, ROW_XPATH("//input[@ng-model='detail.measure_cft']")))
            self.act_weight_kgs_input = Input((By.XPATH, ROW_XPATH("//input[@ng-model='detail.actual_weight_kg']")))
            self.act_weight_lbs_input = Input((By.XPATH, ROW_XPATH("//input[@ng-model='detail.actual_weight_lb']")))
            self.lnkd_checkbox = Checkbox((By.XPATH, ROW_XPATH("//input[@ng-model='detail.isLinked']")))
            self.shpd_checkbox = Checkbox((By.XPATH, ROW_XPATH("//input[@ng-model='detail.is_shipped']")))
            self.m_select = Select((By.XPATH, ROW_XPATH("//select[@ng-model='detail.mode']")))
            self.date_datepicker = Datepicker((By.XPATH, ROW_XPATH("//input[@name='shipped_date']")), (By.XPATH, ROW_XPATH("//input[@ng-value='detail.shipmentShippedDate']")))
            self.b_l_bkg_no_input =  Input((By.XPATH, ROW_XPATH("//input[@ng-model='detail.bl_no']")), (By.XPATH, ROW_XPATH("//a[@ng-bind='detail.shipmentBlNo']")))
