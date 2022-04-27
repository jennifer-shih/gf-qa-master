from selenium.webdriver.common.by import By

from src.elements import *


class PatchDBPage:
    def patch_apply_button(patch_name):
        return Button((By.XPATH, f"//table//tr/td[text()='{patch_name}']/following-sibling::td/button"))

    console_textarea = Textarea((By.XPATH, "//textarea[@ng-model='vm.console']"))
    proceed_button = Button((By.XPATH, "//button[@ng-click='ok()']"))
    cancel_button = Button((By.XPATH, "//button[@ng-click='cancel()']"))
