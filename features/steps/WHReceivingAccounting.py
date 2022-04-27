from time import sleep

from behave import Then, When

import src.pages as Pages
from src.drivers.driver import Driver
from src.helper.log import Logger
from src.helper.transfer import transfer_data


@When("the user clicks WH Receiving 'Create {payment_type}' button")
def step_impl(context, payment_type):
    if payment_type == "Invoice":
        Pages.WHReceivingAccountingInvoiceBasedTab.create_ar_button.click(timeout=10)
    elif payment_type == "D/C Note":
        Pages.WHReceivingAccountingInvoiceBasedTab.create_dc_button.click(timeout=10)
    elif payment_type == "Cost":
        Pages.WHReceivingAccountingInvoiceBasedTab.create_ap_button.click(timeout=10)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    Pages.Common.spin_bar.gone()


@Then("the WH Receiving amounts and profits should show correctly in Invoice Based")
def step_impl(context):
    sleep(5)

    for row in context.table:
        assert Pages.WHReceivingAccountingInvoiceBasedTab.total_revenue_label.get_value(timeout=10) == row["Revenue"]
        assert Pages.WHReceivingAccountingInvoiceBasedTab.total_cost_label.get_value() == row["Cost"]
        assert Pages.WHReceivingAccountingInvoiceBasedTab.total_balance_label.get_value() == row["Balance"]


@When("the user delete all freights in WH Receiving {invoice_type} Billing Based")
def step_impl(context, invoice_type):
    # If empty_info is not visible, then click 'delete all' and delete all freights
    if (
        invoice_type == "revenue"
        and Pages.WHReceivingAccountingBillingBasedTab.revenue.empty_info.is_visible(timeout=0) == False
    ):
        Pages.WHReceivingAccountingBillingBasedTab.revenue.select_all_checkbox.tick(True)
        Pages.WHReceivingAccountingBillingBasedTab.revenue.delete_button.click()
    elif (
        invoice_type == "cost"
        and Pages.WHReceivingAccountingBillingBasedTab.cost.empty_info.is_visible(timeout=0) == False
    ):
        Pages.WHReceivingAccountingBillingBasedTab.cost.select_all_checkbox.tick(True)
        Pages.WHReceivingAccountingBillingBasedTab.cost.delete_button.click()


@Then("WH Receiving has no invoice in {mode} Based")
def step_impl(context, mode):
    if mode == "Billing":
        assert (
            Pages.WHReceivingAccountingBillingBasedTab.revenue.empty_info.is_visible()
        ), "There are some MBL revenue exist"
        assert Pages.WHReceivingAccountingBillingBasedTab.cost.empty_info.is_visible(), "There are some MBL cost exist"
    elif mode == "Invoice":
        assert (
            Pages.WHReceivingAccountingInvoiceBasedTab.ar(1).reference_no_link.is_visible(timeout=0) == False
        ), "There are some MBL AR exist"
        assert (
            Pages.WHReceivingAccountingInvoiceBasedTab.dc(1).reference_no_link.is_visible(timeout=0) == False
        ), "There are some MBL DC exist"
        assert (
            Pages.WHReceivingAccountingInvoiceBasedTab.ap(1).reference_no_link.is_visible(timeout=0) == False
        ), "There are some MBL AP exist"


@When("the user {checks_unchecks} WH Receiving Accounting ({mode}) MBL 'Include Draft Amount' checkbox")
def step_impl(context, checks_unchecks, mode):
    if mode == "Billing Based":
        if checks_unchecks == "checks":
            Pages.WHReceivingAccountingBillingBasedTab.MBLAmount.include_draft_amount_checkbox.tick(True)
        elif checks_unchecks == "unchecks":
            Pages.WHReceivingAccountingBillingBasedTab.MBLAmount.include_draft_amount_checkbox.tick(False)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif mode == "Invoice Based":
        if checks_unchecks == "checks":
            Pages.WHReceivingAccountingInvoiceBasedTab.include_draft_amount_checkbox.tick(True)
        elif checks_unchecks == "unchecks":
            Pages.WHReceivingAccountingInvoiceBasedTab.include_draft_amount_checkbox.tick(False)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@When("the user blocks WH Receiving revenue({index}) in Accounting Billing Based")
def step_impl(context, index):
    Pages.WHReceivingAccountingBillingBasedTab.revenue(index=index).action_button.click()
    Pages.WHReceivingAccountingBillingBasedTab.revenue(index=index).action_block_button.click()
    Pages.Common.spin_bar.gone()


