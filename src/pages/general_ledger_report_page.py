from selenium.webdriver.common.by import By

from src.elements import *


class GeneralLedgerReportPage:
    report_type_radio_group = RadioGroup({"Summary": (By.XPATH, "//input[@name='report_type_summary']"),
                                     "Detail": (By.XPATH, "//input[@name='report_type_detail']"),
                                     "Trade Partner Summary": (By.XPATH, "//input[@name='report_type_trade_partner_summary']"),
                                     "G&A Expense": (By.XPATH, "//input[@name='report_type_ga_expense']")})
    period_period_datepicker = PeriodDatepicker((By.XPATH, "//input[@data-hc-name='gl-report-period']"),
                                               (By.XPATH, "//input[@name='daterangepicker_start']"),
                                               (By.XPATH, "//input[@name='daterangepicker_end']"))
    office_select = Select((By.XPATH, "//select[../../td[.='Office']]"))
    g_l_no_range_start_autocomplete = Autocomplete((By.XPATH, "//*[@name='gl_adv_inv_rev']"), (By.XPATH, "(//*[@name='gl_adv_inv_rev']//input)[2]"))
    g_l_no_range_end_autocomplete = Autocomplete((By.XPATH, "//*[@name='filter_gl_end']"), (By.XPATH, "(//*[@name='filter_gl_end']//input)[2]"))
    print_button = Button((By.XPATH, "//button[@data-hc-name='gl-report-print']"))

    class PrintSummary:
        title_label = Label((By.XPATH, "//div[contains(@class,'text-lg')][text()='G/L Summary']"))
        period_label = Label((By.XPATH, "//h4[@class='text-light margin-t-sm']"))

        class Table:
            @staticmethod
            def get_len():
                sleep(2)
                return Driver.num_of_element("//table[contains(@class, 'table-padding-double')]/tbody/tr/td/a[@class='item-edit']")

            total_debit_label = Label((By.XPATH, "//td[contains(@class, 'text-right') and ../td/strong[.='Total']][1]"))
            total_credit_label = Label((By.XPATH, "//td[contains(@class, 'text-right') and ../td/strong[.='Total']][2]"))
            total_balance_label = Label((By.XPATH, "//td[contains(@class, 'text-right') and ../td/strong[.='Total']][3]"))

    class PrintDetail:
        title_label = Label((By.XPATH, "//div[contains(@class,'text-lg')][contains(text(),'G/L Detail')]"))
        period_label = Label((By.XPATH, "//h4[@class='text-light margin-t-sm']"))

        class Landscape:
            class Table:
                # TODO What does 'length' mean here?
                @staticmethod
                def get_len():
                    sleep(2)
                    return Driver.num_of_element("//table[contains(@class, 'table-padding-double')]/tbody/tr")

                total_balance_label = Label((By.XPATH, "(//td[../td/strong[.='TOTAL']]/strong)[last()]"))
                total_credit_label = Label((By.XPATH, "(//td[../td/strong[.='TOTAL']]/div/span)[2]"))

        class BnEExpense:
            class Table:
                @staticmethod
                def get_len():
                    sleep(2)
                    return Driver.num_of_element("//table[contains(@class, 'table-padding-double')]/tbody/tr/td/a[@class='item-edit']")

                total_balance_label = Label((By.XPATH, "(//td[../td[.='TOTAL']]//span)[last()]"))
                total_credit_label = Label((By.XPATH, "(//td[../td[.='TOTAL']]//span)[2]"))

    class PrintTPSummary:
        title_label = Label((By.XPATH, "//div[contains(@class,'text-lg')][text()='G/L Summary (By Trade Partner)']"))
        period_label = Label((By.XPATH, "//h4[@class='text-light margin-t-sm']"))

        class Table:
            # TODO What does 'length' mean here?
            @staticmethod
            def get_len():
                sleep(2)
                return Driver.num_of_element("//table[contains(@class, 'table-padding-double')]/tbody/tr")

            total_balance_label = Label((By.XPATH, "(//td[../td/strong[.='Total']]/strong)[last()]"))

    class PrintGAExpense:
        title_label = Label((By.XPATH, "//div[contains(@class,'text-lg')][text()='The Statement of G&A Expenses']"))
        period_label = Label((By.XPATH, "//h4[@class='text-light margin-t-sm']"))

        class Table:
            @staticmethod
            def get_len():
                sleep(2)
                return Driver.num_of_element("//table[contains(@class, 'table-padding-double')]/tbody/tr/td/a[@class='item-edit']")

            total_balance_label = Label((By.XPATH, "//td[contains(@class, 'text-right') and ../td/strong[.='TOTAL']][2]"))
