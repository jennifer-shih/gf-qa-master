from selenium.webdriver.common.by import By

from src.elements import *


class NewTradePartnerPage:
    tp_type_select = Select((By.XPATH, "//select[@name='tp_type']"))
    code_input = Input((By.XPATH, "//input[contains(@ng-model,'vm.tp.data.code')]"))
    name_input = Input((By.XPATH, "//input[@name='tp_name']"))
    print_name_input = Input((By.XPATH, "//input[@name='local_name']"))
    office_select = Select((By.XPATH, "//select[@ng-model='vm.tp.data.office']"))
    global_autocomplete = Autocomplete((By.XPATH, "//hc-tp-select[@name='global_tp']"), (By.XPATH, "(//input[@type='search'])[1]"))
    local_address_input = Input((By.XPATH, "//textarea[@ng-model='vm.tp.data.local_address']"))
    city_input = Input((By.XPATH, "//input[@ng-model='vm.tp.data.city_name']"))
    state_input = Input((By.XPATH, "//input[@ng-model='vm.tp.data.state_code']"))
    zip_code_input = Input((By.XPATH, "//input[@ng-model='vm.tp.data.zip_code']"))
    country_autocomplete = Autocomplete((By.XPATH, "//hc-country-select[@name='tp_country']"), (By.XPATH, "//input[@aria-owns='ui-select-choices-0']"))
    tel_input = Input((By.XPATH, "//input[@ng-model='vm.tp.data.phone']"))
    fax_input = Input((By.XPATH, "//input[@ng-model='vm.tp.data.fax']"))
    print_address_contact_info_checkbox = Checkbox((By.XPATH, "//input[@ng-model='vm.tp.data.is_print_tpc']"))
    alias_input = Input((By.XPATH, "//input[@ng-model='vm.tp.data.short_name']"))
    iata_code_input = Input((By.XPATH, "//input[@ng-model='vm.tp.data.iata_code']"))
    iata_prefix_input = Input((By.XPATH, "//input[@ng-model='vm.tp.data.prefix']"))
    firms_code_input = Input((By.XPATH, "//input[@ng-model='vm.tp.data.firm_code']"))
    scac_input = Input((By.XPATH, "//input[@ng-model='vm.tp.data.scac_code']"))
    sales_person_autocomplete = Autocomplete((By.XPATH, "//*[@ng-model='vm.tp.data.sales_person']"), (By.XPATH, "//div[@class='ng-dropdown-header']/div/input"))
    tax_id_usci_no_input = Input((By.XPATH, "//input[@ng-model='vm.tp.data.usci_no']"))
    credit_term_input = Input((By.XPATH, "//input[@ng-model='vm.tp.data.credit_days']"))
    isf_submission_name_input = Input((By.XPATH, "//input[@ng-model='vm.tp.data.isf_submission_name']"))
    importer_code_select = Select((By.XPATH, "//select[@ng-model='vm.tp.data.tax_type']"))
    importer_no_input = Input((By.XPATH, "//input[@ng-model='vm.tp.data.tax_id_no']"))
    see_memo_remark_checkbox = Checkbox((By.XPATH, "//input[@id='is_see_memo_remark']"))

    notification_popup_msg = Label((By.XPATH, "//h4[@ng-bind-html='msg']"))
    notification_popup_cancel_button = Button((By.XPATH, "//button[@ng-click='cancel()']"))
    notification_popup_ok_button = Button((By.XPATH, "//button[@ng-click='ok()']"))

    # Memo
    memo_expand_button = Button((By.XPATH, "//hc-memo/div/div/div[@class='tools']/a[@class='collapse-btn expand']"))
    memo_add_button = Button((By.XPATH, "//button[@ng-click='vm.openMemoModal()']"))
    memo_subject_input = Input((By.XPATH, "//input[@ng-model='vm.memo.subject']"))
    memo_content_input = Input((By.XPATH, "//textarea[@ng-model='vm.memo.content']"))
    memo_save_button = Button((By.XPATH, "//div[@class='modal-dialog']//button[@ng-click='vm.save()']"))

    # contact person information
    cpi_expand_button = Button((By.XPATH, "//div[@id='contactPersonArea']/div[@class='portlet-title']/div[@class='tools']/a[@class='collapse-btn expand']"))
    cpi_collapse_button = Button((By.XPATH, "//div[@id='contactPersonArea']/div[@class='portlet-title']/div[@class='tools']/a[@class='collapse-btn collapse']"))
    cpi_add_button = Button((By.XPATH,"//button[@ng-click='vm.addTpcp()']"))
    cpi_rep_checkbox = Checkbox((By.XPATH, "//input[@ng-model='tpcp.data.is_represent']"))
    cpi_email_checkbox = Checkbox((By.XPATH, "//input[@ng-model='tpcp.data.is_email_recipient']"))
    cpi_name_input = Input((By.NAME, 'tpcp_name'))
    cpi_phone_input = Input((By.XPATH, "//input[@ng-model='tpcp.data.phone']"))
    cpi_fax_input = Input((By.XPATH, "//input[@ng-model='tpcp.data.fax']"))
    cpi_email_address_email_tags = EmailTags((By.XPATH, "//i[@class='fa fa-pencil']"), (By.XPATH, "//div[@id='contactPersonArea']//tbody[@ng-form='tpcp.form'][1]//td[11]//div[@popover-title]"), (By.XPATH, "//td/tags-input/div/div/input"))

    #popup
    similar_trade_partner_name_existed_label = Label((By.XPATH, "//div[@class='modal-dialog']//h4[contains(., 'Similar trade partner name already exists')]"))
    ok_button = Button((By.XPATH, "//div[@class='modal-dialog']//button[@ng-click='ok()']"))

    class LocalNameHasMovedPopover:
        never_show_this_again_checkbox = Checkbox((By.XPATH, """//input[@ng-model="vm.checkboxPopover['localName']"]"""))
        close_button = Button((By.XPATH, """//a[@ng-click="vm.dismissPopover('localName')"]"""))
