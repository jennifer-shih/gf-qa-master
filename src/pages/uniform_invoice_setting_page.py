from selenium.webdriver.common.by import By

from src.elements import *


class UniformInvoiceSettingPage:
    new_invoice_roll_button = Button((By.XPATH, "//button[@data-hc-name='uni-invoice-setting-new-btn']"))
    delete_invoice_roll_button = Button((By.XPATH, "//button[@data-hc-name='uni-invoice-setting-delete-btn']"))
    delete_ok_button = Button((By.XPATH, "//div[@class='modal-footer']//button[contains(., 'OK')]"))

    class InvoiceList:
        _rows = {}
        def __new__(cls, index=1):
                index = int(index) - 1
                if index not in cls._rows:
                    cls._rows[index] = super().__new__(cls)
                return cls._rows[index]

        def __init__(self, index=1):
            index = int(index) - 1
            def ROW_XPATH(xpath):
                return "//div[contains(@class,'portlet-body')]//div[@row-id='{0}']{1}".format(index, xpath)

            self.check_checkbox = Checkbox((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'chk')]//input")), (By.XPATH, ROW_XPATH("//div[@col-id='chk_1']//span")))
            self.invoice_month_label = Label((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'uni_invoice_date')]//div")))
            self.prefix_label = Label((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'prefix')]//div")))
            self.starting_no_label = Label((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'begin_no')]//div")))
            self.current_no_label = Label((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'current_assigned_no')]//div")))
            self.ending_no_label = Label((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'end_no')]//div")))
            self.invoice_type_label = Label((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'uni_invoice_type_display_name')]//div")))
            self.status_label = Label((By.XPATH, ROW_XPATH("//div[contains(@col-id, 'status')]//label")))

    class AddInvoiceRoll:
        prefix_input = Input((By.XPATH, "//input[@data-hc-name='add-uni-invoice-roll-modal-prefix']"))
        year_select = Select((By.XPATH, "//select[@data-hc-name='add-uni-invoice-roll-modal-year']"))
        month_select = Select((By.XPATH, "//select[@data-hc-name='add-uni-invoice-roll-modal-month']"))
        uniform_invoice_type_radio_group = RadioGroup({'Duplicate': (By.XPATH, "(//input[@data-hc-name='add-uni-invoice-roll-modal-type'])[1]"),
                                        'Triplicate': (By.XPATH, "(//input[@data-hc-name='add-uni-invoice-roll-modal-type'])[2]")})
        rolls_input = Input((By.XPATH, "//input[@data-hc-name='add-uni-invoice-roll-modal-rolls']"))
        amount_per_roll_input = Input((By.XPATH, "//input[@data-hc-name='add-uni-invoice-roll-modal-amount-per-roll']"))
        invoice_number_begin_input = Input((By.XPATH, "//input[@data-hc-name='add-uni-invoice-roll-modal-invoice-begin-no']"))

        add_button = Button((By.XPATH, "//button[.='Add'][contains(@class, 'green')]"))
