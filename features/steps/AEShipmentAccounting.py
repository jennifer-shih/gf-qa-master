from time import sleep

from behave import Then, When

import src.pages as Pages
from src.drivers.driver import Driver
from src.helper.log import Logger
from src.helper.transfer import transfer_data


@When("the user clicks AE {MAWB_or_HAWB} 'Create {payment_type}' button")
def step_impl(context, MAWB_or_HAWB, payment_type):
    if MAWB_or_HAWB == "MAWB":
        if payment_type == "AR":
            Pages.AEAccountingInvoiceBasedTab.MAWB.invoice_ar_button.click(timeout=10)
        elif payment_type == "DC":
            Pages.AEAccountingInvoiceBasedTab.MAWB.d_c_note_button.click(timeout=10)
        elif payment_type == "AP":
            Pages.AEAccountingInvoiceBasedTab.MAWB.ap_button.click(timeout=10)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif MAWB_or_HAWB == "HAWB":
        if payment_type == "AR":
            Pages.AEAccountingInvoiceBasedTab.HAWB.invoice_ar_button.click(timeout=10)
        elif payment_type == "DC":
            Pages.AEAccountingInvoiceBasedTab.HAWB.d_c_note_button.click(timeout=10)
        elif payment_type == "AP":
            Pages.AEAccountingInvoiceBasedTab.HAWB.ap_button.click(timeout=10)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    Pages.Common.spin_bar.gone()