@Then("WH Receiving {invoice_type} listed below should be uneditable in Accounting Billing Based")
def step_impl(context, invoice_type):
    if invoice_type == "revenues":
        for row in context.table:
            index = int(row["No."])
            assert Pages.WHReceivingAccountingBillingBasedTab.revenue(index=index).bill_to_autocomplete.is_disabled(
                timeout=0
            )
            assert Pages.WHReceivingAccountingBillingBasedTab.revenue(
                index=index
            ).freight_code_autocomplete.is_disabled(timeout=0)
            assert Pages.WHReceivingAccountingBillingBasedTab.revenue(
                index=index
            ).freight_description_input.is_disabled(timeout=0)
            assert Pages.WHReceivingAccountingBillingBasedTab.revenue(index=index).p_c_select.is_disabled(timeout=0)
            assert Pages.WHReceivingAccountingBillingBasedTab.revenue(index=index).unit_select.is_disabled(timeout=0)
            assert Pages.WHReceivingAccountingBillingBasedTab.revenue(index=index).currency_select.is_disabled(
                timeout=0
            )
            assert Pages.WHReceivingAccountingBillingBasedTab.revenue(index=index).vol_input.is_disabled(timeout=0)
            assert Pages.WHReceivingAccountingBillingBasedTab.revenue(index=index).rate_input.is_disabled(timeout=0)
            assert Pages.WHReceivingAccountingBillingBasedTab.revenue(index=index).amount_input.is_disabled(timeout=0)
            assert Pages.WHReceivingAccountingBillingBasedTab.revenue(index=index).invoice_no_autocomplete.is_disabled(
                timeout=0
            )
    elif invoice_type == "costs":
        for row in context.table:
            index = int(row["No."])
            assert Pages.WHReceivingAccountingBillingBasedTab.cost(index=index).bill_to_autocomplete.is_disabled(
                timeout=0
            )
            assert Pages.WHReceivingAccountingBillingBasedTab.cost(index=index).freight_code_autocomplete.is_disabled(
                timeout=0
            )
            assert Pages.WHReceivingAccountingBillingBasedTab.cost(index=index).freight_description_input.is_disabled(
                timeout=0
            )
            assert Pages.WHReceivingAccountingBillingBasedTab.cost(index=index).p_c_select.is_disabled(timeout=0)
            assert Pages.WHReceivingAccountingBillingBasedTab.cost(index=index).unit_select.is_disabled(timeout=0)
            assert Pages.WHReceivingAccountingBillingBasedTab.cost(index=index).currency_select.is_disabled(timeout=0)
            assert Pages.WHReceivingAccountingBillingBasedTab.cost(index=index).vol_input.is_disabled(timeout=0)
            assert Pages.WHReceivingAccountingBillingBasedTab.cost(index=index).rate_input.is_disabled(timeout=0)
            assert Pages.WHReceivingAccountingBillingBasedTab.cost(index=index).amount_input.is_disabled(timeout=0)
            assert Pages.WHReceivingAccountingBillingBasedTab.cost(
                index=index
            ).vendor_invoice_no_autocomplete.is_disabled(timeout=0)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@When("the user adds freights to WH Receiving {revenue_cost}")
