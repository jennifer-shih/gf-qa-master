from selenium.webdriver.common.by import By

from src.elements import *


class PaymentPlanListPage:
    filter_button = Button((By.XPATH, "//*[@ng-click='vm.resetFilter()']"))
    config_button = Button((By.XPATH, "//a[@ng-click='vm.openListConfigModal()']"))
    excel_button = Button((By.XPATH, "//div[@ng-if='vm.showExcelBtn']//a"))
    excel_download_button = Button((By.XPATH, "//a[@ng-click='vm.downloadExcel()']"))
    excel_config_button = Button((By.XPATH, "//a[@ng-click='vm.openExcelConfigModal()']"))

    list_table = Element((By.XPATH, "//ag-grid-angular"))
    new_payment_plan_button = Button((By.XPATH, "//hc-pagination-btn-group//a[@herf='/accounting/payment-plan/entry/']"))
    make_receive_payment_button = Button((By.XPATH, "//button[contains(., 'Make / Receive Payment')]"))
    delete_button = Button((By.XPATH, "//button[@ng-click='vm.deleteItem()']"))
    page_offset_select = Select((By.XPATH, "//select[@ng-model='vm.list.offset']"))

    class Filter:
        pin_status_icon = StatusIcon((By.XPATH, "//hc-filter-pin//span"),
            {
                "Unpinned": "//hc-filter-pin//span[not(contains(@class, 'pin-lock'))]",
                "Pinned": "//hc-filter-pin//span[contains(@class, 'pin-lock')]"
            })
        keyword_input = Input((By.XPATH, "//input[../label[contains(., 'Keyword')]]"))
        office_autocomplete_multi_select = AutocompleteMultiSelect((By.XPATH, "//hc-department-multi-select[@hc-class='value-sm']"),
                                    (By.XPATH, "//hc-department-multi-select[@hc-class='value-sm']//ng-dropdown-panel//input"),
                                    (By.XPATH, "//hc-department-multi-select[@hc-class='value-sm']//ng-dropdown-panel//div[@role='option'][1]"),
                                    (By.XPATH, "//hc-department-multi-select[@hc-class='value-sm']//span[@title='Clear all']"))
        party_autocomplete = Autocomplete((By.XPATH, "//hc-tp-select[@ng-model=\"vm.filter.input['customer']\"]"),
                                        (By.XPATH, "//hc-tp-select[@ng-model=\"vm.filter.input['customer']\"]//input[@type='search']"))
        plan_type_select = Select((By.XPATH, "//select[../label[contains(., 'Plan Type')]]"))
        post_date_period_datepicker = PeriodDatepicker((By.XPATH, "//input[../label[contains(., 'Post Date')]]"),
                                               (By.XPATH, "//input[@name='daterangepicker_start']"),
                                               (By.XPATH, "//input[@name='daterangepicker_end']"))
        vessel_autocomplete = Autocomplete((By.XPATH, "//hc-vessel-select[@model=\"vm.filter.input['vessel']\"]"),
                                        (By.XPATH, "//hc-vessel-select[@model=\"vm.filter.input['vessel']\"]//input[@type='search']"))

        voyage_input = Input((By.XPATH, "//input[../label[contains(., 'Voyage')]]"))
        amount_min_input = Input((By.XPATH, "//input[../label[contains(., 'Amount')][not(contains(., 'Paid'))]][@ng-model='vm.filter.input[vm.minKey]']"))
        amount_max_input = Input((By.XPATH, "//input[../label[contains(., 'Amount')][not(contains(., 'Paid'))]][@ng-model='vm.filter.input[vm.maxKey]']"))
        paid_amount_min_input = Input((By.XPATH, "//input[../label[contains(., 'Paid Amount')]][@ng-model='vm.filter.input[vm.minKey]']"))
        paid_amount_max_input = Input((By.XPATH, "//input[../label[contains(., 'Paid Amount')]][@ng-model='vm.filter.input[vm.maxKey]']"))
        balance_min_input = Input((By.XPATH, "//input[../label[contains(., 'Balance')]][@ng-model='vm.filter.input[vm.minKey]']"))
        balance_max_input = Input((By.XPATH, "//input[../label[contains(., 'Balance')]][@ng-model='vm.filter.input[vm.minKey]']"))
        flight_no_input = Input((By.XPATH, "//input[../label[contains(., 'Flight No.')]]"))
        container_no_input = Input((By.XPATH, "//input[../label[contains(., 'Container No.')]]"))
        reconciliation_no_input = Input((By.XPATH, "//input[../label[contains(., 'Reconciliation No.')]]"))
        customer_reference_no_input = Input((By.XPATH, "//input[../label[contains(., 'Customer Reference No.')]]"))
        sales_select = Select((By.XPATH, "//select[../label[contains(., 'Sales')]]"))
        issued_by_select = Select((By.XPATH, "//select[../label[contains(., 'Issued by')]]"))
        e_invoice_select = Select((By.XPATH, "//select[../label[contains(., 'E-Invoice')]]"))
        status_dropdown_multi_select = DropdownMultiSelect((By.XPATH, "//ng-dropdown-multiselect[../label[contains(., 'Status')][not(contains(., 'Latest'))]]"))
        latest_status_select = Select((By.XPATH, "//select[../label[contains(., 'Latest Status')]]"))
        apply_filters_button = Button((By.XPATH, "//button[text()='Apply Filters']"))

    class Header:
        def __init__(self, strategy: int = 0):
            def HEADER_XPATH(xpath):
                UNCARED_XPATH = f'(//div[contains(@class, "ag-pinned-left-header")] | //div[contains(@class, "ag-header-viewport")]){xpath}'
                NORMAL_XPATH = f'//div[contains(@class, "ag-header-viewport")]{xpath}'
                PINNED_XPATH = f'//div[contains(@class, "ag-pinned-left-header")]{xpath}'
                if strategy == 0:
                    return UNCARED_XPATH
                elif strategy == 1:
                    return NORMAL_XPATH
                elif strategy == 2:
                    return PINNED_XPATH

            self.check_all_checkbox = Checkbox((By.XPATH, HEADER_XPATH('//div[contains(@col-id, "chk")][contains(@class, "ag-header-cell")]//cellcheckbox//input')))
            self.approval_status_table_header = TableHeader((By.XPATH, HEADER_XPATH('//div[contains(@col-id, "approval_info")]//div[contains(@class, "ag-cell-label-container")]')))
            self.payment_plan_no_table_header = TableHeader((By.XPATH, HEADER_XPATH('//div[contains(@col-id, "payment_plan_no")]//div[contains(@class, "ag-cell-label-container")]')), True)
            self.plan_type_table_header = TableHeader((By.XPATH, HEADER_XPATH('//div[contains(@col-id, "is_paid_by_customer")]//div[contains(@class, "ag-cell-label-container")]')), True)
            self.party_table_header = TableHeader((By.XPATH, HEADER_XPATH('//div[contains(@col-id, "customer")][not(contains(@col-id,"paid_by"))]//div[contains(@class, "ag-cell-label-container")]')), True)
            self.post_date_table_header = TableHeader((By.XPATH, HEADER_XPATH('//div[contains(@col-id, "post_date")]//div[contains(@class, "ag-cell-label-container")]')), True)
            self.file_no_table_header = TableHeader((By.XPATH, HEADER_XPATH('//div[contains(@col-id, "filing_no_list")]//div[contains(@class, "ag-cell-label-container")]')))
            self.mb_l_no_table_header = TableHeader((By.XPATH, HEADER_XPATH('//div[contains(@col-id, "mbl_no_list")]//div[contains(@class, "ag-cell-label-container")]')))
            self.hb_l_no_table_header = TableHeader((By.XPATH, HEADER_XPATH('//div[contains(@col-id, "hbl_no_list")]//div[contains(@class, "ag-cell-label-container")]')))
            self.eta_table_header = TableHeader((By.XPATH, HEADER_XPATH('//div[contains(@col-id, "eta_list")]//div[contains(@class, "ag-cell-label-container")]')))
            self.etd_table_header = TableHeader((By.XPATH, HEADER_XPATH('//div[contains(@col-id, "etd_list")]//div[contains(@class, "ag-cell-label-container")]')))
            self.amount_table_header = TableHeader((By.XPATH, HEADER_XPATH('//span[contains(@class, "ag-header-cell-text")][.="Amount"]')))
            self.amount_receivable_table_header = TableHeader((By.XPATH, HEADER_XPATH('//span[contains(@class, "ag-header-cell-text")][.="Amount (Receivable)"]')))
            self.amount_payable_table_header = TableHeader((By.XPATH, HEADER_XPATH('//span[contains(@class, "ag-header-cell-text")][.="Amount (Payable)"]')))
            self.paid_amount_table_header = TableHeader((By.XPATH, HEADER_XPATH('//span[contains(@class, "ag-header-cell-text")][.="Paid Amount"]')))
            self.paid_amount_collected_table_header = TableHeader((By.XPATH, HEADER_XPATH('//span[contains(@class, "ag-header-cell-text")][.="Paid Amount (Collected)"]')))
            self.paid_amount_paid_out_table_header = TableHeader((By.XPATH, HEADER_XPATH('//span[contains(@class, "ag-header-cell-text")][.="Paid Amount (Paid Out)"]')))
            self.balance_table_header = TableHeader((By.XPATH, HEADER_XPATH('//span[contains(@class, "ag-header-cell-text")][.="Balance"]')))
            self.last_paid_date_table_header = TableHeader((By.XPATH, HEADER_XPATH('//div[contains(@col-id, "last_paid_date")]//div[contains(@class, "ag-cell-label-container")]')))
            self.invoice_no_table_header = TableHeader((By.XPATH, HEADER_XPATH('//div[contains(@col-id, "invoice_no_list")]//div[contains(@class, "ag-cell-label-container")]')))
            self.booking_no_table_header = TableHeader((By.XPATH, HEADER_XPATH('//div[contains(@col-id, "booking_no_list")]//div[contains(@class, "ag-cell-label-container")]')))
            self.flight_no_table_header = TableHeader((By.XPATH, HEADER_XPATH('//div[contains(@col-id, "flight_no_list")]//span[contains(@class, "ag-header-cell-text")]')))
            self.reconciliation_no_table_header = TableHeader((By.XPATH, HEADER_XPATH('//div[contains(@col-id, "reconciliation_no")]//span[contains(@class, "ag-header-cell-text")]')))
            self.customer_reference_no_table_header = TableHeader((By.XPATH, HEADER_XPATH('//div[contains(@col-id, "customer_ref_no")]//span[contains(@class, "ag-header-cell-text")]')))
            self.office_table_header = TableHeader((By.XPATH, HEADER_XPATH('//div[contains(@col-id, "office_name")]//div[contains(@class, "ag-cell-label-container")]')), True)
            self.issued_by_table_header = TableHeader((By.XPATH, HEADER_XPATH('//div[contains(@col-id, "issue_by_name")]//div[contains(@class, "ag-cell-label-container")]')), True)
            self.vessel_table_header = TableHeader((By.XPATH, HEADER_XPATH('//div[contains(@col-id, "vessel_list")]//span[contains(@class, "ag-header-cell-text")]')))
            self.voyage_table_header = TableHeader((By.XPATH, HEADER_XPATH('//div[contains(@col-id, "voyage_list")]//span[contains(@class, "ag-header-cell-text")]')))
            self.operation_table_header = TableHeader((By.XPATH, HEADER_XPATH('//div[contains(@col-id, "operator_name_list")]//span[contains(@class, "ag-header-cell-text")]')))
            self.sales_table_header = TableHeader((By.XPATH, HEADER_XPATH('//div[contains(@col-id, "sales_name_list")]//span[contains(@class, "ag-header-cell-text")]')))
            self.issued_table_header = TableHeader((By.XPATH, HEADER_XPATH('//div[contains(@col-id, "e_invoice_status")]//div[contains(@class, "ag-cell-label-container")]')), True)
            self.e_invoice_no_table_header = TableHeader((By.XPATH, HEADER_XPATH('//div[contains(@col-id, "e_invoice_no_list")]//span[contains(@class, "ag-header-cell-text")]')))
            self.status_table_header = TableHeader((By.XPATH, HEADER_XPATH('//div[contains(@col-id, "accounting_status")]//span[contains(@class, "ag-header-cell-text")]')))

    class SearchResult:
        _instances = {}
        table_element = Element((By.XPATH, "//hcgridcontainer"))
        table_loading_label = Label((By.XPATH, "//hcgridcontainer[contains(@class, 'grid-loading-detail')]"))
        showing_dresciption_label = Label((By.XPATH, "//div[@ng-bind='vm.showRecords()']"))


        def __new__(cls, index=1):
            index = int(index)
            if index not in cls._instances:
                cls._instances[index] = super().__new__(cls)
            return cls._instances[index]

        def __init__(self, index=1):
            index = int(index)
            def ROW_XPATH(xpath):
                return '//hcgridcontainer//div[@role="row"][@row-index="{0}"]{1}'.format(index-1, xpath)
            self.row_element = Element((By.XPATH, f"({ROW_XPATH('')})[1]"))

            self.checkbox_checkbox = Checkbox((By.XPATH, ROW_XPATH('//div[contains(@col-id, "chk")]//input[@type="checkbox"]')), (By.XPATH, ROW_XPATH('//div[contains(@col-id, "chk")]')))
            self.approval_status_label = Label((By.XPATH, ROW_XPATH('//div[contains(@col-id,"approval_info")]//div[last()]')))
            self.payment_plan_no_label = Label((By.XPATH, ROW_XPATH('//div[contains(@col-id,"payment_plan_no")]')))
            self.payment_plan_no_link = Link((By.XPATH, ROW_XPATH('//div[contains(@col-id,"payment_plan_no")]//a')))
            self.plan_type_label = Label((By.XPATH, ROW_XPATH('//div[contains(@col-id,"is_paid_by_customer")]')))
            self.party_label = Label((By.XPATH, ROW_XPATH('//div[contains(@col-id,"customer")][not(contains(@col-id,"paid_by"))]')))
            self.post_date_label = Label((By.XPATH, ROW_XPATH('//div[contains(@col-id,"post_date")]')))
            self.file_no_label = Label((By.XPATH, ROW_XPATH('//div[contains(@col-id,"filing_no_list")]')))
            self.mb_l_no_label = Label((By.XPATH, ROW_XPATH('//div[contains(@col-id,"mbl_no_list")]')))
            self.hb_l_no_label = Label((By.XPATH, ROW_XPATH('//div[contains(@col-id,"hbl_no_list")]')))
            self.eta_label = Label((By.XPATH, ROW_XPATH('//div[@col-id=(//div[contains(@class, "ag-header-cell multiline") and descendant::span[text()="ETA"]]/@col-id)]')))
            self.etd_label = Label((By.XPATH, ROW_XPATH('//div[@col-id=(//div[contains(@class, "ag-header-cell multiline") and descendant::span[text()="ETD"]]/@col-id)]')))
            self.amount_label = Label((By.XPATH, ROW_XPATH('//div[@col-id=(//div[contains(@class, "ag-header-cell multiline") and descendant::span[text()="Amount"]]/@col-id)]')))
            self.amount_receivable_label = Label((By.XPATH, ROW_XPATH('//div[@col-id=(//div[contains(@class, "ag-header-cell multiline") and descendant::span[text()="Amount (Receivable)"]]/@col-id)]')))
            self.amount_payable_label = Label((By.XPATH, ROW_XPATH('//div[@col-id=(//div[contains(@class, "ag-header-cell multiline") and descendant::span[text()="Amount (Payable)"]]/@col-id)]')))
            self.paid_amount_label = Label((By.XPATH, ROW_XPATH('//div[@col-id=(//div[contains(@class, "ag-header-cell multiline") and descendant::span[text()="Paid Amount"]]/@col-id)]')))
            self.paid_amount_collected_label = Label((By.XPATH, ROW_XPATH('//div[@col-id=(//div[contains(@class, "ag-header-cell multiline") and descendant::span[text()="Paid Amount (Collected)"]]/@col-id)]')))
            self.paid_amount_paid_out_label = Label((By.XPATH, ROW_XPATH('//div[@col-id=(//div[contains(@class, "ag-header-cell multiline") and descendant::span[text()="Paid Amount (Paid Out)"]]/@col-id)]')))
            self.balance_label = Label((By.XPATH, ROW_XPATH('//div[@col-id=(//div[contains(@class, "ag-header-cell multiline") and descendant::span[text()="Balance"]]/@col-id)]')))
            self.last_paid_date_label = Label((By.XPATH, ROW_XPATH('//div[contains(@col-id,"last_paid_date")]')))
            self.invoice_no_label = Label((By.XPATH, ROW_XPATH('//div[contains(@col-id,"invoice_no_list")]')))
            self.booking_no_label = Label((By.XPATH, ROW_XPATH('//div[contains(@col-id,"booking_no_list")]')))
            self.flight_no_label = Label((By.XPATH, ROW_XPATH('//div[contains(@col-id,"flight_no_list")]')))
            self.reconciliation_no_label = Label((By.XPATH, ROW_XPATH('//div[contains(@col-id,"reconciliation_no")]')))
            self.customer_reference_no_label = Label((By.XPATH, ROW_XPATH('//div[contains(@col-id,"customer_ref_no")]')))
            self.office_label = Label((By.XPATH, ROW_XPATH('//div[contains(@col-id,"office_name")]')))
            self.issued_by_label = Label((By.XPATH, ROW_XPATH('//div[contains(@col-id,"issue_by_name")]')))
            self.vessel_label = Label((By.XPATH, ROW_XPATH('//div[contains(@col-id,"vessel_list")]')))
            self.voyage_label = Label((By.XPATH, ROW_XPATH('//div[contains(@col-id,"voyage_list")]')))
            self.operation_label = Label((By.XPATH, ROW_XPATH('//div[contains(@col-id,"operator_name_list")]')))
            self.sales_label = Label((By.XPATH, ROW_XPATH('//div[contains(@col-id,"sales_name_list")]')))
            self.issued_label = Label((By.XPATH, ROW_XPATH('//div[contains(@col-id,"e_invoice_status")]')))
            self.issued_info_label = Label((By.XPATH, ROW_XPATH('//div[contains(@col-id,"e_invoice_status")]//i')))
            self.e_invoice_no_label = Label((By.XPATH, ROW_XPATH('//div[contains(@col-id,"e_invoice_no_list")]')))
            self.status_label = Label((By.XPATH, ROW_XPATH('//div[contains(@col-id,"accounting_status")]')))
            # //div[contains(@class, "ag-header-cell multiline") and descendant::span[text()="Amount"]]/@col-id
    class ColConfigModal:
        ENTIRE_CONFIG_XPATH = '//div[@class="modal-dialog"]//ul/li[not(contains(@data-name, "chk"))]'
        CONFIG_WITHOUT_DIVIER = '//div[@class="modal-dialog"]//ul/li[not(contains(@data-name, "chk"))][not(contains(@data-name, "_freeze"))]'
        CONFIG_HAS_CHECKBOX = '//div[@class="modal-dialog"]//ul/li[not(contains(@data-name, "chk"))]//input' # without divider

        def MODAL_XPATH(xpath):
            return '//div[@class="modal-dialog"]{0}'.format(xpath)
        copy_list_view_settings_button = Button((By.XPATH, MODAL_XPATH('//button[@ng-click="vm.handleCopyListViewSettings()"]')))

        freeze_column_divider_col_config = ColConfig((By.XPATH, MODAL_XPATH('//li[@data-name="_freeze"]')))
        approval_status_col_config = ColConfig((By.XPATH, MODAL_XPATH('//li[@data-name="approval_info"]')), (By.XPATH, MODAL_XPATH('//li[@data-name="approval_info"]//input')))
        payment_plan_no_col_config = ColConfig((By.XPATH, MODAL_XPATH('//li[@data-name="payment_plan_no"]')), (By.XPATH, MODAL_XPATH('//li[@data-name="payment_plan_no"]//input')))
        plan_type_col_config = ColConfig((By.XPATH, MODAL_XPATH('//li[@data-name="is_paid_by_customer"]')), (By.XPATH, MODAL_XPATH('//li[@data-name="is_paid_by_customer"]//input')))
        party_col_config = ColConfig((By.XPATH, MODAL_XPATH('//li[@data-name="customer"]')), (By.XPATH, MODAL_XPATH('//li[@data-name="customer"]//input')))
        post_date_col_config = ColConfig((By.XPATH, MODAL_XPATH('//li[@data-name="post_date"]')), (By.XPATH, MODAL_XPATH('//li[@data-name="post_date"]//input')))
        file_no_col_config = ColConfig((By.XPATH, MODAL_XPATH('//li[@data-name="filing_no_list"]')), (By.XPATH, MODAL_XPATH('//li[@data-name="filing_no_list"]//input')))
        mb_l_no_col_config = ColConfig((By.XPATH, MODAL_XPATH('//li[@data-name="mbl_no_list"]')), (By.XPATH, MODAL_XPATH('//li[@data-name="mbl_no_list"]//input')))
        hb_l_no_col_config = ColConfig((By.XPATH, MODAL_XPATH('//li[@data-name="hbl_no_list"]')), (By.XPATH, MODAL_XPATH('//li[@data-name="hbl_no_list"]//input')))
        eta_col_config = ColConfig((By.XPATH, MODAL_XPATH('//li[@data-name="eta_list"]')),(By.XPATH, MODAL_XPATH('//li[@data-name="eta_list"]//input')))
        etd_col_config = ColConfig((By.XPATH, MODAL_XPATH('//li[@data-name="etd_list"]')), (By.XPATH, MODAL_XPATH('//li[@data-name="etd_list"]//input')))
        amount_col_config = ColConfig((By.XPATH, MODAL_XPATH('//li[@data-name="amount"]')), (By.XPATH, MODAL_XPATH('//li[@data-name="amount"]//input')))
        amount_receivable_col_config = ColConfig((By.XPATH, MODAL_XPATH('//li[@data-name="ar_debit_amount"]')), (By.XPATH, MODAL_XPATH('//li[@data-name="ar_debit_amount"]//input')))
        amount_payable_col_config = ColConfig((By.XPATH, MODAL_XPATH('//li[@data-name="ap_credit_amount"]')), (By.XPATH, MODAL_XPATH('//li[@data-name="ap_credit_amount"]//input')))
        paid_amount_col_config = ColConfig((By.XPATH, MODAL_XPATH('//li[@data-name="paid_amount"]')), (By.XPATH, MODAL_XPATH('//li[@data-name="paid_amount"]//input')))
        paid_amount_collected_col_config = ColConfig((By.XPATH, MODAL_XPATH('//li[@data-name="collected"]')), (By.XPATH, MODAL_XPATH('//li[@data-name="collected"]//input')))
        paid_amount_paid_out_col_config = ColConfig((By.XPATH, MODAL_XPATH('//li[@data-name="paid_out"]')), (By.XPATH, MODAL_XPATH('//li[@data-name="paid_out"]//input')))
        balance_col_config = ColConfig((By.XPATH, MODAL_XPATH('//li[@data-name="balance"]')), (By.XPATH, MODAL_XPATH('//li[@data-name="balance"]//input')))
        last_paid_date_col_config = ColConfig((By.XPATH, MODAL_XPATH('//li[@data-name="last_paid_date"]')), (By.XPATH, MODAL_XPATH('//li[@data-name="last_paid_date"]//input')))
        invoice_no_col_config = ColConfig((By.XPATH, MODAL_XPATH('//li[@data-name="invoice_no_list"]')), (By.XPATH, MODAL_XPATH('//li[@data-name="invoice_no_list"]//input')))
        booking_no_col_config = ColConfig((By.XPATH, MODAL_XPATH('//li[@data-name="booking_no_list"]')), (By.XPATH, MODAL_XPATH('//li[@data-name="booking_no_list"]//input')))
        flight_no_col_config = ColConfig((By.XPATH, MODAL_XPATH('//li[@data-name="flight_no_list"]')), (By.XPATH, MODAL_XPATH('//li[@data-name="flight_no_list"]//input')))
        reconciliation_no_col_config = ColConfig((By.XPATH, MODAL_XPATH('//li[@data-name="reconciliation_no"]')), (By.XPATH, MODAL_XPATH('//li[@data-name="reconciliation_no"]//input')))
        customer_reference_no_col_config = ColConfig((By.XPATH, MODAL_XPATH('//li[@data-name="customer_ref_no"]')), (By.XPATH, MODAL_XPATH('//li[@data-name="customer_ref_no"]//input')))
        office_col_config = ColConfig((By.XPATH, MODAL_XPATH('//li[@data-name="office_name"]')), (By.XPATH, MODAL_XPATH('//li[@data-name="office_name"]//input')))
        issued_by_col_config = ColConfig((By.XPATH, MODAL_XPATH('//li[@data-name="issue_by_name"]')), (By.XPATH, MODAL_XPATH('//li[@data-name="issue_by_name"]//input')))
        vessel_col_config = ColConfig((By.XPATH, MODAL_XPATH('//li[@data-name="vessel_list"]')), (By.XPATH, MODAL_XPATH('//li[@data-name="vessel_list"]//input')))
        voyage_col_config = ColConfig((By.XPATH, MODAL_XPATH('//li[@data-name="voyage_list"]')), (By.XPATH, MODAL_XPATH('//li[@data-name="voyage_list"]//input')))
        operation_col_config = ColConfig((By.XPATH, MODAL_XPATH('//li[@data-name="operator_name_list"]')), (By.XPATH, MODAL_XPATH('//li[@data-name="operator_name_list"]//input')))
        sales_col_config = ColConfig((By.XPATH, MODAL_XPATH('//li[@data-name="sales_name_list"]')), (By.XPATH, MODAL_XPATH('//li[@data-name="sales_name_list"]//input')))
        issued_col_config = ColConfig((By.XPATH, MODAL_XPATH('//li[@data-name="e_invoice_status"]')), (By.XPATH, MODAL_XPATH('//li[@data-name="e_invoice_status"]//input')))
        e_invoice_no_col_config = ColConfig((By.XPATH, MODAL_XPATH('//li[@data-name="e_invoice_no_list"]')), (By.XPATH, MODAL_XPATH('//li[@data-name="e_invoice_no_list"]//input')))
        status_col_config = ColConfig((By.XPATH, MODAL_XPATH('//li[@data-name="accounting_status"]')), (By.XPATH, MODAL_XPATH('//li[@data-name="accounting_status"]//input')))

        apply_button = Button((By.XPATH, MODAL_XPATH('//button[@ng-click="vm.ok()"]')))
        cancel_button = Button((By.XPATH, MODAL_XPATH('//button[@ng-click="vm.dismiss()"][contains(@class, "btn")]')))
        save_button = Button((By.XPATH, MODAL_XPATH('//button[@ng-click="vm.handleSave()"]')))
        save_n_download_button = Button((By.XPATH, MODAL_XPATH('//button[@ng-click="vm.handleSaveAndDownload()"]')))