@Then("the AE {MAWB_or_HAWB} amounts and profits should show correctly in Invoice Based")
def step_impl(context, MAWB_or_HAWB):
    sleep(5)

    if MAWB_or_HAWB == "MAWB":
        for row in context.table:
            assert Pages.AEAccountingInvoiceBasedTab.MAWB.total_revenue_label.get_value(timeout=10) == row["Revenue"]
            assert Pages.AEAccountingInvoiceBasedTab.MAWB.total_cost_label.get_value() == row["Cost"]
            assert Pages.AEAccountingInvoiceBasedTab.MAWB.total_balance_label.get_value() == row["Balance"]
            assert (
                Pages.AEAccountingInvoiceBasedTab.MAWB.total_profit_amount_label.get_value(timeout=10)
                == row["Total Profit Amount"]
            )
    elif MAWB_or_HAWB == "HAWB":
        for row in context.table:
            assert Pages.AEAccountingInvoiceBasedTab.HAWB.total_revenue_label.get_value(timeout=10) == row["Revenue"]
            assert Pages.AEAccountingInvoiceBasedTab.HAWB.total_cost_label.get_value() == row["Cost"]
            assert Pages.AEAccountingInvoiceBasedTab.HAWB.total_balance_label.get_value() == row["Balance"]
            assert (
                Pages.AEAccountingInvoiceBasedTab.HAWB.hawb_profit_amount_label.get_value(timeout=10)
                == row["HAWB Profit Amount"]
            )
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@Then("the AE {MAWB_or_HAWB} amounts and profits should show correctly in Billing Based")
def step_impl(context, MAWB_or_HAWB):
    if MAWB_or_HAWB == "MAWB":
        for row in context.table:
            assert (
                Pages.AEAccountingBillingBasedTab.MAWB.MAWBAmount.mawb_revenue_label.get_value() == row["MAWB Revenue"]
            )
            assert Pages.AEAccountingBillingBasedTab.MAWB.MAWBAmount.mawb_cost_label.get_value() == row["MAWB Cost"]
            assert Pages.AEAccountingBillingBasedTab.MAWB.MAWBAmount.mawb_amount_label.get_value() == row["MAWB Amount"]
            assert (
                Pages.AEAccountingBillingBasedTab.MAWB.ShipmentProfit.profit_amount_label.get_value()
                == row["Total Profit Amount"]
            )
    elif MAWB_or_HAWB == "HAWB":
        for row in context.table:
            assert (
                Pages.AEAccountingBillingBasedTab.HAWB.HAWBAmount.hawb_revenue_label.get_value() == row["HAWB Revenue"]
            )
            assert Pages.AEAccountingBillingBasedTab.HAWB.HAWBAmount.hawb_cost_label.get_value() == row["HAWB Cost"]
            assert Pages.AEAccountingBillingBasedTab.HAWB.HAWBAmount.hawb_amount_label.get_value() == row["HAWB Amount"]
            assert (
                Pages.AEAccountingBillingBasedTab.HAWB.ShipmentProfit.profit_amount_label.get_value()
                == row["Profit Amount"]
            )
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@When("the user delete all freights in AE {MAWB_or_HAWB} {invoice_type} Billing Based")
def step_impl(context, MAWB_or_HAWB, invoice_type):
    # If empty_info is not visible, then click 'delete all' and delete all freights
    if MAWB_or_HAWB == "MAWB":
        if (
            invoice_type == "revenue"
            and Pages.AEAccountingBillingBasedTab.MAWB.revenue.empty_info.is_visible(timeout=0) == False
        ):
            Pages.AEAccountingBillingBasedTab.MAWB.revenue.select_all_checkbox.tick(True)
            Pages.AEAccountingBillingBasedTab.MAWB.revenue.delete_button.click()
        elif (
            invoice_type == "cost"
            and Pages.AEAccountingBillingBasedTab.MAWB.cost.empty_info.is_visible(timeout=0) == False
        ):
            Pages.AEAccountingBillingBasedTab.MAWB.cost.select_all_checkbox.tick(True)
            Pages.AEAccountingBillingBasedTab.MAWB.cost.delete_button.click()
    elif MAWB_or_HAWB == "HAWB":
        if (
            invoice_type == "revenue"
            and Pages.AEAccountingBillingBasedTab.HAWB.revenue.empty_info.is_visible(timeout=0) == False
        ):
            Pages.AEAccountingBillingBasedTab.HAWB.revenue.select_all_checkbox.tick(True)
            Pages.AEAccountingBillingBasedTab.HAWB.revenue.delete_button.click()
        elif (
            invoice_type == "cost"
            and Pages.AEAccountingBillingBasedTab.HAWB.cost.empty_info.is_visible(timeout=0) == False
        ):
            Pages.AEAccountingBillingBasedTab.HAWB.cost.select_all_checkbox.tick(True)
            Pages.AEAccountingBillingBasedTab.HAWB.cost.delete_button.click()
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@Then("AE {MAWB_or_HAWB} has no invoice in {mode} Based")
def step_impl(context, MAWB_or_HAWB, mode):
    if mode == "Billing":
        if MAWB_or_HAWB == "MAWB":
            assert (
                Pages.AEAccountingBillingBasedTab.MAWB.revenue.empty_info.is_visible()
            ), "There are some MAWB revenue exist"
            assert Pages.AEAccountingBillingBasedTab.MAWB.cost.empty_info.is_visible(), "There are some MAWB cost exist"
        elif MAWB_or_HAWB == "HAWB":
            assert (
                Pages.AEAccountingBillingBasedTab.HAWB.revenue.empty_info.is_visible()
            ), "There are some HAWB revenue exist"
            assert Pages.AEAccountingBillingBasedTab.HAWB.cost.empty_info.is_visible(), "There are some HAWB cost exist"
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif mode == "Invoice":
        if MAWB_or_HAWB == "MAWB":
            assert (
                Pages.AEAccountingInvoiceBasedTab.MAWB.ar(1).reference_no_link.is_visible(timeout=0) == False
            ), "There are some MAWB AR exist"
            assert (
                Pages.AEAccountingInvoiceBasedTab.MAWB.dc(1).reference_no_link.is_visible(timeout=0) == False
            ), "There are some MAWB DC exist"
            assert (
                Pages.AEAccountingInvoiceBasedTab.MAWB.ap(1).reference_no_link.is_visible(timeout=0) == False
            ), "There are some MAWB AP exist"
        elif MAWB_or_HAWB == "HAWB":
            assert (
                Pages.AEAccountingInvoiceBasedTab.HAWB.ar(1).reference_no_link.is_visible(timeout=0) == False
            ), "There are some HAWB AR exist"
            assert (
                Pages.AEAccountingInvoiceBasedTab.HAWB.dc(1).reference_no_link.is_visible(timeout=0) == False
            ), "There are some HAWB DC exist"
            assert (
                Pages.AEAccountingInvoiceBasedTab.HAWB.ap(1).reference_no_link.is_visible(timeout=0) == False
            ), "There are some HAWB AP exist"
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@When("the user {checks_unchecks} AE Accounting ({mode}) {MAWB_or_HAWB} 'Include Draft Amount' checkbox")
def step_impl(context, checks_unchecks, mode, MAWB_or_HAWB):
    if mode == "Billing Based":
        if MAWB_or_HAWB == "MAWB":
            if checks_unchecks == "checks":
                Pages.AEAccountingBillingBasedTab.MAWB.MAWBAmount.include_draft_amount_checkbox.tick(True)
            elif checks_unchecks == "unchecks":
                Pages.AEAccountingBillingBasedTab.MAWB.MAWBAmount.include_draft_amount_checkbox.tick(False)
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
        elif MAWB_or_HAWB == "HAWB":
            if checks_unchecks == "checks":
                Pages.AEAccountingBillingBasedTab.HAWB.HAWBAmount.include_draft_amount_checkbox.tick(True)
            elif checks_unchecks == "unchecks":
                Pages.AEAccountingBillingBasedTab.HAWB.HAWBAmount.include_draft_amount_checkbox.tick(False)
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif mode == "Invoice Based":
        if MAWB_or_HAWB == "MAWB":
            if checks_unchecks == "checks":
                Pages.AEAccountingInvoiceBasedTab.MAWB.include_draft_amount_checkbox.tick(True)
            elif checks_unchecks == "unchecks":
                Pages.AEAccountingInvoiceBasedTab.MAWB.include_draft_amount_checkbox.tick(False)
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
        elif MAWB_or_HAWB == "HAWB":
            if checks_unchecks == "checks":
                Pages.AEAccountingInvoiceBasedTab.HAWB.include_draft_amount_checkbox.tick(True)
            elif checks_unchecks == "unchecks":
                Pages.AEAccountingInvoiceBasedTab.HAWB.include_draft_amount_checkbox.tick(False)
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@When("the user blocks AE {MAWB_or_HAWB} revenue({index}) in Accounting Billing Based")
def step_impl(context, MAWB_or_HAWB, index):
    if MAWB_or_HAWB == "MAWB":
        Pages.AEAccountingBillingBasedTab.MAWB.revenue(index=index).action_button.click()
        Pages.AEAccountingBillingBasedTab.MAWB.revenue(index=index).action_block_button.click()
    elif MAWB_or_HAWB == "HAWB":
        Pages.AEAccountingBillingBasedTab.HAWB.revenue(index=index).action_button.click()
        Pages.AEAccountingBillingBasedTab.HAWB.revenue(index=index).action_block_button.click()
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)
    Pages.Common.spin_bar.gone()


