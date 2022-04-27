from selenium.webdriver.common.by import By

from src.elements import *


class BaseAccountingBillingBasedMBLRevenue:
    _rows = {}
    # TODO Waiting for improvement
    new_button = Button((By.XPATH, "//*[contains(@containerclass, 'mbl_board')]//div[@slide-title][contains(.,'Revenue')]/..//i[@class='fa fa-plus']"))
    new_five_button = Button((By.XPATH, "//*[contains(@containerclass, 'mbl_board')]//div[@slide-title][contains(.,'Revenue')]/..//button[contains(text(), '+5')]"))
    add_multiple_button = Button((By.XPATH, "//*[contains(@containerclass, 'mbl_board')]//div[@slide-title][contains(.,'Revenue')]/..//button[@dropdowntoggle]"))
    copy_button = Button((By.XPATH, "//*[contains(@containerclass, 'mbl_board')]//div[@slide-title][contains(.,'Revenue')]/..//acctwizardbutton/div/button[1]"))
    copy_to_button = Button((By.XPATH, "//*[contains(@containerclass, 'mbl_board')]//div[@slide-title][contains(.,'Revenue')]/..//acctwizardbutton/div/div/button"))
    delete_button = Button((By.XPATH, "//*[contains(@containerclass, 'mbl_board')]//div[@slide-title][contains(.,'Revenue')]/..//acctwizardbutton/div/button[2]"))
    load_from_template_button = Button((By.XPATH, "//*[contains(@containerclass, 'mbl_board')]//div[@slide-title][contains(.,'Revenue')]/..//button[contains(text(), 'Load from Template')]"))
    save_as_template_button = Button((By.XPATH, "//*[contains(@containerclass, 'mbl_board')]//div[@slide-title][contains(.,'Revenue')]/..//button[contains(text(), 'Save as Template')]"))

    select_all_checkbox = Checkbox(
        (By.XPATH, "//*[contains(@containerclass, 'mbl_board')]//div[@slide-title][contains(.,'Revenue')]/..//div[contains(@class, 'ag-header')]//label[contains(@class, 'chkcontainer')]//input"),
        click_locator=(By.XPATH, "//*[contains(@containerclass, 'mbl_board')]//div[@slide-title][contains(.,'Revenue')]/..//div[contains(@class, 'ag-header')]//label[contains(@class, 'chkcontainer')]//span"))
    empty_info = Element((By.XPATH, "//*[contains(@containerclass, 'mbl_board')]//div[@slide-title][contains(.,'Revenue')]/..//td[@class='col-empty pointer']"))

    def __new__(cls, index=1):
        index = int(index)
        if index not in cls._rows:
            cls._rows[index] = super().__new__(cls)
        return cls._rows[index]

    def __init__(self, index=1):
        index = int(index) - 1
        def ROW_XPATH(xpath):
            return "//*[contains(@containerclass, 'mbl_board')]//div[@slide-title][contains(.,'Revenue')]/..//div[@row-index='{0}']{1}".format(index, xpath)

        self.check_checkbox = Checkbox(
            (By.XPATH, ROW_XPATH("//div[contains(@col-id, 'chk')]//input")),
            click_locator=(By.XPATH, ROW_XPATH("//div[contains(@col-id, 'chk')]//span"))
        )
        self.bill_to_autocomplete = Autocomplete((By.XPATH, ROW_XPATH("//celltpselect")), (By.XPATH, "//ng-dropdown-panel//input[@type='search']"), disabled_locator=(By.XPATH, ROW_XPATH("//celltpselect//input")))
        self.freight_code_autocomplete = Autocomplete((By.XPATH, ROW_XPATH("//cellbillingselect//input")), (By.XPATH, "//ng-dropdown-panel//input"), check_after_input=False)
        self.freight_description_input = Input((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'name')]//input")))
        self.p_c_select = Select((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'freight_term')]//select")))
        self.unit_select = Select((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'unit')]//select")))
        self.currency_select = Select((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'currency')]//select")))
        self.vol_input = Input((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'volume')]//input")))
        self.rate_input = Input((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'rate')]//input")))
        self.tax_select = Select((By.XPATH, "({})[{}]".format(ROW_XPATH("//select"), 4)))
        self.amount_input = Input((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'currency_amount')]//input")))
        self.invoice_no_autocomplete = Autocomplete((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'invoice_no_view')]//ng-select")), (By.XPATH, "//ng-dropdown-panel//input"), disabled_locator=(By.XPATH, ROW_XPATH("//div[contains(@col-id, 'invoice_no_view')]//ng-select//input")))
        self.action_button = Button((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'action')]//div")))
        self.action_block_button = Button((By.XPATH, "//bs-dropdown-container//li[contains(.,'Block')]"))
        self.action_unblock_button = Button((By.XPATH, "//bs-dropdown-container//li[contains(.,'Unblock')]"))
        self.action_print_mail_button = Button((By.XPATH, "//bs-dropdown-container//li[contains(.,'Print / Mail')]"))

    @staticmethod
    def get_len():
        return Driver.num_of_element("//hcslidecontainer[contains(@containerclass, 'mbl_board')]//div[@slide-title][contains(.,'Revenue')]/..//div[@role='rowgroup'][contains(@class, 'ag-center-cols-container')]/div")


