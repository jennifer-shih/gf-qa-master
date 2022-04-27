from selenium.webdriver.common.by import By

from src.elements import *


class ShipmentEntryTab:
    '''
        The Xpaths of elements are different between Accounting Wizard Tab and other tabs,
        so be sure to check both cases before updating the xpath.
    '''

    basic_tab = Link((By.XPATH, "//ul[@class='nav nav-tabs ng-isolate-scope' or @hcnavtab]/li[contains(.,'Basic')]"))
    container_tab = Link((By.XPATH, "//ul[@class='nav nav-tabs ng-isolate-scope' or @hcnavtab]/li[contains(.,'Container & Item')]"))
    accounting_tab = Link((By.XPATH, "//ul[@class='nav nav-tabs ng-isolate-scope']/li[contains(.,'Accounting')]"))
    accounting_mode_switch_button = Button((By.XPATH, "//ul[contains(@class, 'nav nav-tabs')]//li[a[contains(text(), 'Accounting')]]//button"))
    accounting_billing_based_button = Button((By.XPATH, '''//ul[@class='nav nav-tabs ng-isolate-scope']//a[contains(.,'Accounting')]/..//a[@ng-click="tab.onAccountingModeClick('billing', $event)"] | //hcaccountingviewmode/*[.='Billing Based']'''))
    accounting_invoice_based_button = Button((By.XPATH, '''//ul[@class='nav nav-tabs ng-isolate-scope']//a[contains(.,'Accounting')]/..//a[@ng-click="tab.onAccountingModeClick('invoice', $event)"] | //hcaccountingviewmode/*[.='Invoice Based']'''))
    doc_center_tab = Link((By.XPATH, "//ul[@class='nav nav-tabs ng-isolate-scope']/li[contains(.,'Doc Center')]"))
    status_tab = Link((By.XPATH, "//ul[@class='nav nav-tabs ng-isolate-scope']/li[contains(.,'Status')]"))
