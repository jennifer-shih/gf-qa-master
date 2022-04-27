from selenium.webdriver.common.by import By

from src.elements import *


class NavigatorBar:
    dashboard = Link((By.XPATH, "//a[@data-hc-name='navbar-dashboard']"))

    # Ocean Import
    ocean_import = Link((By.XPATH, "//span[@class='title'][contains(text(), 'Ocean Import')]/preceding-sibling::img"))
    ocean_import_new_shipment = Link((By.XPATH, "//a[@data-hc-name='navbar-oi-entry']"))
    ocean_import_my_shipment_list = Link((By.XPATH, "//a[@data-hc-name='navbar-oi-my-shipment']"))
    ocean_import_master_b_l_list = Link((By.XPATH, "//a[@data-hc-name='navbar-oi-mbl-list']"))
    ocean_import_house_b_l_list = Link((By.XPATH, "//a[@data-hc-name='navbar-oi-hbl-list']"))

    # Ocean Export
    ocean_export = Link((By.XPATH, "//span[@class='title'][contains(text(), 'Ocean Export')]/preceding-sibling::img"))
    ocean_export_new_shipment = Link((By.XPATH, "//a[@data-hc-name='navbar-oe-entry']"))

    # Air Import
    air_import = Link((By.XPATH, "//span[@class='title'][contains(text(), 'Air Import')]/preceding-sibling::img"))
    air_import_new_shipment = Link((By.XPATH, "//li[@data-hc-name='navbar-ai-entry']"))
    air_import_my_shipment_list = Link((By.XPATH, "//li[@data-hc-name='navbar-ai-my-shipment']"))
    air_import_mawb_list = Link((By.XPATH, "//li[@data-hc-name='navbar-ai-mawb-list']"))
    air_import_hawb_list = Link((By.XPATH, "//li[@data-hc-name='navbar-ai-hawb-list']"))

    # Air Export
    air_export = Link((By.XPATH, "//span[@class='title'][contains(text(), 'Air Export')]/preceding-sibling::img"))
    air_export_new_shipment = Link((By.XPATH, "//li[@data-hc-name='navbar-ae-entry']"))
    air_export_my_shipment_list = Link((By.XPATH, "//li[@data-hc-name='navbar-ae-my-shipment']"))
    air_export_mawb_list = Link((By.XPATH, "//li[@data-hc-name='navbar-ae-mawb-list']"))
    air_export_hawb_list = Link((By.XPATH, "//li[@data-hc-name='navbar-ae-hawb-list']"))
    air_export_mawb_stock_list = Link((By.XPATH, "//li[@data-hc-name='navbar-ae-mawb-stock-list']"))

    # Truck
    truck = Link((By.XPATH, "//span[@class='title'][contains(text(), 'Truck')]/preceding-sibling::i"))
    truck_new_shipment = Link((By.XPATH, "//li[@data-hc-name='navbar-truck-entry']"))
    truck_my_shipment_list = Link((By.XPATH, "//li[@data-hc-name='navbar-truck-my-shipment']"))
    truck_shipment_list = Link((By.XPATH, "//li[@data-hc-name='navbar-truck-shipment-list']"))

    # Misc
    misc = Link((By.XPATH, "//span[@class='title'][contains(text(), 'Misc')]/preceding-sibling::i"))
    misc_new_operation = Link((By.XPATH, "//li[@data-hc-name='navbar-misc-entry']"))
    misc_my_operation_list = Link((By.XPATH, "//li[@data-hc-name='navbar-truck-my-op']"))
    misc_operation_list = Link((By.XPATH, "//li[@data-hc-name='navbar-truck-op-list']"))

    # Warehouse
    warehouse = Link((By.XPATH, "//span[@class='title'][contains(text(), 'Warehouse')]/preceding-sibling::img"))
    warehouse_receipts = Link((By.XPATH, "//li/a[contains(text(), 'Receipts')]"))
    warehouse_new_receipt = Link((By.XPATH, "//a[@data-hc-name='navbar-wh-receipt-entry']"))
    warehouse_receipt_list = Link((By.XPATH, "//a[@data-hc-name='navbar-wh-receipt-list']"))
    warehouse_receiving_and_shipping = Link((By.XPATH, "//li/a[contains(text(), 'Receiving & Shipping')]"))
    warehouse_new_receiving = Link((By.XPATH, "//a[@data-hc-name='navbar-wh-receiving-entry']"))
    warehouse_receiving_list = Link((By.XPATH, "//a[@data-hc-name='navbar-wh-receiving-list']"))
    warehouse_new_shipping = Link((By.XPATH, "//a[@data-hc-name='navbar-wh-shipping-entry']"))
    warehouse_shipping_list = Link((By.XPATH, "//a[@data-hc-name='navbar-wh-shipping-list']"))

    # Accounting
    accounting = Link((By.XPATH, "//span[@class='title'][contains(text(), 'Accounting')]/preceding-sibling::i"))
    accounting_payment_plan = Link((By.XPATH, "//a[normalize-space(text())='Payment Plan']"))
    accounting_payment_plan_payment_plan_list = Link((By.XPATH, "//a[@data-hc-name='navbar-acct-payment-plan-list']"))
    accounting_payment = Link((By.XPATH, "//a[normalize-space(text())='Payment']"))
    accounting_payment_receive_payment = Link((By.XPATH, "//a[normalize-space(text())='Receive Payment']"))
    accounting_report = Link((By.XPATH, "//a[normalize-space(text())='Report']"))
    accounting_report_balance_sheet = Link((By.XPATH, "//a[@data-hc-name='navbar-acct-balance-sheet']"))
    accounting_report_trial_balance = Link((By.XPATH, "//a[@data-hc-name='navbar-acct-trial-balance']"))
    accounting_report_gl_report = Link((By.XPATH, "//a[@data-hc-name='navbar-acct-gl-report']"))
    accounting_report_income_statement = Link((By.XPATH, "//a[@data-hc-name='navbar-acct-income-statement']"))
    accounting_front_desk = Link((By.LINK_TEXT, 'Front Desk'))
    accounting_front_desk_front_desk_portal = Link((By.XPATH, "//a[@data-hc-name='navbar-acct-front-desk-list']"))
    accounting_front_desk_uniform_invoice_management = Link((By.XPATH, "//a[@data-hc-name='navbar-acct-uni-invoice-management']"))
    accounting_front_desk_uniform_invoice_setting = Link((By.XPATH, "//a[@data-hc-name='navbar-acct-uni-invoice-setting']"))

    # Sales
    sales = Link((By.XPATH, "//span[@class='title'][contains(text(), 'Sales')]/preceding-sibling::i"))
    sales_new_quotation = Link((By.XPATH, "//a[@data-hc-name='navbar-sales-quotation-entry']"))
    sales_quotation_list = Link((By.XPATH, "//a[@data-hc-name='navbar-sales-quotation-list']"))

    # Trade Partner
    trade_partner = Link((By.XPATH, "//span[@class='title'][contains(text(), 'Trade Partner')]/preceding-sibling::i"))
    trade_partner_new_trade_partner = Link((By.XPATH, "//a[@data-hc-name='navbar-tp-entry']"))
    trade_partner_trade_partner_credit_entry = Link((By.XPATH, "//a[@data-hc-name='navbar-tp-credit-entry']"))
    trade_partner_trade_partner_list = Link((By.XPATH, "//a[@data-hc-name='navbar-tp-list']"))

    # Settings
    settings = Link((By.XPATH, "//span[@class='title'][contains(text(), 'Settings')]/preceding-sibling::i"))
    settings_awb_no_management = Link((By.XPATH, "//a[@data-hc-name='navbar-set-awb-no-management']"))
    settings_user_management = Link((By.XPATH, "//a[@data-hc-name='navbar-set-user-management']"))
    settings_tracking_user_management = Link((By.XPATH, "//a[@data-hc-name='navbar-set-tracking-user-management']"))

    # Super User
    super_user = Link((By.XPATH, "//span[@class='title'][contains(text(), 'Super User')]/preceding-sibling::i"))
    super_user_admin = Link((By.XPATH, "//*[normalize-space(text())='Admin']"))
    super_user_super = Link((By.XPATH, "//*[normalize-space(text())='SUPER']"))
    super_user_super_reset_backups_db = Link((By.XPATH, "//*[normalize-space(text())='Reset Backups DB']"))
    super_user_admin_permission_management = Link((By.XPATH, "//a[@data-hc-name='navbar-permission-management']"))
    super_user_admin_office_management = Link((By.XPATH, "//a[@data-hc-name='navbar-office-management']"))
    super_user_admin_company_management = Link((By.XPATH, "//a[@data-hc-name='navbar-company-management']"))
