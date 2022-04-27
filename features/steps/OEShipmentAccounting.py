from time import sleep

from behave import Then, When

import src.pages as Pages
from src.drivers.driver import Driver
from src.helper.log import Logger
from src.helper.transfer import transfer_data


@When("the user clicks OE {MBL_or_HBL} 'Create {payment_type}' button")
def step_impl(context, MBL_or_HBL, payment_type):
    if MBL_or_HBL == "MBL":
        if payment_type == "AR":
            Pages.OEAccountingInvoiceBasedTab.MBL.invoice_ar_button.click(timeout=10)
        elif payment_type == "DC":
            Pages.OEAccountingInvoiceBasedTab.MBL.d_c_note_button.click(timeout=10)
        elif payment_type == "AP":
            Pages.OEAccountingInvoiceBasedTab.MBL.ap_button.click(timeout=10)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif MBL_or_HBL == "HBL":
        if payment_type == "AR":
            Pages.OEAccountingInvoiceBasedTab.HBL.invoice_ar_button.click(timeout=10)
        elif payment_type == "DC":
            Pages.OEAccountingInvoiceBasedTab.HBL.d_c_note_button.click(timeout=10)
        elif payment_type == "AP":
            Pages.OEAccountingInvoiceBasedTab.HBL.ap_button.click(timeout=10)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    Pages.Common.spin_bar.gone()


@Then("the OE {MBL_or_HBL} amounts and profits should show correctly in Invoice Based")
def step_impl(context, MBL_or_HBL):
    sleep(5)

    if MBL_or_HBL == "MBL":
        for row in context.table:
            assert Pages.OEAccountingInvoiceBasedTab.MBL.total_revenue_label.get_value(timeout=10) == row["Revenue"]
            assert Pages.OEAccountingInvoiceBasedTab.MBL.total_cost_label.get_value() == row["Cost"]
            assert Pages.OEAccountingInvoiceBasedTab.MBL.total_balance_label.get_value() == row["Balance"]
            assert (
                Pages.OEAccountingInvoiceBasedTab.MBL.total_profit_amount_label.get_value(timeout=10)
                == row["Total Profit Amount"]
            )
    elif MBL_or_HBL == "HBL":
        for row in context.table:
            assert Pages.OEAccountingInvoiceBasedTab.HBL.total_revenue_label.get_value(timeout=10) == row["Revenue"]
            assert Pages.OEAccountingInvoiceBasedTab.HBL.total_cost_label.get_value() == row["Cost"]
            assert Pages.OEAccountingInvoiceBasedTab.HBL.total_balance_label.get_value() == row["Balance"]
            assert (
                Pages.OEAccountingInvoiceBasedTab.HBL.hbl_profit_amount_label.get_value(timeout=10)
                == row["HB/L Profit Amount"]
            )
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@Then("the OE MBL amounts and profits should show correctly in Billing Based")
def step_impl(context):
    for row in context.table:
        assert Pages.OEAccountingBillingBasedTab.MBL.MBLAmount.mbl_revenue_label.get_value() == row["MB/L Revenue"]
        assert Pages.OEAccountingBillingBasedTab.MBL.MBLAmount.mbl_cost_label.get_value() == row["MB/L Cost"]
        assert Pages.OEAccountingBillingBasedTab.MBL.MBLAmount.mbl_amount_label.get_value() == row["MB/L Amount"]
        assert (
            Pages.OEAccountingBillingBasedTab.MBL.ShipmentProfit.profit_amount_label.get_value()
            == row["Total Profit Amount"]
        )


@Then("the OE HBL amounts and profits should show correctly in Billing Based")
def step_impl(context):
    for row in context.table:
        if "HB/L Revenue" in context.table.headings:
            data_in_field = Pages.OEAccountingBillingBasedTab.HBL.HBLAmount.hbl_revenue_label.get_value()
            assert data_in_field == row["HB/L Revenue"]
        if "HB/L Cost" in context.table.headings:
            data_in_field = Pages.OEAccountingBillingBasedTab.HBL.HBLAmount.hbl_cost_label.get_value()
            assert data_in_field == row["HB/L Cost"]
        if "HB/L Amount" in context.table.headings:
            data_in_field = Pages.OEAccountingBillingBasedTab.HBL.HBLAmount.hbl_amount_label.get_value()
            assert data_in_field == row["HB/L Amount"]
        if "Profit Amount" in context.table.headings:
            data_in_field = Pages.OEAccountingBillingBasedTab.HBL.ShipmentProfit.profit_amount_label.get_value()
            assert data_in_field == row["Profit Amount"]


