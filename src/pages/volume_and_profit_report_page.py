from selenium.webdriver.common.by import By

from src.elements import *


class VolumeAndProfitReportPage:
    period_radio_group = RadioGroup({"Post Date": (By.XPATH, "//input[@name='period_type_post_date']"),
                                     "ETD": (By.XPATH, "//input[@name='period_type_ETD']"),
                                     "ETA": (By.XPATH, "//input[@name='period_type_ETA']")})
    period_period_datepicker = PeriodDatepicker((By.XPATH, "//input[@model-date-start='vm.reportOutput.searchInfo.period_start']"),
                                               (By.XPATH, "//input[@name='daterangepicker_start']"),
                                               (By.XPATH, "//input[@name='daterangepicker_end']"))
    view_button = Button((By.XPATH, "//button[@ng-click='vm.viewReport()']"))

    class table:
        @staticmethod
        def get_len():
            sleep(1)
            return Driver.num_of_element("//div[@ui-grid='vm.reportGrid']//div[@role='row']")
