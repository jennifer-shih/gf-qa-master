from selenium.webdriver.common.by import By

from src.elements import *


class OfficeMngPage:
    sfi_link = Link((By.XPATH, "//a[@ng-href='/superuser/office/entry/1']"))
    lohan_link = Link((By.XPATH, "//a[@ng-href='/superuser/office/entry/1'][contains(.,'LOHAN LOGISTICS Co.,Ltd.')]"))
    ewi_link = Link((By.XPATH, "//a[@ng-href='/superuser/office/entry/1'][contains(.,'EASYWAY INTERNATIONAL LLC')]"))
    ssc_link = Link((By.XPATH, "//a[@ng-href='/superuser/office/entry/1'][contains(.,'SMART SUPPLY CHAIN INC')]"))
    olc_link = Link((By.XPATH, "//a[@ng-href='/superuser/office/entry/2']"))
    olc2_link = Link((By.XPATH, "//a[@ng-href='/superuser/office/entry/2']"))
    mascot_link = Link((By.XPATH, "//a[@ng-href='/superuser/office/entry/1']"))
    olc_qd_link = Link((By.XPATH, "//td[.='QD']/../td/a"))
    olc_tpe_link = Link((By.XPATH, "//td[.='TPE']/../td/a"))
    cfm_link = Link((By.XPATH, "//a[@ng-href='/superuser/office/entry/1'][contains(.,'Hard Core Technology')]"))

    scac_input = Input((By.XPATH, "//input[@ng-model='vm.office.data.scac']"))
    enable_branch_list_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.isEnableOfficeBranchList']"))
    branch_list_tag_input = TagInput((By.XPATH, "//tags-input[@ng-model='vm.office.__officeBranchList']"), (By.XPATH, "//tags-input[@ng-model='vm.office.__officeBranchList']//input[@ng-model='newTag.text']"))
    multiple_port_cut_off_dates_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.office.data.enable_multi_port_cut_off_date']"))
    multiple_pol___pod_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.office.data.enable_multi_pol_pod']"))
    location_list_multi_autocomplete = MultiAutocomplete((By.XPATH, "//hc-location-multi-select[@ng-model='vm.office.__officePortSet']"), (By.XPATH, "//hc-location-multi-select[@ng-model='vm.office.__officePortSet']//ng-dropdown-panel//input"), clear_locator=(By.XPATH, "//hc-location-multi-select[@ng-model='vm.office.__officePortSet']//span[@title='Clear all']"))
    enable_email_function_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.office.data.email_enabled']"))
    smtp_host_input = Input((By.NAME, "smtp_host"))
    smtp_port_input = Input((By.NAME, "smtp_port"))
    security_protocol_select = Select((By.XPATH, "//select[@ng-model='vm.office.data.email_security_protocol']"))
    ip_network_input = Input((By.XPATH, "//input[@ng-model='vm.office.data.ip_network']"))
    default_language_select = Select((By.XPATH, "//select[@ng-model='vm.office.data.language']"))

    date_format_input = Input((By.XPATH, "//input[@ng-model='vm.office.data.date_fmt_default']"))
    package_label_date_format_form_input = Input((By.XPATH, "//input[@ng-model='vm.office.data.date_fmt_form_package_label']"))
    local_statement_date_format_input = Input((By.XPATH, "//input[@ng-model='vm.office.data.date_fmt_local_statement']"))
    human_date_format_input = Input((By.XPATH, "//input[@ng-model='vm.office.data.date_fmt_human']"))
    human_date_format_with_full_month_name_input = Input((By.XPATH, "//input[@ng-model='vm.office.data.date_fmt_human_full']"))

    # 雖然Add logo是button，但使用方法是input
    add_company_logo_add_file_button = AddFileButton((By.XPATH, "//input[@ng-if='vm.logoUploader']"))

    allow_duplicate_hbl_mbl_no_checkbox = Checkbox((By.XPATH, "//input[@name='is_enable_duplicate_mbl_hbl_no']"))

    # Accounting
    tax_billing_autocomplete = Autocomplete((By.XPATH, "//div[@name='billing_tax_freight']"), (By.XPATH, "//div[@name='billing_tax_freight']//input"))
    fixed_asset_depreciation_asset_autocomplete = Autocomplete((By.XPATH, "//div[@name='gl_depreciation_asset']"), (By.XPATH, "//div[@name='gl_depreciation_asset']//input"))
    depreciation_expense_autocomplete = Autocomplete((By.XPATH, "//div[@name='gl_depreciation_expense']"), (By.XPATH, "//div[@name='gl_depreciation_expense']//input"))
    prepaid_expense_asset_autocomplete = Autocomplete((By.XPATH, "//div[@name='gl_prepaid_expense']"), (By.XPATH, "//div[@name='gl_prepaid_expense']//input"))
    prepaid_rental_asset_autocomplete = Autocomplete((By.XPATH, "//div[@name='gl_prepaid_rental']"), (By.XPATH, "//div[@name='gl_prepaid_rental']//input"))
    long_term_deferred_expense_asset_autocomplete = Autocomplete((By.XPATH, "//div[@name='gl_long_term_deferred_expense']"), (By.XPATH, "//div[@name='gl_long_term_deferred_expense']//input"))
    enable_tax_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.office.data.is_enable_tax']"))
    ar_tax_opt_tag_input = TagInput((By.XPATH, "//tags-input[@ng-model='vm.arTaxOptions']//ul[@class='tag-list']"), (By.XPATH, "//tags-input[@ng-model='vm.arTaxOptions']//input[@ng-model='newTag.text']"))
    a_r___tax_value_when_p_c___p_select = Select((By.XPATH, "//select[@ng-model='vm.office.data.default_ar_tax_option_prepaid_freight_term']"))
    ar_0_tax_opt_tag_input = TagInput((By.XPATH, "//tags-input[@ng-model='vm.arZeroTaxOptions']//ul[@class='tag-list']"), (By.XPATH, "//tags-input[@ng-model='vm.arZeroTaxOptions']//input[@ng-model='newTag.text']"))
    a_r___tax_value_when_p_c___c_select = Select((By.XPATH, "//select[@ng-model='vm.office.data.default_ar_tax_option_collect_freight_term']"))
    ar_exempt_opt_tag_input = TagInput((By.XPATH, "//tags-input[@ng-model='vm.arExemptTaxOptions']//ul[@class='tag-list']"), (By.XPATH, "//tags-input[@ng-model='vm.arExemptTaxOptions']//input[@ng-model='newTag.text']"))
    ap_tax_opt_tag_input = TagInput((By.XPATH, "//tags-input[@ng-model='vm.apTaxOptions']//ul[@class='tag-list']"), (By.XPATH, "//tags-input[@ng-model='vm.apTaxOptions']//input[@ng-model='newTag.text']"))
    a_p___tax_value_when_p_c___p_select = Select((By.XPATH, "//select[@ng-model='vm.office.data.default_ap_tax_option_prepaid_freight_term']"))
    ap_0_tax_opt_tag_input = TagInput((By.XPATH, "//tags-input[@ng-model='vm.apZeroTaxOptions']//ul[@class='tag-list']"), (By.XPATH, "//tags-input[@ng-model='vm.apZeroTaxOptions']//input[@ng-model='newTag.text']"))


    save_button = Button((By.XPATH, "//button[@ng-click='vm.save()']"))