@Then("AE {MAWB_or_HAWB} {invoice_type} listed below should be uneditable in Accounting Billing Based")
def step_impl(context, MAWB_or_HAWB, invoice_type):
    if MAWB_or_HAWB == "MAWB":
        if invoice_type == "revenues":
            for row in context.table:
                index = int(row["No."])
                assert Pages.AEAccountingBillingBasedTab.MAWB.revenue(index=index).bill_to_autocomplete.is_disabled(
                    timeout=0
                )
                assert Pages.AEAccountingBillingBasedTab.MAWB.revenue(
                    index=index
                ).freight_code_autocomplete.is_disabled(timeout=0)
                assert Pages.AEAccountingBillingBasedTab.MAWB.revenue(
                    index=index
                ).freight_description_input.is_disabled(timeout=0)
                assert Pages.AEAccountingBillingBasedTab.MAWB.revenue(index=index).p_c_select.is_disabled(timeout=0)
                assert Pages.AEAccountingBillingBasedTab.MAWB.revenue(index=index).unit_select.is_disabled(timeout=0)
                assert Pages.AEAccountingBillingBasedTab.MAWB.revenue(index=index).currency_select.is_disabled(
                    timeout=0
                )
                assert Pages.AEAccountingBillingBasedTab.MAWB.revenue(index=index).vol_input.is_disabled(timeout=0)
                assert Pages.AEAccountingBillingBasedTab.MAWB.revenue(index=index).rate_input.is_disabled(timeout=0)
                assert Pages.AEAccountingBillingBasedTab.MAWB.revenue(index=index).amount_input.is_disabled(timeout=0)
                assert Pages.AEAccountingBillingBasedTab.MAWB.revenue(index=index).invoice_no_autocomplete.is_disabled(
                    timeout=0
                )
        elif invoice_type == "costs":
            for row in context.table:
                index = int(row["No."])
                assert Pages.AEAccountingBillingBasedTab.MAWB.cost(index=index).bill_to_autocomplete.is_disabled(
                    timeout=0
                )
                assert Pages.AEAccountingBillingBasedTab.MAWB.cost(index=index).freight_code_autocomplete.is_disabled(
                    timeout=0
                )
                assert Pages.AEAccountingBillingBasedTab.MAWB.cost(index=index).freight_description_input.is_disabled(
                    timeout=0
                )
                assert Pages.AEAccountingBillingBasedTab.MAWB.cost(index=index).p_c_select.is_disabled(timeout=0)
                assert Pages.AEAccountingBillingBasedTab.MAWB.cost(index=index).unit_select.is_disabled(timeout=0)
                assert Pages.AEAccountingBillingBasedTab.MAWB.cost(index=index).currency_select.is_disabled(timeout=0)
                assert Pages.AEAccountingBillingBasedTab.MAWB.cost(index=index).vol_input.is_disabled(timeout=0)
                assert Pages.AEAccountingBillingBasedTab.MAWB.cost(index=index).rate_input.is_disabled(timeout=0)
                assert Pages.AEAccountingBillingBasedTab.MAWB.cost(index=index).amount_input.is_disabled(timeout=0)
                assert Pages.AEAccountingBillingBasedTab.MAWB.cost(
                    index=index
                ).vendor_invoice_no_autocomplete.is_disabled(timeout=0)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif MAWB_or_HAWB == "HAWB":
        if invoice_type == "revenues":
            for row in context.table:
                index = int(row["No."])
                assert Pages.AEAccountingBillingBasedTab.HAWB.revenue(index=index).bill_to_autocomplete.is_disabled(
                    timeout=0
                )
                assert Pages.AEAccountingBillingBasedTab.HAWB.revenue(
                    index=index
                ).freight_code_autocomplete.is_disabled(timeout=0)
                assert Pages.AEAccountingBillingBasedTab.HAWB.revenue(
                    index=index
                ).freight_description_input.is_disabled(timeout=0)
                assert Pages.AEAccountingBillingBasedTab.HAWB.revenue(index=index).p_c_select.is_disabled(timeout=0)
                assert Pages.AEAccountingBillingBasedTab.HAWB.revenue(index=index).unit_select.is_disabled(timeout=0)
                assert Pages.AEAccountingBillingBasedTab.HAWB.revenue(index=index).currency_select.is_disabled(
                    timeout=0
                )
                assert Pages.AEAccountingBillingBasedTab.HAWB.revenue(index=index).vol_input.is_disabled(timeout=0)
                assert Pages.AEAccountingBillingBasedTab.HAWB.revenue(index=index).rate_input.is_disabled(timeout=0)
                assert Pages.AEAccountingBillingBasedTab.HAWB.revenue(index=index).amount_input.is_disabled(timeout=0)
                assert Pages.AEAccountingBillingBasedTab.HAWB.revenue(index=index).invoice_no_autocomplete.is_disabled(
                    timeout=0
                )
        elif invoice_type == "costs":
            for row in context.table:
                index = int(row["No."])
                assert Pages.AEAccountingBillingBasedTab.HAWB.cost(index=index).bill_to_autocomplete.is_disabled(
                    timeout=0
                )
                assert Pages.AEAccountingBillingBasedTab.HAWB.cost(index=index).freight_code_autocomplete.is_disabled(
                    timeout=0
                )
                assert Pages.AEAccountingBillingBasedTab.HAWB.cost(index=index).freight_description_input.is_disabled(
                    timeout=0
                )
                assert Pages.AEAccountingBillingBasedTab.HAWB.cost(index=index).p_c_select.is_disabled(timeout=0)
                assert Pages.AEAccountingBillingBasedTab.HAWB.cost(index=index).unit_select.is_disabled(timeout=0)
                assert Pages.AEAccountingBillingBasedTab.HAWB.cost(index=index).currency_select.is_disabled(timeout=0)
                assert Pages.AEAccountingBillingBasedTab.HAWB.cost(index=index).vol_input.is_disabled(timeout=0)
                assert Pages.AEAccountingBillingBasedTab.HAWB.cost(index=index).rate_input.is_disabled(timeout=0)
                assert Pages.AEAccountingBillingBasedTab.HAWB.cost(index=index).amount_input.is_disabled(timeout=0)
                assert Pages.AEAccountingBillingBasedTab.HAWB.cost(
                    index=index
                ).vendor_invoice_no_autocomplete.is_disabled(timeout=0)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@When("the user adds freights to AE {MAWB_or_HAWB} {revenue_cost}")
