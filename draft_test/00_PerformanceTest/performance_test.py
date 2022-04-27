import sys

sys.path.append(".")
import re
import shutil
import time
import unittest
from datetime import datetime
from pathlib import Path
from time import sleep

import yaml
from dateutil.relativedelta import relativedelta

import chromedriver.chrome_helper as chrome_helper
import src.pages as Pages
from config import globalparameter as gl
from draft_test.helper.unittest_tool import *
from src.drivers.driver import Driver
from src.helper.gsheet import GSpreadSheet, GWorkSheet
from src.helper.log import Logger
from src.helper.script import login_as
from src.helper.slack_feeder import SlackFeeder

TIME = datetime.now()

FAIL_MSG_FORMAT = """
*{test_naem}* `No.{index}` is Failed :scream_cat:\n \
  *1. Test Server:* {test_server} \n \
  *2. Company:* {company} \n \
  *3. Period:* {start_date} ~ {end_date} \n \
  *4. GSheet ({tab_name}):* <{gsheet_url}> \n \
  *5. Mode:* {mode} \n \
  *6. Test Time:* {test_time} \n \
  *7. Message:* ```{msg}```
"""

GSHEET_RECORD_KEY_INDEX = 0


class PerformanceTestForReport(unittest.TestCase):
    def __init__(
        self,
        test_name,
        test_server,
        company,
        start_date,
        end_date,
        monitor,
        worksheet: GWorkSheet,
        mode,
        index,
        option={},
        timeout=300,
    ):
        super(PerformanceTestForReport, self).__init__(test_name)
        self.TEST_NAME = test_name
        self.SERVER_URL = test_server
        self.COMPANY = company
        self.START_DATE = start_date
        self.END_DATE = end_date
        self.MONITOR = monitor
        self.MODE = mode
        self.INDEX = index
        self.OPTION = option
        self.TIMEOUT = timeout

        self.worksheet = worksheet
        self.gsr = worksheet.init_row_record()
        self.chrome_console_log = []
        self.period = ""
        self.spend_time = ""
        self.test_status = TestStatus(TestStatus.Status.PASS)

    def setUp(self) -> None:
        gl.read_company_config_files()
        gl.company = self.COMPANY
        gl.init_url(custom_base_url=self.SERVER_URL)
        chrome_helper.check_browser_driver_available()
        Driver("Chrome_1", chrome_helper.get_driver_path(), monitor=self.MONITOR)
        print("\n")  # for verbosity=2 formatting

    def tearDown(self) -> None:
        # Check for interruptions caused by other factors (script problems)
        failure_msg = check_testcase_error(self)
        if failure_msg:
            self.test_status.Broken(failure_msg)

        # check browser console log
        for log in self.chrome_console_log:
            if log["level"] == "SEVERE":
                self.test_status.Warning("Error occured in the browser console log")

        # send test result to gsheet
        if options.report == "one-time":
            Logger.getLogger().info("Sending test result to gsheet ... {}".format(self.worksheet.url))
            records = [
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "{}-No.{}".format(self.TEST_NAME, self.INDEX),
                self.COMPANY,
                self.test_status.print_status(),
                self.period,
                self.spend_time,
                self.SERVER_URL,
                self.test_status.print_msg(),
                self.chrome_console_log if self.chrome_console_log else "",
            ]
            for i in range(len(records)):
                col = i + 1  # col 0 is for key
                self.gsr.set(col, records[i])
            self.worksheet.send_record(self.gsr)

        # if test not pass, send msg to the slack channel
        if not self.test_status.is_pass():
            with open(gl.slack_channel_path, encoding="UTF-8") as f:
                slack_channel = yaml.safe_load(f)
            msg = FAIL_MSG_FORMAT.format(
                test_naem=self.TEST_NAME,
                index=self.INDEX,
                test_server=self.SERVER_URL,
                company=self.COMPANY,
                start_date=self.START_DATE,
                end_date=self.END_DATE,
                tab_name=self.worksheet.title,
                gsheet_url=self.worksheet.url,
                mode=self.MODE,
                test_time=self.gsr.key,
                msg=self.test_status.print_msg(),
            )

            scrennshot_name = str(self.INDEX) + "_error.png"
            folder_name = "{0}~{1}".format(self.START_DATE, self.END_DATE)
            error_screenshot = Path(__file__).parent / "screenshot" / "error" / folder_name / scrennshot_name
            Driver.get_screenshot_for_all_windows(error_screenshot)
            SlackFeeder.post_file(
                path=str(error_screenshot),
                channels=slack_channel["performance-test"]["name"],
                file_title="Error screenshot",
                filename="error.png",
                msg=msg,
            )

            # also send the log file
            SlackFeeder.post_file(
                path=Logger.getFilePath(),
                channels=slack_channel["performance-test"]["name"],
                file_title="Log",
                filename="log.txt",
            )

        Driver.quit()

    def test_volume_profit_chart_period_loading_performance(self):
        Logger.getLogger().info("Start Test: [{}] - {}".format(self._testMethodName, self.INDEX))
        Logger.getLogger().info("Test Period: [{0}] ~ [{1}]".format(self.START_DATE, self.END_DATE))

        # go to volume&profit chart page
        Driver.open(gl.URL.VOLUME_AND_PROFIT_CHART)
        login_as("super_admin")
        Pages.Common.spin_bar.gone(timeout=60)

        # input period and submit
        Pages.VolumeAndProfitChartPage.period_period_datepicker.input(f"{ self.START_DATE } ~ { self.END_DATE }")
        Pages.VolumeAndProfitChartPage.view_button.click()

        # count loading time
        timer_start = time.time()
        Pages.Common.spin_bar.gone(timeout=self.TIMEOUT)
        timer_end = time.time()

        if Pages.Common.spin_bar.is_visible():
            self.test_status.Warning("After counting loading time, the spin bar is still exist.")

        # collect log of browser
        self.chrome_console_log = Driver.get_console_logs()

        # show the test result
        period = Pages.VolumeAndProfitChartPage.period_period_datepicker.get_value()
        spend_sec = timer_end - timer_start
        spend_time = time.strftime(r"%M:%S", time.gmtime(spend_sec))
        Logger.getLogger().info(" Test Result ".center(80, "-"))
        Logger.getLogger().info("Period: {}".format(period).ljust(80))
        Logger.getLogger().info("Spend (m:s): {}".format(spend_time).ljust(80))
        Logger.getLogger().info("Spend (sec): {:.2f}".format(spend_sec).ljust(80))
        Logger.getLogger().info("Chrome Console Log: {}".format(self.chrome_console_log).ljust(80))
        Logger.getLogger().info("-" * 80)

        # save test result
        self.period = period
        self.spend_time = spend_time

        self.assertTrue(
            "{0} ~ {1}".format(self.START_DATE, self.END_DATE) == self.period,
            msg="The testing start_date({0}) and end_date({1}) is not equal to Period({2}) in webpage.".format(
                self.START_DATE, self.END_DATE, self.period
            ),
        )

        Logger.getLogger().info("Performance test end")

    def test_trial_balance_loading_performance(self):
        Logger.getLogger().info("Start Test: [{}] - {}".format(self._testMethodName, self.INDEX))
        Logger.getLogger().info("Test Period: [{0}] ~ [{1}]".format(self.START_DATE, self.END_DATE))

        # go to trial balance chart page
        Driver.open(gl.URL.TRIAL_BALANCE)
        login_as("super_admin")
        Pages.Common.spin_bar.gone(timeout=15)

        # input period and submit
        Pages.TrialBalancePage.period_period_datepicker.input(f"{ self.START_DATE } ~ { self.END_DATE }")
        Pages.TrialBalancePage.print_button.click()
        Driver.switch_to(window_index=1)

        # count loading time
        timer_start = time.time()
        seconds = self.TIMEOUT
        while True:
            current_time = time.time()
            elapsed_time = current_time - timer_start
            self.chrome_console_log = Driver.get_console_logs()
            if Pages.TrialBalancePage.Print.title_label.is_visible(timeout=10):
                print_item_count = Pages.TrialBalancePage.Print.Table.get_len()
                print_period_title = Pages.TrialBalancePage.Print.period_label.get_value()
                if print_item_count <= 0:
                    self.test_status.Warning("No items show on the tracking balance print.")
                if print_period_title != "Period: {0} ~ {1}".format(self.START_DATE, self.END_DATE):
                    self.test_status.Warning(
                        "Period title [{}] is not correct on the trial balance print.".format(print_period_title)
                    )
                break
            elif Driver.is_text_in_page_source("502 Bad Gateway"):
                self.test_status.Fail("502 Bad Gateway")
                break
            elif Driver.is_text_in_page_source("504 Bad Gateway"):
                self.test_status.Fail("504 Bad Gateway")
                break
            elif elapsed_time > seconds:
                self.test_status.Fail("Wait to {} sec timeout".format(seconds))
                break
            else:
                continue
        timer_end = time.time()

        Driver.switch_to(window_index=0)

        # show the test result
        period = Pages.TrialBalancePage.period_period_datepicker.get_value()
        spend_sec = timer_end - timer_start
        spend_time = time.strftime(r"%M:%S", time.gmtime(spend_sec))
        Logger.getLogger().info(" Test Result ".center(80, "-"))
        Logger.getLogger().info("Period: {}".format(period).ljust(80))
        Logger.getLogger().info("Spend (m:s): {}".format(spend_time).ljust(80))
        Logger.getLogger().info("Spend (sec): {:.2f}".format(spend_sec).ljust(80))
        Logger.getLogger().info("Chrome Console Log: {}".format(self.chrome_console_log).ljust(80))
        Logger.getLogger().info("-" * 80)

        # save test result
        self.period = period
        self.spend_time = spend_time

        self.assertTrue(
            "{0} ~ {1}".format(self.START_DATE, self.END_DATE) == self.period,
            msg="The testing start_date({0}) and end_date({1}) is not equal to Period({2}) in webpage.".format(
                self.START_DATE, self.END_DATE, self.period
            ),
        )

        # ? Bug GFACCT-1275
        self.chrome_console_log = self.filt_GFACCT_1275(self.chrome_console_log)
        # ?

        Logger.getLogger().info("Performance test end")

    def test_volume_profit_report_loading_performance(self):
        Logger.getLogger().info("Start Test: [{}] - {}".format(self._testMethodName, self.INDEX))
        Logger.getLogger().info("Test Period: [{0}] ~ [{1}]".format(self.START_DATE, self.END_DATE))

        # go to volume&profit report page
        Driver.open(gl.URL.VOLUME_AND_PROFIT_REPORT)
        login_as("super_admin")
        Pages.Common.spin_bar.gone(timeout=30)

        # input period and submit
        Pages.VolumeAndProfitReportPage.period_period_datepicker.input(f"{ self.START_DATE } ~ { self.END_DATE }")
        Pages.VolumeAndProfitReportPage.view_button.click()

        # count loading time
        timer_start = time.time()
        Pages.Common.spin_bar.gone(timeout=self.TIMEOUT)
        timer_end = time.time()

        if Pages.Common.spin_bar.is_visible():
            self.test_status.Warning("After counting loading time, the spin bar is still exist.")
        if Pages.VolumeAndProfitReportPage.table.get_len() == 0:
            self.test_status.Warning("No elements show on the table")

        Driver.go_to_position(0, 200)

        # collect log of browser
        self.chrome_console_log = Driver.get_console_logs()

        # show the test result
        period = Pages.VolumeAndProfitReportPage.period_period_datepicker.get_value()
        spend_sec = timer_end - timer_start
        spend_time = time.strftime(r"%M:%S", time.gmtime(spend_sec))
        Logger.getLogger().info(" Test Result ".center(80, "-"))
        Logger.getLogger().info("Period: {}".format(period).ljust(80))
        Logger.getLogger().info("Spend (m:s): {}".format(spend_time).ljust(80))
        Logger.getLogger().info("Spend (sec): {:.2f}".format(spend_sec).ljust(80))
        Logger.getLogger().info("Chrome Console Log: {}".format(self.chrome_console_log).ljust(80))
        Logger.getLogger().info("-" * 80)

        # save test result
        self.period = period
        self.spend_time = spend_time

        self.assertTrue(
            "{0} ~ {1}".format(self.START_DATE, self.END_DATE) == self.period,
            msg="The testing start_date({0}) and end_date({1}) is not equal to Period({2}) in webpage.".format(
                self.START_DATE, self.END_DATE, self.period
            ),
        )

        Logger.getLogger().info("Performance test end")

    def test_general_ledger_report_loading_performance(self):
        Logger.getLogger().info("Start Test: [{}] - {}".format(self._testMethodName, self.INDEX))
        Logger.getLogger().info("Test Period: [{0}] ~ [{1}]".format(self.START_DATE, self.END_DATE))

        # go to gl report page
        Driver.open(gl.URL.GENERAL_LEDGER_REPORT)
        login_as("super_admin")
        Pages.Common.spin_bar.gone(timeout=15)

        # select Report Type
        if self.OPTION["Report Type"] == 1:
            Pages.GeneralLedgerReportPage.report_type_radio_group.click("Summary")
        elif self.OPTION["Report Type"] == 2:
            Pages.GeneralLedgerReportPage.report_type_radio_group.click("Detail")

        # input period and submit
        Pages.GeneralLedgerReportPage.period_period_datepicker.input(f"{ self.START_DATE } ~ { self.END_DATE }")
        Pages.GeneralLedgerReportPage.print_button.click()
        Driver.switch_to(window_index=1)

        # count loading time
        timer_start = time.time()
        seconds = self.TIMEOUT
        while True:
            current_time = time.time()
            elapsed_time = current_time - timer_start
            self.chrome_console_log = Driver.get_console_logs()
            if self.OPTION["Report Type"] == 1:
                if Pages.GeneralLedgerReportPage.PrintSummary.title_label.is_visible(timeout=10):
                    print_item_count = Pages.GeneralLedgerReportPage.PrintSummary.Table.get_len()
                    print_period_title = Pages.GeneralLedgerReportPage.PrintSummary.period_label.get_value()
                    if print_item_count <= 0:
                        self.test_status.Warning("No items show on the gl report print.")
                    if print_period_title != "Period: {0} ~ {1}".format(self.START_DATE, self.END_DATE):
                        self.test_status.Warning(
                            "Period title [{}] is not correct on the gl report print.".format(print_period_title)
                        )
                    break
            elif self.OPTION["Report Type"] == 2:
                if Pages.GeneralLedgerReportPage.PrintDetail.title_label.is_visible(timeout=10):
                    print_item_count = Pages.GeneralLedgerReportPage.PrintDetail.Table.get_len()
                    print_period_title = Pages.GeneralLedgerReportPage.PrintDetail.period_label.get_value()
                    if print_item_count <= 0:
                        self.test_status.Warning("No items show on the gl report print.")
                    if print_period_title != "Period: {0} ~ {1}".format(self.START_DATE, self.END_DATE):
                        self.test_status.Warning(
                            "Period title [{}] is not correct on the gl report print.".format(print_period_title)
                        )
                    break
            elif Driver.is_text_in_page_source("502 Bad Gateway"):
                self.test_status.Fail("502 Bad Gateway")
                break
            elif Driver.is_text_in_page_source("504 Bad Gateway"):
                self.test_status.Fail("504 Bad Gateway")
                break
            elif elapsed_time > seconds:
                self.test_status.Fail("Wait to {} sec timeout".format(seconds))
                break
            else:
                continue
        timer_end = time.time()

        Driver.switch_to(window_index=0)

        # show the test result
        period = Pages.GeneralLedgerReportPage.period_period_datepicker.get_value()
        spend_sec = timer_end - timer_start
        spend_time = time.strftime(r"%M:%S", time.gmtime(spend_sec))
        Logger.getLogger().info(" Test Result ".center(80, "-"))
        Logger.getLogger().info("Period: {}".format(period).ljust(80))
        Logger.getLogger().info("Spend (m:s): {}".format(spend_time).ljust(80))
        Logger.getLogger().info("Spend (sec): {:.2f}".format(spend_sec).ljust(80))
        Logger.getLogger().info("Chrome Console Log: {}".format(self.chrome_console_log).ljust(80))
        Logger.getLogger().info("-" * 80)

        # save test result
        self.period = period
        self.spend_time = spend_time

        self.assertTrue(
            "{0} ~ {1}".format(self.START_DATE, self.END_DATE) == self.period,
            msg="The testing start_date({0}) and end_date({1}) is not equal to Period({2}) in webpage.".format(
                self.START_DATE, self.END_DATE, self.period
            ),
        )

        # ? Bug GFACCT-1275
        self.chrome_console_log = self.filt_GFACCT_1275(self.chrome_console_log)
        # ?

        Logger.getLogger().info("Performance test end")

    def test_agent_local_statement_loading_performance(self):
        Logger.getLogger().info("Start Test: [{}] - {}".format(self._testMethodName, self.INDEX))
        Logger.getLogger().info("Test Period: [{0}] ~ [{1}]".format(self.START_DATE, self.END_DATE))

        # clear the pdf and excel folder
        pdf_folder = Path(__file__).parent / "pdf"
        excel_folder = Path(__file__).parent / "excel"
        if pdf_folder.is_dir():
            shutil.rmtree(str(pdf_folder))
        if excel_folder.is_dir():
            shutil.rmtree(str(excel_folder))

        # go to AL statement page
        Driver.open(gl.URL.AGENT_LOCAL_STATEMENT)
        login_as("super_admin")
        Pages.Common.spin_bar.gone(timeout=15)

        # select Partner type and input partner
        Pages.AgentLocalStatementPage.partner_type_radio_group.click("Account Group")
        Pages.AgentLocalStatementPage.partner_autocomplete.input("CIF")

        # input Period
        Pages.AgentLocalStatementPage.period_period_datepicker.input(f"{ self.START_DATE } ~ { self.END_DATE }")

        # select Filter by
        Pages.AgentLocalStatementPage.filter_by_radio_group.click("All")

        # click search and calculate time
        Pages.AgentLocalStatementPage.search_button.click()

        if self.OPTION["Test Stage"] == 1:
            # count loading time
            timer_start = time.time()
            Pages.Common.spin_bar.gone(timeout=self.TIMEOUT)
            timer_end = time.time()
            self.chrome_console_log = Driver.get_console_logs()
            self.assertFalse(
                Pages.Common.spin_bar.is_visible(timeout=1),
                "The spin bar is still exist.",
            )
        else:
            Pages.Common.spin_bar.gone(timeout=300)

            self.assertFalse(
                Pages.Common.spin_bar.is_visible(timeout=1),
                "The spin bar is still exist.",
            )
            if Pages.AgentLocalStatementPage.invoice_table.get_len() == 0:
                self.test_status.Fail("No item appear in invoice table")

            # select all invoice
            Pages.AgentLocalStatementPage.invoice_table.check_all_checkbox.tick(True)

            # tick attach original invoice(s)
            Pages.AgentLocalStatementPage.attach_original_invoices_checkbox.tick(True)

        if self.OPTION["Test Stage"] == 2:
            # click view buttno and count loading time
            Pages.AgentLocalStatementPage.view_button.click()

            # count loading time
            timer_start = time.time()
            Pages.Common.spin_bar.gone(timeout=60)
            Driver.switch_to(window_index=1)
            Pages.Common.spin_bar.gone(timeout=self.TIMEOUT)
            timer_end = time.time()

            self.assertFalse(
                Pages.Common.spin_bar.is_visible(timeout=1),
                "Wait {} sec and the spin bar is still exist.".format(self.TIMEOUT),
            )
            # TODO: 抓不到元素該如何檢查顯示是否正常？
            # Pages.AgentLocalStatementPage.print.table_title_label.is_visible(20)
            # if Pages.AgentLocalStatementPage.print.get_len() == 0:
            #     self.test_status.Fail("No item appear in AL Statement Print table")
            self.chrome_console_log = Driver.get_console_logs()

            Driver.switch_to(window_index=0)

        if self.OPTION["Test Stage"] == 3:
            Driver.set_download_path(Path(__file__).parent / "pdf")
            Pages.AgentLocalStatementPage.downlaod_pdf_button.click()

            # count loading time
            timer_start = time.time()
            Pages.Common.spin_bar.gone(timeout=self.TIMEOUT)
            timer_end = time.time()

            if Pages.Common.spin_bar.is_visible():
                self.test_status.Warning("After counting loading time, the spin bar is still exist.")
                assert False, "GoFreight download processing is waiting for {} sec".format(self.TIMEOUT)

            # check download file is exist
            timer = time.time()
            seconds = 300
            while True:
                current_time = time.time()
                elapsed_time = current_time - timer
                file = Path(__file__).parent / "pdf" / "Agent Local Statement - CIF.pdf"
                if file.is_file() == True:
                    Logger.getLogger().info("Downloading pdf is success")
                    file.unlink()
                    break
                elif elapsed_time > seconds:
                    self.test_status.Fail("Download pdf timeout ({} sec)".format(seconds))
                    break
                else:
                    continue
            self.chrome_console_log = Driver.get_console_logs()

        if self.OPTION["Test Stage"] == 4:
            Driver.set_download_path(Path(__file__).parent / "excel")
            Pages.AgentLocalStatementPage.downlaod_excel_button.click()

            # count loading time
            timer_start = time.time()
            Pages.Common.spin_bar.gone(timeout=self.TIMEOUT)
            timer_end = time.time()

            if Pages.Common.spin_bar.is_visible():
                self.test_status.Warning("After counting loading time, the spin bar is still exist.")
                assert False, "GoFreight download processing is waiting for {} sec".format(self.TIMEOUT)

            # check download file is exist
            timer = time.time()
            seconds = 300
            while True:
                current_time = time.time()
                elapsed_time = current_time - timer
                file = (
                    Path(__file__).parent
                    / "excel"
                    / "Agent_Local_Statement_Report_{}.xlsx".format(TIME.strftime(r"%m-%d-%Y"))
                )
                if file.is_file() == True:
                    Logger.getLogger().info("Downloading excel is success")
                    file.unlink()
                    break
                elif elapsed_time > seconds:
                    self.test_status.Fail("Download excel timeout ({} sec)".format(seconds))
                    break
                else:
                    continue
            self.chrome_console_log = Driver.get_console_logs()

        if self.OPTION["Test Stage"] == 5:
            Driver.set_download_path(Path(__file__).parent / "pdf")
            Pages.AgentLocalStatementPage.downlaod_pdf_button.click()
            Pages.Common.spin_bar.gone(timeout=600)

            if Pages.Common.spin_bar.is_visible():
                self.test_status.Warning("After counting loading time, the spin bar is still exist.")
                assert False, "GoFreight download processing is waiting for {} sec".format(self.TIMEOUT)

            Driver.refresh()
            Pages.AgentLocalStatementPage.generated_document_list(1).action_button.click()
            Pages.AgentLocalStatementPage.generated_document_list(1).reload_button.click()
            # count loading time
            timer_start = time.time()
            Pages.Common.spin_bar.gone(timeout=self.TIMEOUT)
            timer_end = time.time()
            # check result
            self.assertTrue(
                Pages.AgentLocalStatementPage.partner_type_radio_group.get_value() == "Account Group",
                "Partner Type should be [Account Group]",
            )
            self.assertTrue(
                Pages.AgentLocalStatementPage.partner_autocomplete.get_value() == "CIF",
                "Partner should be [CIF]",
            )
            self.assertTrue(
                Pages.AgentLocalStatementPage.period_period_datepicker.get_value()
                == "{0} ~ {1}".format(self.START_DATE, self.END_DATE),
                "Period should be [{0} ~ {1}]".format(self.START_DATE, self.END_DATE),
            )
            self.assertTrue(
                Pages.AgentLocalStatementPage.filter_by_radio_group.get_value() == "All",
                "Filter by should be [All]",
            )
            if Pages.AgentLocalStatementPage.invoice_table.get_len() == 0:
                self.test_status.Fail("No item appear in invoice table when reload generated document")
            self.chrome_console_log = Driver.get_console_logs()

        # show the test result
        period = Pages.AgentLocalStatementPage.period_period_datepicker.get_value()
        spend_sec = timer_end - timer_start
        spend_time = time.strftime(r"%M:%S", time.gmtime(spend_sec))
        Logger.getLogger().info(" Test Result ".center(80, "-"))
        Logger.getLogger().info("Period: {}".format(period).ljust(80))
        Logger.getLogger().info("Spend (m:s): {}".format(spend_time).ljust(80))
        Logger.getLogger().info("Spend (sec): {:.2f}".format(spend_sec).ljust(80))
        Logger.getLogger().info("Chrome Console Log: {}".format(self.chrome_console_log).ljust(80))
        Logger.getLogger().info("-" * 80)

        # save test result
        self.period = period
        self.spend_time = spend_time

        self.assertTrue(
            "{0} ~ {1}".format(self.START_DATE, self.END_DATE) == self.period,
            msg="The testing start_date({0}) and end_date({1}) is not equal to Period({2}) in webpage.".format(
                self.START_DATE, self.END_DATE, self.period
            ),
        )

        Logger.getLogger().info("Performance test end")

    def test_aging_report_loading_performance(self):
        Logger.getLogger().info("Start Test: [{}] - {}".format(self._testMethodName, self.INDEX))
        Logger.getLogger().info("Test Period: [{0}] ~ [{1}]".format(self.START_DATE, self.END_DATE))

        # go to aging report page
        Driver.open(gl.URL.AGING_REPORT)
        login_as("super_admin")
        Pages.Common.spin_bar.gone(timeout=15)
        sleep(2)  # 2021/08/19 not detect element, so add sleep() for it

        # input Ending Date
        Pages.AgingReportPage.ending_date_period_type_select.select("Range")
        Pages.AgingReportPage.ending_date_period_datepicker.input(f"{ self.START_DATE } ~ { self.END_DATE }")

        # select Report Type
        if self.OPTION["Report Type"] == 1:
            Pages.AgingReportPage.report_type_radio_group.click("Summary")
        elif self.OPTION["Report Type"] == 2:
            Pages.AgingReportPage.report_type_radio_group.click("Detail")

        if self.OPTION["Test Stage"] == 1:
            Pages.AgingReportPage.search_button.click()

            # count loading time
            timer_start = time.time()
            Pages.Common.spin_bar.gone(timeout=self.TIMEOUT)
            timer_end = time.time()

            if Pages.AgingReportPage.Table.get_len() == 0:
                self.test_status.Fail("No item show on the table when click 'Search' button")
            self.chrome_console_log = Driver.get_console_logs()

        elif self.OPTION["Test Stage"] == 2:
            Pages.AgingReportPage.print_button.click()
            Driver.switch_to(window_index=1)

            # count loading time
            timer_start = time.time()
            Pages.Common.spin_bar.gone(timeout=self.TIMEOUT)
            timer_end = time.time()

            if self.OPTION["Report Type"] == 1:
                item_count = Pages.AgingReportPage.PrintSummary.get_len()
            elif self.OPTION["Report Type"] == 2:
                item_count = Pages.AgingReportPage.PrintDetail.get_len()

            if item_count == 0:
                self.test_status.Warning("No item show on the table when click 'Print' button")
            self.chrome_console_log = Driver.get_console_logs()

            Driver.switch_to(window_index=0)

        # show the test result
        period = Pages.AgingReportPage.ending_date_period_datepicker.get_value()
        spend_sec = timer_end - timer_start
        spend_time = time.strftime(r"%M:%S", time.gmtime(spend_sec))
        Logger.getLogger().info(" Test Result ".center(80, "-"))
        Logger.getLogger().info("Period: {}".format(period).ljust(80))
        Logger.getLogger().info("Spend (m:s): {}".format(spend_time).ljust(80))
        Logger.getLogger().info("Spend (sec): {:.2f}".format(spend_sec).ljust(80))
        Logger.getLogger().info("Chrome Console Log: {}".format(self.chrome_console_log).ljust(80))
        Logger.getLogger().info("-" * 80)

        # save test result
        self.period = period
        self.spend_time = spend_time

        self.assertTrue(
            "{0} ~ {1}".format(self.START_DATE, self.END_DATE) == self.period,
            msg="The testing start_date({0}) and end_date({1}) is not equal to Period({2}) in webpage.".format(
                self.START_DATE, self.END_DATE, self.period
            ),
        )

        Logger.getLogger().info("Performance test end")

    def test_income_statement_loading_performance(self):
        Logger.getLogger().info("Start Test: [{}] - {}".format(self._testMethodName, self.INDEX))
        Logger.getLogger().info("Test Period: [{0}] ~ [{1}]".format(self.START_DATE, self.END_DATE))

        # go to Income Statement page
        Driver.open(gl.URL.INCOME_STATEMENT)
        login_as("super_admin")
        Pages.Common.spin_bar.gone(timeout=15)
        sleep(2)  # 2021/08/19 not detect element, so add sleep() for it

        # input Period
        Pages.IncomeStatementPage.period_period_datepicker.input(f"{ self.START_DATE } ~ { self.END_DATE }")

        Pages.IncomeStatementPage.print_button.click()
        Driver.switch_to(window_index=1)

        # count loading time
        timer_start = time.time()
        Pages.IncomeStatementPage.Print.title_label.is_visible(self.TIMEOUT)
        Pages.IncomeStatementPage.Print.period_label.is_visible()
        timer_end = time.time()

        if Pages.IncomeStatementPage.Print.Table.get_len() == 0:
            self.test_status.Warning("No items show on the Print")

        self.chrome_console_log = Driver.get_console_logs()
        Driver.switch_to(window_index=0)

        # show the test result
        period = Pages.IncomeStatementPage.period_period_datepicker.get_value()
        spend_sec = timer_end - timer_start
        spend_time = time.strftime(r"%M:%S", time.gmtime(spend_sec))
        Logger.getLogger().info(" Test Result ".center(80, "-"))
        Logger.getLogger().info("Period: {}".format(period).ljust(80))
        Logger.getLogger().info("Spend (m:s): {}".format(spend_time).ljust(80))
        Logger.getLogger().info("Spend (sec): {:.2f}".format(spend_sec).ljust(80))
        Logger.getLogger().info("Chrome Console Log: {}".format(self.chrome_console_log).ljust(80))
        Logger.getLogger().info("-" * 80)

        # save test result
        self.period = period
        self.spend_time = spend_time

        self.assertTrue(
            "{0} ~ {1}".format(self.START_DATE, self.END_DATE) == self.period,
            msg="The testing start_date({0}) and end_date({1}) is not equal to Period({2}) in webpage.".format(
                self.START_DATE, self.END_DATE, self.period
            ),
        )

        # ? Bug GFACCT-1275
        self.chrome_console_log = self.filt_GFACCT_1275(self.chrome_console_log)
        # ?

        Logger.getLogger().info("Performance test end")

    def test_journal_report_loading_performance(self):
        Logger.getLogger().info("Start Test: [{}] - {}".format(self._testMethodName, self.INDEX))
        Logger.getLogger().info("Test Period: [{0}] ~ [{1}]".format(self.START_DATE, self.END_DATE))

        # go to Income Statement page
        Driver.open(gl.URL.JOURNAL_REPORT)
        login_as("super_admin")
        Pages.Common.spin_bar.gone(timeout=15)
        sleep(2)  # 2021/08/19 not detect element, so add sleep() for it

        # input Period
        Pages.JournalReportPage.period_period_datepicker.input(f"{ self.START_DATE } ~ { self.END_DATE }")

        Pages.JournalReportPage.print_button.click()
        Driver.switch_to(window_index=1)

        # count loading time
        timer_start = time.time()
        Pages.JournalReportPage.Print.title_label.is_visible(self.TIMEOUT)
        Pages.JournalReportPage.Print.period_label.is_visible()
        timer_end = time.time()

        if Pages.JournalReportPage.Print.get_len() == 0:
            self.test_status.Warning("No items show on the Print")

        self.chrome_console_log = Driver.get_console_logs()
        Driver.switch_to(window_index=0)

        # show the test result
        period = Pages.JournalReportPage.period_period_datepicker.get_value()
        spend_sec = timer_end - timer_start
        spend_time = time.strftime(r"%M:%S", time.gmtime(spend_sec))
        Logger.getLogger().info(" Test Result ".center(80, "-"))
        Logger.getLogger().info("Period: {}".format(period).ljust(80))
        Logger.getLogger().info("Spend (m:s): {}".format(spend_time).ljust(80))
        Logger.getLogger().info("Spend (sec): {:.2f}".format(spend_sec).ljust(80))
        Logger.getLogger().info("Chrome Console Log: {}".format(self.chrome_console_log).ljust(80))
        Logger.getLogger().info("-" * 80)

        # save test result
        self.period = period
        self.spend_time = spend_time

        self.assertTrue(
            "{0} ~ {1}".format(self.START_DATE, self.END_DATE) == self.period,
            msg="The testing start_date({0}) and end_date({1}) is not equal to Period({2}) in webpage.".format(
                self.START_DATE, self.END_DATE, self.period
            ),
        )

        # ? Bug GFACCT-1275
        self.chrome_console_log = self.filt_GFACCT_1275(self.chrome_console_log)
        # ?

        Logger.getLogger().info("Performance test end")

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