@When("the user delete all freights in OE {MBL_or_HBL} {invoice_type} Billing Based")
def step_impl(context, MBL_or_HBL, invoice_type):
    # If empty_info is not visible, then click 'delete all' and delete all freights
    if MBL_or_HBL == "MBL":
        if (
            invoice_type == "revenue"
            and Pages.OEAccountingBillingBasedTab.MBL.revenue.empty_info.is_visible(timeout=0) == False
        ):
            Pages.OEAccountingBillingBasedTab.MBL.revenue.select_all_checkbox.tick(True)
            Pages.OEAccountingBillingBasedTab.MBL.revenue.delete_button.click()
        elif (
            invoice_type == "cost"
            and Pages.OEAccountingBillingBasedTab.MBL.cost.empty_info.is_visible(timeout=0) == False
        ):
            Pages.OEAccountingBillingBasedTab.MBL.cost.select_all_checkbox.tick(True)
            Pages.OEAccountingBillingBasedTab.MBL.cost.delete_button.click()
    elif MBL_or_HBL == "HBL":
        if (
            invoice_type == "revenue"
            and Pages.OEAccountingBillingBasedTab.HBL.revenue.empty_info.is_visible(timeout=0) == False
        ):
            Pages.OEAccountingBillingBasedTab.HBL.revenue.select_all_checkbox.tick(True)
            Pages.OEAccountingBillingBasedTab.HBL.revenue.delete_button.click()
        elif (
            invoice_type == "cost"
            and Pages.OEAccountingBillingBasedTab.HBL.cost.empty_info.is_visible(timeout=0) == False
        ):
            Pages.OEAccountingBillingBasedTab.HBL.cost.select_all_checkbox.tick(True)
            Pages.OEAccountingBillingBasedTab.HBL.cost.delete_button.click()
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@Then("OE {MBL_or_HBL} has no invoice in {mode} Based")
def step_impl(context, MBL_or_HBL, mode):
    if mode == "Billing":
        if MBL_or_HBL == "MBL":
            assert (
                Pages.OEAccountingBillingBasedTab.MBL.revenue.empty_info.is_visible()
            ), "There are some MBL revenue exist"
            assert Pages.OEAccountingBillingBasedTab.MBL.cost.empty_info.is_visible(), "There are some MBL cost exist"
        elif MBL_or_HBL == "HBL":
            assert (
                Pages.OEAccountingBillingBasedTab.HBL.revenue.empty_info.is_visible()
            ), "There are some HBL revenue exist"
            assert Pages.OEAccountingBillingBasedTab.HBL.cost.empty_info.is_visible(), "There are some HBL cost exist"
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif mode == "Invoice":
        if MBL_or_HBL == "MBL":
            assert (
                Pages.OEAccountingInvoiceBasedTab.MBL.ar(1).reference_no_link.is_visible(timeout=0) == False
            ), "There are some MBL AR exist"
            assert (
                Pages.OEAccountingInvoiceBasedTab.MBL.dc(1).reference_no_link.is_visible(timeout=0) == False
            ), "There are some MBL DC exist"
            assert (
                Pages.OEAccountingInvoiceBasedTab.MBL.ap(1).reference_no_link.is_visible(timeout=0) == False
            ), "There are some MBL AP exist"
        elif MBL_or_HBL == "HBL":
            assert (
                Pages.OEAccountingInvoiceBasedTab.HBL.ar(1).reference_no_link.is_visible(timeout=0) == False
            ), "There are some HBL AR exist"
            assert (
                Pages.OEAccountingInvoiceBasedTab.HBL.dc(1).reference_no_link.is_visible(timeout=0) == False
            ), "There are some HBL DC exist"
            assert (
                Pages.OEAccountingInvoiceBasedTab.HBL.ap(1).reference_no_link.is_visible(timeout=0) == False
            ), "There are some HBL AP exist"
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@When("the user {checks_unchecks} OE Accounting ({mode}) {MBL_or_HBL} 'Include Draft Amount' checkbox")
def step_impl(context, checks_unchecks, mode, MBL_or_HBL):
    if mode == "Billing Based":
        if MBL_or_HBL == "MBL":
            if checks_unchecks == "checks":
                Pages.OEAccountingBillingBasedTab.MBL.MBLAmount.include_draft_amount_checkbox.tick(True)
            elif checks_unchecks == "unchecks":
                Pages.OEAccountingBillingBasedTab.MBL.MBLAmount.include_draft_amount_checkbox.tick(False)
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
        elif MBL_or_HBL == "HBL":
            if checks_unchecks == "checks":
                Pages.OEAccountingBillingBasedTab.HBL.HBLAmount.include_draft_amount_checkbox.tick(True)
            elif checks_unchecks == "unchecks":
                Pages.OEAccountingBillingBasedTab.HBL.HBLAmount.include_draft_amount_checkbox.tick(False)
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif mode == "Invoice Based":
        if MBL_or_HBL == "MBL":
            if checks_unchecks == "checks":
                Pages.OEAccountingInvoiceBasedTab.MBL.include_draft_amount_checkbox.tick(True)
            elif checks_unchecks == "unchecks":
                Pages.OEAccountingInvoiceBasedTab.MBL.include_draft_amount_checkbox.tick(False)
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
        elif MBL_or_HBL == "HBL":
            if checks_unchecks == "checks":
                Pages.OEAccountingInvoiceBasedTab.HBL.include_draft_amount_checkbox.tick(True)
            elif checks_unchecks == "unchecks":
                Pages.OEAccountingInvoiceBasedTab.HBL.include_draft_amount_checkbox.tick(False)
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@When("the user blocks OE {MBL_or_HBL} revenue({index}) in Accounting Billing Based")
def step_impl(context, MBL_or_HBL, index):
    if MBL_or_HBL == "MBL":
        Pages.OEAccountingBillingBasedTab.MBL.revenue(index=index).action_button.click()
        Pages.OEAccountingBillingBasedTab.MBL.revenue(index=index).action_block_button.click()
    elif MBL_or_HBL == "HBL":
        Pages.OEAccountingBillingBasedTab.HBL.revenue(index=index).action_button.click()
        Pages.OEAccountingBillingBasedTab.HBL.revenue(index=index).action_block_button.click()
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)
    Pages.Common.spin_bar.gone()