def step_impl(context, MAWB_or_HAWB, revenue_cost):
    if MAWB_or_HAWB == "MAWB":
        if revenue_cost == "revenue":
            freight_index = Pages.AEAccountingBillingBasedTab.MAWB.revenue.get_len() + 1

            for row in context.table:
                Pages.AEAccountingBillingBasedTab.MAWB.revenue.new_button.click()
                sleep(1)
                Pages.AEAccountingBillingBasedTab.MAWB.revenue(freight_index).bill_to_autocomplete.input(
                    transfer_data(row["Bill to"])
                )
                Pages.AEAccountingBillingBasedTab.MAWB.revenue(freight_index).freight_code_autocomplete.input(
                    row["Freight code"]
                )
                Pages.AEAccountingBillingBasedTab.MAWB.revenue(freight_index).vol_input.input(row["Volume"])
                Pages.AEAccountingBillingBasedTab.MAWB.revenue(freight_index).rate_input.input(row["Rate"])
                freight_index += 1
        elif revenue_cost == "cost":
            freight_index = Pages.AEAccountingBillingBasedTab.MAWB.cost.get_len() + 1

            for row in context.table:
                Pages.AEAccountingBillingBasedTab.MAWB.cost.new_button.click()
                sleep(1)
                Pages.AEAccountingBillingBasedTab.MAWB.cost(freight_index).bill_to_autocomplete.input(
                    transfer_data(row["Bill to"])
                )
                Pages.AEAccountingBillingBasedTab.MAWB.cost(freight_index).freight_code_autocomplete.input(
                    row["Freight code"]
                )
                Pages.AEAccountingBillingBasedTab.MAWB.cost(freight_index).vol_input.input(row["Volume"])
                Pages.AEAccountingBillingBasedTab.MAWB.cost(freight_index).rate_input.input(row["Rate"])
                freight_index += 1
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif MAWB_or_HAWB == "HAWB":
        if revenue_cost == "revenue":
            freight_index = Pages.AEAccountingBillingBasedTab.HAWB.revenue.get_len() + 1

            for row in context.table:
                Pages.AEAccountingBillingBasedTab.HAWB.revenue.new_button.click()
                sleep(1)
                Pages.AEAccountingBillingBasedTab.HAWB.revenue(freight_index).bill_to_autocomplete.input(
                    transfer_data(row["Bill to"])
                )
                Pages.AEAccountingBillingBasedTab.HAWB.revenue(freight_index).freight_code_autocomplete.input(
                    row["Freight code"]
                )
                Pages.AEAccountingBillingBasedTab.HAWB.revenue(freight_index).vol_input.input(row["Volume"])
                Pages.AEAccountingBillingBasedTab.HAWB.revenue(freight_index).rate_input.input(row["Rate"])
                freight_index += 1
        elif revenue_cost == "cost":
            freight_index = Pages.AEAccountingBillingBasedTab.HAWB.cost.get_len() + 1

            for row in context.table:
                Pages.AEAccountingBillingBasedTab.HAWB.cost.new_button.click()
                sleep(1)
                Pages.AEAccountingBillingBasedTab.HAWB.cost(freight_index).bill_to_autocomplete.input(
                    transfer_data(row["Bill to"])
                )
                Pages.AEAccountingBillingBasedTab.HAWB.cost(freight_index).freight_code_autocomplete.input(
                    row["Freight code"]
                )
                Pages.AEAccountingBillingBasedTab.HAWB.cost(freight_index).vol_input.input(row["Volume"])
                Pages.AEAccountingBillingBasedTab.HAWB.cost(freight_index).rate_input.input(row["Rate"])
                freight_index += 1
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@Then("values in AE {MAWB_or_HAWB} {revenue_cost} should be correct")
def step_impl(context, MAWB_or_HAWB, revenue_cost):
    if MAWB_or_HAWB == "MAWB":
        if revenue_cost == "revenue":
            for row in context.table:
                if "Currency" in context.table.headings and row["Currency"]:
                    answer = row["Currency"]
                    real_value = Pages.AEAccountingBillingBasedTab.MAWB.revenue(
                        int(row["No."])
                    ).currency_select.get_value(timeout=1)
                    assert (
                        answer == real_value
                    ), "The currency in MAWB revenue No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
                if "Amount" in context.table.headings and row["Amount"]:
                    answer = row["Amount"]
                    real_value = Pages.AEAccountingBillingBasedTab.MAWB.revenue(int(row["No."])).amount_input.get_value(
                        timeout=1
                    )
                    assert answer == real_value, "The amount in MAWB revenue No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
        elif revenue_cost == "cost":
            for row in context.table:
                if "Currency" in context.table.headings and row["Currency"]:
                    answer = row["Currency"]
                    real_value = Pages.AEAccountingBillingBasedTab.MAWB.cost(int(row["No."])).currency_select.get_value(
                        timeout=1
                    )
                    assert answer == real_value, "The currency in MAWB cost No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
                if "Amount" in context.table.headings and row["Amount"]:
                    answer = row["Amount"]
                    real_value = Pages.AEAccountingBillingBasedTab.MAWB.cost(int(row["No."])).amount_input.get_value(
                        timeout=1
                    )
                    assert answer == real_value, "The amount in MAWB cost No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif MAWB_or_HAWB == "HAWB":
        if revenue_cost == "revenue":
            for row in context.table:
                if "Currency" in context.table.headings and row["Currency"]:
                    answer = row["Currency"]
                    real_value = Pages.AEAccountingBillingBasedTab.HAWB.revenue(
                        int(row["No."])
                    ).currency_select.get_value(timeout=1)
                    assert (
                        answer == real_value
                    ), "The currency in HAWB revenue No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
                if "Amount" in context.table.headings and row["Amount"]:
                    answer = row["Amount"]
                    real_value = Pages.AEAccountingBillingBasedTab.HAWB.revenue(int(row["No."])).amount_input.get_value(
                        timeout=1
                    )
                    assert answer == real_value, "The amount in HAWB revenue No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
        elif revenue_cost == "cost":
            for row in context.table:
                if "Currency" in context.table.headings and row["Currency"]:
                    answer = row["Currency"]
                    real_value = Pages.AEAccountingBillingBasedTab.HAWB.cost(int(row["No."])).currency_select.get_value(
                        timeout=1
                    )
                    assert answer == real_value, "The currency in HAWB cost No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
                if "Amount" in context.table.headings and row["Amount"]:
                    answer = row["Amount"]
                    real_value = Pages.AEAccountingBillingBasedTab.HAWB.cost(int(row["No."])).amount_input.get_value(
                        timeout=1
                    )
                    assert answer == real_value, "The amount in HAWB cost No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@When("the user deletes freights in AE {MAWB_or_HAWB} {invoice_type}")