class BaseAccountingBillingBasedMBLCost:
    _rows = {}
    new_button = Button((By.XPATH, "//*[contains(@containerclass, 'mbl_board')]//div[@slide-title][contains(.,'Cost')]/..//i[@class='fa fa-plus']"))
    new_five_button = Button((By.XPATH, "//*[contains(@containerclass, 'mbl_board')]//div[@slide-title][contains(.,'Cost')]/..//button[contains(text(), '+5')]"))
    add_multiple_button = Button((By.XPATH, "//*[contains(@containerclass, 'mbl_board')]//div[@slide-title][contains(.,'Cost')]/..//button[@dropdowntoggle]"))
    copy_button = Button((By.XPATH, "//*[contains(@containerclass, 'mbl_board')]//div[@slide-title][contains(.,'Cost')]/..//acctwizardbutton/div/button[1]"))
    copy_to_button = Button((By.XPATH, "//*[contains(@containerclass, 'mbl_board')]//div[@slide-title][contains(.,'Cost')]/..//acctwizardbutton/div/div/button"))
    delete_button = Button((By.XPATH, "//*[contains(@containerclass, 'mbl_board')]//div[@slide-title][contains(.,'Cost')]/..//acctwizardbutton/div/button[2]"))
    load_from_template_button = Button((By.XPATH, "//*[contains(@containerclass, 'mbl_board')]//div[@slide-title][contains(.,'Cost')]/..//button[contains(text(), 'Load from Template')]"))
    save_as_template_button = Button((By.XPATH, "//*[contains(@containerclass, 'mbl_board')]//div[@slide-title][contains(.,'Cost')]/..//button[contains(text(), 'Save as Template')]"))

    select_all_checkbox = Checkbox(
        (By.XPATH, "//*[contains(@containerclass, 'mbl_board')]//div[@slide-title][contains(.,'Cost')]/..//div[contains(@class, 'ag-header')]//label[contains(@class, 'chkcontainer')]//input"),
        click_locator=(By.XPATH, "//*[contains(@containerclass, 'mbl_board')]//div[@slide-title][contains(.,'Cost')]/..//div[contains(@class, 'ag-header')]//label[contains(@class, 'chkcontainer')]//span"))
    empty_info = Element((By.XPATH, "//*[contains(@containerclass, 'mbl_board')]//div[@slide-title][contains(.,'Cost')]/..//td[@class='col-empty pointer']"))

    def __new__(cls, index=1):
        index = int(index)
        if index not in cls._rows:
            cls._rows[index] = super().__new__(cls)
        return cls._rows[index]

    def __init__(self, index=1):
        index = int(index) - 1
        def ROW_XPATH(xpath):
            return "//*[contains(@containerclass, 'mbl_board')]//div[@slide-title][contains(.,'Cost')]/..//div[@row-index='{0}']{1}".format(index, xpath)

        self.check_checkbox = Checkbox(
            (By.XPATH, ROW_XPATH("//div[contains(@col-id, 'chk')]//input")),
            click_locator=(By.XPATH, ROW_XPATH("//div[contains(@col-id, 'chk')]//span"))
        )
        self.bill_to_autocomplete = Autocomplete((By.XPATH, ROW_XPATH("//celltpselect")), (By.XPATH, "//ng-dropdown-panel//input[@type='search']"), disabled_locator=(By.XPATH, ROW_XPATH("//celltpselect//input")))
        self.freight_code_autocomplete = Autocomplete((By.XPATH, ROW_XPATH("//cellbillingselect//input")), (By.XPATH, "//ng-dropdown-panel//input"), check_after_input=False)
        self.freight_description_input = Input((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'name')]//input")))
        self.p_c_select = Select((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'freight_term')]//select")))
        self.unit_select = Select((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'unit')]//select")))
        self.currency_select = Select((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'currency')]//select")))
        self.vol_input = Input((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'volume')]//input")))
        self.rate_input = Input((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'rate')]//input")))
        self.amount_input = Input((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'currency_amount')]//input")))
        self.vendor_invoice_no_autocomplete = Autocomplete((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'invoice_no_view')]//ng-select")), (By.XPATH, "//ng-dropdown-panel//input"), disabled_locator=(By.XPATH, ROW_XPATH("//div[contains(@col-id, 'invoice_no_view')]//ng-select//input")))
        self.action_button = Button((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'action')]//div")))
        self.action_block_button = Button((By.XPATH, "//bs-dropdown-container//li[contains(.,'Block')]"))
        self.action_unblock_button = Button((By.XPATH, "//bs-dropdown-container//li[contains(.,'Unblock')]"))
        self.action_print_mail_button = Button((By.XPATH, "//bs-dropdown-container//li[contains(.,'Print / Mail')]"))

    @staticmethod
    def get_len():
        return Driver.num_of_element("//hcslidecontainer[contains(@containerclass, 'mbl_board')]//div[@slide-title][contains(.,'Cost')]/..//div[@role='rowgroup'][contains(@class, 'ag-center-cols-container')]/div")