@Then("OE {MBL_or_HBL} {invoice_type} listed below should be uneditable in Accounting Billing Based")
def step_impl(context, MBL_or_HBL, invoice_type):
    if MBL_or_HBL == "MBL":
        if invoice_type == "revenues":
            for row in context.table:
                index = int(row["No."])
                assert Pages.OEAccountingBillingBasedTab.MBL.revenue(index=index).bill_to_autocomplete.is_disabled(
                    timeout=0
                )
                assert Pages.OEAccountingBillingBasedTab.MBL.revenue(index=index).freight_code_autocomplete.is_disabled(
                    timeout=0
                )
                assert Pages.OEAccountingBillingBasedTab.MBL.revenue(index=index).freight_description_input.is_disabled(
                    timeout=0
                )
                assert Pages.OEAccountingBillingBasedTab.MBL.revenue(index=index).p_c_select.is_disabled(timeout=0)
                assert Pages.OEAccountingBillingBasedTab.MBL.revenue(index=index).unit_select.is_disabled(timeout=0)
                assert Pages.OEAccountingBillingBasedTab.MBL.revenue(index=index).currency_select.is_disabled(timeout=0)
                assert Pages.OEAccountingBillingBasedTab.MBL.revenue(index=index).vol_input.is_disabled(timeout=0)
                assert Pages.OEAccountingBillingBasedTab.MBL.revenue(index=index).rate_input.is_disabled(timeout=0)
                assert Pages.OEAccountingBillingBasedTab.MBL.revenue(index=index).amount_input.is_disabled(timeout=0)
                assert Pages.OEAccountingBillingBasedTab.MBL.revenue(index=index).invoice_no_autocomplete.is_disabled(
                    timeout=0
                )
        elif invoice_type == "costs":
            for row in context.table:
                index = int(row["No."])
                assert Pages.OEAccountingBillingBasedTab.MBL.cost(index=index).bill_to_autocomplete.is_disabled(
                    timeout=0
                )
                assert Pages.OEAccountingBillingBasedTab.MBL.cost(index=index).freight_code_autocomplete.is_disabled(
                    timeout=0
                )
                assert Pages.OEAccountingBillingBasedTab.MBL.cost(index=index).freight_description_input.is_disabled(
                    timeout=0
                )
                assert Pages.OEAccountingBillingBasedTab.MBL.cost(index=index).p_c_select.is_disabled(timeout=0)
                assert Pages.OEAccountingBillingBasedTab.MBL.cost(index=index).unit_select.is_disabled(timeout=0)
                assert Pages.OEAccountingBillingBasedTab.MBL.cost(index=index).currency_select.is_disabled(timeout=0)
                assert Pages.OEAccountingBillingBasedTab.MBL.cost(index=index).vol_input.is_disabled(timeout=0)
                assert Pages.OEAccountingBillingBasedTab.MBL.cost(index=index).rate_input.is_disabled(timeout=0)
                assert Pages.OEAccountingBillingBasedTab.MBL.cost(index=index).amount_input.is_disabled(timeout=0)
                assert Pages.OEAccountingBillingBasedTab.MBL.cost(
                    index=index
                ).vendor_invoice_no_autocomplete.is_disabled(timeout=0)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif MBL_or_HBL == "HBL":
        if invoice_type == "revenues":
            for row in context.table:
                index = int(row["No."])
                assert Pages.OEAccountingBillingBasedTab.HBL.revenue(index=index).bill_to_autocomplete.is_disabled(
                    timeout=0
                )
                assert Pages.OEAccountingBillingBasedTab.HBL.revenue(index=index).freight_code_autocomplete.is_disabled(
                    timeout=0
                )
                assert Pages.OEAccountingBillingBasedTab.HBL.revenue(index=index).freight_description_input.is_disabled(
                    timeout=0
                )
                assert Pages.OEAccountingBillingBasedTab.HBL.revenue(index=index).p_c_select.is_disabled(timeout=0)
                assert Pages.OEAccountingBillingBasedTab.HBL.revenue(index=index).unit_select.is_disabled(timeout=0)
                assert Pages.OEAccountingBillingBasedTab.HBL.revenue(index=index).currency_select.is_disabled(timeout=0)
                assert Pages.OEAccountingBillingBasedTab.HBL.revenue(index=index).vol_input.is_disabled(timeout=0)
                assert Pages.OEAccountingBillingBasedTab.HBL.revenue(index=index).rate_input.is_disabled(timeout=0)
                assert Pages.OEAccountingBillingBasedTab.HBL.revenue(index=index).amount_input.is_disabled(timeout=0)
                assert Pages.OEAccountingBillingBasedTab.HBL.revenue(index=index).invoice_no_autocomplete.is_disabled(
                    timeout=0
                )
        elif invoice_type == "costs":
            for row in context.table:
                index = int(row["No."])
                assert Pages.OEAccountingBillingBasedTab.HBL.cost(index=index).bill_to_autocomplete.is_disabled(
                    timeout=0
                )
                assert Pages.OEAccountingBillingBasedTab.HBL.cost(index=index).freight_code_autocomplete.is_disabled(
                    timeout=0
                )
                assert Pages.OEAccountingBillingBasedTab.HBL.cost(index=index).freight_description_input.is_disabled(
                    timeout=0
                )
                assert Pages.OEAccountingBillingBasedTab.HBL.cost(index=index).p_c_select.is_disabled(timeout=0)
                assert Pages.OEAccountingBillingBasedTab.HBL.cost(index=index).unit_select.is_disabled(timeout=0)
                assert Pages.OEAccountingBillingBasedTab.HBL.cost(index=index).currency_select.is_disabled(timeout=0)
                assert Pages.OEAccountingBillingBasedTab.HBL.cost(index=index).vol_input.is_disabled(timeout=0)
                assert Pages.OEAccountingBillingBasedTab.HBL.cost(index=index).rate_input.is_disabled(timeout=0)
                assert Pages.OEAccountingBillingBasedTab.HBL.cost(index=index).amount_input.is_disabled(timeout=0)
                assert Pages.OEAccountingBillingBasedTab.HBL.cost(
                    index=index
                ).vendor_invoice_no_autocomplete.is_disabled(timeout=0)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@When("the user adds freights to OE {MBL_or_HBL} {revenue_cost}")
