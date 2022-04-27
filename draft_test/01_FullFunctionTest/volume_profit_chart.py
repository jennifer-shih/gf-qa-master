import sys

sys.path.append(".")
import json
import time
import unittest
from datetime import datetime
from pathlib import Path
from time import sleep

import yaml

import chromedriver.chrome_helper as chrome_helper
import src.pages as Pages
from config import globalparameter as gl
from draft_test.helper.unittest_tool import *
from src.drivers.driver import Driver
from src.helper.log import Logger
from src.helper.script import login_as
from src.helper.slack_feeder import SlackFeeder

TIME = datetime.now()

FAIL_MSG_FORMAT = """
*{test_name}* `No.{index}` is Failed \n \
  *1. Test Server:* {test_server} \n \
  *2. Company:* {company} \n \
  *3. Period:* {start_date} ~ {end_date} \n \
  *5. Message:* `{msg}`  \n \
  *6. Options:* ```{test_options}```
"""


class FullFunctionTestForVolumeProfitChart(unittest.TestCase):
    def __init__(
        self,
        test_name,
        test_options,
        start_date,
        end_date,
        test_server,
        monitor,
        company,
        index,
    ):
        super(FullFunctionTestForVolumeProfitChart, self).__init__(test_name)
        self.TEST_NAME = test_name
        self.TEST_OPTIONS = test_options
        self.START_DATE = start_date
        self.END_DATE = end_date
        self.SERVER_URL = test_server
        self.MONITOR = monitor
        self.COMPANY = company
        self.INDEX = index

        self.chrome_console_log = ""
        self.spend_time = ""
        self.test_status = TestStatus(TestStatus.Status.PASS)

    def get_unittest_result(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]

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

        # if test fail, send msg to the slack channel
        with open(gl.slack_channel_path, encoding="UTF-8") as f:
            slack_channel = yaml.safe_load(f)

        if self.test_status.is_pass() == False:
            msg = FAIL_MSG_FORMAT.format(
                test_name=self.TEST_NAME,
                index=self.INDEX,
                test_server=self.SERVER_URL,
                company=self.COMPANY,
                start_date=self.START_DATE,
                end_date=self.END_DATE,
                msg=self.test_status.print_msg(),
                test_options=json.dumps(self.TEST_OPTIONS, indent=2),
            )

            scrennshot_name = str(self.INDEX) + "_error.png"
            folder_name = "{0}~{1}".format(self.START_DATE, self.END_DATE)
            error_screenshot = Path(__file__).parent / "screenshot" / "error" / folder_name / scrennshot_name
            Driver.get_screenshot_for_all_windows(error_screenshot)
            SlackFeeder.post_file(
                path=str(error_screenshot),
                channels=slack_channel["full-option-test"]["name"],
                file_title="Error screenshot",
                filename="error.png",
                msg=msg,
            )

            # also send the log file
            SlackFeeder.post_file(
                path=Logger.getFilePath(),
                channels=slack_channel["full-option-test"]["name"],
                file_title="Log",
                filename="log.txt",
            )

        Driver.quit()

    def test_volume_profit_chart_full_function_test(self):
        Logger.getLogger().info("Start Test: [{0}] (No.{1})".format(self._testMethodName, self.INDEX))
        Logger.getLogger().info("Test Period: [{0}] ~ [{1}]".format(self.START_DATE, self.END_DATE))
        Logger.getLogger().info("Test Options: {}".format(self.TEST_OPTIONS))

        # go to volume&profit chart page
        Driver.open(gl.URL.VOLUME_AND_PROFIT_CHART)
        login_as("super_admin")
        Pages.Common.spin_bar.gone(timeout=60)

        # input fields
        # 1. Period
        Pages.VolumeAndProfitChartPage.period_radio_group.click(self.TEST_OPTIONS["PERIOD_OPTION"])
        Pages.VolumeAndProfitChartPage.period_period_datepicker.input(val=f"{ self.START_DATE } ~ { self.END_DATE }")
        # 2. Shipping Type
        if self.TEST_OPTIONS["SHIPPING_TYPE"] == "All":
            checked = [True, True, True, True, True, True, True]
        elif self.TEST_OPTIONS["SHIPPING_TYPE"] == "Ocean Import":
            checked = [True, False, False, False, False, False, False]
        elif self.TEST_OPTIONS["SHIPPING_TYPE"] == "Ocean Export":
            checked = [False, True, False, False, False, False, False]
        elif self.TEST_OPTIONS["SHIPPING_TYPE"] == "Air Import":
            checked = [False, False, True, False, False, False, False]
        elif self.TEST_OPTIONS["SHIPPING_TYPE"] == "Air Export":
            checked = [False, False, False, True, False, False, False]
        elif self.TEST_OPTIONS["SHIPPING_TYPE"] == "Truck":
            checked = [False, False, False, False, True, False, False]
        elif self.TEST_OPTIONS["SHIPPING_TYPE"] == "Misc":
            checked = [False, False, False, False, False, True, False]
        elif self.TEST_OPTIONS["SHIPPING_TYPE"] == "Warehouse":
            checked = [False, False, False, False, False, False, True]
        Pages.VolumeAndProfitChartPage.ocean_import_checkbox.tick(checked[0])
        Pages.VolumeAndProfitChartPage.ocean_export_checkbox.tick(checked[1])
        Pages.VolumeAndProfitChartPage.air_import_checkbox.tick(checked[2])
        Pages.VolumeAndProfitChartPage.air_export_checkbox.tick(checked[3])
        Pages.VolumeAndProfitChartPage.truck_checkbox.tick(checked[4])
        Pages.VolumeAndProfitChartPage.misc_checkbox.tick(checked[5])
        Pages.VolumeAndProfitChartPage.warehouse_checkbox.tick(checked[6])
        # 3. Volume Unit
        Pages.VolumeAndProfitChartPage.volume_unit_select.select(self.TEST_OPTIONS["VOLUME_UNIT"])
        # 4. Chart Type
        Pages.VolumeAndProfitChartPage.chart_type_select.select(self.TEST_OPTIONS["CHART_TYPE"])
        # 5. Office
        if self.TEST_OPTIONS["OFFICE"] == "All":
            # Pages.VolumeAndProfitChartPage.office_autocomplete_multi_select.clear()
            # Pages.VolumeAndProfitChartPage.office_autocomplete_multi_select.input('STRAIGHT;MEOW;SFI;Proactive;Point')
            pass
        else:
            Pages.VolumeAndProfitChartPage.office_autocomplete_multi_select.clear()
            Pages.VolumeAndProfitChartPage.office_autocomplete_multi_select.input(self.TEST_OPTIONS["OFFICE"])
        # 6. Sales
        Pages.VolumeAndProfitChartPage.sales_select.select(self.TEST_OPTIONS["SALES"])
        # 7. Bar Segment
        if self.TEST_OPTIONS["BAR_SEGMENT"] != None:
            Pages.VolumeAndProfitChartPage.bar_segment_select.select(self.TEST_OPTIONS["BAR_SEGMENT"])
        # 8. Status
        Pages.VolumeAndProfitChartPage.status_radio_group.click(self.TEST_OPTIONS["STATUS"])
        # submit then see the result
        Pages.VolumeAndProfitChartPage.view_button.click()

        # count loading time
        timer_start = time.time()
        Pages.Common.spin_bar.gone(timeout=300)
        timer_end = time.time()

        # collect log of browser
        self.chrome_console_log = Driver.get_console_logs()
        sleep(5)  # wait the chart loading completely

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
        self.spend_time = spend_time

        Logger.getLogger().info("Full test end")


