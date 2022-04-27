from time import sleep

from behave import Then, When

import src.pages as Pages
from src.drivers.driver import Driver
from src.helper.log import Logger
from src.helper.transfer import transfer_data


@When("the user create an AR and add some empty freight items")
def step_impl(context):
    Pages.ShipmentEntryTab.accounting_tab.click()
    Pages.AccountingInvoiceBased.MBL.invoice_ar_button.click()
    Pages.Common.spin_bar.gone()
    Pages.AREntry.bill_to_autocomplete.input("3891 DELTA PORT 809")
    Pages.AREntry.new_freight_button.click()
    assert Pages.AREntry.freight.get_len() == 1, "Adding freight is failed"
    Pages.AREntry.save_button.click()


@Then("the AR should save successfully and ignore empty freight items")
def step_impl(context):
    assert Pages.Common.save_msg.is_visible() == True, "Not show the saving successfully message"
    Pages.AccountingInvoiceBased.MBL.ar(1).reference_no_link.click()
    Pages.Common.spin_bar.gone()
    assert Pages.AREntry.freight.get_len() == 0, "There are freights in the AR, excepting the freight list is empty"


@When("the user clicks OI {MBL_or_HBL} 'Create {payment_type}' button")
def step_impl(context, MBL_or_HBL, payment_type):
    if MBL_or_HBL == "MBL":
        if payment_type == "AR":
            Pages.OIAccountingInvoiceBasedTab.MBL.invoice_ar_button.click(timeout=10)
        elif payment_type == "DC":
            Pages.OIAccountingInvoiceBasedTab.MBL.d_c_note_button.click(timeout=10)
        elif payment_type == "AP":
            Pages.OIAccountingInvoiceBasedTab.MBL.ap_button.click(timeout=10)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif MBL_or_HBL == "HBL":
        if payment_type == "AR":
            Pages.OIAccountingInvoiceBasedTab.HBL.invoice_ar_button.click(timeout=10)
        elif payment_type == "DC":
            Pages.OIAccountingInvoiceBasedTab.HBL.d_c_note_button.click(timeout=10)
        elif payment_type == "AP":
            Pages.OIAccountingInvoiceBasedTab.HBL.ap_button.click(timeout=10)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    Pages.Common.spin_bar.gone()