def step_impl(context, MBL_or_HBL, revenue_cost):
    if MBL_or_HBL == "MBL":
        if revenue_cost == "revenue":
            freight_index = Pages.OEAccountingBillingBasedTab.MBL.revenue.get_len() + 1

            for row in context.table:
                Pages.OEAccountingBillingBasedTab.MBL.revenue.new_button.click()
                sleep(1)
                Pages.OEAccountingBillingBasedTab.MBL.revenue(freight_index).bill_to_autocomplete.input(
                    transfer_data(row["Bill to"])
                )
                Pages.OEAccountingBillingBasedTab.MBL.revenue(freight_index).freight_code_autocomplete.input(
                    row["Freight code"]
                )
                Pages.OEAccountingBillingBasedTab.MBL.revenue(freight_index).vol_input.input(row["Volume"])
                Pages.OEAccountingBillingBasedTab.MBL.revenue(freight_index).rate_input.input(row["Rate"])
                freight_index += 1
        elif revenue_cost == "cost":
            freight_index = Pages.OEAccountingBillingBasedTab.MBL.cost.get_len() + 1

            for row in context.table:
                Pages.OEAccountingBillingBasedTab.MBL.cost.new_button.click()
                sleep(1)
                Pages.OEAccountingBillingBasedTab.MBL.cost(freight_index).bill_to_autocomplete.input(
                    transfer_data(row["Bill to"])
                )
                Pages.OEAccountingBillingBasedTab.MBL.cost(freight_index).freight_code_autocomplete.input(
                    row["Freight code"]
                )
                Pages.OEAccountingBillingBasedTab.MBL.cost(freight_index).vol_input.input(row["Volume"])
                Pages.OEAccountingBillingBasedTab.MBL.cost(freight_index).rate_input.input(row["Rate"])
                freight_index += 1
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif MBL_or_HBL == "HBL":
        if revenue_cost == "revenue":
            freight_index = Pages.OEAccountingBillingBasedTab.HBL.revenue.get_len() + 1

            for row in context.table:
                Pages.OEAccountingBillingBasedTab.HBL.revenue.new_button.click()
                sleep(1)
                Pages.OEAccountingBillingBasedTab.HBL.revenue(freight_index).bill_to_autocomplete.input(
                    transfer_data(row["Bill to"])
                )
                Pages.OEAccountingBillingBasedTab.HBL.revenue(freight_index).freight_code_autocomplete.input(
                    row["Freight code"]
                )
                Pages.OEAccountingBillingBasedTab.HBL.revenue(freight_index).vol_input.input(row["Volume"])
                Pages.OEAccountingBillingBasedTab.HBL.revenue(freight_index).rate_input.input(row["Rate"])
                freight_index += 1
        elif revenue_cost == "cost":
            freight_index = Pages.OEAccountingBillingBasedTab.HBL.cost.get_len() + 1

            for row in context.table:
                Pages.OEAccountingBillingBasedTab.HBL.cost.new_button.click()
                sleep(1)
                Pages.OEAccountingBillingBasedTab.HBL.cost(freight_index).bill_to_autocomplete.input(
                    transfer_data(row["Bill to"])
                )
                Pages.OEAccountingBillingBasedTab.HBL.cost(freight_index).freight_code_autocomplete.input(
                    row["Freight code"]
                )
                Pages.OEAccountingBillingBasedTab.HBL.cost(freight_index).vol_input.input(row["Volume"])
                Pages.OEAccountingBillingBasedTab.HBL.cost(freight_index).rate_input.input(row["Rate"])
                freight_index += 1
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@Then("values in OE {MBL_or_HBL} {revenue_cost} should be correct")
def step_impl(context, MBL_or_HBL, revenue_cost):
    if MBL_or_HBL == "MBL":
        if revenue_cost == "revenue":
            for row in context.table:
                if "Currency" in context.table.headings and row["Currency"]:
                    answer = row["Currency"]
                    real_value = Pages.OEAccountingBillingBasedTab.MBL.revenue(
                        int(row["No."])
                    ).currency_select.get_value()
                    assert (
                        answer == real_value
                    ), "The currency in MBL revenue No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
                if "Amount" in context.table.headings and row["Amount"]:
                    answer = row["Amount"]
                    real_value = Pages.OEAccountingBillingBasedTab.MBL.revenue(int(row["No."])).amount_input.get_value(
                        timeout=0
                    )
                    assert answer == real_value, "The amount in MBL revenue No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
        elif revenue_cost == "cost":
            for row in context.table:
                if "Currency" in context.table.headings and row["Currency"]:
                    answer = row["Currency"]
                    real_value = Pages.OEAccountingBillingBasedTab.MBL.cost(int(row["No."])).currency_select.get_value()
                    assert answer == real_value, "The currency in MBL cost No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
                if "Amount" in context.table.headings and row["Amount"]:
                    answer = row["Amount"]
                    real_value = Pages.OEAccountingBillingBasedTab.MBL.cost(int(row["No."])).amount_input.get_value(
                        timeout=0
                    )
                    assert answer == real_value, "The amount in MBL cost No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif MBL_or_HBL == "HBL":
        if revenue_cost == "revenue":
            for row in context.table:
                if "Currency" in context.table.headings and row["Currency"]:
                    answer = row["Currency"]
                    real_value = Pages.OEAccountingBillingBasedTab.HBL.revenue(
                        int(row["No."])
                    ).currency_select.get_value()
                    assert (
                        answer == real_value
                    ), "The currency in HBL revenue No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
                if "Amount" in context.table.headings and row["Amount"]:
                    answer = row["Amount"]
                    real_value = Pages.OEAccountingBillingBasedTab.HBL.revenue(int(row["No."])).amount_input.get_value(
                        timeout=0
                    )
                    assert answer == real_value, "The amount in HBL revenue No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
        elif revenue_cost == "cost":
            for row in context.table:
                if "Currency" in context.table.headings and row["Currency"]:
                    answer = row["Currency"]
                    real_value = Pages.OEAccountingBillingBasedTab.HBL.cost(int(row["No."])).currency_select.get_value()
                    assert answer == real_value, "The currency in HBL cost No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
                if "Amount" in context.table.headings and row["Amount"]:
                    answer = row["Amount"]
                    real_value = Pages.OEAccountingBillingBasedTab.HBL.cost(int(row["No."])).amount_input.get_value(
                        timeout=0
                    )
                    assert answer == real_value, "The amount in HBL cost No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@When("the user deletes freights in OE {MBL_or_HBL} {invoice_type}")
