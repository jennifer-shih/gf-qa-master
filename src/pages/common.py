from selenium.webdriver.common.by import By

from src.elements import *


class Common:
    save_button = Button((By.XPATH, "//button[@ng-click='vm.save()']"))

    # Some page's save button doesn't have ng-click attribute
    save_button_alt = Button((By.XPATH, "//button[@type='submit'][contains(@class,'btn green')]"))

    save_msg = Label((By.XPATH, "//div[contains(@class, 'alert-success')]"))
    save_fail_msg = Label((By.XPATH, "//div[@class='bootstrap-growl alert alert-danger alert-dismissible']"))
    spin_bar = SpinBar((By.XPATH, "//div[@class='page-spinner-bar']"))  # TODO: There are two types of spinbar, but I can't find...

    ok_button = Button((By.XPATH, "//button[@ng-click='ok()']"))
    shipment_ok_button = Button((By.XPATH, "//div[@class='modal-dialog']//button[contains(@class, 'btn blue')]")) # delete, copy shipment
    notice_modal_ok_button = Button((By.XPATH, "//button[@data-hc-name='notice-modal-ok-btn']"))
    popup_modal_msg_label = Label((By.XPATH, "//*[contains(@class, 'modal-title')]"))
    pupup_modal_element = Element((By.XPATH, "//div[@class='modal-dialog']/div[@class='modal-content'][@uib-modal-transclude]"))
