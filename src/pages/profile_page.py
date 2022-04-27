from selenium.webdriver.common.by import By

from src.elements import *


class ProfilePage:
    my_profile_label = Label((By.XPATH, "//span[contains(.,'My Profile')]"))

    # side pannel
    setting_button = Button((By.XPATH, "//a[@href='#settings']"))

    # settings
    language_select = Select((By.XPATH, "//select[@ng-model='vm.lang']"))
    in_gate_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.tracking_pref.tk_email_stage_in_gate']"))
    rail_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.tracking_pref.tk_email_stage_rail']"))
    vessel_departure_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.tracking_pref.tk_email_stage_vessel_departed']"))
    outgate_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.tracking_pref.tk_email_stage_outgate']"))
    vessel_arrival_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.tracking_pref.tk_email_stage_vessel_arrived']"))
    unloaded_from_vessel_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.tracking_pref.tk_email_stage_vessel_unloaded']"))
    etd_updated_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.tracking_pref.tk_email_etd_updated']"))
    eta_updated_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.tracking_pref.tk_email_eta_updated']"))
    new_document_uploaded_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.tracking_pref.tk_email_doc_uploaded']"))
    shipment_report_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.tracking_pref.tk_email_weekly_report']"))
    detention_report_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.tracking_pref.tk_email_detention_report']"))
    suspicious_report_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.tracking_pref.tk_email_suspicious_report']"))

    save_changes_button = Button((By.XPATH, "//input[@ng-disabled='settingsForm.$invalid || !settingsForm.$dirty']"))