def step_impl(context, revenue_cost):
    if revenue_cost == "revenue":
        freight_index = Pages.WHReceivingAccountingBillingBasedTab.revenue.get_len() + 1

        for row in context.table:
            Pages.WHReceivingAccountingBillingBasedTab.revenue.new_button.click()
            sleep(1)
            Pages.WHReceivingAccountingBillingBasedTab.revenue(freight_index).bill_to_autocomplete.input(
                transfer_data(row["Bill to"])
            )
            Pages.WHReceivingAccountingBillingBasedTab.revenue(freight_index).freight_code_autocomplete.input(
                row["Freight code"]
            )
            Pages.WHReceivingAccountingBillingBasedTab.revenue(freight_index).vol_input.input(row["Volume"])
            Pages.WHReceivingAccountingBillingBasedTab.revenue(freight_index).rate_input.input(row["Rate"])
            freight_index += 1
    elif revenue_cost == "cost":
        freight_index = Pages.WHReceivingAccountingBillingBasedTab.cost.get_len() + 1

        for row in context.table:
            Pages.WHReceivingAccountingBillingBasedTab.cost.new_button.click()
            sleep(1)
            Pages.WHReceivingAccountingBillingBasedTab.cost(freight_index).bill_to_autocomplete.input(
                transfer_data(row["Bill to"])
            )
            Pages.WHReceivingAccountingBillingBasedTab.cost(freight_index).freight_code_autocomplete.input(
                row["Freight code"]
            )
            Pages.WHReceivingAccountingBillingBasedTab.cost(freight_index).vol_input.input(row["Volume"])
            Pages.WHReceivingAccountingBillingBasedTab.cost(freight_index).rate_input.input(row["Rate"])
            freight_index += 1
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@Then("values in WH Receiving {revenue_cost} should be correct")
def step_impl(context, revenue_cost):
    if revenue_cost == "revenue":
        for row in context.table:
            if "Currency" in context.table.headings and row["Currency"]:
                answer = row["Currency"]
                real_value = Pages.WHReceivingAccountingBillingBasedTab.revenue(
                    int(row["No."])
                ).currency_select.get_value()
                assert answer == real_value, "The currency in MBL revenue No. {0} should be {1}, but {2} now".format(
                    row["No."], answer, real_value
                )
            if "Amount" in context.table.headings and row["Amount"]:
                answer = row["Amount"]
                real_value = Pages.WHReceivingAccountingBillingBasedTab.revenue(int(row["No."])).amount_input.get_value(
                    timeout=1
                )
                assert answer == real_value, "The amount in MBL revenue No. {0} should be {1}, but {2} now".format(
                    row["No."], answer, real_value
                )
    elif revenue_cost == "cost":
        for row in context.table:
            if "Currency" in context.table.headings and row["Currency"]:
                answer = row["Currency"]
                real_value = Pages.WHReceivingAccountingBillingBasedTab.cost(
                    int(row["No."])
                ).currency_select.get_value()
                assert answer == real_value, "The currency in MBL cost No. {0} should be {1}, but {2} now".format(
                    row["No."], answer, real_value
                )
            if "Amount" in context.table.headings and row["Amount"]:
                answer = row["Amount"]
                real_value = Pages.WHReceivingAccountingBillingBasedTab.cost(int(row["No."])).amount_input.get_value(
                    timeout=1
                )
                assert answer == real_value, "The amount in MBL cost No. {0} should be {1}, but {2} now".format(
                    row["No."], answer, real_value
                )
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@When("the user deletes freights in WH Receiving {invoice_type}")
def step_impl(context, invoice_type):
    if invoice_type == "revenue":
        for row in context.table:
            Pages.WHReceivingAccountingBillingBasedTab.revenue(int(row["No."])).check_checkbox.tick(True)
        Pages.WHReceivingAccountingBillingBasedTab.revenue.delete_button.click()
    elif invoice_type == "cost":
        for row in context.table:
            Pages.WHReceivingAccountingBillingBasedTab.cost(int(row["No."])).check_checkbox.tick(True)
        Pages.WHReceivingAccountingBillingBasedTab.cost.delete_button.click()
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    sleep(1)


@When("the user changes currency of freights in WH Receiving {invoice_type}")
def step_impl(context, invoice_type):
    if invoice_type == "revenue":
        for row in context.table:
            Pages.WHReceivingAccountingBillingBasedTab.revenue(int(row["No."])).currency_select.select(row["Currency"])
    elif invoice_type == "cost":
        for row in context.table:
            Pages.WHReceivingAccountingBillingBasedTab.cost(int(row["No."])).currency_select.select(row["Currency"])
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    sleep(1)


@When("the user copys freights from WH Receiving {from_invoice_type} to MBL {to_invoice_type}")
def step_impl(context, from_invoice_type, to_invoice_type):
    if from_invoice_type == "revenue":
        for row in context.table:
            Pages.WHReceivingAccountingBillingBasedTab.revenue(int(row["No."])).check_checkbox.tick(True)
        Pages.WHReceivingAccountingBillingBasedTab.revenue.copy_to_button.click()
    elif from_invoice_type == "cost":
        for row in context.table:
            Pages.WHReceivingAccountingBillingBasedTab.cost(int(row["No."])).check_checkbox.tick(True)
        Pages.WHReceivingAccountingBillingBasedTab.cost.copy_to_button.click()
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    sleep(1)

    if to_invoice_type == "revenue":
        Pages.WHReceivingAccountingBillingBasedTab.Common.copy_to_dropdown.MBL_revenue_checkbox.tick(True)
    elif to_invoice_type == "cost":
        Pages.WHReceivingAccountingBillingBasedTab.Common.copy_to_dropdown.MBL_cost_checkbox.tick(True)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    Pages.WHReceivingAccountingBillingBasedTab.Common.copy_to_dropdown.copy_button.click()
    sleep(5)


