from selenium.webdriver.common.by import By

from src.elements import *


class TrackingUserMngPage:
    create_user_button = Button((By.XPATH, "//a[@href='/settings/user/management/create/']"))
    filter_button = Button((By.XPATH, "//*[@ng-click='vm.resetFilter()']"))
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
                return f"(//ag-grid-angular//div[@role='row'][div[contains(@col-id, 'username')]//a[contains(., '{ username }')]]){ xpath }"

            self.user_id_link = Link((By.XPATH, ROW_XPATH("/div[contains(@col-id, 'username')]//a")))
            self.user_id_label = Label((By.XPATH, ROW_XPATH("/div[contains(@col-id, 'username')]//a")))
            self.first_name_label = Label((By.XPATH, ROW_XPATH("/div[contains(@col-id, 'first_name')]")))
            self.last_name_label = Label((By.XPATH, ROW_XPATH("/div[contains(@col-id, 'last_name')]")))
            self.e_mail_label = Label((By.XPATH, ROW_XPATH("/div[contains(@col-id, 'email')]")))
            self.role_label = Label((By.XPATH, ROW_XPATH("/div[contains(@col-id, 'role')]")))
            self.trade_partner_label = Label((By.XPATH, ROW_XPATH("/div[contains(@col-id, 'trade_partner')]")))
            self.status_label = Label((By.XPATH, ROW_XPATH("/div[contains(@col-id, 'is_active')]")))
