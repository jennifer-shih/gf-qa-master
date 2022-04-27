from selenium.webdriver.common.by import By

from src.elements import *


class ARInvoiceDefaultStyle:
    mbl_no_title_label = Label((By.XPATH, "//div[contains(@class, 'con')]/table[1]//*[contains(text(),'MB/L No.')]"))

class ARInvoiceOLCStyle:
    file_no_title_label = Label((By.XPATH, "//div[contains(@class, 'con')]/table[1]//*[contains(text(),'File No.')]"))
    mbl_no_title_label = Label((By.XPATH, "//div[contains(@class, 'con')]/table[1]//*[contains(text(),'MB/L No.')]"))
    cust_ref_no_title_label = Label((By.XPATH, "//div[contains(@class, 'con')]/table[1]//*[contains(.,'CUST')]"))

class ARInvoiceVinworldStyle:
    bill_to_title_label = Label((By.XPATH, "//div[contains(@class, 'con')]/table[1]//*[contains(text(),'BILL TO')]"))
    ship_to_title_label = Label((By.XPATH, "//div[contains(@class, 'con')]/table[1]//*[contains(text(),'SHIP TO')]"))