def step_impl(context, MBL_or_HBL, invoice_type):
    if MBL_or_HBL == "MBL":
        if invoice_type == "revenue":
            for row in context.table:
                Pages.OEAccountingBillingBasedTab.MBL.revenue(int(row["No."])).check_checkbox.tick(True)
            Pages.OEAccountingBillingBasedTab.MBL.revenue.delete_button.click()
        elif invoice_type == "cost":
            for row in context.table:
                Pages.OEAccountingBillingBasedTab.MBL.cost(int(row["No."])).check_checkbox.tick(True)
            Pages.OEAccountingBillingBasedTab.MBL.cost.delete_button.click()
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif MBL_or_HBL == "HBL":
        if invoice_type == "revenue":
            for row in context.table:
                Pages.OEAccountingBillingBasedTab.HBL.revenue(int(row["No."])).check_checkbox.tick(True)
            Pages.OEAccountingBillingBasedTab.HBL.revenue.delete_button.click()
        elif invoice_type == "cost":
            for row in context.table:
                Pages.OEAccountingBillingBasedTab.HBL.cost(int(row["No."])).check_checkbox.tick(True)
            Pages.OEAccountingBillingBasedTab.HBL.cost.delete_button.click()
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    sleep(1)


@When("the user changes currency of freights in OE {MBL_or_HBL} {invoice_type}")
def step_impl(context, MBL_or_HBL, invoice_type):
    if MBL_or_HBL == "MBL":
        if invoice_type == "revenue":
            for row in context.table:
                Pages.OEAccountingBillingBasedTab.MBL.revenue(int(row["No."])).currency_select.select(row["Currency"])
        elif invoice_type == "cost":
            for row in context.table:
                Pages.OEAccountingBillingBasedTab.MBL.cost(int(row["No."])).currency_select.select(row["Currency"])
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif MBL_or_HBL == "HBL":
        if invoice_type == "revenue":
            for row in context.table:
                Pages.OEAccountingBillingBasedTab.HBL.revenue(int(row["No."])).currency_select.select(row["Currency"])
        elif invoice_type == "cost":
            for row in context.table:
                Pages.OEAccountingBillingBasedTab.HBL.cost(int(row["No."])).currency_select.select(row["Currency"])
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    sleep(1)