class TestOptions:
    def __init__(
        self,
        test_name: str = None,
        test_server: str = None,
        company: str = None,
        test_start: datetime = None,
        test_end: datetime = None,
        time_step: relativedelta = None,
        seq: str = "asc",
        monitor: int = 0,
        gsheet_tab_name: str = "Performance",
        mode="section",
        report="1",
        timeout="0:5:0",
    ):
        self._test_name = test_name
        self._test_server = test_server
        self._company = company
        self._test_start = test_start
        self._test_end = test_end
        self._time_step = time_step
        self._seq = seq
        self._monitor = monitor
        self._gsheet_tab_name = gsheet_tab_name
        self._mode = mode
        self._report = report
        self._timeout = timeout

    @property
    def test_name(self):
        return self._test_name

    @test_name.setter
    def test_name(self, value):
        testcases = get_testcases_name(PerformanceTestForReport)
        if type(value) is str and value in testcases:
            self._test_name = value
        else:
            raise Exception("Invalid test_name.")

    @property
    def test_server(self):
        return self._test_server

    @test_server.setter
    def test_server(self, value):
        self._test_server = str(value)

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, value):
        self._company = str(value)

    @property
    def test_start(self):
        return self._test_start

    @test_start.setter
    def test_start(self, value):
        if type(value) is str:
            self._test_start = datetime.strptime(value, "%Y-%m-%d")
        elif type(value) is datetime:
            self._test_start = value
        else:
            raise Exception("Invalid test_start type.")

    @property
    def test_end(self):
        return self._test_end

    @test_end.setter
    def test_end(self, value):
        if type(value) is str:
            self._test_end = datetime.strptime(value, "%Y-%m-%d")
        elif type(value) is datetime:
            self._test_end = value
        else:
            raise Exception("Invalid test_end type.")

    @property
    def time_step(self):
        return self._time_step

    @time_step.setter
    def time_step(self, value):
        if type(value) is str:
            year, month, day = re.match(r"(\d+)\-(\d+)\-(\d+)", value).groups()
            self._time_step = relativedelta(years=int(year), months=int(month), days=int(day))
        elif type(value) is relativedelta:
            self._time_step = value
        else:
            raise Exception("Invalid time_step type.")

    @property
    def seq(self):
        return self._seq

    @seq.setter
    def seq(self, value):
        if value in ["asc", "desc"]:
            self._seq = value
        else:
            raise Exception("Invalid seq type.")

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self, value):
        if int(value) in [0, 1, 2, 3, 4]:
            self._monitor = int(value)
        else:
            raise Exception("Invalid monitor type.")

    @property
    def gsheet_tab_name(self):
        return self._gsheet_tab_name

    @gsheet_tab_name.setter
    def gsheet_tab_name(self, value):
        if type(value) is str:
            self._gsheet_tab_name = value
        else:
            raise Exception("Invalid gsheet tab name type.")

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        if type(value) is str and value in ["section", "accumulation"]:
            self._mode = value
        else:
            raise Exception("Invalid mode type.")

    @property
    def report(self):
        return self._report

    @report.setter
    def report(self, value):
        if type(value) is str and value in ["one-time"]:
            self._report = value
        else:
            raise Exception("Invalid report type.")

    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, value):
        if type(value) is str:
            hour, min, sec = re.match(r"(\d+)\:(\d+)\:(\d+)", value).groups()
            self._timeout = int(hour) * 3600 + int(min) * 60 + int(sec)
        else:
            raise Exception("Invalid timeout type.")

    def is_options_valid(self):
        # 比較 "資料間" 的關係
        msg = []
        for k, v in self.__dict__.items():
            if v == None:
                msg.append("[{}] is None".format(k[1:]))
        if msg:
            return (False, msg)

        if self.time_step.days < 1 and self.time_step.months < 1 and self.time_step.years < 1:
            msg.append("time_step should greater than 0")
        if self.test_start >= self.test_end:
            msg.append(
                "test_end[{0}}] should greater than test_start[{1}]".format(
                    self.test_end.strftime("%m-%d-%Y"),
                    self.test_start.strftime(r"%m-%d-%Y"),
                )
            )
        if self.timeout <= 0:
            msg.append("timeout must bigger than 0")

        if msg:
            return (False, msg)
        else:
            return (True, [])


