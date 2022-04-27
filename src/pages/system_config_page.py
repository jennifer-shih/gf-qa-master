from selenium.webdriver.common.by import By

from src.elements import *


class SystemConfigPage:
    save_button = Button((By.XPATH, "//button[.='Save'][contains(@class, 'green')]"))

    # Basic
    target_select = Select((By.XPATH, "//select[@name='office_id']"))

    # Form
    oe_hbl_style_select = Select((By.XPATH, "//select[@name='oe_hbl_style']"))
    oe_hbl_booking_confirmation_style_select = Select((By.XPATH, "//select[@name='oe_hbl_booking_confirmation_style']"))
    enable_oe_vessel_freight_list_checkbox = Checkbox((By.XPATH, "//input[@name='oe_enable_vessel_freight_list']"))
    accounting_wizard_print_invoice_tp_name_style_select = Select((By.XPATH, "//select[@formcontrolname='acct_wizard_print_invoice_tp_name_style']"))

    # Shipment

    enable_allocate_fcl_profits_per_shipment_others_by_cbm_share_checkbox = Checkbox((By.XPATH, "//input[@name='is_fcl_allocate_profit_per_shipment']"))
    vessel_based_merge_split_bookings_checkbox = Checkbox((By.XPATH, "//input[@name='oe_is_vessel_based']"))
    enable_fcl_lcl_checkbox = Checkbox((By.XPATH, "//input[@name='oe_enable_switch_to_fcl_lcl']"))
    enable_back_date_checkbox = Checkbox((By.XPATH, "//input[@name='oe_enable_backdate']"))
    show_extra_agent_in_oe_booking_checkbox = Checkbox((By.XPATH, "//input[@name='oe_enable_extra_agent']"))
    enable_auto_gen_cntr_from_booking_checkbox = Checkbox((By.XPATH, "//input[@name='oe_enable_auto_gen_container_from_booking']"))
    enable_cost_share_checkbox = Checkbox((By.XPATH, "//input[@name='is_enable_hbl_cost_share']"))
    enable_handle_agent_at_container_list_checkbox = Checkbox((By.XPATH, "//input[@name='is_enable_container_handle_agent']"))
    enable_copy_existing_hawb_checkbox = Checkbox((By.XPATH, "//input[@name='air_is_enable_copy_existing_hawb']"))

    # Payment
    # Report

    # Accounting
    enable_front_desk_portal_checkbox = Checkbox((By.XPATH, "//input[@name='enable_front_desk']"))
