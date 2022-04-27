from time import sleep

from behave import Then, When

import src.pages as Pages
from src.drivers.driver import Driver
from src.helper.log import Logger
from src.helper.transfer import transfer_data


@When("the user clicks WH Shipping 'Create {payment_type}' button")
def step_impl(context, payment_type):
    if payment_type == "Invoice":
        Pages.WHShippingAccountingInvoiceBasedTab.create_ar_button.click(timeout=10)
    elif payment_type == "D/C Note":
        Pages.WHShippingAccountingInvoiceBasedTab.create_dc_button.click(timeout=10)
    elif payment_type == "Cost":
        Pages.WHShippingAccountingInvoiceBasedTab.create_ap_button.click(timeout=10)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    Pages.Common.spin_bar.gone()


@Then("the WH Shipping amounts and profits should show correctly in Invoice Based")
def step_impl(context):
    sleep(5)

    for row in context.table:
        assert Pages.WHShippingAccountingInvoiceBasedTab.total_revenue_label.get_value(timeout=10) == row["Revenue"]
        assert Pages.WHShippingAccountingInvoiceBasedTab.total_cost_label.get_value() == row["Cost"]
        assert Pages.WHShippingAccountingInvoiceBasedTab.total_balance_label.get_value() == row["Balance"]


@When("the user delete all freights in WH Shipping {invoice_type} Billing Based")
def step_impl(context, invoice_type):
    # If empty_info is not visible, then click 'delete all' and delete all freights
    if (
        invoice_type == "revenue"
        and Pages.WHShippingAccountingBillingBasedTab.revenue.empty_info.is_visible(timeout=0) == False
    ):
        Pages.WHShippingAccountingBillingBasedTab.revenue.select_all_checkbox.tick(True)
        Pages.WHShippingAccountingBillingBasedTab.revenue.delete_button.click()
    elif (
        invoice_type == "cost"
        and Pages.WHShippingAccountingBillingBasedTab.cost.empty_info.is_visible(timeout=0) == False
    ):
        Pages.WHShippingAccountingBillingBasedTab.cost.select_all_checkbox.tick(True)
        Pages.WHShippingAccountingBillingBasedTab.cost.delete_button.click()


@Then("WH Shipping has no invoice in {mode} Based")
def step_impl(context, mode):
    if mode == "Billing":
        assert (
            Pages.WHShippingAccountingBillingBasedTab.revenue.empty_info.is_visible()
        ), "There are some MBL revenue exist"
        assert Pages.WHShippingAccountingBillingBasedTab.cost.empty_info.is_visible(), "There are some MBL cost exist"
    elif mode == "Invoice":
        assert (
            Pages.WHShippingAccountingInvoiceBasedTab.ar(1).reference_no_link.is_visible(timeout=0) == False
        ), "There are some MBL AR exist"
        assert (
            Pages.WHShippingAccountingInvoiceBasedTab.dc(1).reference_no_link.is_visible(timeout=0) == False
        ), "There are some MBL DC exist"
        assert (
            Pages.WHShippingAccountingInvoiceBasedTab.ap(1).reference_no_link.is_visible(timeout=0) == False
        ), "There are some MBL AP exist"


@When("the user {checks_unchecks} WH Shipping Accounting ({mode}) MBL 'Include Draft Amount' checkbox")
def step_impl(context, checks_unchecks, mode):
    if mode == "Billing Based":
        if checks_unchecks == "checks":
            Pages.WHShippingAccountingBillingBasedTab.MBLAmount.include_draft_amount_checkbox.tick(True)
        elif checks_unchecks == "unchecks":
            Pages.WHShippingAccountingBillingBasedTab.MBLAmount.include_draft_amount_checkbox.tick(False)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif mode == "Invoice Based":
        if checks_unchecks == "checks":
            Pages.WHShippingAccountingInvoiceBasedTab.include_draft_amount_checkbox.tick(True)
        elif checks_unchecks == "unchecks":
            Pages.WHShippingAccountingInvoiceBasedTab.include_draft_amount_checkbox.tick(False)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@When("the user blocks WH Shipping revenue({index}) in Accounting Billing Based")
def step_impl(context, index):
    Pages.WHShippingAccountingBillingBasedTab.revenue(index=index).action_button.click()
    Pages.WHShippingAccountingBillingBasedTab.revenue(index=index).action_block_button.click()
    Pages.Common.spin_bar.gone()