@Then("the OI {MBL_or_HBL} amounts and profits should show correctly in Invoice Based")
def step_impl(context, MBL_or_HBL):
    sleep(5)

    if MBL_or_HBL == "MBL":
        for row in context.table:
            assert Pages.OIAccountingInvoiceBasedTab.MBL.total_revenue_label.get_value(timeout=10) == row["Revenue"]
            assert Pages.OIAccountingInvoiceBasedTab.MBL.total_cost_label.get_value() == row["Cost"]
            assert Pages.OIAccountingInvoiceBasedTab.MBL.total_balance_label.get_value() == row["Balance"]
            assert (
                Pages.OIAccountingInvoiceBasedTab.MBL.total_profit_amount_label.get_value(timeout=10)
                == row["Total Profit Amount"]
            )
    elif MBL_or_HBL == "HBL":
        for row in context.table:
            assert Pages.OIAccountingInvoiceBasedTab.HBL.total_revenue_label.get_value(timeout=10) == row["Revenue"]
            assert Pages.OIAccountingInvoiceBasedTab.HBL.total_cost_label.get_value() == row["Cost"]
            assert Pages.OIAccountingInvoiceBasedTab.HBL.total_balance_label.get_value() == row["Balance"]
            assert (
                Pages.OIAccountingInvoiceBasedTab.HBL.hbl_profit_amount_label.get_value(timeout=10)
                == row["HB/L Profit Amount"]
            )
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@Then("the OI {MBL_or_HBL} amounts and profits should show correctly in Billing Based")
def step_impl(context, MBL_or_HBL):
    if MBL_or_HBL == "MBL":
        for row in context.table:
            assert Pages.OIAccountingBillingBasedTab.MBL.MBLAmount.mbl_revenue_label.get_value() == row["MB/L Revenue"]
            assert Pages.OIAccountingBillingBasedTab.MBL.MBLAmount.mbl_cost_label.get_value() == row["MB/L Cost"]
            assert Pages.OIAccountingBillingBasedTab.MBL.MBLAmount.mbl_amount_label.get_value() == row["MB/L Amount"]
            assert (
                Pages.OIAccountingBillingBasedTab.MBL.ShipmentProfit.profit_amount_label.get_value()
                == row["Total Profit Amount"]
            )
    elif MBL_or_HBL == "HBL":
        for row in context.table:
            assert Pages.OIAccountingBillingBasedTab.HBL.HBLAmount.hbl_revenue_label.get_value() == row["HB/L Revenue"]
            assert Pages.OIAccountingBillingBasedTab.HBL.HBLAmount.hbl_cost_label.get_value() == row["HB/L Cost"]
            assert Pages.OIAccountingBillingBasedTab.HBL.HBLAmount.hbl_amount_label.get_value() == row["HB/L Amount"]
            assert (
                Pages.OIAccountingBillingBasedTab.HBL.ShipmentProfit.profit_amount_label.get_value()
                == row["Profit Amount"]
            )
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@When("the user delete all freights in OI {MBL_or_HBL} {invoice_type} Billing Based")
def step_impl(context, MBL_or_HBL, invoice_type):
    # If empty_info is not visible, then click 'delete all' and delete all freights
    if MBL_or_HBL == "MBL":
        if (
            invoice_type == "revenue"
            and Pages.OIAccountingBillingBasedTab.MBL.revenue.empty_info.is_visible(timeout=0) == False
        ):
            Pages.OIAccountingBillingBasedTab.MBL.revenue.select_all_checkbox.tick(True)
            Pages.OIAccountingBillingBasedTab.MBL.revenue.delete_button.click()
        elif (
            invoice_type == "cost"
            and Pages.OIAccountingBillingBasedTab.MBL.cost.empty_info.is_visible(timeout=0) == False
        ):
            Pages.OIAccountingBillingBasedTab.MBL.cost.select_all_checkbox.tick(True)
            Pages.OIAccountingBillingBasedTab.MBL.cost.delete_button.click()
    elif MBL_or_HBL == "HBL":
        if (
            invoice_type == "revenue"
            and Pages.OIAccountingBillingBasedTab.HBL.revenue.empty_info.is_visible(timeout=0) == False
        ):
            Pages.OIAccountingBillingBasedTab.HBL.revenue.select_all_checkbox.tick(True)
            Pages.OIAccountingBillingBasedTab.HBL.revenue.delete_button.click()
        elif (
            invoice_type == "cost"
            and Pages.OIAccountingBillingBasedTab.HBL.cost.empty_info.is_visible(timeout=0) == False
        ):
            Pages.OIAccountingBillingBasedTab.HBL.cost.select_all_checkbox.tick(True)
            Pages.OIAccountingBillingBasedTab.HBL.cost.delete_button.click()
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@Then("OI {MBL_or_HBL} has no invoice in {mode} Based")
def step_impl(context, MBL_or_HBL, mode):
    if mode == "Billing":
        if MBL_or_HBL == "MBL":
            assert (
                Pages.OIAccountingBillingBasedTab.MBL.revenue.empty_info.is_visible()
            ), "There are some MBL revenue exist"
            assert Pages.OIAccountingBillingBasedTab.MBL.cost.empty_info.is_visible(), "There are some MBL cost exist"
        elif MBL_or_HBL == "HBL":
            assert (
                Pages.OIAccountingBillingBasedTab.HBL.revenue.empty_info.is_visible()
            ), "There are some HBL revenue exist"
            assert Pages.OIAccountingBillingBasedTab.HBL.cost.empty_info.is_visible(), "There are some HBL cost exist"
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif mode == "Invoice":
        if MBL_or_HBL == "MBL":
            assert (
                Pages.OIAccountingInvoiceBasedTab.MBL.ar(1).reference_no_link.is_visible(timeout=0) == False
            ), "There are some MBL AR exist"
            assert (
                Pages.OIAccountingInvoiceBasedTab.MBL.dc(1).reference_no_link.is_visible(timeout=0) == False
            ), "There are some MBL DC exist"
            assert (
                Pages.OIAccountingInvoiceBasedTab.MBL.ap(1).reference_no_link.is_visible(timeout=0) == False
            ), "There are some MBL AP exist"
        elif MBL_or_HBL == "HBL":
            assert (
                Pages.OIAccountingInvoiceBasedTab.HBL.ar(1).reference_no_link.is_visible(timeout=0) == False
            ), "There are some HBL AR exist"
            assert (
                Pages.OIAccountingInvoiceBasedTab.HBL.dc(1).reference_no_link.is_visible(timeout=0) == False
            ), "There are some HBL DC exist"
            assert (
                Pages.OIAccountingInvoiceBasedTab.HBL.ap(1).reference_no_link.is_visible(timeout=0) == False
            ), "There are some HBL AP exist"
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@When("the user {checks_unchecks} OI Accounting ({mode}) {MBL_or_HBL} 'Include Draft Amount' checkbox")
def step_impl(context, checks_unchecks, mode, MBL_or_HBL):
    if mode == "Billing Based":
        if MBL_or_HBL == "MBL":
            if checks_unchecks == "checks":
                Pages.OIAccountingBillingBasedTab.MBL.MBLAmount.include_draft_amount_checkbox.tick(True)
            elif checks_unchecks == "unchecks":
                Pages.OIAccountingBillingBasedTab.MBL.MBLAmount.include_draft_amount_checkbox.tick(False)
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
        elif MBL_or_HBL == "HBL":
            if checks_unchecks == "checks":
                Pages.OIAccountingBillingBasedTab.HBL.HBLAmount.include_draft_amount_checkbox.tick(True)
            elif checks_unchecks == "unchecks":
                Pages.OIAccountingBillingBasedTab.HBL.HBLAmount.include_draft_amount_checkbox.tick(False)
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif mode == "Invoice Based":
        if MBL_or_HBL == "MBL":
            if checks_unchecks == "checks":
                Pages.OIAccountingInvoiceBasedTab.MBL.include_draft_amount_checkbox.tick(True)
            elif checks_unchecks == "unchecks":
                Pages.OIAccountingInvoiceBasedTab.MBL.include_draft_amount_checkbox.tick(False)
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
        elif MBL_or_HBL == "HBL":
            if checks_unchecks == "checks":
                Pages.OIAccountingInvoiceBasedTab.HBL.include_draft_amount_checkbox.tick(True)
            elif checks_unchecks == "unchecks":
                Pages.OIAccountingInvoiceBasedTab.HBL.include_draft_amount_checkbox.tick(False)
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@When("the user blocks OI {MBL_or_HBL} revenue({index}) in Accounting Billing Based")
def step_impl(context, MBL_or_HBL, index):
    if MBL_or_HBL == "MBL":
        Pages.OIAccountingBillingBasedTab.MBL.revenue(index=index).action_button.click()
        Pages.OIAccountingBillingBasedTab.MBL.revenue(index=index).action_block_button.click()
    elif MBL_or_HBL == "HBL":
        Pages.OIAccountingBillingBasedTab.HBL.revenue(index=index).action_button.click()
        Pages.OIAccountingBillingBasedTab.HBL.revenue(index=index).action_block_button.click()
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)
    Pages.Common.spin_bar.gone()