@When("the user copys freights from OE {from_MBL_or_HBL} {from_invoice_type} to {to_MBL_or_HBL} {to_invoice_type}")
def step_impl(context, from_MBL_or_HBL, from_invoice_type, to_MBL_or_HBL, to_invoice_type):
    if from_MBL_or_HBL == "MBL":
        if from_invoice_type == "revenue":
            for row in context.table:
                Pages.OEAccountingBillingBasedTab.MBL.revenue(int(row["No."])).check_checkbox.tick(True)
            Pages.OEAccountingBillingBasedTab.MBL.revenue.copy_to_button.click()
        elif from_invoice_type == "cost":
            for row in context.table:
                Pages.OEAccountingBillingBasedTab.MBL.cost(int(row["No."])).check_checkbox.tick(True)
            Pages.OEAccountingBillingBasedTab.MBL.cost.copy_to_button.click()
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif from_MBL_or_HBL == "HBL":
        if from_invoice_type == "revenue":
            for row in context.table:
                Pages.OEAccountingBillingBasedTab.HBL.revenue(int(row["No."])).check_checkbox.tick(True)
            Pages.OEAccountingBillingBasedTab.HBL.revenue.copy_to_button.click()
        elif from_invoice_type == "cost":
            for row in context.table:
                Pages.OEAccountingBillingBasedTab.HBL.cost(int(row["No."])).check_checkbox.tick(True)
            Pages.OEAccountingBillingBasedTab.HBL.cost.copy_to_button.click()
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    sleep(1)

    if to_MBL_or_HBL == "MBL":
        if to_invoice_type == "revenue":
            Pages.OEAccountingBillingBasedTab.Common.copy_to_dropdown.MBL_revenue_checkbox.tick(True)
        elif to_invoice_type == "cost":
            Pages.OEAccountingBillingBasedTab.Common.copy_to_dropdown.MBL_cost_checkbox.tick(True)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif to_MBL_or_HBL == "HBL":
        if to_invoice_type == "revenue":
            Pages.OEAccountingBillingBasedTab.Common.copy_to_dropdown.HBL_revenue_checkbox.tick(True)
        elif to_invoice_type == "cost":
            Pages.OEAccountingBillingBasedTab.Common.copy_to_dropdown.HBL_cost_checkbox.tick(True)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)
    Pages.OEAccountingBillingBasedTab.Common.copy_to_dropdown.copy_button.click()
    sleep(5)