@Then("WH Shipping {invoice_type} listed below should be uneditable in Accounting Billing Based")
def step_impl(context, invoice_type):
    if invoice_type == "revenues":
        for row in context.table:
            index = int(row["No."])
            assert Pages.WHShippingAccountingBillingBasedTab.revenue(index=index).bill_to_autocomplete.is_disabled(
                timeout=0
            )
            assert Pages.WHShippingAccountingBillingBasedTab.revenue(index=index).freight_code_autocomplete.is_disabled(
                timeout=0
            )
            assert Pages.WHShippingAccountingBillingBasedTab.revenue(index=index).freight_description_input.is_disabled(
                timeout=0
            )
            assert Pages.WHShippingAccountingBillingBasedTab.revenue(index=index).p_c_select.is_disabled(timeout=0)
            assert Pages.WHShippingAccountingBillingBasedTab.revenue(index=index).unit_select.is_disabled(timeout=0)
            assert Pages.WHShippingAccountingBillingBasedTab.revenue(index=index).currency_select.is_disabled(timeout=0)
            assert Pages.WHShippingAccountingBillingBasedTab.revenue(index=index).vol_input.is_disabled(timeout=0)
            assert Pages.WHShippingAccountingBillingBasedTab.revenue(index=index).rate_input.is_disabled(timeout=0)
            assert Pages.WHShippingAccountingBillingBasedTab.revenue(index=index).amount_input.is_disabled(timeout=0)
            assert Pages.WHShippingAccountingBillingBasedTab.revenue(index=index).invoice_no_autocomplete.is_disabled(
                timeout=0
            )
    elif invoice_type == "costs":
        for row in context.table:
            index = int(row["No."])
            assert Pages.WHShippingAccountingBillingBasedTab.cost(index=index).bill_to_autocomplete.is_disabled(
                timeout=0
            )
            assert Pages.WHShippingAccountingBillingBasedTab.cost(index=index).freight_code_autocomplete.is_disabled(
                timeout=0
            )
            assert Pages.WHShippingAccountingBillingBasedTab.cost(index=index).freight_description_input.is_disabled(
                timeout=0
            )
            assert Pages.WHShippingAccountingBillingBasedTab.cost(index=index).p_c_select.is_disabled(timeout=0)
            assert Pages.WHShippingAccountingBillingBasedTab.cost(index=index).unit_select.is_disabled(timeout=0)
            assert Pages.WHShippingAccountingBillingBasedTab.cost(index=index).currency_select.is_disabled(timeout=0)
            assert Pages.WHShippingAccountingBillingBasedTab.cost(index=index).vol_input.is_disabled(timeout=0)
            assert Pages.WHShippingAccountingBillingBasedTab.cost(index=index).rate_input.is_disabled(timeout=0)
            assert Pages.WHShippingAccountingBillingBasedTab.cost(index=index).amount_input.is_disabled(timeout=0)
            assert Pages.WHShippingAccountingBillingBasedTab.cost(
                index=index
            ).vendor_invoice_no_autocomplete.is_disabled(timeout=0)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@When("the user adds freights to WH Shipping {revenue_cost}")