@Then("OI {MBL_or_HBL} {invoice_type} listed below should be uneditable in Accounting Billing Based")
def step_impl(context, MBL_or_HBL, invoice_type):
    if MBL_or_HBL == "MBL":
        if invoice_type == "revenues":
            for row in context.table:
                index = int(row["No."])
                assert Pages.OIAccountingBillingBasedTab.MBL.revenue(index=index).bill_to_autocomplete.is_disabled(
                    timeout=0
                )
                assert Pages.OIAccountingBillingBasedTab.MBL.revenue(index=index).freight_code_autocomplete.is_disabled(
                    timeout=0
                )
                assert Pages.OIAccountingBillingBasedTab.MBL.revenue(index=index).freight_description_input.is_disabled(
                    timeout=0
                )
                assert Pages.OIAccountingBillingBasedTab.MBL.revenue(index=index).p_c_select.is_disabled(timeout=0)
                assert Pages.OIAccountingBillingBasedTab.MBL.revenue(index=index).unit_select.is_disabled(timeout=0)
                assert Pages.OIAccountingBillingBasedTab.MBL.revenue(index=index).currency_select.is_disabled(timeout=0)
                assert Pages.OIAccountingBillingBasedTab.MBL.revenue(index=index).vol_input.is_disabled(timeout=0)
                assert Pages.OIAccountingBillingBasedTab.MBL.revenue(index=index).rate_input.is_disabled(timeout=0)
                assert Pages.OIAccountingBillingBasedTab.MBL.revenue(index=index).amount_input.is_disabled(timeout=0)
                assert Pages.OIAccountingBillingBasedTab.MBL.revenue(index=index).invoice_no_autocomplete.is_disabled(
                    timeout=0
                )
        elif invoice_type == "costs":
            for row in context.table:
                index = int(row["No."])
                assert Pages.OIAccountingBillingBasedTab.MBL.cost(index=index).bill_to_autocomplete.is_disabled(
                    timeout=0
                )
                assert Pages.OIAccountingBillingBasedTab.MBL.cost(index=index).freight_code_autocomplete.is_disabled(
                    timeout=0
                )
                assert Pages.OIAccountingBillingBasedTab.MBL.cost(index=index).freight_description_input.is_disabled(
                    timeout=0
                )
                assert Pages.OIAccountingBillingBasedTab.MBL.cost(index=index).p_c_select.is_disabled(timeout=0)
                assert Pages.OIAccountingBillingBasedTab.MBL.cost(index=index).unit_select.is_disabled(timeout=0)
                assert Pages.OIAccountingBillingBasedTab.MBL.cost(index=index).currency_select.is_disabled(timeout=0)
                assert Pages.OIAccountingBillingBasedTab.MBL.cost(index=index).vol_input.is_disabled(timeout=0)
                assert Pages.OIAccountingBillingBasedTab.MBL.cost(index=index).rate_input.is_disabled(timeout=0)
                assert Pages.OIAccountingBillingBasedTab.MBL.cost(index=index).amount_input.is_disabled(timeout=0)
                assert Pages.OIAccountingBillingBasedTab.MBL.cost(
                    index=index
                ).vendor_invoice_no_autocomplete.is_disabled(timeout=0)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif MBL_or_HBL == "HBL":
        if invoice_type == "revenues":
            for row in context.table:
                index = int(row["No."])
                assert Pages.OIAccountingBillingBasedTab.HBL.revenue(index=index).bill_to_autocomplete.is_disabled(
                    timeout=0
                )
                assert Pages.OIAccountingBillingBasedTab.HBL.revenue(index=index).freight_code_autocomplete.is_disabled(
                    timeout=0
                )
                assert Pages.OIAccountingBillingBasedTab.HBL.revenue(index=index).freight_description_input.is_disabled(
                    timeout=0
                )
                assert Pages.OIAccountingBillingBasedTab.HBL.revenue(index=index).p_c_select.is_disabled(timeout=0)
                assert Pages.OIAccountingBillingBasedTab.HBL.revenue(index=index).unit_select.is_disabled(timeout=0)
                assert Pages.OIAccountingBillingBasedTab.HBL.revenue(index=index).currency_select.is_disabled(timeout=0)
                assert Pages.OIAccountingBillingBasedTab.HBL.revenue(index=index).vol_input.is_disabled(timeout=0)
                assert Pages.OIAccountingBillingBasedTab.HBL.revenue(index=index).rate_input.is_disabled(timeout=0)
                assert Pages.OIAccountingBillingBasedTab.HBL.revenue(index=index).amount_input.is_disabled(timeout=0)
                assert Pages.OIAccountingBillingBasedTab.HBL.revenue(index=index).invoice_no_autocomplete.is_disabled(
                    timeout=0
                )
        elif invoice_type == "costs":
            for row in context.table:
                index = int(row["No."])
                assert Pages.OIAccountingBillingBasedTab.HBL.cost(index=index).bill_to_autocomplete.is_disabled(
                    timeout=0
                )
                assert Pages.OIAccountingBillingBasedTab.HBL.cost(index=index).freight_code_autocomplete.is_disabled(
                    timeout=0
                )
                assert Pages.OIAccountingBillingBasedTab.HBL.cost(index=index).freight_description_input.is_disabled(
                    timeout=0
                )
                assert Pages.OIAccountingBillingBasedTab.HBL.cost(index=index).p_c_select.is_disabled(timeout=0)
                assert Pages.OIAccountingBillingBasedTab.HBL.cost(index=index).unit_select.is_disabled(timeout=0)
                assert Pages.OIAccountingBillingBasedTab.HBL.cost(index=index).currency_select.is_disabled(timeout=0)
                assert Pages.OIAccountingBillingBasedTab.HBL.cost(index=index).vol_input.is_disabled(timeout=0)
                assert Pages.OIAccountingBillingBasedTab.HBL.cost(index=index).rate_input.is_disabled(timeout=0)
                assert Pages.OIAccountingBillingBasedTab.HBL.cost(index=index).amount_input.is_disabled(timeout=0)
                assert Pages.OIAccountingBillingBasedTab.HBL.cost(
                    index=index
                ).vendor_invoice_no_autocomplete.is_disabled(timeout=0)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@When("the user adds freights to OI {MBL_or_HBL} {revenue_cost}")