def step_impl(context, MAWB_or_HAWB, invoice_type):
    if MAWB_or_HAWB == "MAWB":
        if invoice_type == "revenue":
            for row in context.table:
                Pages.AEAccountingBillingBasedTab.MAWB.revenue(int(row["No."])).check_checkbox.tick(True)
            Pages.AEAccountingBillingBasedTab.MAWB.revenue.delete_button.click()
        elif invoice_type == "cost":
            for row in context.table:
                Pages.AEAccountingBillingBasedTab.MAWB.cost(int(row["No."])).check_checkbox.tick(True)
            Pages.AEAccountingBillingBasedTab.MAWB.cost.delete_button.click()
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif MAWB_or_HAWB == "HAWB":
        if invoice_type == "revenue":
            for row in context.table:
                Pages.AEAccountingBillingBasedTab.HAWB.revenue(int(row["No."])).check_checkbox.tick(True)
            Pages.AEAccountingBillingBasedTab.HAWB.revenue.delete_button.click()
        elif invoice_type == "cost":
            for row in context.table:
                Pages.AEAccountingBillingBasedTab.HAWB.cost(int(row["No."])).check_checkbox.tick(True)
            Pages.AEAccountingBillingBasedTab.HAWB.cost.delete_button.click()
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    sleep(1)