def step_impl(context, revenue_cost):
    if revenue_cost == "revenue":
        freight_index = Pages.WHShippingAccountingBillingBasedTab.revenue.get_len() + 1

        for row in context.table:
            Pages.WHShippingAccountingBillingBasedTab.revenue.new_button.click()
            sleep(1)
            Pages.WHShippingAccountingBillingBasedTab.revenue(freight_index).bill_to_autocomplete.input(
                transfer_data(row["Bill to"])
            )
            Pages.WHShippingAccountingBillingBasedTab.revenue(freight_index).freight_code_autocomplete.input(
                row["Freight code"]
            )
            Pages.WHShippingAccountingBillingBasedTab.revenue(freight_index).vol_input.input(row["Volume"])
            Pages.WHShippingAccountingBillingBasedTab.revenue(freight_index).rate_input.input(row["Rate"])
            freight_index += 1
    elif revenue_cost == "cost":
        freight_index = Pages.WHShippingAccountingBillingBasedTab.cost.get_len() + 1

        for row in context.table:
            Pages.WHShippingAccountingBillingBasedTab.cost.new_button.click()
            sleep(1)
            Pages.WHShippingAccountingBillingBasedTab.cost(freight_index).bill_to_autocomplete.input(
                transfer_data(row["Bill to"])
            )
            Pages.WHShippingAccountingBillingBasedTab.cost(freight_index).freight_code_autocomplete.input(
                row["Freight code"]
            )
            Pages.WHShippingAccountingBillingBasedTab.cost(freight_index).vol_input.input(row["Volume"])
            Pages.WHShippingAccountingBillingBasedTab.cost(freight_index).rate_input.input(row["Rate"])
            freight_index += 1
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@Then("values in WH Shipping {revenue_cost} should be correct")
def step_impl(context, revenue_cost):
    if revenue_cost == "revenue":
        for row in context.table:
            if "Currency" in context.table.headings and row["Currency"]:
                answer = row["Currency"]
                real_value = Pages.WHShippingAccountingBillingBasedTab.revenue(
                    int(row["No."])
                ).currency_select.get_value()
                assert answer == real_value, "The currency in MBL revenue No. {0} should be {1}, but {2} now".format(
                    row["No."], answer, real_value
                )
            if "Amount" in context.table.headings and row["Amount"]:
                answer = row["Amount"]
                real_value = Pages.WHShippingAccountingBillingBasedTab.revenue(int(row["No."])).amount_input.get_value(
                    timeout=1
                )
                assert answer == real_value, "The amount in MBL revenue No. {0} should be {1}, but {2} now".format(
                    row["No."], answer, real_value
                )
    elif revenue_cost == "cost":
        for row in context.table:
            if "Currency" in context.table.headings and row["Currency"]:
                answer = row["Currency"]
                real_value = Pages.WHShippingAccountingBillingBasedTab.cost(int(row["No."])).currency_select.get_value()
                assert answer == real_value, "The currency in MBL cost No. {0} should be {1}, but {2} now".format(
                    row["No."], answer, real_value
                )
            if "Amount" in context.table.headings and row["Amount"]:
                answer = row["Amount"]
                real_value = Pages.WHShippingAccountingBillingBasedTab.cost(int(row["No."])).amount_input.get_value(
                    timeout=1
                )
                assert answer == real_value, "The amount in MBL cost No. {0} should be {1}, but {2} now".format(
                    row["No."], answer, real_value
                )
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@When("the user deletes freights in WH Shipping {invoice_type}")
def step_impl(context, invoice_type):
    if invoice_type == "revenue":
        for row in context.table:
            Pages.WHShippingAccountingBillingBasedTab.revenue(int(row["No."])).check_checkbox.tick(True)
        Pages.WHShippingAccountingBillingBasedTab.revenue.delete_button.click()
    elif invoice_type == "cost":
        for row in context.table:
            Pages.WHShippingAccountingBillingBasedTab.cost(int(row["No."])).check_checkbox.tick(True)
        Pages.WHShippingAccountingBillingBasedTab.cost.delete_button.click()
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    sleep(1)


@When("the user changes currency of freights in WH Shipping {invoice_type}")
def step_impl(context, invoice_type):
    if invoice_type == "revenue":
        for row in context.table:
            Pages.WHShippingAccountingBillingBasedTab.revenue(int(row["No."])).currency_select.select(row["Currency"])
    elif invoice_type == "cost":
        for row in context.table:
            Pages.WHShippingAccountingBillingBasedTab.cost(int(row["No."])).currency_select.select(row["Currency"])
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    sleep(1)


@When("the user copys freights from WH Shipping {from_invoice_type} to MBL {to_invoice_type}")
def step_impl(context, from_invoice_type, to_invoice_type):
    if from_invoice_type == "revenue":
        for row in context.table:
            Pages.WHShippingAccountingBillingBasedTab.revenue(int(row["No."])).check_checkbox.tick(True)
        Pages.WHShippingAccountingBillingBasedTab.revenue.copy_to_button.click()
    elif from_invoice_type == "cost":
        for row in context.table:
            Pages.WHShippingAccountingBillingBasedTab.cost(int(row["No."])).check_checkbox.tick(True)
        Pages.WHShippingAccountingBillingBasedTab.cost.copy_to_button.click()
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    sleep(1)

    if to_invoice_type == "revenue":
        Pages.WHShippingAccountingBillingBasedTab.Common.copy_to_dropdown.MBL_revenue_checkbox.tick(True)
    elif to_invoice_type == "cost":
        Pages.WHShippingAccountingBillingBasedTab.Common.copy_to_dropdown.MBL_cost_checkbox.tick(True)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    Pages.WHShippingAccountingBillingBasedTab.Common.copy_to_dropdown.copy_button.click()
    sleep(5)