def step_impl(context, MBL_or_HBL, revenue_cost):
    if MBL_or_HBL == "MBL":
        if revenue_cost == "revenue":
            freight_index = Pages.OIAccountingBillingBasedTab.MBL.revenue.get_len() + 1

            for row in context.table:
                Pages.OIAccountingBillingBasedTab.MBL.revenue.new_button.click()
                sleep(1)
                Pages.OIAccountingBillingBasedTab.MBL.revenue(freight_index).bill_to_autocomplete.input(
                    transfer_data(row["Bill to"])
                )
                Pages.OIAccountingBillingBasedTab.MBL.revenue(freight_index).freight_code_autocomplete.input(
                    row["Freight code"]
                )
                Pages.OIAccountingBillingBasedTab.MBL.revenue(freight_index).vol_input.input(row["Volume"])
                Pages.OIAccountingBillingBasedTab.MBL.revenue(freight_index).rate_input.input(row["Rate"])
                freight_index += 1
        elif revenue_cost == "cost":
            freight_index = Pages.OIAccountingBillingBasedTab.MBL.cost.get_len() + 1

            for row in context.table:
                Pages.OIAccountingBillingBasedTab.MBL.cost.new_button.click()
                sleep(1)
                Pages.OIAccountingBillingBasedTab.MBL.cost(freight_index).bill_to_autocomplete.input(
                    transfer_data(row["Bill to"])
                )
                Pages.OIAccountingBillingBasedTab.MBL.cost(freight_index).freight_code_autocomplete.input(
                    row["Freight code"]
                )
                Pages.OIAccountingBillingBasedTab.MBL.cost(freight_index).vol_input.input(row["Volume"])
                Pages.OIAccountingBillingBasedTab.MBL.cost(freight_index).rate_input.input(row["Rate"])
                freight_index += 1
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif MBL_or_HBL == "HBL":
        if revenue_cost == "revenue":
            freight_index = Pages.OIAccountingBillingBasedTab.HBL.revenue.get_len() + 1

            for row in context.table:
                Pages.OIAccountingBillingBasedTab.HBL.revenue.new_button.click()
                sleep(1)
                Pages.OIAccountingBillingBasedTab.HBL.revenue(freight_index).bill_to_autocomplete.input(
                    transfer_data(row["Bill to"])
                )
                Pages.OIAccountingBillingBasedTab.HBL.revenue(freight_index).freight_code_autocomplete.input(
                    row["Freight code"]
                )
                Pages.OIAccountingBillingBasedTab.HBL.revenue(freight_index).vol_input.input(row["Volume"])
                Pages.OIAccountingBillingBasedTab.HBL.revenue(freight_index).rate_input.input(row["Rate"])
                freight_index += 1
        elif revenue_cost == "cost":
            freight_index = Pages.OIAccountingBillingBasedTab.HBL.cost.get_len() + 1

            for row in context.table:
                Pages.OIAccountingBillingBasedTab.HBL.cost.new_button.click()
                sleep(1)
                Pages.OIAccountingBillingBasedTab.HBL.cost(freight_index).bill_to_autocomplete.input(
                    transfer_data(row["Bill to"])
                )
                Pages.OIAccountingBillingBasedTab.HBL.cost(freight_index).freight_code_autocomplete.input(
                    row["Freight code"]
                )
                Pages.OIAccountingBillingBasedTab.HBL.cost(freight_index).vol_input.input(row["Volume"])
                Pages.OIAccountingBillingBasedTab.HBL.cost(freight_index).rate_input.input(row["Rate"])
                freight_index += 1
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@Then("values in OI {MBL_or_HBL} {revenue_cost} should be correct")
def step_impl(context, MBL_or_HBL, revenue_cost):
    if MBL_or_HBL == "MBL":
        if revenue_cost == "revenue":
            for row in context.table:
                if "Currency" in context.table.headings and row["Currency"]:
                    answer = row["Currency"]
                    real_value = Pages.OIAccountingBillingBasedTab.MBL.revenue(
                        int(row["No."])
                    ).currency_select.get_value(timeout=1)
                    assert (
                        answer == real_value
                    ), "The currency in MBL revenue No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
                if "Amount" in context.table.headings and row["Amount"]:
                    answer = row["Amount"]
                    real_value = Pages.OIAccountingBillingBasedTab.MBL.revenue(int(row["No."])).amount_input.get_value(
                        timeout=1
                    )
                    assert answer == real_value, "The amount in MBL revenue No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
        elif revenue_cost == "cost":
            for row in context.table:
                if "Currency" in context.table.headings and row["Currency"]:
                    answer = row["Currency"]
                    real_value = Pages.OIAccountingBillingBasedTab.MBL.cost(int(row["No."])).currency_select.get_value(
                        timeout=1
                    )
                    assert answer == real_value, "The currency in MBL cost No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
                if "Amount" in context.table.headings and row["Amount"]:
                    answer = row["Amount"]
                    real_value = Pages.OIAccountingBillingBasedTab.MBL.cost(int(row["No."])).amount_input.get_value(
                        timeout=1
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
                    real_value = Pages.OIAccountingBillingBasedTab.HBL.revenue(
                        int(row["No."])
                    ).currency_select.get_value(timeout=1)
                    assert answer == real_value, "The amount in HBL revenue No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
                if "Amount" in context.table.headings and row["Amount"]:
                    answer = row["Amount"]
                    real_value = Pages.OIAccountingBillingBasedTab.HBL.revenue(int(row["No."])).amount_input.get_value(
                        timeout=1
                    )
                    assert answer == real_value, "The amount in HBL revenue No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
        elif revenue_cost == "cost":
            for row in context.table:
                if "Currency" in context.table.headings and row["Currency"]:
                    answer = row["Currency"]
                    real_value = Pages.OIAccountingBillingBasedTab.HBL.cost(int(row["No."])).currency_select.get_value(
                        timeout=1
                    )
                    assert answer == real_value, "The amount in HBL cost No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
                if "Amount" in context.table.headings and row["Amount"]:
                    answer = row["Amount"]
                    real_value = Pages.OIAccountingBillingBasedTab.HBL.cost(int(row["No."])).amount_input.get_value(
                        timeout=1
                    )
                    assert answer == real_value, "The amount in HBL cost No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@When("the user deletes freights in OI {MBL_or_HBL} {invoice_type}")
def step_impl(context, MBL_or_HBL, invoice_type):
    if MBL_or_HBL == "MBL":
        if invoice_type == "revenue":
            for row in context.table:
                Pages.OIAccountingBillingBasedTab.MBL.revenue(int(row["No."])).check_checkbox.tick(True)
            Pages.OIAccountingBillingBasedTab.MBL.revenue.delete_button.click()
        elif invoice_type == "cost":
            for row in context.table:
                Pages.OIAccountingBillingBasedTab.MBL.cost(int(row["No."])).check_checkbox.tick(True)
            Pages.OIAccountingBillingBasedTab.MBL.cost.delete_button.click()
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif MBL_or_HBL == "HBL":
        if invoice_type == "revenue":
            for row in context.table:
                Pages.OIAccountingBillingBasedTab.HBL.revenue(int(row["No."])).check_checkbox.tick(True)
            Pages.OIAccountingBillingBasedTab.HBL.revenue.delete_button.click()
        elif invoice_type == "cost":
            for row in context.table:
                Pages.OIAccountingBillingBasedTab.HBL.cost(int(row["No."])).check_checkbox.tick(True)
            Pages.OIAccountingBillingBasedTab.HBL.cost.delete_button.click()
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    sleep(1)


@When("the user changes currency of freights in OI {MBL_or_HBL} {invoice_type}")
def step_impl(context, MBL_or_HBL, invoice_type):
    if MBL_or_HBL == "MBL":
        if invoice_type == "revenue":
            for row in context.table:
                Pages.OIAccountingBillingBasedTab.MBL.revenue(int(row["No."])).currency_select.select(row["Currency"])
        elif invoice_type == "cost":
            for row in context.table:
                Pages.OIAccountingBillingBasedTab.MBL.cost(int(row["No."])).currency_select.select(row["Currency"])
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif MBL_or_HBL == "HBL":
        if invoice_type == "revenue":
            for row in context.table:
                Pages.OIAccountingBillingBasedTab.HBL.revenue(int(row["No."])).currency_select.select(row["Currency"])
        elif invoice_type == "cost":
            for row in context.table:
                Pages.OIAccountingBillingBasedTab.HBL.cost(int(row["No."])).currency_select.select(row["Currency"])
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    sleep(1)


@When("the user copys freights from OI {from_MBL_or_HBL} {from_invoice_type} to {to_MBL_or_HBL} {to_invoice_type}")
def step_impl(context, from_MBL_or_HBL, from_invoice_type, to_MBL_or_HBL, to_invoice_type):
    if from_MBL_or_HBL == "MBL":
        if from_invoice_type == "revenue":
            for row in context.table:
                Pages.OIAccountingBillingBasedTab.MBL.revenue(int(row["No."])).check_checkbox.tick(True)
            Pages.OIAccountingBillingBasedTab.MBL.revenue.copy_to_button.click()
        elif from_invoice_type == "cost":
            for row in context.table:
                Pages.OIAccountingBillingBasedTab.MBL.cost(int(row["No."])).check_checkbox.tick(True)
            Pages.OIAccountingBillingBasedTab.MBL.cost.copy_to_button.click()
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif from_MBL_or_HBL == "HBL":
        if from_invoice_type == "revenue":
            for row in context.table:
                Pages.OIAccountingBillingBasedTab.HBL.revenue(int(row["No."])).check_checkbox.tick(True)
            Pages.OIAccountingBillingBasedTab.HBL.revenue.copy_to_button.click()
        elif from_invoice_type == "cost":
            for row in context.table:
                Pages.OIAccountingBillingBasedTab.HBL.cost(int(row["No."])).check_checkbox.tick(True)
            Pages.OIAccountingBillingBasedTab.HBL.cost.copy_to_button.click()
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    sleep(1)

    if to_MBL_or_HBL == "MBL":
        if to_invoice_type == "revenue":
            Pages.OIAccountingBillingBasedTab.Common.copy_to_dropdown.MBL_revenue_checkbox.tick(True)
        elif to_invoice_type == "cost":
            Pages.OIAccountingBillingBasedTab.Common.copy_to_dropdown.MBL_cost_checkbox.tick(True)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif to_MBL_or_HBL == "HBL":
        if to_invoice_type == "revenue":
            Pages.OIAccountingBillingBasedTab.Common.copy_to_dropdown.HBL_revenue_checkbox.tick(True)
        elif to_invoice_type == "cost":
            Pages.OIAccountingBillingBasedTab.Common.copy_to_dropdown.HBL_cost_checkbox.tick(True)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)
    Pages.OIAccountingBillingBasedTab.Common.copy_to_dropdown.copy_button.click()
    sleep(5)


