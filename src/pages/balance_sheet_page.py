from selenium.webdriver.common.by import By

from src.drivers.driver import Driver
from src.elements import *


class BalanceSheetPage:
    as_of_datepicker = Datepicker((By.XPATH, "//input[@id='bs_as_of_date']"))
    office_select = Select((By.XPATH, "//select[@data-hc-name='balance-sheet-office']"))
    print_button = Button((By.XPATH, "//button[@data-hc-name='balance-sheet-print']"))

    class Print:
        title_label = Label((By.XPATH, "//div[@class='text-lg text-bold'][contains(.,'Balance Sheet')]"))
        as_of_label = Label((By.XPATH, "//h4[../div[@class='text-lg text-bold'][text()='Balance Sheet']][contains(., 'As of')]"))

        class Table:
            net_income_for_this_period_link = Link((By.XPATH, "//a[contains(text(), 'NET INCOME FOR THIS PERIOD')]"))
            net_income_for_this_period_label = Label((By.XPATH, "//tr[td/span/text()='NET INCOME FOR THIS PERIOD']/td[2]"))
            retained_earnings_label = Label((By.XPATH, "//tr[td/span/text()='RETAINED EARNINGS']/td[2]"))
            total_liabilities_and_stockholders_equity_label = Label((By.XPATH, """//td[contains(@class, 'text-right') and ../td/strong[.="TOTAL LIABILITIES AND STOCKHOLDERS' EQUITY"]]//strong"""))

            @staticmethod
            def get_len():
                sleep(2)
                return Driver.num_of_element("//table[@class='table-padding-double']/tbody/tr")