class BaseAccountingBillingBasedHBLRevenue:
    _rows = {}
    new_button = Button((By.XPATH, "//*[contains(@class,'hbl_board')]//div[@slide-title][contains(.,'Revenue')]/..//div[contains(@class, 'btn-group')]//i[@class='fa fa-plus']"))
    new_five_button = Button((By.XPATH, "//*[contains(@class,'hbl_board')]//div[@slide-title][contains(.,'Revenue')]/..//button[contains(.,'+5')]"))
    add_multiple_button = Button((By.XPATH, "//*[contains(@class,'hbl_board')]//div[@slide-title][contains(.,'Revenue')]/..//button[@dropdowntoggle]"))
    copy_button = Button((By.XPATH, "//*[contains(@class,'hbl_board')]//div[@slide-title][contains(.,'Revenue')]/..//acctwizardbutton/div/button[1]"))
    copy_to_button = Button((By.XPATH, "//*[contains(@class,'hbl_board')]//div[@slide-title][contains(.,'Revenue')]/..//acctwizardbutton/div/div/button"))
    delete_button = Button((By.XPATH, "//*[contains(@class,'hbl_board')]//div[@slide-title][contains(.,'Revenue')]/..//acctwizardbutton/div/button[2]"))
    load_from_template_button = Button((By.XPATH, "//*[contains(@class,'hbl_board')]//div[@slide-title][contains(.,'Revenue')]/..//button[contains(text(), 'Load from Template')]"))
    save_as_template_button = Button((By.XPATH, "//*[contains(@class,'hbl_board')]//div[@slide-title][contains(.,'Revenue')]/..//button[contains(text(), 'Save as Template')]"))

    select_all_checkbox = Checkbox(
        (By.XPATH, "//*[contains(@class,'hbl_board')]//div[@slide-title][contains(.,'Revenue')]/..//div[@class='ag-header-row']//label[contains(@class, 'chkcontainer')]//input"),
        click_locator=(By.XPATH, "//*[contains(@class,'hbl_board')]//div[@slide-title][contains(.,'Revenue')]/..//div[@class='ag-header-row']//label[contains(@class, 'chkcontainer')]//span"))
    empty_info = Element((By.XPATH, "//*[contains(@class,'hbl_board')]//div[@slide-title][contains(.,'Revenue')]/..//td[@class='col-empty pointer']"))

    def __new__(cls, index=1):
        index = int(index)
        if index not in cls._rows:
            cls._rows[index] = super().__new__(cls)
        return cls._rows[index]

    def __init__(self, index=1):
        index = int(index) - 1
        def ROW_XPATH(xpath):
            return "//*[contains(@class,'hbl_board')]//div[@slide-title][contains(.,'Revenue')]/..//div[@row-index='{0}']{1}".format(index, xpath)

        self.check_checkbox = Checkbox(
            (By.XPATH, ROW_XPATH("//div[contains(@col-id, 'chk')]//input")),
            click_locator=(By.XPATH, ROW_XPATH("//div[contains(@col-id, 'chk')]//span"))
        )
        self.bill_to_autocomplete = Autocomplete((By.XPATH, ROW_XPATH("//celltpselect")), (By.XPATH, "//ng-dropdown-panel//input[@type='search']"), disabled_locator=(By.XPATH, ROW_XPATH("//celltpselect//input")))
        self.freight_code_autocomplete = Autocomplete((By.XPATH, ROW_XPATH("//cellbillingselect//input")), (By.XPATH, "//ng-dropdown-panel//input[@type='text']"), check_after_input=False)
        self.freight_description_input = Input((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'name')]//input")))
        self.p_c_select = Select((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'freight_term')]//select")))
        self.unit_select = Select((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'unit')]//select")))
        self.currency_select = Select((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'currency')]//select")))
        self.vol_input = Input((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'volume')]//input")))
        self.rate_input = Input((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'rate')]//input")))
        self.tax_select = Select((By.XPATH, "({})[{}]".format(ROW_XPATH("//select"), 4)))
        self.amount_input = Input((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'currency_amount')]//input")))
        self.invoice_no_autocomplete = Autocomplete((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'invoice_no_view')]//ng-select")), (By.XPATH, "//ng-dropdown-panel//input"), disabled_locator=(By.XPATH, ROW_XPATH("//div[contains(@col-id, 'invoice_no_view')]//ng-select//input")))
        self.action_button = Button((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'action')]//div[@dropdown]")))
        self.action_block_button = Button((By.XPATH, "//bs-dropdown-container//li[contains(.,'Block')]"))
        self.action_unblock_button = Button((By.XPATH, "//bs-dropdown-container//li[contains(.,'Unblock')]"))
        self.action_print_mail_button = Button((By.XPATH, "//bs-dropdown-container//li[contains(.,'Print / Mail')]"))

    @staticmethod
    def get_len():
        return Driver.num_of_element("//*[contains(@class, 'hbl_board')]//div[@slide-title][contains(.,'Revenue')]/..//div[@role='rowgroup'][contains(@class, 'ag-center-cols-container')]/div")