@When("the user input freights information to OI {MBL_or_HBL} {invoice_type}")
def step_impl(context, MBL_or_HBL, invoice_type):
    if MBL_or_HBL == "MBL":
        if invoice_type == "revenue":
            for row in context.table:
                Pages.OIAccountingBillingBasedTab.MBL.revenue(int(row["No."])).bill_to_autocomplete.input(
                    row["Bill to"]
                )
        elif invoice_type == "cost":
            for row in context.table:
                Pages.OIAccountingBillingBasedTab.MBL.cost(int(row["No."])).bill_to_autocomplete.input(row["Bill to"])
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif MBL_or_HBL == "HBL":
        if invoice_type == "revenue":
            for row in context.table:
                Pages.OIAccountingBillingBasedTab.HBL.revenue(int(row["No."])).bill_to_autocomplete.input(
                    row["Bill to"]
                )
        elif invoice_type == "cost":
            for row in context.table:
                Pages.OIAccountingBillingBasedTab.HBL.cost(int(row["No."])).bill_to_autocomplete.input(row["Bill to"])
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@When("the user clicks 'Action -> Print / Mail' to OI {MBL_or_HBL} {invoice_type}({index})")
def step_impl(context, MBL_or_HBL, invoice_type, index):
    if MBL_or_HBL == "MBL":
        if invoice_type == "revenue":
            Pages.OIAccountingBillingBasedTab.MBL.revenue(int(index)).action_button.click()
            Pages.OIAccountingBillingBasedTab.MBL.revenue(int(index)).action_print_mail_button.click()
        elif invoice_type == "cost":
            Pages.OIAccountingBillingBasedTab.MBL.cost(int(index)).action_button.click()
            Pages.OIAccountingBillingBasedTab.MBL.cost(int(index)).action_print_mail_button.click()
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif MBL_or_HBL == "HBL":
        if invoice_type == "revenue":
            Pages.OIAccountingBillingBasedTab.HBL.revenue(int(index)).action_button.click()
            Pages.OIAccountingBillingBasedTab.HBL.revenue(int(index)).action_print_mail_button.click()
        elif invoice_type == "cost":
            Pages.OIAccountingBillingBasedTab.HBL.cost(int(index)).action_button.click()
            Pages.OIAccountingBillingBasedTab.HBL.cost(int(index)).action_print_mail_button.click()
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    sleep(4)
    Driver.switch_to(window_name="Invoice Print")