def cmd_option():
    """
    test_name: the test case name                           e.g., test_volume_profit_chart_period_loading_performance
    test_server:                                            e.g., https://fms-stage-stress-1.gofreight.co
    monitor: driver monitor mode.                           e.g., 0
    time_step: increase or decrease step                    e.g., 0-1-0 (y-m-d)
    seq: asc / desc                                         e.g., asc
    test_start: the start date of test                      e.g., 01-01-2015
    test_end: the end date of test                          e.g., 04-30-2021
    company: who's DB                                       e.g., SFI
    gsheet_tab_name: tab name of gsheet for saving result   e.g., Performance
    mode: start/end date rule (section, accumulation)       e.g., section
    report: one-time -> clear worksheet
            daily -> save result in the end column          e.g., one-time
    """

    test_options = TestOptions()
    args_map = {}

    for arg in sys.argv[1:]:
        key, val = arg.split("=")
        args_map[key.lower()] = val
        Logger.getLogger().debug("[{}] = [{}]".format(key, val))

    for k, v in vars(test_options).items():
        Logger.getLogger().debug("k = [{}]".format(k))
        _k = k[1:]
        if _k in args_map:
            Logger.getLogger().debug("exec: test_options.{0}=args_map['{1}']".format(_k, _k))
            exec("test_options.{0} = args_map['{1}']".format(_k, _k))

    Logger.getLogger().info(" Test Parametes ".center(80, "*"))
    Logger.getLogger().info("test_server: {0}".format(test_options.test_server).ljust(80))
    Logger.getLogger().info("company: {0}".format(test_options.company).ljust(80))
    Logger.getLogger().info("test_start: {0}".format(test_options.test_start).ljust(80))
    Logger.getLogger().info("test_end: {0}".format(test_options.test_end).ljust(80))
    Logger.getLogger().info("seq: {0}".format(test_options.seq).ljust(80))
    Logger.getLogger().info("time_step: {0}".format(test_options.time_step).ljust(80))
    Logger.getLogger().info("monitor: {0}".format(test_options.monitor).ljust(80))
    Logger.getLogger().info("gsheet_tab_name: {0}".format(test_options.gsheet_tab_name).ljust(80))
    Logger.getLogger().info("report: {0}".format(test_options.report).ljust(80))
    Logger.getLogger().info("*" * 80)

    valid_result = test_options.is_options_valid()
    if valid_result[0] == False:
        msg = ""
        for m in valid_result[1]:
            msg = msg + "\n" + m
        raise Exception("option is not valid." + msg)

    return test_options