def cmd_option():
    """
    test_server: testing url                                e.g., https://fms-stage-stress-1.gofreight.co
    monitor: driver monitor mode.                           e.g., 0
    start_date: the start date of test                      e.g., 01-01-2015
    end_date: the end date of test                          e.g., 04-30-2021
    company: who's DB                                       e.g., SFI
    """
    args_map = {}

    for arg in sys.argv[1:]:
        key, val = arg.split("=")
        args_map[key.lower()] = val
        Logger.getLogger().debug("[{}] = [{}]".format(key, val))

    Logger.getLogger().info(" Test Parametes ".center(80, "*"))
    Logger.getLogger().info("test_server: {0}".format(args_map["test_server"]).ljust(80))
    Logger.getLogger().info("company: {0}".format(args_map["company"]).ljust(80))
    Logger.getLogger().info("start_date: {0}".format(args_map["start_date"]).ljust(80))
    Logger.getLogger().info("end_date: {0}".format(args_map["end_date"]).ljust(80))
    Logger.getLogger().info("monitor: {0}".format(args_map["monitor"]).ljust(80))
    Logger.getLogger().info("*" * 80)

    return args_map


if __name__ == "__main__":

    Logger(
        name="FullFunctionTestForVolumeProfitChart",
        level="debug",
        path=Path(__file__).parent
        / "log"
        / Path(Path(__file__).stem + "_" + TIME.strftime(r"%Y-%m-%d_%H_%M_%S") + ".log"),
    )

    PERIOD_OPTION = ["Post Date", "ETD", "ETA"]

    SHIPPING_TYPE = ["All"]
    # SHIPPING_TYPE = ['All',
    #                  'Ocean Import',
    #                  'Ocean Export',
    #                  'Air Import',
    #                  'Air Export',
    #                  'Truck',
    #                  'Misc',
    #                  'Warehouse']

    VOLUME_UNIT = ["#TEU", "#Container/CBM", "#B/L(AWB)"]

    CHART_TYPE = ["Month"]
    # CHART_TYPE = ['Month',
    #              'Oversea Agent',
    #              'Shipper',
    #              'Consignee',
    #              'Customer',
    #              'Customer (by Account Group)',
    #              'Bill To',
    #              'POL',
    #              'POD',
    #              'DEL',
    #              'Final Destination',
    #              'Carrier',
    #              'Sales Person',
    #              'Operation',
    #              'Incoterms',
    #              'Service Term',
    #              'Office',
    #              'Shipping Type']

    OFFICE = ["All"]
    # OFFICE = ['All',
    #           'STRAIGHT',
    #           'MEOW',
    #           'SFI',
    #           'Proactive',
    #           'Point']

    SALES = ["All"]
    # SALES = ['All',
    #         'Chris Lo (1234)']

    BAR_SEGMENT = ["Shipping Type", "Incoterms", "Sales Type", "Ship Mode"]

    STATUS = ["All"]
    # STATUS = ['All',
    #           'Open',
    #           'Blocked']

    # create all combination test
    all_cases = []
    for po in PERIOD_OPTION:
        for st in SHIPPING_TYPE:
            for vu in VOLUME_UNIT:
                for ct in CHART_TYPE:
                    for of in OFFICE:
                        for sal in SALES:
                            # 只有在 Volume Unit = #B/L(AWB) 時，Bar Segment才會 enable
                            if vu == "#B/L(AWB)":
                                for bs in BAR_SEGMENT:
                                    for sta in STATUS:
                                        all_cases.append(
                                            {
                                                "PERIOD_OPTION": po,
                                                "SHIPPING_TYPE": st,
                                                "VOLUME_UNIT": vu,
                                                "CHART_TYPE": ct,
                                                "OFFICE": of,
                                                "SALES": sal,
                                                "BAR_SEGMENT": bs,
                                                "STATUS": sta,
                                            }
                                        )
                            else:
                                for sta in STATUS:
                                    all_cases.append(
                                        {
                                            "PERIOD_OPTION": po,
                                            "SHIPPING_TYPE": st,
                                            "VOLUME_UNIT": vu,
                                            "CHART_TYPE": ct,
                                            "OFFICE": of,
                                            "SALES": sal,
                                            "BAR_SEGMENT": None,
                                            "STATUS": sta,
                                        }
                                    )

    options = cmd_option()
    suite = unittest.TestSuite()
    index = 0  # 圖形辨識使用的截圖編號
    for case in all_cases:
        suite.addTest(
            FullFunctionTestForVolumeProfitChart(
                test_name="test_volume_profit_chart_full_function_test",
                test_options=case,
                start_date=datetime.strptime(options["start_date"], "%Y-%m-%d").strftime("%m-%d-%Y"),
                end_date=datetime.strptime(options["end_date"], "%Y-%m-%d").strftime("%m-%d-%Y"),
                test_server=options["test_server"],
                monitor=options["monitor"],
                company=options["company"],
                index=index,
            )
        )
        index += 1

    unittest.TextTestRunner(verbosity=2).run(suite)