@When("the user goes back to OI Shipment '{shipment_name}'")
def step_impl(context, shipment_name):
    Driver.open(context._vp.get("shipment_url")[shipment_name])
    Pages.Common.spin_bar.gone()


@Then("the {block_unblock} bottom in OI {MBL_or_HBL} {invoice_type}({index}) should be invisible")
def step_impl(context, block_unblock, MBL_or_HBL, invoice_type, index):
    if MBL_or_HBL == "MBL":
        if invoice_type == "revenue":
            Pages.OIAccountingBillingBasedTab.MBL.revenue(int(index)).action_button.click()
            if block_unblock == "block":
                assert (
                    Pages.OIAccountingBillingBasedTab.MBL.revenue(int(index)).action_block_button.is_visible() == False
                )
            elif block_unblock == "unblock":
                assert (
                    Pages.OIAccountingBillingBasedTab.MBL.revenue(int(index)).action_unblock_button.is_visible()
                    == False
                )
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
            Pages.OIAccountingBillingBasedTab.MBL.revenue(int(index)).action_button.click()
        elif invoice_type == "cost":
            Pages.OIAccountingBillingBasedTab.MBL.cost(int(index)).action_button.click()
            if block_unblock == "block":
                assert Pages.OIAccountingBillingBasedTab.MBL.cost(int(index)).action_block_button.is_visible() == False
            elif block_unblock == "unblock":
                assert (
                    Pages.OIAccountingBillingBasedTab.MBL.cost(int(index)).action_unblock_button.is_visible() == False
                )
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
            Pages.OIAccountingBillingBasedTab.MBL.cost(int(index)).action_button.click()
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif MBL_or_HBL == "HBL":
        if invoice_type == "revenue":
            Pages.OIAccountingBillingBasedTab.HBL.revenue(int(index)).action_button.click()
            if block_unblock == "block":
                assert (
                    Pages.OIAccountingBillingBasedTab.HBL.revenue(int(index)).action_block_button.is_visible() == False
                )
            elif block_unblock == "unblock":
                assert (
                    Pages.OIAccountingBillingBasedTab.HBL.revenue(int(index)).action_unblock_button.is_visible()
                    == False
                )
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
            Pages.OIAccountingBillingBasedTab.HBL.revenue(int(index)).action_button.click()
        elif invoice_type == "cost":
            Pages.OIAccountingBillingBasedTab.HBL.cost(int(index)).action_button.click()
            if block_unblock == "block":
                assert Pages.OIAccountingBillingBasedTab.HBL.cost(int(index)).action_block_button.is_visible() == False
            elif block_unblock == "unblock":
                assert (
                    Pages.OIAccountingBillingBasedTab.HBL.cost(int(index)).action_unblock_button.is_visible() == False
                )
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
            Pages.OIAccountingBillingBasedTab.HBL.cost(int(index)).action_button.click()
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@Then("The OI Accounting Billing Based page should show normally")
def step_impl(context):
    assert Pages.OIAccountingBillingBasedTab.MBL.revenue.new_button.is_visible()
    assert Pages.OIAccountingBillingBasedTab.MBL.revenue.new_five_button.is_visible()
    assert Pages.OIAccountingBillingBasedTab.MBL.revenue.add_multiple_button.is_visible()
    assert Pages.OIAccountingBillingBasedTab.MBL.revenue.copy_button.is_visible()
    assert Pages.OIAccountingBillingBasedTab.MBL.revenue.copy_to_button.is_visible()
    assert Pages.OIAccountingBillingBasedTab.MBL.revenue.delete_button.is_visible()
    assert Pages.OIAccountingBillingBasedTab.MBL.revenue.load_from_template_button.is_visible()
    assert Pages.OIAccountingBillingBasedTab.MBL.cost.new_button.is_visible()
    assert Pages.OIAccountingBillingBasedTab.MBL.cost.new_five_button.is_visible()
    assert Pages.OIAccountingBillingBasedTab.MBL.cost.add_multiple_button.is_visible()
    assert Pages.OIAccountingBillingBasedTab.MBL.cost.copy_button.is_visible()
    assert Pages.OIAccountingBillingBasedTab.MBL.cost.copy_to_button.is_visible()
    assert Pages.OIAccountingBillingBasedTab.MBL.cost.delete_button.is_visible()
    assert Pages.OIAccountingBillingBasedTab.MBL.cost.load_from_template_button.is_visible()
    assert Pages.OIAccountingBillingBasedTab.MBL.MBLAmount.include_draft_amount_checkbox.is_visible()
    assert Pages.OIAccountingBillingBasedTab.MBL.MBLAmount.mbl_amount_label.is_visible()
    assert Pages.OIAccountingBillingBasedTab.MBL.ShipmentProfit.profit_amount_label.is_visible()
    assert Pages.OIAccountingBillingBasedTab.MBL.tool_button.is_visible()
    assert Pages.OIAccountingBillingBasedTab.MBL.Memo.memo_title_button.is_visible()

    assert Pages.OIAccountingBillingBasedTab.HBL.revenue.new_button.is_visible()
    assert Pages.OIAccountingBillingBasedTab.HBL.revenue.new_five_button.is_visible()
    assert Pages.OIAccountingBillingBasedTab.HBL.revenue.add_multiple_button.is_visible()
    assert Pages.OIAccountingBillingBasedTab.HBL.revenue.copy_button.is_visible()
    assert Pages.OIAccountingBillingBasedTab.HBL.revenue.copy_to_button.is_visible()
    assert Pages.OIAccountingBillingBasedTab.HBL.revenue.delete_button.is_visible()
    assert Pages.OIAccountingBillingBasedTab.HBL.revenue.load_from_template_button.is_visible()
    assert Pages.OIAccountingBillingBasedTab.HBL.cost.new_button.is_visible()
    assert Pages.OIAccountingBillingBasedTab.HBL.cost.new_five_button.is_visible()
    assert Pages.OIAccountingBillingBasedTab.HBL.cost.add_multiple_button.is_visible()
    assert Pages.OIAccountingBillingBasedTab.HBL.cost.copy_button.is_visible()
    assert Pages.OIAccountingBillingBasedTab.HBL.cost.copy_to_button.is_visible()
    assert Pages.OIAccountingBillingBasedTab.HBL.cost.delete_button.is_visible()
    assert Pages.OIAccountingBillingBasedTab.HBL.cost.load_from_template_button.is_visible()
    assert Pages.OIAccountingBillingBasedTab.HBL.HBLAmount.hbl_amount_label.is_visible()
    assert Pages.OIAccountingBillingBasedTab.HBL.ShipmentProfit.profit_amount_label.is_visible()
    assert Pages.OIAccountingBillingBasedTab.HBL.tool_button.is_visible()
    assert Pages.OIAccountingBillingBasedTab.HBL.HBLAmount.include_draft_amount_checkbox.is_visible()
    assert Pages.OIAccountingBillingBasedTab.HBL.Memo.memo_title_button.is_visible()


