from selenium.webdriver.common.by import By

from src.elements import *


class CompanyMngPage:
    save_button = Button((By.XPATH, "//button[@ng-click='vm.save()']"))

    # Company Management - Feature
    enable_warehouse_checkbox = Checkbox((By.NAME, "enable_warehouse"))
    enable_warehouse_app_checkbox = Checkbox((By.NAME, "enable_warehouse_app"))
    enable_quotation_checkbox = Checkbox((By.NAME, "enable_quotation"))
    enable_aes_direct_select = Select((By.XPATH, "//select[@name='aes_setup_style']"))

    # Company Management - GoFreight Tracking
    login_checkbox = Checkbox((By.XPATH, "//*[@ng-model='vm.company.data.enable_tracking_login']"))
    auto_create_user_checkbox = Checkbox((By.XPATH, "//*[@ng-model='vm.company.data.enable_auto_create_tracking_user']"))
    enable_tracking_user_management_checkbox = Checkbox((By.XPATH, "//*[@ng-model='vm.company.data.enable_tracking_user_management']"))
    enable_edi_checkbox = Checkbox((By.XPATH, "//*[@ng-model='vm.company.data.enable_tracking_edi']"))
    enable_email_notification_checkbox = Checkbox((By.XPATH, "//*[@ng-model='vm.company.data.enable_tracking_email_notification']"))
    show_tracking_user_email_preference_checkbox = Checkbox((By.XPATH, "//*[@ng-model='vm.company.data.enable_tracking_user_email_preference']"))

    # Company Management - Container Ordering
    container_ordering_ocean_import_checkbox = Checkbox((By.XPATH, "//*[@ng-model='vm.company.data.container_ordering_oi']"))
    container_ordering_ocean_export_checkbox = Checkbox((By.XPATH, "//*[@ng-model='vm.company.data.container_ordering_oe']"))
    container_ordering_truck_checkbox = Checkbox((By.XPATH, "//*[@ng-model='vm.company.data.container_ordering_tk']"))
    container_ordering_misc_checkbox = Checkbox((By.XPATH, "//*[@ng-model='vm.company.data.container_ordering_ms']"))
    container_ordering_ocean_booking_checkbox = Checkbox((By.XPATH, "//*[@ng-model='vm.company.data.container_ordering_ob']"))

    # Accounting
    enable_accounting_wizard_checkbox = Checkbox((By.XPATH, "//input[@name='enable_accounting_wizard']"))
    accounting_wizard_billing_style_radio_group = RadioGroup({
        "Separated": (By.XPATH, "//*[text()='Separated']//input[@ng-model='vm.company.data.is_accounting_wizard_billing_separated']"),
        "Merged": (By.XPATH, "//*[text()='Merged']//input[@ng-model='vm.company.data.is_accounting_wizard_billing_separated']"),
    })
    invoice_accounting_wizard_form_style_select = Select((By.XPATH, "//select[@ng-model='vm.company.data.invoice_accounting_wizard_style']"))
    enable_tax_checkbox = Checkbox((By.XPATH, "//input[@data-hc-name='enable-tax']"))
    tax_billing_autocomplete = Autocomplete((By.XPATH, "//hc-billing-select[@data-hc-name='billing-tax-freight']"), (By.XPATH, "//hc-billing-select[@data-hc-name='billing-tax-freight']//input[@type='search']"))
    enable_payment_plan_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.company.data.enable_payment_plan']"))
    payment_plan_display_mode_radio_group = RadioGroup({
        "Invoice Based": (By.XPATH, "//input[@ng-model='vm.company.data.payment_plan_display_mode' and @value='I']"),
        "Freight Based": (By.XPATH, "//input[@ng-model='vm.company.data.payment_plan_display_mode' and @value='F']"),
    })

    # Currency
    main_currency_input = Input((By.XPATH, "//input[@name='main_currency']"))
    multi_currency_enable_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.company.data.is_multi_ccy_enabled']"))
    other_currency_tag_input = TagInput((By.XPATH, "//tags-input[@name='sub_currency']/div[@class='host']/div[@class='tags']/ul[@class='tag-list']"), (By.XPATH, "//tags-input[@name='sub_currency']/div[@class='host']/div[@class='tags']/input[@ng-model='newTag.text']"))
