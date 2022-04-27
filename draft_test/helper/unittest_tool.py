import re
import unittest
from enum import Enum

import chromedriver.chrome_helper as chrome_helper
from config import globalparameter as gl
from src.drivers.driver import Driver


def check_testcase_error(testcase: unittest.TestCase) -> str:
    result = testcase.defaultTestResult()
    testcase._feedErrorsToResult(result, testcase._outcome.errors)
    error = ""
    failure = ""
    if result.errors and result.errors[-1][0] is testcase:
        error = result.errors[-1][1]
    if result.failures and result.failures[-1][0] is testcase:
        failure = result.failures[-1][1]
    ok = not error and not failure
    failure_msg = ""
    if not ok:
        typ, text = ("ERROR", error) if error else ("FAIL", failure)
        msg = [x for x in text.split("\n")[1:] if not x.startswith(" ")][0]
        failure_msg = "[{0}]: {1}\n    {2}".format(typ, testcase.id(), msg)

    return failure_msg


def get_testcases_name(object):
    methodList = []
    regex = r"test_.+"
    for method_name in dir(object):
        if re.match(regex, method_name) != None:
            methodList.append(str(method_name))
    return methodList


def get_unittest_result(self, exc_list):
    if exc_list and exc_list[-1][0] is self:
        return exc_list[-1][1]


def base_setup(test):
    gl.read_company_config_files()
    gl.init_url()
    chrome_helper.check_browser_driver_available()
    Driver("Chrome_1", chrome_helper.get_driver_path(), monitor=gl.monitor)
    print("\n")  # for verbosity=2 formatting


def base_teardown(test):
    Driver.quit()


class TestStatus(object):
    class Status(Enum):
        Null = 0
        PASS = 1
        FAIL = 2
        WARNING = 3
        Broken = 4

    def __init__(self, status):
        # self._status = TestStatus.Status(0)
        self._status = TestStatus.Status(status)
        self._msg = []

    def Pass(self, msg=""):
        if (
            self._status != TestStatus.Status.Broken
            and self._status != TestStatus.Status.FAIL
            and self._status != TestStatus.Status.WARNING
        ):
            self._status = TestStatus.Status.PASS
        self._msg.append(msg)

    def Fail(self, msg=""):
        if self._status != TestStatus.Status.Broken:
            self._status = TestStatus.Status.FAIL
            self._msg.append(msg)

    def Warning(self, msg=""):
        if self._status != TestStatus.Status.Broken and self._status != TestStatus.Status.FAIL:
            self._status = TestStatus.Status.WARNING
        self._msg.append(msg)

    def Broken(self, msg=""):
        self._status = TestStatus.Status.Broken
        self._msg.append(msg)

    def get_status(self):
        return self._status

    def get_msg(self):
        return self._msg

    def print_status(self):
        return self._status.name

    def print_msg(self):
        if len(self._msg) > 0:
            return "\n".join("{0}. {1}".format(msg[0], msg[1]) for msg in enumerate([m for m in self._msg], start=1))
        else:
            return ""

    def is_fail(self):
        return self._status == TestStatus.Status.FAIL

    def is_pass(self):
        return self._status == TestStatus.Status.PASS