if __name__ == "__main__":
    """
    Usage:
    in project fold "gf-qa"
    cmd > python ./draft_test/00_PerformanceTest/performance.py test_server=https://fms-stage-stress-1.gofreight.co test_start=01-01-2015 test_end=05-30-2021 time_step=365 seq=desc monitor=3 company=SFI gsheet_tab_name=Performance
    """

    Logger(
        name="PerformanceTestForReport",
        level="debug",
        path=Path(__file__).parent
        / "log"
        / Path(Path(__file__).stem + "_" + TIME.strftime(r"%Y-%m-%d_%H_%M_%S") + ".log"),
    )

    options = cmd_option()

    suite = unittest.TestSuite()

    with open(gl.gsheet_config_path, encoding="UTF-8") as f:
        gsheet_config = yaml.safe_load(f)
        key = gsheet_config["test_report"]["key"]
    spreadsheet = GSpreadSheet(gl.gsheet_client_secret_path, gsheet_config["test_report"]["key"])
    worksheet = spreadsheet.get_worksheet(options.gsheet_tab_name, key_index=GSHEET_RECORD_KEY_INDEX)
    if options.report == "one-time":
        worksheet.delete_all()

    # TODO report of daily mode

    # Add test case by month accumulation
    # If time_step bigger than the period (test_end ~ test_start), than do only one time test. (test_end ~ test_start)
    # Otherwise, use flag to save current test start/end date, and test them step by step
    num = 1
    if options.test_start + options.time_step > options.test_end:
        flag = options.test_start + relativedelta(days=1)
    else:
        flag = (
            options.test_start + (num * options.time_step) - relativedelta(days=1)
            if options.seq == "asc"
            else options.test_end - (num * options.time_step) + relativedelta(days=1)
        )
    while options.test_start < flag < options.test_end:
        if options.seq == "asc":
            flag = options.test_start + (num * options.time_step)
            if flag > options.test_end:
                flag = options.test_end
            if options.mode == "section":
                c_start = datetime.strftime(options.test_start + (num - 1) * options.time_step, "%m-%d-%Y")
            else:
                c_start = datetime.strftime(options.test_start, "%m-%d-%Y")
            c_end = datetime.strftime(flag, "%m-%d-%Y")
        elif options.seq == "desc":
            flag = options.test_end - (num * options.time_step)
            if flag < options.test_start:
                flag = options.test_start
            c_start = datetime.strftime(flag, "%m-%d-%Y")
            if options.mode == "section":
                c_end = datetime.strftime(options.test_end - (num - 1) * options.time_step, "%m-%d-%Y")
            else:
                c_end = datetime.strftime(options.test_end, "%m-%d-%Y")
        else:
            break

        if options.test_name == "test_general_ledger_report_loading_performance":
            Logger.getLogger().info("Add test [{}-Summary] -->  [{}] ~ [{}]".format(num, c_start, c_end))
            suite.addTest(
                PerformanceTestForReport(
                    test_name=options.test_name,
                    test_server=options.test_server,
                    company=options.company,
                    start_date=c_start,
                    end_date=c_end,
                    monitor=options.monitor,
                    worksheet=worksheet,
                    mode=options.mode,
                    index="{}-Summary".format(num),
                    option={"Report Type": 1},
                    timeout=options.timeout,
                )
            )

            # Allways fail ...
            # Logger.getLogger().info('Add test [{}-Detail] -->  [{}] ~ [{}]'.format(num, c_start, c_end))
            # suite.addTest(PerformanceTestForReport(test_name=options.test_name,
            #                                     test_server=options.test_server,
            #                                     company=options.company,
            #                                     start_date=c_start,
            #                                     end_date=c_end,
            #                                     monitor=options.monitor,
            #                                     worksheet=worksheet,
            #                                     mode=options.mode,
            #                                     index='{}-Detail'.format(num),
            #                                     option={'Report Type':2},
            #                                     timeout=options.timeout))
        elif options.test_name == "test_agent_local_statement_loading_performance":
            Logger.getLogger().info("Add test [{}-Search] -->  [{}] ~ [{}]".format(num, c_start, c_end))
            suite.addTest(
                PerformanceTestForReport(
                    test_name=options.test_name,
                    test_server=options.test_server,
                    company=options.company,
                    start_date=c_start,
                    end_date=c_end,
                    monitor=options.monitor,
                    worksheet=worksheet,
                    mode=options.mode,
                    index="{}-Search".format(num),
                    option={"Test Stage": 1},
                    timeout=options.timeout,
                )
            )

            Logger.getLogger().info("Add test [{}-View] -->  [{}] ~ [{}]".format(num, c_start, c_end))
            suite.addTest(
                PerformanceTestForReport(
                    test_name=options.test_name,
                    test_server=options.test_server,
                    company=options.company,
                    start_date=c_start,
                    end_date=c_end,
                    monitor=options.monitor,
                    worksheet=worksheet,
                    mode=options.mode,
                    index="{}-View".format(num),
                    option={"Test Stage": 2},
                    timeout=options.timeout,
                )
            )

            Logger.getLogger().info("Add test [{}-Download PDF] -->  [{}] ~ [{}]".format(num, c_start, c_end))
            suite.addTest(
                PerformanceTestForReport(
                    test_name=options.test_name,
                    test_server=options.test_server,
                    company=options.company,
                    start_date=c_start,
                    end_date=c_end,
                    monitor=options.monitor,
                    worksheet=worksheet,
                    mode=options.mode,
                    index="{}-Download PDF".format(num),
                    option={"Test Stage": 3},
                    timeout=options.timeout,
                )
            )

            Logger.getLogger().info("Add test [{}-Download Excel] -->  [{}] ~ [{}]".format(num, c_start, c_end))
            suite.addTest(
                PerformanceTestForReport(
                    test_name=options.test_name,
                    test_server=options.test_server,
                    company=options.company,
                    start_date=c_start,
                    end_date=c_end,
                    monitor=options.monitor,
                    worksheet=worksheet,
                    mode=options.mode,
                    index="{}-Download Excel".format(num),
                    option={"Test Stage": 4},
                    timeout=options.timeout,
                )
            )

            Logger.getLogger().info("Add test [{}-Reload] -->  [{}] ~ [{}]".format(num, c_start, c_end))
            suite.addTest(
                PerformanceTestForReport(
                    test_name=options.test_name,
                    test_server=options.test_server,
                    company=options.company,
                    start_date=c_start,
                    end_date=c_end,
                    monitor=options.monitor,
                    worksheet=worksheet,
                    mode=options.mode,
                    index="{}-Reload".format(num),
                    option={"Test Stage": 5},
                    timeout=options.timeout,
                )
            )

        elif options.test_name == "test_aging_report_loading_performance":
            Logger.getLogger().info("Add test [{}-Summary-Search] -->  [{}] ~ [{}]".format(num, c_start, c_end))
            suite.addTest(
                PerformanceTestForReport(
                    test_name=options.test_name,
                    test_server=options.test_server,
                    company=options.company,
                    start_date=c_start,
                    end_date=c_end,
                    monitor=options.monitor,
                    worksheet=worksheet,
                    mode=options.mode,
                    index="{}-Summary-Search".format(num),
                    option={"Report Type": 1, "Test Stage": 1},
                    timeout=options.timeout,
                )
            )

            Logger.getLogger().info("Add test [{}-Summary-Print] -->  [{}] ~ [{}]".format(num, c_start, c_end))
            suite.addTest(
                PerformanceTestForReport(
                    test_name=options.test_name,
                    test_server=options.test_server,
                    company=options.company,
                    start_date=c_start,
                    end_date=c_end,
                    monitor=options.monitor,
                    worksheet=worksheet,
                    mode=options.mode,
                    index="{}-Summary-Print".format(num),
                    option={"Report Type": 1, "Test Stage": 2},
                    timeout=options.timeout,
                )
            )

            Logger.getLogger().info("Add test [{}-Detail-Search] -->  [{}] ~ [{}]".format(num, c_start, c_end))
            suite.addTest(
                PerformanceTestForReport(
                    test_name=options.test_name,
                    test_server=options.test_server,
                    company=options.company,
                    start_date=c_start,
                    end_date=c_end,
                    monitor=options.monitor,
                    worksheet=worksheet,
                    mode=options.mode,
                    index="{}-Detail-Search".format(num),
                    option={"Report Type": 2, "Test Stage": 1},
                    timeout=options.timeout,
                )
            )

            Logger.getLogger().info("Add test [{}-Detail-Print] -->  [{}] ~ [{}]".format(num, c_start, c_end))
            suite.addTest(
                PerformanceTestForReport(
                    test_name=options.test_name,
                    test_server=options.test_server,
                    company=options.company,
                    start_date=c_start,
                    end_date=c_end,
                    monitor=options.monitor,
                    worksheet=worksheet,
                    mode=options.mode,
                    index="{}-Detail-Print".format(num),
                    option={"Report Type": 2, "Test Stage": 2},
                    timeout=options.timeout,
                )
            )

        else:
            Logger.getLogger().info("Add test [{}] -->  [{}] ~ [{}]".format(num, c_start, c_end))
            suite.addTest(
                PerformanceTestForReport(
                    test_name=options.test_name,
                    test_server=options.test_server,
                    company=options.company,
                    start_date=c_start,
                    end_date=c_end,
                    monitor=options.monitor,
                    worksheet=worksheet,
                    mode=options.mode,
                    index=num,
                    timeout=options.timeout,
                )
            )
        num = num + 1

    unittest.TextTestRunner(verbosity=2).run(suite)
