from selenium.webdriver.common.by import By

from src.drivers.driver import Driver
from src.elements import *


class TrialBalancePage:
    period_period_datepicker = PeriodDatepicker((By.XPATH, "//input[@id='periodRangePicker']"),
                                               (By.XPATH, "//input[@name='daterangepicker_start']"),
                                               (By.XPATH, "//input[@name='daterangepicker_end']"))
    office_select = Select((By.XPATH, "//select[../../td[.='Office']]"))
    format_radio_group = RadioGroup({
        "Standard Style": (By.XPATH, "//input[@name='report_format_default']"),
        "Display Balance by Debit/Credit": (By.XPATH, "//input[@name='report_format_balance_by_dc']"),
        "Display Currency Detail": (By.XPATH, "//input[@name='report_format_currency_detail']")
    })
    print_button = Button((By.XPATH, "//button[@class='btn bg-blue-madison']"))

    class Print:
        download_pdf_button = Button((By.XPATH, "//button[@data-original-title='Download PDF']"))
        title_label = Label((By.XPATH, "//div[text()='Trial Balance']"))
        period_label = Label((By.XPATH, "//h4"))

        class Table:
            @staticmethod
            def get_len():
                sleep(2)
                return Driver.num_of_element("//table[@class='table-padding-double']/tbody/tr[not(contains(@class, 'text-bold'))]")

            gl_no_10100_link = Link((By.XPATH, "//tr[td[1]/span/text() = '10100']/td[1]/a"))
            gl_no_10100_balance_debit_label = Label((By.XPATH, "//tr[td[1]/span/text() = '10100']/td[7]"))

            total_beginning_balance_label = Label((By.XPATH, "//td[contains(@class, 'text-right') and ../td[.='TOTAL']][1]"))
            total_debit_label = Label((By.XPATH, "//td[contains(@class, 'text-right') and ../td[.='TOTAL']][2]"))
            total_credit_label = Label((By.XPATH, "//td[contains(@class, 'text-right') and ../td[.='TOTAL']][3]"))
            total_balance_label = Label((By.XPATH, "//td[contains(@class, 'text-right') and ../td[.='TOTAL']][4]"))