class BaseAccountingBillingBasedHBLCost:
    _rows = {}
    new_button = Button((By.XPATH, "//*[contains(@class,'hbl_board')]//div[@slide-title][contains(.,'Cost')]/..//i[@class='fa fa-plus']"))
    new_five_button = Button((By.XPATH, "//*[contains(@class,'hbl_board')]//div[@slide-title][contains(.,'Cost')]/..//button[contains(.,'+5')]"))
    add_multiple_button = Button((By.XPATH, "//*[contains(@class,'hbl_board')]//div[@slide-title][contains(.,'Cost')]/..//button[@dropdowntoggle]"))
    copy_button = Button((By.XPATH, "//*[contains(@class,'hbl_board')]//div[@slide-title][contains(.,'Cost')]/..//acctwizardbutton/div/button[1]"))
    copy_to_button = Button((By.XPATH, "//*[contains(@class,'hbl_board')]//div[@slide-title][contains(.,'Cost')]/..//acctwizardbutton/div/div/button"))
    delete_button = Button((By.XPATH, "//*[contains(@class,'hbl_board')]//div[@slide-title][contains(.,'Cost')]/..//acctwizardbutton/div/button[2]"))
    load_from_template_button = Button((By.XPATH, "//*[contains(@class,'hbl_board')]//div[@slide-title][contains(.,'Cost')]/..//button[contains(text(), 'Load from Template')]"))
    save_as_template_button = Button((By.XPATH, "//*[contains(@class,'hbl_board')]//div[@slide-title][contains(.,'Cost')]/..//button[contains(text(), 'Save as Template')]"))

    select_all_checkbox = Checkbox(
            (By.XPATH, "//*[contains(@class,'hbl_board')]//div[@slide-title][contains(.,'Cost')]/..//div[@class='ag-header-row']//label[contains(@class, 'chkcontainer')]//input"),
            click_locator=(By.XPATH, "//*[contains(@class,'hbl_board')]//div[@slide-title][contains(.,'Cost')]/..//div[@class='ag-header-row']//label[contains(@class, 'chkcontainer')]//span"))
    empty_info = Element((By.XPATH, "//*[contains(@class,'hbl_board')]//div[@slide-title][contains(.,'Cost')]/..//td[@class='col-empty pointer']"))

    def __new__(cls, index=1):
        index = int(index)
        if index not in cls._rows:
            cls._rows[index] = super().__new__(cls)
        return cls._rows[index]

    def __init__(self, index=1):
        index = int(index) - 1
        def ROW_XPATH(xpath):
            return "//*[contains(@class,'hbl_board')]//div[@slide-title][contains(.,'Cost')]/..//div[@row-index='{0}']{1}".format(index, xpath)

        self.check_checkbox = Checkbox(
                (By.XPATH, ROW_XPATH("//div[contains(@col-id, 'chk')]//input")),
                click_locator=(By.XPATH, ROW_XPATH("//div[contains(@col-id, 'chk')]//span"))
            )
        self.cost_share_checkbox = Checkbox((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'is_cost_share')]//input")), click_locator=((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'is_cost_share')]//span"))))
        self.bill_to_autocomplete = Autocomplete((By.XPATH, ROW_XPATH("//celltpselect")), (By.XPATH, "//ng-dropdown-panel//input[@type='search']"), disabled_locator=(By.XPATH, ROW_XPATH("//celltpselect//input")))
        self.freight_code_autocomplete = Autocomplete((By.XPATH, ROW_XPATH("//cellbillingselect//input")), (By.XPATH, "//ng-dropdown-panel//input"), check_after_input=False)
        self.freight_description_input = Input((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'name')]//input")))
        self.p_c_select = Select((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'freight_term')]//select")))
        self.unit_select = Select((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'unit')]//select")))
        self.currency_select = Select((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'currency')]//select")))
        self.vol_input = Input((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'volume')]//input")))
        self.rate_input = Input((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'rate')]//input")))
        self.amount_input = Input((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'currency_amount')]//input")))
        self.vendor_invoice_no_autocomplete = Autocomplete((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'invoice_no_view')]//ng-select")), (By.XPATH, "//ng-dropdown-panel//input"), disabled_locator=(By.XPATH, ROW_XPATH("//div[contains(@col-id, 'invoice_no_view')]//ng-select//input")))
        self.action_button = Button((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'action')]//div[@dropdown]")))
        self.action_block_button = Button((By.XPATH, "//bs-dropdown-container//li[contains(.,'Block')]"))
        self.action_unblock_button = Button((By.XPATH, "//bs-dropdown-container//li[contains(.,'Unblock')]"))
        self.action_print_mail_button = Button((By.XPATH, "//bs-dropdown-container//li[contains(.,'Print / Mail')]"))

    @staticmethod
    def get_len():
        return Driver.num_of_element("//*[contains(@class, 'hbl_board')]//div[@slide-title][contains(.,'Cost')]/..//div[@role='rowgroup'][contains(@class, 'ag-center-cols-container')]/div")


