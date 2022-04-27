from selenium.webdriver.common.by import By

from src.elements import *


class VolumeAndProfitChartPage:
    period_radio_group = RadioGroup({"Post Date": (By.XPATH, "//input[@name='period_type_post_date']"),
                                     "ETD": (By.XPATH, "//input[@name='period_type_ETD']"),
                                     "ETA": (By.XPATH, "//input[@name='period_type_ETA']")})
    period_period_datepicker = PeriodDatepicker((By.XPATH, "//input[@model-date-start='vm.search_info.period_start']"),
                                               (By.XPATH, "//input[@name='daterangepicker_start']"),
                                               (By.XPATH, "//input[@name='daterangepicker_end']"))
    view_button = Button((By.XPATH, "//button[@ng-click='vm.reloadChartData()']"))

    ocean_import_checkbox = Checkbox((By.XPATH, "//input[@type='checkbox'][@name='OI']"))
    ocean_export_checkbox = Checkbox((By.XPATH, "//input[@type='checkbox'][@name='OE']"))
    air_import_checkbox = Checkbox((By.XPATH, "//input[@type='checkbox'][@name='AI']"))
    air_export_checkbox = Checkbox((By.XPATH, "//input[@type='checkbox'][@name='AE']"))
    truck_checkbox = Checkbox((By.XPATH, "//input[@type='checkbox'][@name='TK']"))
    misc_checkbox = Checkbox((By.XPATH, "//input[@type='checkbox'][@name='MS']"))
    warehouse_checkbox = Checkbox((By.XPATH, "//input[@type='checkbox'][@name='WH']"))

    volume_unit_select = Select((By.XPATH, "//select[@ng-model='vm.search_info.volume_unit']"))
    chart_type_select = Select((By.XPATH, "//select[@ng-model='vm.search_info.chart_type']"))
    office_autocomplete_multi_select = AutocompleteMultiSelect((By.XPATH, "//hc-department-multi-select[@hc-class='value-sm']"),
                                    (By.XPATH, "//hc-department-multi-select[@hc-class='value-sm']//ng-dropdown-panel//input"),
                                    (By.XPATH, "//hc-department-multi-select[@hc-class='value-sm']//ng-dropdown-panel//div[@role='option'][1]"),
                                    (By.XPATH, "//hc-department-multi-select[@hc-class='value-sm']//span[@title='Clear all']"))
    sales_select = Select((By.XPATH, "//select[@ng-model='vm.search_info.sales_person']"))
    bar_segment_select = Select((By.XPATH, "//select[@ng-model='vm.search_info.bar_segment']"))
    status_radio_group = RadioGroup({"All": (By.XPATH, "//input[@name='block_status'][@value='all']"),
                                     "Open": (By.XPATH, "//input[@name='block_status'][@value='open']"),
                                     "Blocked": (By.XPATH, "//input[@name='block_status'][@value='block']")})
