from selenium.webdriver.common.by import By

from src.elements import *


class UserMngCreatePage:
    id_existing_alert = Element((By.XPATH, "//div[contains(@class,'form-group has-error')]"))
    user_id_input = Input((By.XPATH, "//input[@ng-model='vm.user.username']"))
    password_input = Input((By.XPATH, "//input[@ng-model='vm.user.password']"))
    confirm_password_input = Input((By.XPATH, "//input[@ng-model='vm.user.c_password']"))
    first_name_input = Input((By.XPATH, "//input[@ng-model='vm.user.first_name']"))
    last_name_input = Input((By.XPATH, "//input[@ng-model='vm.user.last_name']"))
    office_multi_autocomplete = MultiAutocomplete((By.XPATH, "(//div[contains(@class,'ng-select-container')])[1]"), (By.XPATH, "//ng-dropdown-panel/div/div/input"))
    role_popup_select = PopupSelect(
        (By.XPATH, "//a[@ng-click='vm.onEditRoles()']"), (By.XPATH, "//button[@ng-click='vm.onRolesApply()']"),
        {
            'Accounting': (By.XPATH, "//td[text()='Accounting']//preceding-sibling::td[1]"),
            'Admin': (By.XPATH, "//td[text()='Admin']//preceding-sibling::td[1]"),
            'Accounting_Manager': (By.XPATH, "//td[text()='Accounting Manager']//preceding-sibling::td[1]"),
            'Customer': (By.XPATH, "//td[text()='Customer']//preceding-sibling::td[1]"),
            'EDI_Agent': (By.XPATH, "//td[text()='EDI Agent']//preceding-sibling::td[1]"),
            'General_Manager': (By.XPATH, "//td[text()='General Manager']//preceding-sibling::td[1]"),
            'Operation': (By.XPATH, "//td[text()='Operation']//preceding-sibling::td[1]"),
            'Operation_Assistant':  (By.XPATH, "//td[text()='Operation Assistant']//preceding-sibling::td[1]"),
            'Operation_Manager': (By.XPATH, "//td[text()='Operation Manager']//preceding-sibling::td[1]"),
            'Sales': (By.XPATH, "//td[text()='Sales']//preceding-sibling::td[1]"),
            'Sales_Assistant': (By.XPATH, "//td[text()='Sales Assistant']//preceding-sibling::td[1]"),
            'Sales_Manager': (By.XPATH, "//td[text()='Sales Manager']//preceding-sibling::td[1]"),
            'Warehouse_App_Customer': (By.XPATH, "//td[text()='Warehouse App Customer']//preceding-sibling::td[1]")
        }
    )
    e_mail_input = Input((By.XPATH, "//*[@id='email_input']"))
    allow_remote_access_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.user.allow_remote_access']"))
    create_user_button = Button((By.XPATH, "//button[contains(.,'Create User')]"))
    create_user_sure_button = Button((By.XPATH, "//button[@ng-click='vm.onSave()']"))
