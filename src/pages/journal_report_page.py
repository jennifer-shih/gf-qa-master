from time import sleep

from selenium.webdriver.common.by import By

from src.elements import *


class JournalReportPage:
    period_period_datepicker = PeriodDatepicker((By.XPATH, "//input[@daterangepicker]"),
                                               (By.XPATH, "//input[@name='daterangepicker_start']"),
                                               (By.XPATH, "//input[@name='daterangepicker_end']"))

    print_button = Button((By.XPATH, "//button[@type='button'][@class='btn bg-blue-madison']"))

    class Print:
        title_label = Label((By.XPATH, "//h5"))
        period_label = Label((By.XPATH, "//h4"))
        @staticmethod
        def get_len():
            sleep(2)
            return Driver.num_of_element("//table[@class='table-padding-double']/tbody/tr")
