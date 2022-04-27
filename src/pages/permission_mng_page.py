from selenium.webdriver.common.by import By

from src.elements import *


class PermissionMngPage:
    save_button = Button((By.XPATH, "//button[@ng-click='vm.onSave()']"))

    filter_text_input = Input((By.XPATH, "//*[@ng-model='vm.filterText']"))
    invoice_filter_button = Button((By.XPATH, "//*[contains(@ng-click, 'vm.filterTag')][text()='Invoice']"))
    office_select = Select((By.XPATH, "//select[@ng-model='vm.officeId']"))
    office_department_select = Select((By.XPATH, "//select[@ng-model='vm.departmentId']"))
    user_select = Select((By.XPATH, "//select[@ng-model='vm.userId']"))
    view_button = Button((By.XPATH, "//button[@ng-click='vm.view()']"))

    navigator_accounting_payment_plan_select = Select((By.XPATH, "//select[@ng-model='vm.genericPermMapping[row.code][role.id]'][../../td[.='* Navigator Accounting Payment Plan']]"))
    navigator_accounting_payment_plan_excel_select = Select((By.XPATH, "//select[@ng-model='vm.genericPermMapping[row.code][role.id]'][../../td[.='* Navigator Accounting Payment Plan Excel']]"))
    navigator_accounting_payment_plan_list_select = Select((By.XPATH, "//select[@ng-model='vm.genericPermMapping[row.code][role.id]'][../../td[.='* Navigator Accounting Payment Plan List']]"))
    navigator_mawb_no_stock_list_select = Select((By.XPATH, "//select[@ng-model='vm.genericPermMapping[row.code][role.id]'][../../td[.='* Navigator Mawb No. Stock List']]"))
    navigator_setting___awb_no_management_select = Select((By.XPATH, "//select[@ng-model='vm.genericPermMapping[row.code][role.id]'][../../td[.='* Navigator Setting - AWB No. Management']]"))
    mawb_no_stock_list_view_select = Select((By.XPATH, "//select[@ng-model='vm.genericPermMapping[row.code][role.id]'][../../td[.='MAWB No Stock List View']]"))
    mawb_no_stock_list_edit_select = Select((By.XPATH, "//select[@ng-model='vm.genericPermMapping[row.code][role.id]'][../../td[.='MAWB No Stock List Edit']]"))
    trade_partner_edit_select = Select((By.XPATH, "//select[@ng-model='vm.genericPermMapping[row.code][role.id]'][../../td[.='Trade Partner Edit']]"))
    setting_code_delete_select = Select((By.XPATH, "//select[@ng-model='vm.genericPermMapping[row.code][role.id]'][../../td[.='Setting Code Delete']]"))
    setting_code_edit_select = Select((By.XPATH, "//select[@ng-model='vm.genericPermMapping[row.code][role.id]'][../../td[.='Setting Code Edit']]"))
    setting_code_view_select = Select((By.XPATH, "//select[@ng-model='vm.genericPermMapping[row.code][role.id]'][../../td[.='Setting Code View']]"))
    uniform_invoice_edit_void_valid_select = Select((By.XPATH, "//select[@ng-model='vm.genericPermMapping[row.code][role.id]'][../../td[.='Uniform Invoice Edit Void/Valid']]"))
    invoice_ap_view_select = Select((By.XPATH, "//select[@ng-model='vm.genericPermMapping[row.code][role.id]'][../../td[.='Invoice AP View']]"))
    invoice_ar_view_select = Select((By.XPATH, "//select[@ng-model='vm.genericPermMapping[row.code][role.id]'][../../td[.='Invoice AR View']]"))
    invoice_block_select = Select((By.XPATH, "//select[@ng-model='vm.genericPermMapping[row.code][role.id]'][../../td[.='Invoice Block']]"))
    invoice_block_unblock_button_visible_select = Select((By.XPATH, "//select[@ng-model='vm.genericPermMapping[row.code][role.id]'][../../td[.='Invoice Block/Unblock Button Visible']]"))
    invoice_delete_select = Select((By.XPATH, "//select[@ng-model='vm.genericPermMapping[row.code][role.id]'][../../td[.='Invoice Delete']]"))
    invoice_edit_select = Select((By.XPATH, "//select[@ng-model='vm.genericPermMapping[row.code][role.id]'][../../td[.='Invoice Edit']]"))
    invoice_make_receive_payment_button_visible_select = Select((By.XPATH, "//select[@ng-model='vm.genericPermMapping[row.code][role.id]'][../../td[.='Invoice Make/Receive Payment Button Visible']]"))
    invoice_unblock_select = Select((By.XPATH, "//select[@ng-model='vm.genericPermMapping[row.code][role.id]'][../../td[.='Invoice Unblock']]"))
    payment_plan_entry_delete_select = Select((By.XPATH, "//select[@ng-model='vm.genericPermMapping[row.code][role.id]'][../../td[.='Payment Plan Entry Delete']]"))
    payment_plan_entry_edit_select = Select((By.XPATH, "//select[@ng-model='vm.genericPermMapping[row.code][role.id]'][../../td[.='Payment Plan Entry Edit']]"))
    payment_plan_entry_view_self_select = Select((By.XPATH, "//select[@ng-model='vm.genericPermMapping[row.code][role.id]'][../../td[.='Payment Plan Entry View Self']]"))
    payment_plan_entry_view_all_select = Select((By.XPATH, "//select[@ng-model='vm.genericPermMapping[row.code][role.id]'][../../td[.='Payment Plan Entry View All']]"))
    payment_plan_excel_upload_file_select = Select((By.XPATH, "//select[@ng-model='vm.genericPermMapping[row.code][role.id]'][../../td[.='Payment Plan Excel Upload File']]"))
    payment_plan_excel_view_select = Select((By.XPATH, "//select[@ng-model='vm.genericPermMapping[row.code][role.id]'][../../td[.='Payment Plan Excel View']]"))
    payment_plan_list_export_excel_select = Select((By.XPATH, "//select[@ng-model='vm.genericPermMapping[row.code][role.id]'][../../td[.='Payment Plan List Export Excel']]"))
    payment_plan_list_view_all_select = Select((By.XPATH, "//select[@ng-model='vm.genericPermMapping[row.code][role.id]'][../../td[.='Payment Plan List View All']]"))

    class PermissionTable:
        """When we only select 'Office' and click 'view'"""

        _instances = {}
        role_index_mappint = {
            'Admin': 2,
            'Accounting': 3,
            'AM': 4,
            'Sales': 5,
            'SM': 6,
            'SA': 7,
            'OP': 8,
            'OPM': 9,
            'OPA': 10,
            'GM': 11
        }

        def __new__(cls, role):
            if role not in cls.role_index_mappint:
                assert False, 'No role named {}'.format(role)

            if role not in cls._instances:
                cls._instances[role] = super().__new__(cls)
            return cls._instances[role]

        def __init__(self, role):

            def COLUMN_XPATH(xpath):
                index = self.role_index_mappint[role]
                return xpath + "/../td[{0}]//select".format(index)

            # def COLUMN_CHECKBOXX_XPATH(xpath):
            #     index = self.role_index_mappint[role]
            #     return xpath + "/../td[{0}]//span".format(index)

            # # Not working for unknow reason, input可以檢查到值，但span才能點得到
            # self.invoice_ap_view_checkbox = Checkbox((By.XPATH, COLUMN_CHECKBOXX_XPATH("//*[text() = 'Invoice AP View']")))
            # self.invoice_ar_view_checkbox = Checkbox((By.XPATH, COLUMN_CHECKBOXX_XPATH("//*[text() = 'Invoice AR View']")))

            self.invoice_ap_view_select = Select((By.XPATH, COLUMN_XPATH("//*[text() = 'Invoice AP View']")))
            self.invoice_ar_view_select = Select((By.XPATH, COLUMN_XPATH("//*[text() = 'Invoice AR View']")))
            self.invoice_block_select = Select((By.XPATH, COLUMN_XPATH("//*[text() = 'Invoice Block']")))
            self.invoice_block_unblock_button_visible_select = Select((By.XPATH, COLUMN_XPATH("//*[text() = 'Invoice Block/Unblock Button Visible']")))
            self.invoice_delete_select = Select((By.XPATH, COLUMN_XPATH("//*[text() = 'Invoice Delete']")))
            self.invoice_edit_select = Select((By.XPATH, COLUMN_XPATH("//*[text() = 'Invoice Edit']")))
            self.invoice_unblock_select = Select((By.XPATH, COLUMN_XPATH("//*[text() = 'Invoice Unblock']")))
