from time import sleep

from selenium.webdriver.common.by import By

from src.elements import *


class AgingReportPage:
    report_type_radio_group = RadioGroup({"Summary": (By.XPATH, "//input[@name='report-type'][@value='summary']"),
                                          "Detail": (By.XPATH, "//input[@name='report-type'][@value='detail']")})
    ending_date_period_type_select = Select((By.XPATH, "//select[@ng-model='vm.filter_period_type']"))
    ending_date_period_datepicker = PeriodDatepicker((By.XPATH, "//div[@class='input-group date']/input[contains(@date-range-picker,.)][@model-date-start='vm.filter_period_start_date']"),
                                               (By.XPATH, "//input[@name='daterangepicker_start']"),
                                               (By.XPATH, "//input[@name='daterangepicker_end']"))
    search_button = Button((By.XPATH, "//button[@ng-click='vm.search()']"))
    print_button = Button((By.XPATH, "//button[@ng-click='vm.print()']"))
    batch_email_button = Button((By.XPATH, "//button[@ng-click='vm.openBatchEmailModal()']"))


    class Table:
        @staticmethod
        def get_len():
            sleep(2)
            return Driver.num_of_element("//div[@ref='eBodyViewport']//div[@role='rowgroup']/div[@role='row']")

    class PrintSummary:
        @staticmethod
        def get_len():
            sleep(2)
            return Driver.num_of_element("//table[@class='table-padding-double margin-t']/tbody/tr[@ng-repeat='inv in vm.invoices | orderBy:vm.getOrderBy()']")

    class PrintDetail:
        @staticmethod
        def get_len():
            sleep(2)
            return Driver.num_of_element("//table[@class='table-padding-double margin-t']/tbody/tr[not(@class='text-bold')]")
