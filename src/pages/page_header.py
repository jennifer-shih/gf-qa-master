from selenium.webdriver.common.by import By

from src.elements import *


class PageHeader:
    dashboard_logo = Element((By.XPATH, "//img[@alt='logo']"))
    dashboard_icon = Element((By.XPATH, "//i[@class='icon-home']"))
    profile = Button((By.XPATH, "//span[contains(@class, 'username')][contains(@class, 'username-hide-on-mobile')]"))
    home_page_navigator_link = Link((By.XPATH, "(//a[@href='/'])[3]"))
    log_out_link = Link((By.XPATH, "(//a[@href='#logout'])"))
    for_evaluation_propose_only_bar = Button((By.XPATH, "//div[@class='metronic-alerts alert bg-red-flamingo']"))