@When("the user changes currency of freights in AE {MAWB_or_HAWB} {invoice_type}")
def step_impl(context, MAWB_or_HAWB, invoice_type):
    if MAWB_or_HAWB == "MAWB":
        if invoice_type == "revenue":
            for row in context.table:
                Pages.AEAccountingBillingBasedTab.MAWB.revenue(int(row["No."])).currency_select.select(row["Currency"])
        elif invoice_type == "cost":
            for row in context.table:
                Pages.AEAccountingBillingBasedTab.MAWB.cost(int(row["No."])).currency_select.select(row["Currency"])
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif MAWB_or_HAWB == "HAWB":
        if invoice_type == "revenue":
            for row in context.table:
                Pages.AEAccountingBillingBasedTab.HAWB.revenue(int(row["No."])).currency_select.select(row["Currency"])
        elif invoice_type == "cost":
            for row in context.table:
                Pages.AEAccountingBillingBasedTab.HAWB.cost(int(row["No."])).currency_select.select(row["Currency"])
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    sleep(1)


@When("the user copys freights from AE {from_MAWB_or_HAWB} {from_invoice_type} to {to_MAWB_or_HAWB} {to_invoice_type}")
def step_impl(context, from_MAWB_or_HAWB, from_invoice_type, to_MAWB_or_HAWB, to_invoice_type):
    if from_MAWB_or_HAWB == "MAWB":
        if from_invoice_type == "revenue":
            for row in context.table:
                Pages.AEAccountingBillingBasedTab.MAWB.revenue(int(row["No."])).check_checkbox.tick(True)
            Pages.AEAccountingBillingBasedTab.MAWB.revenue.copy_to_button.click()
        elif from_invoice_type == "cost":
            for row in context.table:
                Pages.AEAccountingBillingBasedTab.MAWB.cost(int(row["No."])).check_checkbox.tick(True)
            Pages.AEAccountingBillingBasedTab.MAWB.cost.copy_to_button.click()
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif from_MAWB_or_HAWB == "HAWB":
        if from_invoice_type == "revenue":
            for row in context.table:
                Pages.AEAccountingBillingBasedTab.HAWB.revenue(int(row["No."])).check_checkbox.tick(True)
            Pages.AEAccountingBillingBasedTab.HAWB.revenue.copy_to_button.click()
        elif from_invoice_type == "cost":
            for row in context.table:
                Pages.AEAccountingBillingBasedTab.HAWB.cost(int(row["No."])).check_checkbox.tick(True)
            Pages.AEAccountingBillingBasedTab.HAWB.cost.copy_to_button.click()
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    sleep(1)

    if to_MAWB_or_HAWB == "MAWB":
        if to_invoice_type == "revenue":
            Pages.AEAccountingBillingBasedTab.Common.copy_to_dropdown.MAWB_revenue_checkbox.tick(True)
        elif to_invoice_type == "cost":
            Pages.AEAccountingBillingBasedTab.Common.copy_to_dropdown.MAWB_cost_checkbox.tick(True)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif to_MAWB_or_HAWB == "HAWB":
        if to_invoice_type == "revenue":
            Pages.AEAccountingBillingBasedTab.Common.copy_to_dropdown.HAWB_revenue_checkbox.tick(True)
        elif to_invoice_type == "cost":
            Pages.AEAccountingBillingBasedTab.Common.copy_to_dropdown.HAWB_cost_checkbox.tick(True)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)
    Pages.AEAccountingBillingBasedTab.Common.copy_to_dropdown.copy_button.click()
    sleep(5)