class BaseMBLAmount:
    include_draft_amount_checkbox = Checkbox((By.XPATH, "//acctwizardtable//span/input"))
    mbl_revenue_label = Label((By.XPATH, "//acctwizardtable//div[@class='w-49per'][1]//td[contains(@class, 'text-primary')][1]"))
    mbl_cost_label = Label((By.XPATH, "//acctwizardtable//div[@class='w-49per'][1]//td[contains(@class, 'text-primary')][2]"))
    mbl_amount_label = Label((By.XPATH, "//acctwizardtable//div[@class='w-49per'][1]//td[contains(@class, 'text-primary')][3]"))


class BaseHBLAmount:
    include_draft_amount_checkbox = Checkbox((By.XPATH, "//acctwizardtablehbl//span/input"))
    hbl_revenue_label = Label((By.XPATH, "//acctwizardtablehbl//div[@class='w-49per'][1]//td[contains(@class, 'text-primary')][1]"))
    hbl_cost_label = Label((By.XPATH, "//acctwizardtablehbl//div[@class='w-49per'][1]//td[contains(@class, 'text-primary')][2]"))
    hbl_amount_label = Label((By.XPATH, "//acctwizardtablehbl//div[@class='w-49per'][1]//td[contains(@class, 'text-primary')][3]"))


