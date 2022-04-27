from selenium.webdriver.common.by import By

from src.elements import *


class SalesQuotPage:
    save_button = Button((By.XPATH, "//button[contains(text(),'Save')]"))
    remove_prompt_button = Button((By.XPATH, "//a[./i[contains(@class, 'glyphicon-remove')]]"))
    shipping_type_select = Select((By.XPATH, "//select[@formcontrolname='department']"))
    customer_autocomplete = Autocomplete((By.XPATH, "//*[@formcontrolname='customer']"), (By.XPATH, "//*[@formcontrolname='customer']//input[@type='search']"))
    quote_no_input = Input((By.XPATH, "//*[@formcontrolname='quotation_no']"))
    office_autocomplete = Autocomplete((By.XPATH, "//hcdepartmentselect[@officecontrolname='office']"), (By.XPATH, "//hcdepartmentselect[@officecontrolname='office']//ng-dropdown-panel//input"))
