from time import sleep

from selenium.webdriver.common.by import By

from src.elements import *


class IncomeStatementPage:
    type_radio_group = RadioGroup({"Standard": (By.XPATH, "//label[contains(., 'Standard')]//input"),
                                          "By Month": (By.XPATH, "//label[contains(., 'By Month')]//input")})

    period_period_datepicker = PeriodDatepicker((By.XPATH, "//input[@daterangepicker]"),
                                               (By.XPATH, "//input[@name='daterangepicker_start']"),
                                               (By.XPATH, "//input[@name='daterangepicker_end']"))
    office_select = Select((By.XPATH, "//select[contains(@class, 'value-sm')]"))

    print_button = Button((By.XPATH, "//button[@type='button'][@class='btn bg-blue-madison']"))

    class Print:
        title_label = Label((By.XPATH, "//div[@class='header']//h5/following-sibling::div"))
        period_label = Label((By.XPATH, "//h4"))


        class Table:
            net_income_loss_label = Label((By.XPATH, "//tr[td/strong/text()='NET INCOME/LOSS']/td[2]/strong"))

            @staticmethod
            def get_len():
                sleep(2)
                return Driver.num_of_element("//tbody/tr[@class='border-b-grey']/td")