@When("the user input freights information to OE {MBL_or_HBL} {invoice_type}")
def step_impl(context, MBL_or_HBL, invoice_type):
    if MBL_or_HBL == "MBL":
        if invoice_type == "revenue":
            for row in context.table:
                index = int(row["No."])
                if "Bill to" in context.table.headings:
                    Pages.OEAccountingBillingBasedTab.MBL.revenue(index).bill_to_autocomplete.input(row["Bill to"])
        elif invoice_type == "cost":
            for row in context.table:
                index = int(row["No."])
                if "Bill to" in context.table.headings:
                    Pages.OEAccountingBillingBasedTab.MBL.cost(index).bill_to_autocomplete.input(row["Bill to"])
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif MBL_or_HBL == "HBL":
        if invoice_type == "revenue":
            for row in context.table:
                index = int(row["No."])
                if "Bill to" in context.table.headings:
                    Pages.OEAccountingBillingBasedTab.HBL.revenue(index).bill_to_autocomplete.input(row["Bill to"])
        elif invoice_type == "cost":
            for row in context.table:
                index = int(row["No."])
                if "Bill to" in context.table.headings:
                    Pages.OEAccountingBillingBasedTab.HBL.cost(index).bill_to_autocomplete.input(row["Bill to"])
                if "Cost Share" in context.table.headings:
                    input_data = transfer_data(row["Cost Share"])
                    Pages.OEAccountingBillingBasedTab.HBL.cost(index).cost_share_checkbox.tick(input_data)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@When("the user clicks 'Action -> Print / Mail' to OE {MBL_or_HBL} {invoice_type}({index})")
def step_impl(context, MBL_or_HBL, invoice_type, index):
    if MBL_or_HBL == "MBL":
        if invoice_type == "revenue":
            Pages.OEAccountingBillingBasedTab.MBL.revenue(int(index)).action_button.click()
            Pages.OEAccountingBillingBasedTab.MBL.revenue(int(index)).action_print_mail_button.click()
        elif invoice_type == "cost":
            Pages.OEAccountingBillingBasedTab.MBL.cost(int(index)).action_button.click()
            Pages.OEAccountingBillingBasedTab.MBL.cost(int(index)).action_print_mail_button.click()
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif MBL_or_HBL == "HBL":
        if invoice_type == "revenue":
            Pages.OEAccountingBillingBasedTab.HBL.revenue(int(index)).action_button.click()
            Pages.OEAccountingBillingBasedTab.HBL.revenue(int(index)).action_print_mail_button.click()
        elif invoice_type == "cost":
            Pages.OEAccountingBillingBasedTab.HBL.cost(int(index)).action_button.click()
            Pages.OEAccountingBillingBasedTab.HBL.cost(int(index)).action_print_mail_button.click()
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    sleep(4)
    Driver.switch_to(window_name="Invoice Print")


@When("the user goes back to OE Shipment '{shipment_name}'")
def step_impl(context, shipment_name):
    Driver.open(context._vp.get("shipment_url")[shipment_name])
    Pages.Common.spin_bar.gone()


