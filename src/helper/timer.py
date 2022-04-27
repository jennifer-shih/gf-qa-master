import time
from pathlib import Path
from time import sleep

import src.pages as Pages
from src.drivers.driver import Driver
from src.elements.element import Element


class DownloadTimer:
    def __init__(self, file_path: str, timeout: int):
        self.file_path = Path(file_path).as_posix()
        self.timeout = timeout

    def start(self):
        end_time = time.time() + self.timeout

        while True:
            if time.time() > end_time:
                assert False, "Wait {} sec, still cannot found file: {}".format(self.timeout, self.file_path)
            elif Path(self.file_path).is_file():
                break
            elif Driver.is_text_in_page_source("502 Bad Gateway"):
                assert False, "Occured 502 Bad Gateway wehn downloading file"
            elif Driver.is_text_in_page_source("504 Bad Gateway"):
                assert False, "Occured 504 Bad Gateway wehn downloading file"
            # elif Driver.get_console_error_logs():
            #     assert False, "Server Error...\n{0}".format(Driver.get_console_error_logs())
            else:
                sleep(1)


class PatchDBTimer:
    def __init__(self, success_msg: str, timeout: int):
        self.success_msg = success_msg
        self.timeout = timeout
        self.result = None  # (is_passed, text in textarea)

    def start(self):
        is_passed = False
        console_textarea = ""
        end_time = time.time() + self.timeout
        while True:
            console_textarea = Pages.PatchDBPage.console_textarea.get_value()
            is_passed = self.success_msg in console_textarea
            # get expected value or timeout then break the loop
            if is_passed or time.time() > end_time:
                break
            sleep(0.5)

        self.result = (is_passed, console_textarea)

    def is_passed(self) -> bool:
        return self.result[0]

    def get_console_textarea_text(self) -> str:
        return self.result[1]

    def get_result(self) -> tuple:
        return self.result


class PageLoadingTimer:
    """
    Page在loading時，url 為 about:blank
    此時如果對driver操作，會等page loading結束後才會執行
    example.
        driver.open('...')
        element.is_visible(300)
    此時並不是檢查page open後300sec內有沒有element出現
    而是element在page loading 結束後，300秒內element有沒有出現
    """

    def __init__(self, element: Element, page_timeout: int, element_timeout: int):
        self.page_timeout = page_timeout
        self.element_timeout = element_timeout
        self.element = element
        self.result = None

    def start(self):
        is_passed = False
        msg = ""
        Driver.set_page_load_timeout(self.page_timeout)

        if self.element.is_visible(self.element_timeout):  # this row will execute after the page has been loaded
            is_passed = True
        elif Driver.is_text_in_page_source("502 Bad Gateway"):
            is_passed = False
            msg = "Occured 502 Bad Gateway "
        elif Driver.is_text_in_page_source("504 Bad Gateway"):
            is_passed = False
            msg = "Occured 504 Bad Gateway"
        else:
            is_passed = False
            msg = f"The page has been loaded for {self.page_timeout}sec"

        self.result = (is_passed, msg)
        Driver.set_default_page_load_timeout()

    def get_result(self) -> tuple:
        return self.result