class BaseMAWBAmount:
    include_draft_amount_checkbox = Checkbox((By.XPATH, "//acctwizardtable//span/input"))
    mawb_revenue_label = Label((By.XPATH, "//acctwizardtable//div[@class='w-49per'][1]//td[contains(@class, 'text-primary')][1]"))
    mawb_cost_label = Label((By.XPATH, "//acctwizardtable//div[@class='w-49per'][1]//td[contains(@class, 'text-primary')][2]"))
    mawb_amount_label = Label((By.XPATH, "//acctwizardtable//div[@class='w-49per'][1]//td[contains(@class, 'text-primary')][3]"))


class BaseHAWBAmount:
    include_draft_amount_checkbox = Checkbox((By.XPATH, "//acctwizardtablehbl//span/input"))
    hawb_revenue_label = Label((By.XPATH, "//acctwizardtablehbl//div[@class='w-49per'][1]//td[contains(@class, 'text-primary')][1]"))
    hawb_cost_label = Label((By.XPATH, "//acctwizardtablehbl//div[@class='w-49per'][1]//td[contains(@class, 'text-primary')][2]"))
    hawb_amount_label = Label((By.XPATH, "//acctwizardtablehbl//div[@class='w-49per'][1]//td[contains(@class, 'text-primary')][3]"))


class BaseMBLShipmentProfit:
    profit_amount_label = Label((By.XPATH, "//acctwizardtable//div[@class='w-49per'][2]//tr[last()]/td[contains(@class, 'bold')][1]"))
    profit_percentage_label = Label((By.XPATH, "//acctwizardtable//div[@class='w-49per'][2]//td[@rowspan][1]"))
    profit_margin_label = Label((By.XPATH, "//acctwizardtable//div[@class='w-49per'][2]//td[@rowspan][2]"))


class BaseHBLShipmentProfit:
    profit_amount_label = Label((By.XPATH, "//acctwizardtablehbl//div[@class='w-49per'][2]//tr[last()]/td[contains(@class, 'bold')][1]"))
    profit_percentage_label = Label((By.XPATH, "//acctwizardtablehbl//div[@class='w-49per'][2]//td[@rowspan][1]"))
    profit_margin_label = Label((By.XPATH, "//acctwizardtablehbl//div[@class='w-49per'][2]//td[@rowspan][2]"))
