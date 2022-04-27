from selenium.webdriver.common.by import By

from src.elements import *


class UserMngPage:
    create_user_button = Button((By.XPATH, "//a[@href='/settings/user/management/create/']"))
    filter_button = Button((By.XPATH, "//*[@ng-click='vm.filter.reset()']"))
    create_message = Label((By.XPATH, "//div[@class='bootstrap-growl alert alert-info alert-dismissible']"))

    class Filter:
        keyword_input = Input((By.XPATH, "//input[@ng-model='vm.filter.input[vm.key]']"))
        apply_filters_button = Button((By.XPATH, "//button[text()='Apply Filters']"))

    class UserRow:
        _rows = {}
        def __new__(cls, username):
            if username not in cls._rows:
                cls._rows[username] = super().__new__(cls)
            return cls._rows[username]

        def __init__(self, username):
            def ROW_XPATH(xpath):
                return f"//tbody/tr[td//strong[@ng-bind='u.username']/text()='{ username }']{ xpath }"

            self.user_id_link = Link((By.XPATH, ROW_XPATH("/td[1]/a")))