@Then("the {block_unblock} bottom in OE {MBL_or_HBL} {invoice_type}({index}) should be invisible")
def step_impl(context, block_unblock, MBL_or_HBL, invoice_type, index):
    if MBL_or_HBL == "MBL":
        if invoice_type == "revenue":
            Pages.OEAccountingBillingBasedTab.MBL.revenue(int(index)).action_button.click()
            if block_unblock == "block":
                assert (
                    Pages.OEAccountingBillingBasedTab.MBL.revenue(int(index)).action_block_button.is_visible() == False
                )
            elif block_unblock == "unblock":
                assert (
                    Pages.OEAccountingBillingBasedTab.MBL.revenue(int(index)).action_unblock_button.is_visible()
                    == False
                )
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
            Pages.OEAccountingBillingBasedTab.MBL.revenue(int(index)).action_button.click()
        elif invoice_type == "cost":
            Pages.OEAccountingBillingBasedTab.MBL.cost(int(index)).action_button.click()
            if block_unblock == "block":
                assert Pages.OEAccountingBillingBasedTab.MBL.cost(int(index)).action_block_button.is_visible() == False
            elif block_unblock == "unblock":
                assert (
                    Pages.OEAccountingBillingBasedTab.MBL.cost(int(index)).action_unblock_button.is_visible() == False
                )
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
            Pages.OEAccountingBillingBasedTab.MBL.cost(int(index)).action_button.click()
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif MBL_or_HBL == "HBL":
        if invoice_type == "revenue":
            Pages.OEAccountingBillingBasedTab.HBL.revenue(int(index)).action_button.click()
            if block_unblock == "block":
                assert (
                    Pages.OEAccountingBillingBasedTab.HBL.revenue(int(index)).action_block_button.is_visible() == False
                )
            elif block_unblock == "unblock":
                assert (
                    Pages.OEAccountingBillingBasedTab.HBL.revenue(int(index)).action_unblock_button.is_visible()
                    == False
                )
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
            Pages.OEAccountingBillingBasedTab.HBL.revenue(int(index)).action_button.click()
        elif invoice_type == "cost":
            Pages.OEAccountingBillingBasedTab.HBL.cost(int(index)).action_button.click()
            if block_unblock == "block":
                assert Pages.OEAccountingBillingBasedTab.HBL.cost(int(index)).action_block_button.is_visible() == False
            elif block_unblock == "unblock":
                assert (
                    Pages.OEAccountingBillingBasedTab.HBL.cost(int(index)).action_unblock_button.is_visible() == False
                )
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
            Pages.OEAccountingBillingBasedTab.HBL.cost(int(index)).action_button.click()
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@Then("The OE Accounting Billing Based page should show normally")
def step_impl(context):
    assert Pages.OEAccountingBillingBasedTab.MBL.revenue.new_button.is_visible()
    assert Pages.OEAccountingBillingBasedTab.MBL.revenue.new_five_button.is_visible()
    assert Pages.OEAccountingBillingBasedTab.MBL.revenue.add_multiple_button.is_visible()
    assert Pages.OEAccountingBillingBasedTab.MBL.revenue.copy_button.is_visible()
    assert Pages.OEAccountingBillingBasedTab.MBL.revenue.copy_to_button.is_visible()
    assert Pages.OEAccountingBillingBasedTab.MBL.revenue.delete_button.is_visible()
    assert Pages.OEAccountingBillingBasedTab.MBL.revenue.load_from_template_button.is_visible()
    assert Pages.OEAccountingBillingBasedTab.MBL.cost.new_button.is_visible()
    assert Pages.OEAccountingBillingBasedTab.MBL.cost.new_five_button.is_visible()
    assert Pages.OEAccountingBillingBasedTab.MBL.cost.add_multiple_button.is_visible()
    assert Pages.OEAccountingBillingBasedTab.MBL.cost.copy_button.is_visible()
    assert Pages.OEAccountingBillingBasedTab.MBL.cost.copy_to_button.is_visible()
    assert Pages.OEAccountingBillingBasedTab.MBL.cost.delete_button.is_visible()
    assert Pages.OEAccountingBillingBasedTab.MBL.cost.load_from_template_button.is_visible()
    assert Pages.OEAccountingBillingBasedTab.MBL.MBLAmount.include_draft_amount_checkbox.is_visible()
    assert Pages.OEAccountingBillingBasedTab.MBL.MBLAmount.mbl_amount_label.is_visible()
    assert Pages.OEAccountingBillingBasedTab.MBL.ShipmentProfit.profit_amount_label.is_visible()
    assert Pages.OEAccountingBillingBasedTab.MBL.tool_button.is_visible()
    assert Pages.OEAccountingBillingBasedTab.MBL.Memo.memo_title_button.is_visible()

    assert Pages.OEAccountingBillingBasedTab.HBL.revenue.new_button.is_visible()
    assert Pages.OEAccountingBillingBasedTab.HBL.revenue.new_five_button.is_visible()
    assert Pages.OEAccountingBillingBasedTab.HBL.revenue.add_multiple_button.is_visible()
    assert Pages.OEAccountingBillingBasedTab.HBL.revenue.copy_button.is_visible()
    assert Pages.OEAccountingBillingBasedTab.HBL.revenue.copy_to_button.is_visible()
    assert Pages.OEAccountingBillingBasedTab.HBL.revenue.delete_button.is_visible()
    assert Pages.OEAccountingBillingBasedTab.HBL.revenue.load_from_template_button.is_visible()
    assert Pages.OEAccountingBillingBasedTab.HBL.cost.new_button.is_visible()
    assert Pages.OEAccountingBillingBasedTab.HBL.cost.new_five_button.is_visible()
    assert Pages.OEAccountingBillingBasedTab.HBL.cost.add_multiple_button.is_visible()
    assert Pages.OEAccountingBillingBasedTab.HBL.cost.copy_button.is_visible()
    assert Pages.OEAccountingBillingBasedTab.HBL.cost.copy_to_button.is_visible()
    assert Pages.OEAccountingBillingBasedTab.HBL.cost.delete_button.is_visible()
    assert Pages.OEAccountingBillingBasedTab.HBL.cost.load_from_template_button.is_visible()
    assert Pages.OEAccountingBillingBasedTab.HBL.HBLAmount.hbl_amount_label.is_visible()
    assert Pages.OEAccountingBillingBasedTab.HBL.ShipmentProfit.profit_amount_label.is_visible()
    assert Pages.OEAccountingBillingBasedTab.HBL.tool_button.is_visible()
    assert Pages.OEAccountingBillingBasedTab.HBL.HBLAmount.include_draft_amount_checkbox.is_visible()
    assert Pages.OEAccountingBillingBasedTab.HBL.Memo.memo_title_button.is_visible()


@When("the user clicks save button in OE Accounting Billing Based")
def step_impl(context):
    if Pages.OEAccountingBillingBasedTab.save_button.is_enable():
        Pages.OEAccountingBillingBasedTab.save_button.click()
        Pages.Common.spin_bar.gone()
        sleep(2)
    else:
        Logger.getLogger().warning("The save button is not clickable")


@Then("the save button in OE shipment Accounting Billing Based should be disabled")
def step_impl(context):
    assert Pages.OEAccountingBillingBasedTab.save_button.is_disabled(), "The save button should be disabled"
