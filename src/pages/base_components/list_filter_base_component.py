from selenium.webdriver.common.by import By

from src.elements import *


class BaseListFilter:
    pin_status_icon = StatusIcon((By.XPATH, "//hc-filter-pin//span"),
        {
            "Unpinned": "(//hc-filter-pin | //hcfilterpin)//span[not(contains(@class, 'pin-lock'))]",
            "Pinned": "(//hc-filter-pin | //hcfilterpin)//span[contains(@class, 'pin-lock')]"
        })
    keyword_input = Input((By.XPATH, "(//hc-filter//hc-keyword-filter | //hcfilter//*[@formcontrolname='keyword'])//input"))
    apply_filters_button = Button((By.XPATH, "//button[contains(text(), 'Apply Filters')]"))