@When("the user input freights information to WH Receiving {invoice_type}")
def step_impl(context, invoice_type):
    if invoice_type == "revenue":
        for row in context.table:
            Pages.WHReceivingAccountingBillingBasedTab.revenue(int(row["No."])).bill_to_autocomplete.input(
                row["Bill to"]
            )
    elif invoice_type == "cost":
        for row in context.table:
            Pages.WHReceivingAccountingBillingBasedTab.cost(int(row["No."])).bill_to_autocomplete.input(row["Bill to"])
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@When("the user clicks 'Action -> Print / Mail' to WH Receiving {invoice_type}({index})")
def step_impl(context, invoice_type, index):
    if invoice_type == "revenue":
        Pages.WHReceivingAccountingBillingBasedTab.revenue(int(index)).action_button.click()
        Pages.WHReceivingAccountingBillingBasedTab.revenue(int(index)).action_print_mail_button.click()
    elif invoice_type == "cost":
        Pages.WHReceivingAccountingBillingBasedTab.cost(int(index)).action_button.click()
        Pages.WHReceivingAccountingBillingBasedTab.cost(int(index)).action_print_mail_button.click()
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    sleep(4)
    Driver.switch_to(window_name="Invoice Print")


@When("the user goes back to WH Receiving '{shipment_name}'")
def step_impl(context, shipment_name):
    Driver.open(context._vp.get("shipment_url")[shipment_name])
    Pages.Common.spin_bar.gone()


@Then("the {block_unblock} bottom in WH Receiving {invoice_type}({index}) should be invisible")
def step_impl(context, block_unblock, invoice_type, index):
    if invoice_type == "revenue":
        Pages.WHReceivingAccountingBillingBasedTab.revenue(int(index)).action_button.click()
        if block_unblock == "block":
            assert (
                Pages.WHReceivingAccountingBillingBasedTab.revenue(int(index)).action_block_button.is_visible() == False
            )
        elif block_unblock == "unblock":
            assert (
                Pages.WHReceivingAccountingBillingBasedTab.revenue(int(index)).action_unblock_button.is_visible()
                == False
            )
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
        Pages.WHReceivingAccountingBillingBasedTab.revenue(int(index)).action_button.click()
    elif invoice_type == "cost":
        Pages.WHReceivingAccountingBillingBasedTab.cost(int(index)).action_button.click()
        if block_unblock == "block":
            assert Pages.WHReceivingAccountingBillingBasedTab.cost(int(index)).action_block_button.is_visible() == False
        elif block_unblock == "unblock":
            assert (
                Pages.WHReceivingAccountingBillingBasedTab.cost(int(index)).action_unblock_button.is_visible() == False
            )
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
        Pages.WHReceivingAccountingBillingBasedTab.cost(int(index)).action_button.click()
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@Then("The WH Receiving Accounting Billing Based page should show normally")
def step_impl(context):
    assert Pages.WHReceivingAccountingBillingBasedTab.revenue.new_button.is_visible()
    assert Pages.WHReceivingAccountingBillingBasedTab.revenue.new_five_button.is_visible()
    assert Pages.WHReceivingAccountingBillingBasedTab.revenue.add_multiple_button.is_visible()
    assert Pages.WHReceivingAccountingBillingBasedTab.revenue.copy_button.is_visible()
    assert Pages.WHReceivingAccountingBillingBasedTab.revenue.copy_to_button.is_visible()
    assert Pages.WHReceivingAccountingBillingBasedTab.revenue.delete_button.is_visible()
    assert Pages.WHReceivingAccountingBillingBasedTab.revenue.load_from_template_button.is_visible()
    assert Pages.WHReceivingAccountingBillingBasedTab.cost.new_button.is_visible()
    assert Pages.WHReceivingAccountingBillingBasedTab.cost.new_five_button.is_visible()
    assert Pages.WHReceivingAccountingBillingBasedTab.cost.add_multiple_button.is_visible()
    assert Pages.WHReceivingAccountingBillingBasedTab.cost.copy_button.is_visible()
    assert Pages.WHReceivingAccountingBillingBasedTab.cost.copy_to_button.is_visible()
    assert Pages.WHReceivingAccountingBillingBasedTab.cost.delete_button.is_visible()
    assert Pages.WHReceivingAccountingBillingBasedTab.cost.load_from_template_button.is_visible()
    assert Pages.WHReceivingAccountingBillingBasedTab.tool_button.is_visible()
    assert Pages.WHReceivingAccountingBillingBasedTab.Memo.memo_title_button.is_visible()


@When("the user clicks save button in WH Receiving Accounting Billing Based")
def step_impl(context):
    if Pages.WHReceivingAccountingBillingBasedTab.save_button.is_enable():
        Pages.WHReceivingAccountingBillingBasedTab.save_button.click()
        Pages.Common.spin_bar.gone()
        sleep(2)
    else:
        Logger.getLogger().warning("The save button is not clickable")


@Then("the save button in WH Receiving Accounting Billing Based should be disabled")
def step_impl(context):
    assert Pages.WHReceivingAccountingBillingBasedTab.save_button.is_disabled(), "The save button should be disabled"
