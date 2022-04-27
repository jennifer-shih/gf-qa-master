from behave import *

import src.pages as Pages
from config import globalparameter as gl
from src.drivers.driver import Driver
from src.helper.function import wday
from src.helper.script import login_as


@Then("'Accounting Mode' switch {should_or_not} show on 'Accounting' tab")
def step_impl(context, should_or_not):
    if should_or_not.lower() == "should":
        result = Pages.ShipmentEntryTab.accounting_mode_switch_button.is_visible()
    elif should_or_not.lower() == "should not":
        result = Pages.ShipmentEntryTab.accounting_mode_switch_button.is_disable()  # TODO GQT-423 檢查是否沒出現在 DOM 上
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    assert result == True, "'Accounting Mode' switch button doesn't match the setting"


@Given("company main currency = '{currency}'")
def step_impl(context, currency):
    login_as("Super Admin")
    Driver.open(gl.URL.COMPANY_MANAGEMENT)
    val = Pages.CompanyMngPage.main_currency_input.get_value()
    assert currency == val, "currency [{0}] is not matched the expect value [{1}].".format(val, currency)


@Given("company other currency contains '{currency}'")
def step_impl(context, currency):
    login_as("Super Admin")
    Driver.open(gl.URL.COMPANY_MANAGEMENT)
    val1 = Pages.CompanyMngPage.multi_currency_enable_checkbox.get_value()
    val2 = Pages.CompanyMngPage.other_currency_tag_input.get_value()
    assert True == val1, "multi currency is not enabled"
    assert currency.lower() in val2.lower().strip(), "currency tag expect [{0}], but get [{1}]".format(
        currency.lower(), val2.lower().strip()
    )


@Given("exchange rate is 1 '{main}' = {rate} '{other_currency}'")
def step_impl(context, main, rate, other_currency):
    login_as("Super Admin")
    Driver.open(gl.URL.CURRENCY_TABLE)
    Pages.Common.spin_bar.gone()
    Pages.CurrencyTablePage.from_currency_select.select(main)
    Pages.CurrencyTablePage.to_currency_select.select(other_currency)

    # 如果有舊的currency table row, 則將其刪除
    # if not CurrencyTablePage.check_all_checkbox.is_disable():
    #     CurrencyTablePage.check_all_checkbox.tick(True)
    #     CurrencyTablePage.delete_button.click()

    # add the currecny row
    Pages.CurrencyTablePage.new_button.click()
    index = Pages.CurrencyTablePage.row.get_len()  # new row will be inserted to the second last of rows
    Pages.CurrencyTablePage.row(index).as_of_datepicker.input(wday(0))
    Pages.CurrencyTablePage.row(index).rate_internal_input.input(rate)
    Pages.CurrencyTablePage.row(index).rate_external_input.input(rate)
    Pages.CurrencyTablePage.save_button.click()
    Pages.Common.spin_bar.gone()


@Given("the shipment has no invoice created")
def step_impl(context):
    Pages.ShipmentEntryTab.accounting_tab.click()
    Pages.Common.spin_bar.gone()
    assert (
        True == Pages.AccountingBillingBasedTab.MBL.revenue.empty_info.is_visible()
    ), "The invoice has already been created"


@Given("the company set 'Invoice Accounting Wizard Form Style' to '{style}' in 'Company Management' page")
def step_impl(context, style):
    login_as("Super Admin")
    Driver.open(gl.URL.COMPANY_MANAGEMENT)
    Pages.Common.spin_bar.gone()

    if style == "Default" or style == "OLC" or style == "Vinworld":
        Pages.CompanyMngPage.invoice_accounting_wizard_form_style_select.select(style)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    if not Pages.Common.save_button.is_disabled():  # TODO GQT-423 檢查 enable 就好了吧？
        Pages.Common.save_button.click(2)


@Then("the {invoice_type} form should be in '{style_name}' style")
def step_impl(context, invoice_type, style_name):
    if invoice_type == "AR":
        if style_name == "Default":
            assert Pages.ARInvoiceDefaultStyle.mbl_no_title_label.is_visible()
            assert Pages.ARInvoiceOLCStyle.file_no_title_label.is_visible(timeout=0) == False
            assert Pages.ARInvoiceVinworldStyle.bill_to_title_label.is_visible(timeout=0) == False
        elif style_name == "OLC":
            assert Pages.ARInvoiceOLCStyle.file_no_title_label.is_visible()
            assert Pages.ARInvoiceOLCStyle.cust_ref_no_title_label.is_visible()
            assert Pages.ARInvoiceVinworldStyle.bill_to_title_label.is_visible(timeout=0) == False
        elif style_name == "Vinworld":
            assert Pages.ARInvoiceDefaultStyle.mbl_no_title_label.is_visible(timeout=0) == False
            assert Pages.ARInvoiceOLCStyle.file_no_title_label.is_visible(timeout=0) == False
            assert Pages.ARInvoiceVinworldStyle.bill_to_title_label.is_visible()
            assert Pages.ARInvoiceVinworldStyle.ship_to_title_label.is_visible()
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Under construction."