@When("the user clicks save button in OI Accounting Billing Based")
def step_impl(context):
    if Pages.OIAccountingBillingBasedTab.save_button.is_enable():
        Pages.OIAccountingBillingBasedTab.save_button.click()
        Pages.Common.spin_bar.gone()
        sleep(2)
    else:
        Logger.getLogger().warning("The save button is not clickable")


@Then("the save button in OI shipment Accounting Billing Based should be disabled")
def step_impl(context):
    assert Pages.OIAccountingBillingBasedTab.save_button.is_disabled(), "The save button should be disabled"


@When("the user goes to OI {mbl_or_hbl:S} {invoice_type:S}({index:d})")
def step_impl(context, mbl_or_hbl, invoice_type, index):
    index_int = int(index)
    if mbl_or_hbl == "MBL" and invoice_type == "AR":
        Pages.OIAccountingInvoiceBasedTab.MBL.ar(index_int).reference_no_link.click()
    elif mbl_or_hbl == "MBL" and invoice_type == "DC":
        Pages.OIAccountingInvoiceBasedTab.MBL.dc(index_int).reference_no_link.click()
    elif mbl_or_hbl == "MBL" and invoice_type == "AP":
        Pages.OIAccountingInvoiceBasedTab.MBL.ap(index_int).reference_no_link.click()
    elif mbl_or_hbl == "HBL" and invoice_type == "AR":
        Pages.OIAccountingInvoiceBasedTab.HBL.ar(index_int).reference_no_link.click()
    elif mbl_or_hbl == "HBL" and invoice_type == "DC":
        Pages.OIAccountingInvoiceBasedTab.HBL.dc(index_int).reference_no_link.click()
    elif mbl_or_hbl == "HBL" and invoice_type == "AP":
        Pages.OIAccountingInvoiceBasedTab.HBL.ap(index_int).reference_no_link.click()
