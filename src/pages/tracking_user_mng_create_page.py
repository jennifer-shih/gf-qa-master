from selenium.webdriver.common.by import By

from src.elements import *


class TrackingUserMngCreatePage:
    id_existing_alert = Element((By.XPATH, "//div[contains(@class,'error')]"))
    user_id_input = Input((By.XPATH, "//input[@formcontrolname='userId']"))
    first_name_input = Input((By.XPATH, "//input[@formcontrolname='userFirstName']"))
    last_name_input = Input((By.XPATH, "//input[@formcontrolname='userLastName']"))
    password_input = Input((By.XPATH, "//input[@formcontrolname='userPassword']"))
    confirm_password_input = Input((By.XPATH, "//input[@formcontrolname='userConfirmPassword']"))
    e_mail_input = Input((By.XPATH, "//input[@formcontrolname='userEmail']"))

    trade_partner_multi_autocomplete = MultiAutocomplete((By.XPATH, "(//div[contains(@class,'ng-select-container')])[1]"), (By.XPATH, "//ng-dropdown-panel/div/div/input"))
    role_select = Select((By.XPATH, "//select[@formcontrolname='userTpRole']"))

    in_gate_checkbox = Checkbox((By.XPATH, "//input[@formcontrolname='prefStageInGate']"))
    rail_checkbox = Checkbox((By.XPATH, "//input[@formcontrolname='prefStageRail']"))
    vessel_departure_checkbox = Checkbox((By.XPATH, "//input[@formcontrolname='prefStageVesselDeparted']"))
    outgate_checkbox = Checkbox((By.XPATH, "//input[@formcontrolname='prefStageOutgate']"))
    vessel_arrival_checkbox = Checkbox((By.XPATH, "//input[@formcontrolname='prefStageVesselArrived']"))
    unloaded_from_vessel_checkbox = Checkbox((By.XPATH, "//input[@formcontrolname='prefStageVesselUnloaded']"))
    etd_updated_checkbox = Checkbox((By.XPATH, "//input[@formcontrolname='prefETDUpdated']"))
    eta_updated_checkbox = Checkbox((By.XPATH, "//input[@formcontrolname='prefETAUpdated']"))
    new_document_uploaded_checkbox = Checkbox((By.XPATH, "//input[@formcontrolname='prefDocumentUpload']"))
    shipment_report_checkbox = Checkbox((By.XPATH, "//input[@formcontrolname='prefCustomerWeeklyReport']"))
    detention_report_checkbox = Checkbox((By.XPATH, "//input[@formcontrolname='prefDetentionReport']"))

    create_user_button = Button((By.XPATH, "//button[contains(.,'Create')]"))