@When("the user input freights information to AE {MAWB_or_HAWB} {invoice_type}")
def step_impl(context, MAWB_or_HAWB, invoice_type):
    if MAWB_or_HAWB == "MAWB":
        if invoice_type == "revenue":
            for row in context.table:
                Pages.AEAccountingBillingBasedTab.MAWB.revenue(int(row["No."])).bill_to_autocomplete.input(
                    row["Bill to"]
                )
        elif invoice_type == "cost":
            for row in context.table:
                Pages.AEAccountingBillingBasedTab.MAWB.cost(int(row["No."])).bill_to_autocomplete.input(row["Bill to"])
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif MAWB_or_HAWB == "HAWB":
        if invoice_type == "revenue":
            for row in context.table:
                Pages.AEAccountingBillingBasedTab.HAWB.revenue(int(row["No."])).bill_to_autocomplete.input(
                    row["Bill to"]
                )
        elif invoice_type == "cost":
            for row in context.table:
                Pages.AEAccountingBillingBasedTab.HAWB.cost(int(row["No."])).bill_to_autocomplete.input(row["Bill to"])
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@When("the user clicks 'Action -> Print / Mail' to AE {MAWB_or_HAWB} {invoice_type}({index})")
def step_impl(context, MAWB_or_HAWB, invoice_type, index):
    if MAWB_or_HAWB == "MAWB":
        if invoice_type == "revenue":
            Pages.AEAccountingBillingBasedTab.MAWB.revenue(int(index)).action_button.click()
            Pages.AEAccountingBillingBasedTab.MAWB.revenue(int(index)).action_print_mail_button.click()
        elif invoice_type == "cost":
            Pages.AEAccountingBillingBasedTab.MAWB.cost(int(index)).action_button.click()
            Pages.AEAccountingBillingBasedTab.MAWB.cost(int(index)).action_print_mail_button.click()
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif MAWB_or_HAWB == "HAWB":
        if invoice_type == "revenue":
            Pages.AEAccountingBillingBasedTab.HAWB.revenue(int(index)).action_button.click()
            Pages.AEAccountingBillingBasedTab.HAWB.revenue(int(index)).action_print_mail_button.click()
        elif invoice_type == "cost":
            Pages.AEAccountingBillingBasedTab.HAWB.cost(int(index)).action_button.click()
            Pages.AEAccountingBillingBasedTab.HAWB.cost(int(index)).action_print_mail_button.click()
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    sleep(4)
    Driver.switch_to(window_name="Invoice Print")


@When("the user goes back to AE Shipment '{shipment_name}'")
def step_impl(context, shipment_name):
    Driver.open(context._vp.get("shipment_url")[shipment_name])
    Pages.Common.spin_bar.gone()