@When("the user input freights information to WH Shipping {invoice_type}")
def step_impl(context, invoice_type):
    if invoice_type == "revenue":
        for row in context.table:
            Pages.WHShippingAccountingBillingBasedTab.revenue(int(row["No."])).bill_to_autocomplete.input(
                row["Bill to"]
            )
    elif invoice_type == "cost":
        for row in context.table:
            Pages.WHShippingAccountingBillingBasedTab.cost(int(row["No."])).bill_to_autocomplete.input(row["Bill to"])
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@When("the user clicks 'Action -> Print / Mail' to WH Shipping {invoice_type}({index})")
def step_impl(context, invoice_type, index):
    if invoice_type == "revenue":
        Pages.WHShippingAccountingBillingBasedTab.revenue(int(index)).action_button.click()
        Pages.WHShippingAccountingBillingBasedTab.revenue(int(index)).action_print_mail_button.click()
    elif invoice_type == "cost":
        Pages.WHShippingAccountingBillingBasedTab.cost(int(index)).action_button.click()
        Pages.WHShippingAccountingBillingBasedTab.cost(int(index)).action_print_mail_button.click()
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    sleep(4)
    Driver.switch_to(window_name="Invoice Print")


@When("the user goes back to WH Shipping '{shipment_name}'")
def step_impl(context, shipment_name):
    Driver.open(context._vp.get("shipment_url")[shipment_name])
    Pages.Common.spin_bar.gone()


@Then("the {block_unblock} bottom in WH Shipping {invoice_type}({index}) should be invisible")
def step_impl(context, block_unblock, invoice_type, index):
    if invoice_type == "revenue":
        Pages.WHShippingAccountingBillingBasedTab.revenue(int(index)).action_button.click()
        if block_unblock == "block":
            assert (
                Pages.WHShippingAccountingBillingBasedTab.revenue(int(index)).action_block_button.is_visible() == False
            )
        elif block_unblock == "unblock":
            assert (
                Pages.WHShippingAccountingBillingBasedTab.revenue(int(index)).action_unblock_button.is_visible()
                == False
            )
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
        Pages.WHShippingAccountingBillingBasedTab.revenue(int(index)).action_button.click()
    elif invoice_type == "cost":
        Pages.WHShippingAccountingBillingBasedTab.cost(int(index)).action_button.click()
        if block_unblock == "block":
            assert Pages.WHShippingAccountingBillingBasedTab.cost(int(index)).action_block_button.is_visible() == False
        elif block_unblock == "unblock":
            assert (
                Pages.WHShippingAccountingBillingBasedTab.cost(int(index)).action_unblock_button.is_visible() == False
            )
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
        Pages.WHShippingAccountingBillingBasedTab.cost(int(index)).action_button.click()
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@Then("The WH Shipping Accounting Billing Based page should show normally")
def step_impl(context):
    assert Pages.WHShippingAccountingBillingBasedTab.revenue.new_button.is_visible()
    assert Pages.WHShippingAccountingBillingBasedTab.revenue.new_five_button.is_visible()
    assert Pages.WHShippingAccountingBillingBasedTab.revenue.add_multiple_button.is_visible()
    assert Pages.WHShippingAccountingBillingBasedTab.revenue.copy_button.is_visible()
    assert Pages.WHShippingAccountingBillingBasedTab.revenue.copy_to_button.is_visible()
    assert Pages.WHShippingAccountingBillingBasedTab.revenue.delete_button.is_visible()
    assert Pages.WHShippingAccountingBillingBasedTab.revenue.load_from_template_button.is_visible()
    assert Pages.WHShippingAccountingBillingBasedTab.cost.new_button.is_visible()
    assert Pages.WHShippingAccountingBillingBasedTab.cost.new_five_button.is_visible()
    assert Pages.WHShippingAccountingBillingBasedTab.cost.add_multiple_button.is_visible()
    assert Pages.WHShippingAccountingBillingBasedTab.cost.copy_button.is_visible()
    assert Pages.WHShippingAccountingBillingBasedTab.cost.copy_to_button.is_visible()
    assert Pages.WHShippingAccountingBillingBasedTab.cost.delete_button.is_visible()
    assert Pages.WHShippingAccountingBillingBasedTab.cost.load_from_template_button.is_visible()
    assert Pages.WHShippingAccountingBillingBasedTab.tool_button.is_visible()
    assert Pages.WHShippingAccountingBillingBasedTab.Memo.memo_title_button.is_visible()


@When("the user clicks save button in WH Shipping Accounting Billing Based")
def step_impl(context):
    if Pages.WHShippingAccountingBillingBasedTab.save_button.is_enable():
        Pages.WHShippingAccountingBillingBasedTab.save_button.click()
        Pages.Common.spin_bar.gone()
        sleep(2)
    else:
        Logger.getLogger().warning("The save button is not clickable")


@Then("the save button in WH Shipping Accounting Billing Based should be disabled")
def step_impl(context):
    assert Pages.WHShippingAccountingBillingBasedTab.save_button.is_disabled(), "The save button should be disabled"
