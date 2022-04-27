import sys

sys.path.append(".")
import unittest
from datetime import datetime

import src.pages as Pages
from config import globalparameter as gl
from draft_test.helper.unittest_tool import base_setup, base_teardown
from src.api.gofreight_config import GBy, GoFreightConfig
from src.drivers.driver import Driver
from src.helper.script import login_as


class GLReportWithoutStartAndEndDate(unittest.TestCase):
    def setUp(self) -> None:
        base_setup(self)

    def tearDown(self) -> None:
        base_teardown(self)

    def test_GFACCT_1290(self):
        # go to gl report page
        Driver.open(gl.URL.GENERAL_LEDGER_REPORT)
        login_as("super_admin")
        Pages.Common.spin_bar.gone(timeout=15)

        gfc = GoFreightConfig(
            gl.companyConfig[gl.company]["url"],
            gl.companyConfig[gl.company]["sa"],
            gl.companyConfig[gl.company]["sa_password"],
        )

        dfmt = gfc.get_date_format(1, GBy.OID)
        # input period from None to Today
        end_date = datetime.strftime(datetime.now(), dfmt)
        Pages.GeneralLedgerReportPage.period_period_datepicker.input(val=f" ~ { end_date }", timeout=10)
        Pages.GeneralLedgerReportPage.print_button.click()
        Driver.switch_to(window_index=1)

        TIMEOUT = 300

        if Pages.GeneralLedgerReportPage.PrintSummary.title_label.is_visible(timeout=TIMEOUT):
            print_item_count = Pages.GeneralLedgerReportPage.PrintSummary.Table.get_len()
            print_period_title = Pages.GeneralLedgerReportPage.PrintSummary.period_label.get_value()
            period_date_text = "Period: {0} ~ {1}".format("[First Record]", end_date)
            if print_item_count <= 0:
                assert False, "No items show on the gl report print."
            if print_period_title != period_date_text:
                assert False, "Period title [{0}] is not equal to [{1}] on the gl report print.".format(
                    print_period_title, period_date_text
                )
        else:
            assert False, "Waitimg for {} sec and no items show".format(TIMEOUT)

        self.chrome_console_log = Driver.get_console_logs()

        # ? Bug GFACCT-1275
        self.chrome_console_log = self.filt_GFACCT_1275(self.chrome_console_log)
        # ?
        assert self.chrome_console_log == [], "\n".join(
            "{0}. {1}".format(msg[0], msg[1]) for msg in enumerate(self.chrome_console_log, start=1)
        )

    def test_GFACCT_1295(self):
        # go to gl report page
        Driver.open(gl.URL.GENERAL_LEDGER_REPORT)
        login_as("super_admin")
        Pages.Common.spin_bar.gone(timeout=15)

        gfc = GoFreightConfig(
            gl.companyConfig[gl.company]["url"],
            gl.companyConfig[gl.company]["sa"],
            gl.companyConfig[gl.company]["sa_password"],
        )

        gfc.get_date_format(1, GBy.OID)
        # input period from None to None
        Pages.GeneralLedgerReportPage.period_period_datepicker.input(val=" ~ ", timeout=10)
        Pages.GeneralLedgerReportPage.print_button.click()
        Driver.switch_to(window_index=1)

        TIMEOUT = 300

        if Pages.GeneralLedgerReportPage.PrintSummary.title_label.is_visible(timeout=TIMEOUT):
            print_item_count = Pages.GeneralLedgerReportPage.PrintSummary.Table.get_len()
            print_period_title = Pages.GeneralLedgerReportPage.PrintSummary.period_label.get_value()
            period_date_text = "Period: {0} ~ {1}".format("[First Record]", "[Last Record]")
            if print_item_count <= 0:
                assert False, "No items show on the gl report print."
            if print_period_title != period_date_text:
                assert False, "Period title [{0}] is not equal to [{1}] on the gl report print.".format(
                    print_period_title, period_date_text
                )
        else:
            assert False, "Waitimg for {} sec and no items show".format(TIMEOUT)

        self.chrome_console_log = Driver.get_console_logs()

        # ? Bug GFACCT-1275
        self.chrome_console_log = self.filt_GFACCT_1275(self.chrome_console_log)
        # ?
        assert self.chrome_console_log == [], "\n".join(
            "{0}. {1}".format(msg[0], msg[1]) for msg in enumerate(self.chrome_console_log, start=1)
        )

    @staticmethod
    def filt_GFACCT_1275(chrome_console_log: list) -> bool:
        # caused by sentry api
        # remove knwon issue
        error_msg_1 = "No 'Access-Control-Allow-Origin' header is present on the requested resource."
        error_msg_2 = "Failed to load resource: net::ERR_FAILED"
        error_msgs = [error_msg_1, error_msg_2]
        for em in error_msgs:
            for log in chrome_console_log:
                if em in log["message"]:
                    chrome_console_log.remove(log)

        return chrome_console_log