@Then("the {block_unblock} bottom in AE {MAWB_or_HAWB} {invoice_type}({index}) should be invisible")
def step_impl(context, block_unblock, MAWB_or_HAWB, invoice_type, index):
    if MAWB_or_HAWB == "MAWB":
        if invoice_type == "revenue":
            Pages.AEAccountingBillingBasedTab.MAWB.revenue(int(index)).action_button.click()
            if block_unblock == "block":
                assert (
                    Pages.AEAccountingBillingBasedTab.MAWB.revenue(int(index)).action_block_button.is_visible() == False
                )
            elif block_unblock == "unblock":
                assert (
                    Pages.AEAccountingBillingBasedTab.MAWB.revenue(int(index)).action_unblock_button.is_visible()
                    == False
                )
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
            Pages.AEAccountingBillingBasedTab.MAWB.revenue(int(index)).action_button.click()
        elif invoice_type == "cost":
            Pages.AEAccountingBillingBasedTab.MAWB.cost(int(index)).action_button.click()
            if block_unblock == "block":
                assert Pages.AEAccountingBillingBasedTab.MAWB.cost(int(index)).action_block_button.is_visible() == False
            elif block_unblock == "unblock":
                assert (
                    Pages.AEAccountingBillingBasedTab.MAWB.cost(int(index)).action_unblock_button.is_visible() == False
                )
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
            Pages.AEAccountingBillingBasedTab.MAWB.cost(int(index)).action_button.click()
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif MAWB_or_HAWB == "HAWB":
        if invoice_type == "revenue":
            Pages.AEAccountingBillingBasedTab.HAWB.revenue(int(index)).action_button.click()
            if block_unblock == "block":
                assert (
                    Pages.AEAccountingBillingBasedTab.HAWB.revenue(int(index)).action_block_button.is_visible() == False
                )
            elif block_unblock == "unblock":
                assert (
                    Pages.AEAccountingBillingBasedTab.HAWB.revenue(int(index)).action_unblock_button.is_visible()
                    == False
                )
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
            Pages.AEAccountingBillingBasedTab.HAWB.revenue(int(index)).action_button.click()
        elif invoice_type == "cost":
            Pages.AEAccountingBillingBasedTab.HAWB.cost(int(index)).action_button.click()
            if block_unblock == "block":
                assert Pages.AEAccountingBillingBasedTab.HAWB.cost(int(index)).action_block_button.is_visible() == False
            elif block_unblock == "unblock":
                assert (
                    Pages.AEAccountingBillingBasedTab.HAWB.cost(int(index)).action_unblock_button.is_visible() == False
                )
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
            Pages.AEAccountingBillingBasedTab.HAWB.cost(int(index)).action_button.click()
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@Then("The AE Accounting Billing Based page should show normally")
def step_impl(context):
    assert Pages.AEAccountingBillingBasedTab.MAWB.revenue.new_button.is_visible()
    assert Pages.AEAccountingBillingBasedTab.MAWB.revenue.new_five_button.is_visible()
    assert Pages.AEAccountingBillingBasedTab.MAWB.revenue.add_multiple_button.is_visible()
    assert Pages.AEAccountingBillingBasedTab.MAWB.revenue.copy_button.is_visible()
    assert Pages.AEAccountingBillingBasedTab.MAWB.revenue.copy_to_button.is_visible()
    assert Pages.AEAccountingBillingBasedTab.MAWB.revenue.delete_button.is_visible()
    assert Pages.AEAccountingBillingBasedTab.MAWB.revenue.load_from_template_button.is_visible()
    assert Pages.AEAccountingBillingBasedTab.MAWB.cost.new_button.is_visible()
    assert Pages.AEAccountingBillingBasedTab.MAWB.cost.new_five_button.is_visible()
    assert Pages.AEAccountingBillingBasedTab.MAWB.cost.add_multiple_button.is_visible()
    assert Pages.AEAccountingBillingBasedTab.MAWB.cost.copy_button.is_visible()
    assert Pages.AEAccountingBillingBasedTab.MAWB.cost.copy_to_button.is_visible()
    assert Pages.AEAccountingBillingBasedTab.MAWB.cost.delete_button.is_visible()
    assert Pages.AEAccountingBillingBasedTab.MAWB.cost.load_from_template_button.is_visible()
    assert Pages.AEAccountingBillingBasedTab.MAWB.MAWBAmount.include_draft_amount_checkbox.is_visible()
    assert Pages.AEAccountingBillingBasedTab.MAWB.MAWBAmount.mawb_amount_label.is_visible()
    assert Pages.AEAccountingBillingBasedTab.MAWB.ShipmentProfit.profit_amount_label.is_visible()
    assert Pages.AEAccountingBillingBasedTab.MAWB.tool_button.is_visible()
    assert Pages.AEAccountingBillingBasedTab.MAWB.Memo.memo_title_button.is_visible()

    assert Pages.AEAccountingBillingBasedTab.HAWB.revenue.new_button.is_visible()
    assert Pages.AEAccountingBillingBasedTab.HAWB.revenue.new_five_button.is_visible()
    assert Pages.AEAccountingBillingBasedTab.HAWB.revenue.add_multiple_button.is_visible()
    assert Pages.AEAccountingBillingBasedTab.HAWB.revenue.copy_button.is_visible()
    assert Pages.AEAccountingBillingBasedTab.HAWB.revenue.copy_to_button.is_visible()
    assert Pages.AEAccountingBillingBasedTab.HAWB.revenue.delete_button.is_visible()
    assert Pages.AEAccountingBillingBasedTab.HAWB.revenue.load_from_template_button.is_visible()
    assert Pages.AEAccountingBillingBasedTab.HAWB.cost.new_button.is_visible()
    assert Pages.AEAccountingBillingBasedTab.HAWB.cost.new_five_button.is_visible()
    assert Pages.AEAccountingBillingBasedTab.HAWB.cost.add_multiple_button.is_visible()
    assert Pages.AEAccountingBillingBasedTab.HAWB.cost.copy_button.is_visible()
    assert Pages.AEAccountingBillingBasedTab.HAWB.cost.copy_to_button.is_visible()
    assert Pages.AEAccountingBillingBasedTab.HAWB.cost.delete_button.is_visible()
    assert Pages.AEAccountingBillingBasedTab.HAWB.cost.load_from_template_button.is_visible()
    assert Pages.AEAccountingBillingBasedTab.HAWB.HAWBAmount.hawb_amount_label.is_visible()
    assert Pages.AEAccountingBillingBasedTab.HAWB.ShipmentProfit.profit_amount_label.is_visible()
    assert Pages.AEAccountingBillingBasedTab.HAWB.tool_button.is_visible()
    assert Pages.AEAccountingBillingBasedTab.HAWB.HAWBAmount.include_draft_amount_checkbox.is_visible()
    assert Pages.AEAccountingBillingBasedTab.HAWB.Memo.memo_title_button.is_visible()


@When("the user clicks save button in AE Accounting Billing Based")
def step_impl(context):
    if Pages.AEAccountingBillingBasedTab.save_button.is_enable():
        Pages.AEAccountingBillingBasedTab.save_button.click()
        Pages.Common.spin_bar.gone()
        sleep(2)
    else:
        Logger.getLogger().warning("The save button is not clickable")


@Then("the save button in AE shipment Accounting Billing Based should be disabled")
def step_impl(context):
    assert Pages.AEAccountingBillingBasedTab.save_button.is_disable(), "The save button should be disabled"


@Then("AE 'MAWB No.' should be '{mawb_no}'")
def step_impl(context, mawb_no):
    val = Pages.AEBasicTab.MAWB.mawb_no_input.get_value()
    assert mawb_no == val, f"MAWB No. should be [{mawb_no}], but now is [{val}]"
