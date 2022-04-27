from time import sleep

from behave import Then, When

import src.pages as Pages
from src.drivers.driver import Driver
from src.helper.log import Logger
from src.helper.transfer import transfer_data


@When("the user clicks OEVS {VS_or_BK_or_HBL} 'Create {payment_type}' button")
def step_impl(context, VS_or_BK_or_HBL, payment_type):
    sleep(3)
    if VS_or_BK_or_HBL == "VS":
        if payment_type == "AR":
            Pages.OEVSAccountingInvoiceBasedTab.VS.invoice_ar_button.click(timeout=10)
        elif payment_type == "DC":
            Pages.OEVSAccountingInvoiceBasedTab.VS.d_c_note_button.click(timeout=10)
        elif payment_type == "AP":
            Pages.OEVSAccountingInvoiceBasedTab.VS.ap_button.click(timeout=10)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif VS_or_BK_or_HBL == "BK":
        if payment_type == "AR":
            Pages.OEVSAccountingInvoiceBasedTab.BK.invoice_ar_button.click(timeout=10)
        elif payment_type == "DC":
            Pages.OEVSAccountingInvoiceBasedTab.BK.d_c_note_button.click(timeout=10)
        elif payment_type == "AP":
            Pages.OEVSAccountingInvoiceBasedTab.BK.ap_button.click(timeout=10)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif VS_or_BK_or_HBL == "HBL":
        if payment_type == "AR":
            Pages.OEVSAccountingInvoiceBasedTab.HBL.invoice_ar_button.click(timeout=10)
        elif payment_type == "DC":
            Pages.OEVSAccountingInvoiceBasedTab.HBL.d_c_note_button.click(timeout=10)
        elif payment_type == "AP":
            Pages.OEVSAccountingInvoiceBasedTab.HBL.ap_button.click(timeout=10)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    Pages.Common.spin_bar.gone()


@Then("the OEVS {VS_or_BK_or_HBL} amounts and profits should show correctly in Invoice Based")
def step_impl(context, VS_or_BK_or_HBL):
    sleep(5)

    if VS_or_BK_or_HBL == "VS":
        for row in context.table:
            assert Pages.OEVSAccountingInvoiceBasedTab.VS.total_revenue_label.get_value(timeout=10) == row["Revenue"]
            assert Pages.OEVSAccountingInvoiceBasedTab.VS.total_cost_label.get_value() == row["Cost"]
            assert Pages.OEVSAccountingInvoiceBasedTab.VS.total_balance_label.get_value() == row["Balance"]
            assert (
                Pages.OEVSAccountingInvoiceBasedTab.VS.total_profit_amount_label.get_value(timeout=10)
                == row["Total Profit Amount"]
            )
    elif VS_or_BK_or_HBL == "BK":
        for row in context.table:
            assert Pages.OEVSAccountingInvoiceBasedTab.BK.total_revenue_label.get_value(timeout=10) == row["Revenue"]
            assert Pages.OEVSAccountingInvoiceBasedTab.BK.total_cost_label.get_value() == row["Cost"]
            assert Pages.OEVSAccountingInvoiceBasedTab.BK.total_balance_label.get_value() == row["Balance"]
            assert (
                Pages.OEVSAccountingInvoiceBasedTab.BK.hbl_profit_amount_label.get_value(timeout=10)
                == row["HB/L Profit Amount"]
            )
    elif VS_or_BK_or_HBL == "HBL":
        for row in context.table:
            assert Pages.OEVSAccountingInvoiceBasedTab.HBL.total_revenue_label.get_value(timeout=10) == row["Revenue"]
            assert Pages.OEVSAccountingInvoiceBasedTab.HBL.total_cost_label.get_value() == row["Cost"]
            assert Pages.OEVSAccountingInvoiceBasedTab.HBL.total_balance_label.get_value() == row["Balance"]
            assert (
                Pages.OEVSAccountingInvoiceBasedTab.HBL.hbl_profit_amount_label.get_value(timeout=10)
                == row["HB/L Profit Amount"]
            )
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@Then("the OEVS {BK_or_HBL} amounts and profits should show correctly in Billing Based")
def step_impl(context, BK_or_HBL):
    if BK_or_HBL == "BK":
        for row in context.table:
            if "HB/L Revenue" in context.table.headings:
                data_in_field = Pages.OEVSAccountingBillingBasedTab.BK.HBLAmount.hbl_revenue_label.get_value()
                assert data_in_field == row["HB/L Revenue"]
            if "HB/L Cost" in context.table.headings:
                data_in_field = Pages.OEVSAccountingBillingBasedTab.BK.HBLAmount.hbl_cost_label.get_value()
                assert data_in_field == row["HB/L Cost"]
            if "HB/L Amount" in context.table.headings:
                data_in_field = Pages.OEVSAccountingBillingBasedTab.BK.HBLAmount.hbl_amount_label.get_value()
                assert data_in_field == row["HB/L Amount"]
            if "Profit Amount" in context.table.headings:
                data_in_field = Pages.OEVSAccountingBillingBasedTab.BK.ShipmentProfit.profit_amount_label.get_value()
                assert data_in_field == row["Profit Amount"]
    elif BK_or_HBL == "HBL":
        for row in context.table:
            if "HB/L Revenue" in context.table.headings:
                data_in_field = Pages.OEVSAccountingBillingBasedTab.HBL.HBLAmount.hbl_revenue_label.get_value()
                assert data_in_field == row["HB/L Revenue"]
            if "HB/L Cost" in context.table.headings:
                data_in_field = Pages.OEVSAccountingBillingBasedTab.HBL.HBLAmount.hbl_cost_label.get_value()
                assert data_in_field == row["HB/L Cost"]
            if "HB/L Amount" in context.table.headings:
                data_in_field = Pages.OEVSAccountingBillingBasedTab.HBL.HBLAmount.hbl_amount_label.get_value()
                assert data_in_field == row["HB/L Amount"]
            if "Profit Amount" in context.table.headings:
                data_in_field = Pages.OEVSAccountingBillingBasedTab.HBL.ShipmentProfit.profit_amount_label.get_value()
                assert data_in_field == row["Profit Amount"]
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@When("the user delete all freights in OEVS {BK_or_HBL} {invoice_type} Billing Based")
def step_impl(context, BK_or_HBL, invoice_type):
    # If empty_info is not visible, then click 'delete all' and delete all freights
    if BK_or_HBL == "BK":
        if (
            invoice_type == "revenue"
            and Pages.OEVSAccountingBillingBasedTab.BK.revenue.empty_info.is_visible(timeout=0) == False
        ):
            Pages.OEVSAccountingBillingBasedTab.BK.revenue.select_all_checkbox.tick(True)
            Pages.OEVSAccountingBillingBasedTab.BK.revenue.delete_button.click()
        elif (
            invoice_type == "cost"
            and Pages.OEVSAccountingBillingBasedTab.BK.cost.empty_info.is_visible(timeout=0) == False
        ):
            Pages.OEVSAccountingBillingBasedTab.BK.cost.select_all_checkbox.tick(True)
            Pages.OEVSAccountingBillingBasedTab.BK.cost.delete_button.click()
    elif BK_or_HBL == "HBL":
        if (
            invoice_type == "revenue"
            and Pages.OEVSAccountingBillingBasedTab.HBL.revenue.empty_info.is_visible(timeout=0) == False
        ):
            Pages.OEVSAccountingBillingBasedTab.HBL.revenue.select_all_checkbox.tick(True)
            Pages.OEVSAccountingBillingBasedTab.HBL.revenue.delete_button.click()
        elif (
            invoice_type == "cost"
            and Pages.OEVSAccountingBillingBasedTab.HBL.cost.empty_info.is_visible(timeout=0) == False
        ):
            Pages.OEVSAccountingBillingBasedTab.HBL.cost.select_all_checkbox.tick(True)
            Pages.OEVSAccountingBillingBasedTab.HBL.cost.delete_button.click()
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@Then("OEVS {VS_or_BK_or_HBL} has no invoice in {mode} Based")
def step_impl(context, VS_or_BK_or_HBL, mode):
    if mode == "Billing":
        if VS_or_BK_or_HBL == "BK":
            assert (
                Pages.OEVSAccountingBillingBasedTab.BK.revenue.empty_info.is_visible()
            ), "There are some BK revenue exist"
            assert Pages.OEVSAccountingBillingBasedTab.BK.cost.empty_info.is_visible(), "There are some BK cost exist"
        elif VS_or_BK_or_HBL == "HBL":
            assert (
                Pages.OEVSAccountingBillingBasedTab.HBL.revenue.empty_info.is_visible()
            ), "There are some HBL revenue exist"
            assert Pages.OEVSAccountingBillingBasedTab.HBL.cost.empty_info.is_visible(), "There are some HBL cost exist"
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif mode == "Invoice":
        if VS_or_BK_or_HBL == "VS":
            assert (
                Pages.OEVSAccountingInvoiceBasedTab.VS.ar(1).reference_no_link.is_visible(timeout=0) == False
            ), "There are some VS AR exist"
            assert (
                Pages.OEVSAccountingInvoiceBasedTab.VS.dc(1).reference_no_link.is_visible(timeout=0) == False
            ), "There are some VS DC exist"
            assert (
                Pages.OEVSAccountingInvoiceBasedTab.VS.ap(1).reference_no_link.is_visible(timeout=0) == False
            ), "There are some VS AP exist"
        elif VS_or_BK_or_HBL == "BK":
            assert (
                Pages.OEVSAccountingInvoiceBasedTab.BK.ar(1).reference_no_link.is_visible(timeout=0) == False
            ), "There are some BK AR exist"
            assert (
                Pages.OEVSAccountingInvoiceBasedTab.BK.dc(1).reference_no_link.is_visible(timeout=0) == False
            ), "There are some BK DC exist"
            assert (
                Pages.OEVSAccountingInvoiceBasedTab.BK.ap(1).reference_no_link.is_visible(timeout=0) == False
            ), "There are some BK AP exist"
        elif VS_or_BK_or_HBL == "HBL":
            assert (
                Pages.OEVSAccountingInvoiceBasedTab.HBL.ar(1).reference_no_link.is_visible(timeout=0) == False
            ), "There are some HBL AR exist"
            assert (
                Pages.OEVSAccountingInvoiceBasedTab.HBL.dc(1).reference_no_link.is_visible(timeout=0) == False
            ), "There are some HBL DC exist"
            assert (
                Pages.OEVSAccountingInvoiceBasedTab.HBL.ap(1).reference_no_link.is_visible(timeout=0) == False
            ), "There are some HBL AP exist"
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@When("the user {checks_unchecks} OEVS Accounting ({mode}) {VS_or_BK_or_HBL} 'Include Draft Amount' checkbox")
def step_impl(context, checks_unchecks, mode, VS_or_BK_or_HBL):
    if mode == "Billing Based":
        if VS_or_BK_or_HBL == "BK":
            if checks_unchecks == "checks":
                Pages.OEVSAccountingBillingBasedTab.BK.HBLAmount.include_draft_amount_checkbox.tick(True)
            elif checks_unchecks == "unchecks":
                Pages.OEVSAccountingBillingBasedTab.BK.HBLAmount.include_draft_amount_checkbox.tick(False)
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
        elif VS_or_BK_or_HBL == "HBL":
            if checks_unchecks == "checks":
                Pages.OEVSAccountingBillingBasedTab.HBL.HBLAmount.include_draft_amount_checkbox.tick(True)
            elif checks_unchecks == "unchecks":
                Pages.OEVSAccountingBillingBasedTab.HBL.HBLAmount.include_draft_amount_checkbox.tick(False)
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif mode == "Invoice Based":
        if VS_or_BK_or_HBL == "VS":
            if checks_unchecks == "checks":
                Pages.OEVSAccountingInvoiceBasedTab.VS.include_draft_amount_checkbox.tick(True)
            elif checks_unchecks == "unchecks":
                Pages.OEVSAccountingInvoiceBasedTab.VS.include_draft_amount_checkbox.tick(False)
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
        elif VS_or_BK_or_HBL == "BK":
            if checks_unchecks == "checks":
                Pages.OEVSAccountingInvoiceBasedTab.BK.include_draft_amount_checkbox.tick(True)
            elif checks_unchecks == "unchecks":
                Pages.OEVSAccountingInvoiceBasedTab.BK.include_draft_amount_checkbox.tick(False)
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
        elif VS_or_BK_or_HBL == "HBL":
            if checks_unchecks == "checks":
                Pages.OEVSAccountingInvoiceBasedTab.HBL.include_draft_amount_checkbox.tick(True)
            elif checks_unchecks == "unchecks":
                Pages.OEVSAccountingInvoiceBasedTab.HBL.include_draft_amount_checkbox.tick(False)
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@When("the user blocks OEVS {BK_or_HBL} revenue({index}) in Accounting Billing Based")
def step_impl(context, BK_or_HBL, index):
    sleep(3)
    if BK_or_HBL == "BK":
        Pages.OEVSAccountingBillingBasedTab.BK.revenue(index=index).action_button.click()
        Pages.OEVSAccountingBillingBasedTab.BK.revenue(index=index).action_block_button.click()
    elif BK_or_HBL == "HBL":
        Pages.OEVSAccountingBillingBasedTab.HBL.revenue(index=index).action_button.click()
        Pages.OEVSAccountingBillingBasedTab.HBL.revenue(index=index).action_block_button.click()
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    Pages.Common.spin_bar.gone()


@Then("OEVS {BK_or_HBL} {invoice_type} listed below should be uneditable in Accounting Billing Based")
def step_impl(context, BK_or_HBL, invoice_type):
    if BK_or_HBL == "BK":
        if invoice_type == "revenues":
            for row in context.table:
                index = int(row["No."])
                assert Pages.OEVSAccountingBillingBasedTab.BK.revenue(index=index).bill_to_autocomplete.is_disabled(
                    timeout=0
                )
                assert Pages.OEVSAccountingBillingBasedTab.BK.revenue(
                    index=index
                ).freight_code_autocomplete.is_disabled(timeout=0)
                assert Pages.OEVSAccountingBillingBasedTab.BK.revenue(
                    index=index
                ).freight_description_input.is_disabled(timeout=0)
                assert Pages.OEVSAccountingBillingBasedTab.BK.revenue(index=index).p_c_select.is_disabled(timeout=0)
                assert Pages.OEVSAccountingBillingBasedTab.BK.revenue(index=index).unit_select.is_disabled(timeout=0)
                assert Pages.OEVSAccountingBillingBasedTab.BK.revenue(index=index).currency_select.is_disabled(
                    timeout=0
                )
                assert Pages.OEVSAccountingBillingBasedTab.BK.revenue(index=index).vol_input.is_disabled(timeout=0)
                assert Pages.OEVSAccountingBillingBasedTab.BK.revenue(index=index).rate_input.is_disabled(timeout=0)
                assert Pages.OEVSAccountingBillingBasedTab.BK.revenue(index=index).amount_input.is_disabled(timeout=0)
                assert Pages.OEVSAccountingBillingBasedTab.BK.revenue(index=index).invoice_no_autocomplete.is_disabled(
                    timeout=0
                )
        elif invoice_type == "costs":
            for row in context.table:
                index = int(row["No."])
                assert Pages.OEVSAccountingBillingBasedTab.BK.cost(index=index).bill_to_autocomplete.is_disabled(
                    timeout=0
                )
                assert Pages.OEVSAccountingBillingBasedTab.BK.cost(index=index).freight_code_autocomplete.is_disabled(
                    timeout=0
                )
                assert Pages.OEVSAccountingBillingBasedTab.BK.cost(index=index).freight_description_input.is_disabled(
                    timeout=0
                )
                assert Pages.OEVSAccountingBillingBasedTab.BK.cost(index=index).p_c_select.is_disabled(timeout=0)
                assert Pages.OEVSAccountingBillingBasedTab.BK.cost(index=index).unit_select.is_disabled(timeout=0)
                assert Pages.OEVSAccountingBillingBasedTab.BK.cost(index=index).currency_select.is_disabled(timeout=0)
                assert Pages.OEVSAccountingBillingBasedTab.BK.cost(index=index).vol_input.is_disabled(timeout=0)
                assert Pages.OEVSAccountingBillingBasedTab.BK.cost(index=index).rate_input.is_disabled(timeout=0)
                assert Pages.OEVSAccountingBillingBasedTab.BK.cost(index=index).amount_input.is_disabled(timeout=0)
                assert Pages.OEVSAccountingBillingBasedTab.BK.cost(
                    index=index
                ).vendor_invoice_no_autocomplete.is_disabled(timeout=0)
    elif BK_or_HBL == "HBL":
        if invoice_type == "revenues":
            for row in context.table:
                index = int(row["No."])
                assert Pages.OEVSAccountingBillingBasedTab.HBL.revenue(index=index).bill_to_autocomplete.is_disabled(
                    timeout=0
                )
                assert Pages.OEVSAccountingBillingBasedTab.HBL.revenue(
                    index=index
                ).freight_code_autocomplete.is_disabled(timeout=0)
                assert Pages.OEVSAccountingBillingBasedTab.HBL.revenue(
                    index=index
                ).freight_description_input.is_disabled(timeout=0)
                assert Pages.OEVSAccountingBillingBasedTab.HBL.revenue(index=index).p_c_select.is_disabled(timeout=0)
                assert Pages.OEVSAccountingBillingBasedTab.HBL.revenue(index=index).unit_select.is_disabled(timeout=0)
                assert Pages.OEVSAccountingBillingBasedTab.HBL.revenue(index=index).currency_select.is_disabled(
                    timeout=0
                )
                assert Pages.OEVSAccountingBillingBasedTab.HBL.revenue(index=index).vol_input.is_disabled(timeout=0)
                assert Pages.OEVSAccountingBillingBasedTab.HBL.revenue(index=index).rate_input.is_disabled(timeout=0)
                assert Pages.OEVSAccountingBillingBasedTab.HBL.revenue(index=index).amount_input.is_disabled(timeout=0)
                assert Pages.OEVSAccountingBillingBasedTab.HBL.revenue(index=index).invoice_no_autocomplete.is_disabled(
                    timeout=0
                )
        elif invoice_type == "costs":
            for row in context.table:
                index = int(row["No."])
                assert Pages.OEVSAccountingBillingBasedTab.HBL.cost(index=index).bill_to_autocomplete.is_disabled(
                    timeout=0
                )
                assert Pages.OEVSAccountingBillingBasedTab.HBL.cost(index=index).freight_code_autocomplete.is_disabled(
                    timeout=0
                )
                assert Pages.OEVSAccountingBillingBasedTab.HBL.cost(index=index).freight_description_input.is_disabled(
                    timeout=0
                )
                assert Pages.OEVSAccountingBillingBasedTab.HBL.cost(index=index).p_c_select.is_disabled(timeout=0)
                assert Pages.OEVSAccountingBillingBasedTab.HBL.cost(index=index).unit_select.is_disabled(timeout=0)
                assert Pages.OEVSAccountingBillingBasedTab.HBL.cost(index=index).currency_select.is_disabled(timeout=0)
                assert Pages.OEVSAccountingBillingBasedTab.HBL.cost(index=index).vol_input.is_disabled(timeout=0)
                assert Pages.OEVSAccountingBillingBasedTab.HBL.cost(index=index).rate_input.is_disabled(timeout=0)
                assert Pages.OEVSAccountingBillingBasedTab.HBL.cost(index=index).amount_input.is_disabled(timeout=0)
                assert Pages.OEVSAccountingBillingBasedTab.HBL.cost(
                    index=index
                ).vendor_invoice_no_autocomplete.is_disabled(timeout=0)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@When("the user adds freights to OEVS {VS_or_BK_or_HBL} {revenue_cost}")
def step_impl(context, VS_or_BK_or_HBL, revenue_cost):
    if VS_or_BK_or_HBL == "VS":
        if revenue_cost == "revenue":
            freight_index = Pages.OEVSAccountingBillingBasedTab.VS.revenue.get_len() + 1

            for row in context.table:
                Pages.OEVSAccountingBillingBasedTab.VS.revenue.new_button.click()
                sleep(1)
                Pages.OEVSAccountingBillingBasedTab.VS.revenue(freight_index).bill_to_autocomplete.input(
                    transfer_data(row["Bill to"])
                )
                Pages.OEVSAccountingBillingBasedTab.VS.revenue(freight_index).freight_code_autocomplete.input(
                    row["Freight code"]
                )
                Pages.OEVSAccountingBillingBasedTab.VS.revenue(freight_index).vol_input.input(row["Volume"])
                Pages.OEVSAccountingBillingBasedTab.VS.revenue(freight_index).rate_input.input(row["Rate"])
                freight_index += 1
        elif revenue_cost == "cost":
            freight_index = Pages.OEVSAccountingBillingBasedTab.VS.cost.get_len() + 1

            for row in context.table:
                Pages.OEVSAccountingBillingBasedTab.VS.cost.new_button.click()
                sleep(1)
                Pages.OEVSAccountingBillingBasedTab.VS.cost(freight_index).bill_to_autocomplete.input(
                    transfer_data(row["Bill to"])
                )
                Pages.OEVSAccountingBillingBasedTab.VS.cost(freight_index).freight_code_autocomplete.input(
                    row["Freight code"]
                )
                Pages.OEVSAccountingBillingBasedTab.VS.cost(freight_index).vol_input.input(row["Volume"])
                Pages.OEVSAccountingBillingBasedTab.VS.cost(freight_index).rate_input.input(row["Rate"])
                freight_index += 1
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif VS_or_BK_or_HBL == "BK":
        if revenue_cost == "revenue":
            freight_index = Pages.OEVSAccountingBillingBasedTab.BK.revenue.get_len() + 1

            for row in context.table:
                Pages.OEVSAccountingBillingBasedTab.BK.revenue.new_button.click()
                sleep(1)
                Pages.OEVSAccountingBillingBasedTab.BK.revenue(freight_index).bill_to_autocomplete.input(
                    transfer_data(row["Bill to"])
                )
                Pages.OEVSAccountingBillingBasedTab.BK.revenue(freight_index).freight_code_autocomplete.input(
                    row["Freight code"]
                )
                Pages.OEVSAccountingBillingBasedTab.BK.revenue(freight_index).vol_input.input(row["Volume"])
                Pages.OEVSAccountingBillingBasedTab.BK.revenue(freight_index).rate_input.input(row["Rate"])
                freight_index += 1
        elif revenue_cost == "cost":
            freight_index = Pages.OEVSAccountingBillingBasedTab.BK.cost.get_len() + 1

            for row in context.table:
                Pages.OEVSAccountingBillingBasedTab.BK.cost.new_button.click()
                sleep(1)
                Pages.OEVSAccountingBillingBasedTab.BK.cost(freight_index).bill_to_autocomplete.input(
                    transfer_data(row["Bill to"])
                )
                Pages.OEVSAccountingBillingBasedTab.BK.cost(freight_index).freight_code_autocomplete.input(
                    row["Freight code"]
                )
                Pages.OEVSAccountingBillingBasedTab.BK.cost(freight_index).vol_input.input(row["Volume"])
                Pages.OEVSAccountingBillingBasedTab.BK.cost(freight_index).rate_input.input(row["Rate"])
                freight_index += 1
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif VS_or_BK_or_HBL == "HBL":
        if revenue_cost == "revenue":
            freight_index = Pages.OEVSAccountingBillingBasedTab.HBL.revenue.get_len() + 1

            for row in context.table:
                Pages.OEVSAccountingBillingBasedTab.HBL.revenue.new_button.click()
                Pages.OEVSAccountingBillingBasedTab.HBL.revenue(freight_index).bill_to_autocomplete.input(
                    transfer_data(row["Bill to"])
                )
                Pages.OEVSAccountingBillingBasedTab.HBL.revenue(freight_index).freight_code_autocomplete.input(
                    row["Freight code"]
                )
                Pages.OEVSAccountingBillingBasedTab.HBL.revenue(freight_index).vol_input.input(row["Volume"])
                Pages.OEVSAccountingBillingBasedTab.HBL.revenue(freight_index).rate_input.input(row["Rate"])
                freight_index += 1
        elif revenue_cost == "cost":
            freight_index = Pages.OEVSAccountingBillingBasedTab.HBL.cost.get_len() + 1

            for row in context.table:
                Pages.OEVSAccountingBillingBasedTab.HBL.cost.new_button.click()
                Pages.OEVSAccountingBillingBasedTab.HBL.cost(freight_index).bill_to_autocomplete.input(
                    transfer_data(row["Bill to"])
                )
                Pages.OEVSAccountingBillingBasedTab.HBL.cost(freight_index).freight_code_autocomplete.input(
                    row["Freight code"]
                )
                Pages.OEVSAccountingBillingBasedTab.HBL.cost(freight_index).vol_input.input(row["Volume"])
                Pages.OEVSAccountingBillingBasedTab.HBL.cost(freight_index).rate_input.input(row["Rate"])
                freight_index += 1
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@Then("values in OEVS {VS_or_BK_or_HBL} {revenue_cost} should be correct")
def step_impl(context, VS_or_BK_or_HBL, revenue_cost):
    if VS_or_BK_or_HBL == "VS":
        if revenue_cost == "revenue":
            for row in context.table:
                if "Currency" in context.table.headings and row["Currency"]:
                    answer = row["Currency"]
                    real_value = Pages.OEVSAccountingBillingBasedTab.VS.revenue(
                        int(row["No."])
                    ).currency_select.get_value()
                    assert answer == real_value, "The currency in VS revenue No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
                if "Amount" in context.table.headings and row["Amount"]:
                    answer = row["Amount"]
                    real_value = Pages.OEVSAccountingBillingBasedTab.VS.revenue(int(row["No."])).amount_input.get_value(
                        timeout=1
                    )
                    assert answer == real_value, "The amount in VS revenue No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
        elif revenue_cost == "cost":
            for row in context.table:
                if "Currency" in context.table.headings and row["Currency"]:
                    answer = row["Currency"]
                    real_value = Pages.OEVSAccountingBillingBasedTab.VS.cost(
                        int(row["No."])
                    ).currency_select.get_value()
                    assert answer == real_value, "The currency in VS cost No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
                if "Amount" in context.table.headings and row["Amount"]:
                    answer = row["Amount"]
                    real_value = Pages.OEVSAccountingBillingBasedTab.VS.cost(int(row["No."])).amount_input.get_value(
                        timeout=1
                    )
                    assert answer == real_value, "The amount in VS cost No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif VS_or_BK_or_HBL == "BK":
        if revenue_cost == "revenue":
            for row in context.table:
                if "Currency" in context.table.headings and row["Currency"]:
                    answer = row["Currency"]
                    real_value = Pages.OEVSAccountingBillingBasedTab.BK.revenue(
                        int(row["No."])
                    ).currency_select.get_value()
                    assert answer == real_value, "The currency in BK revenue No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
                if "Amount" in context.table.headings and row["Amount"]:
                    answer = row["Amount"]
                    real_value = Pages.OEVSAccountingBillingBasedTab.BK.revenue(int(row["No."])).amount_input.get_value(
                        timeout=1
                    )
                    assert answer == real_value, "The amount in BK revenue No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
        elif revenue_cost == "cost":
            for row in context.table:
                if "Currency" in context.table.headings and row["Currency"]:
                    answer = row["Currency"]
                    real_value = Pages.OEVSAccountingBillingBasedTab.BK.cost(
                        int(row["No."])
                    ).currency_select.get_value()
                    assert answer == real_value, "The currency in BK cost No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
                if "Amount" in context.table.headings and row["Amount"]:
                    answer = row["Amount"]
                    real_value = Pages.OEVSAccountingBillingBasedTab.BK.cost(int(row["No."])).amount_input.get_value(
                        timeout=1
                    )
                    assert answer == real_value, "The amount in BK cost No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
                if "Cost Share" in context.table.headings and row["Cost Share"]:
                    answer = row["Cost Share"] == r"{on}"
                    real_value = Pages.OEVSAccountingBillingBasedTab.BK.cost(
                        int(row["No."])
                    ).cost_share_checkbox.get_value()
                    assert answer == real_value, "The cost share in BK cost No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif VS_or_BK_or_HBL == "HBL":
        if revenue_cost == "revenue":
            for row in context.table:
                if "Currency" in context.table.headings and row["Currency"]:
                    answer = row["Currency"]
                    real_value = Pages.OEVSAccountingBillingBasedTab.HBL.revenue(
                        int(row["No."])
                    ).currency_select.get_value()
                    assert answer == real_value, "The amount in HBL revenue No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
                if "Amount" in context.table.headings and row["Amount"]:
                    answer = row["Amount"]
                    real_value = Pages.OEVSAccountingBillingBasedTab.HBL.revenue(
                        int(row["No."])
                    ).amount_input.get_value(timeout=0)
                    assert answer == real_value, "The amount in HBL revenue No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
        elif revenue_cost == "cost":
            for row in context.table:
                if "Currency" in context.table.headings and row["Currency"]:
                    answer = row["Currency"]
                    real_value = Pages.OEVSAccountingBillingBasedTab.HBL.cost(
                        int(row["No."])
                    ).currency_select.get_value()
                    assert answer == real_value, "The amount in HBL cost No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
                if "Amount" in context.table.headings and row["Amount"]:
                    answer = row["Amount"]
                    real_value = Pages.OEVSAccountingBillingBasedTab.HBL.cost(int(row["No."])).amount_input.get_value(
                        timeout=0
                    )
                    assert answer == real_value, "The amount in HBL cost No. {0} should be {1}, but {2} now".format(
                        row["No."], answer, real_value
                    )
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@When("the user deletes freights in OEVS {VS_or_BK_or_HBL} {invoice_type}")
def step_impl(context, VS_or_BK_or_HBL, invoice_type):
    if VS_or_BK_or_HBL == "VS":
        if invoice_type == "revenue":
            for row in context.table:
                Pages.OEVSAccountingBillingBasedTab.VS.revenue(int(row["No."])).check_checkbox.tick(True)
            Pages.OEVSAccountingBillingBasedTab.VS.revenue.delete_button.click()
        elif invoice_type == "cost":
            for row in context.table:
                Pages.OEVSAccountingBillingBasedTab.VS.cost(int(row["No."])).check_checkbox.tick(True)
            Pages.OEVSAccountingBillingBasedTab.VS.cost.delete_button.click()
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif VS_or_BK_or_HBL == "BK":
        if invoice_type == "revenue":
            for row in context.table:
                Pages.OEVSAccountingBillingBasedTab.BK.revenue(int(row["No."])).check_checkbox.tick(True)
            Pages.OEVSAccountingBillingBasedTab.BK.revenue.delete_button.click()
        elif invoice_type == "cost":
            for row in context.table:
                Pages.OEVSAccountingBillingBasedTab.BK.cost(int(row["No."])).check_checkbox.tick(True)
            Pages.OEVSAccountingBillingBasedTab.BK.cost.delete_button.click()
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif VS_or_BK_or_HBL == "HBL":
        if invoice_type == "revenue":
            for row in context.table:
                Pages.OEVSAccountingBillingBasedTab.HBL.revenue(int(row["No."])).check_checkbox.tick(True)
            Pages.OEVSAccountingBillingBasedTab.HBL.revenue.delete_button.click()
        elif invoice_type == "cost":
            for row in context.table:
                Pages.OEVSAccountingBillingBasedTab.HBL.cost(int(row["No."])).check_checkbox.tick(True)
            Pages.OEVSAccountingBillingBasedTab.HBL.cost.delete_button.click()
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    sleep(1)


@When("the user changes currency of freights in OEVS {VS_or_BK_or_HBL} {invoice_type}")
def step_impl(context, VS_or_BK_or_HBL, invoice_type):
    if VS_or_BK_or_HBL == "VS":
        if invoice_type == "revenue":
            for row in context.table:
                Pages.OEVSAccountingBillingBasedTab.VS.revenue(int(row["No."])).currency_select.select(row["Currency"])
        elif invoice_type == "cost":
            for row in context.table:
                Pages.OEVSAccountingBillingBasedTab.VS.cost(int(row["No."])).currency_select.select(row["Currency"])
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif VS_or_BK_or_HBL == "BK":
        if invoice_type == "revenue":
            for row in context.table:
                Pages.OEVSAccountingBillingBasedTab.BK.revenue(int(row["No."])).currency_select.select(row["Currency"])
        elif invoice_type == "cost":
            for row in context.table:
                Pages.OEVSAccountingBillingBasedTab.BK.cost(int(row["No."])).currency_select.select(row["Currency"])
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif VS_or_BK_or_HBL == "HBL":
        if invoice_type == "revenue":
            for row in context.table:
                Pages.OEVSAccountingBillingBasedTab.HBL.revenue(int(row["No."])).currency_select.select(row["Currency"])
        elif invoice_type == "cost":
            for row in context.table:
                Pages.OEVSAccountingBillingBasedTab.HBL.cost(int(row["No."])).currency_select.select(row["Currency"])
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    sleep(1)


@When("the user copys freights from OEVS BK {from_invoice_type} to BK {to_invoice_type}")
def step_impl(context, from_invoice_type, to_invoice_type):
    if from_invoice_type == "revenue":
        for row in context.table:
            Pages.OEVSAccountingBillingBasedTab.BK.revenue(int(row["No."])).check_checkbox.tick(True)
        Pages.OEVSAccountingBillingBasedTab.BK.revenue.copy_to_button.click()
    elif from_invoice_type == "cost":
        for row in context.table:
            Pages.OEVSAccountingBillingBasedTab.BK.cost(int(row["No."])).check_checkbox.tick(True)
        Pages.OEVSAccountingBillingBasedTab.BK.cost.copy_to_button.click()
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    sleep(1)

    if to_invoice_type == "revenue":
        Pages.OEVSAccountingBillingBasedTab.Common.copy_to_dropdown.HBL_revenue_checkbox.tick(True)
    elif to_invoice_type == "cost":
        Pages.OEVSAccountingBillingBasedTab.Common.copy_to_dropdown.HBL_cost_checkbox.tick(True)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)
    Pages.OEVSAccountingBillingBasedTab.Common.copy_to_dropdown.copy_button.click()
    sleep(5)


@When("the user copys freights from OEVS HBL {from_invoice_type} to HBL {to_invoice_type}")
def step_impl(context, from_invoice_type, to_invoice_type):
    if from_invoice_type == "revenue":
        for row in context.table:
            Pages.OEVSAccountingBillingBasedTab.HBL.revenue(int(row["No."])).check_checkbox.tick(True)
        Pages.OEVSAccountingBillingBasedTab.HBL.revenue.copy_to_button.click()
    elif from_invoice_type == "cost":
        for row in context.table:
            Pages.OEVSAccountingBillingBasedTab.HBL.cost(int(row["No."])).check_checkbox.tick(True)
        Pages.OEVSAccountingBillingBasedTab.HBL.cost.copy_to_button.click()
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    sleep(1)

    if to_invoice_type == "revenue":
        Pages.OEVSAccountingBillingBasedTab.Common.copy_to_dropdown.HBL_revenue_checkbox.tick(True)
    elif to_invoice_type == "cost":
        Pages.OEVSAccountingBillingBasedTab.Common.copy_to_dropdown.HBL_cost_checkbox.tick(True)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)
    Pages.OEVSAccountingBillingBasedTab.Common.copy_to_dropdown.copy_button.click()
    sleep(5)


@When("the user input freights information to OEVS {VS_or_BK_or_HBL} {invoice_type}")
def step_impl(context, VS_or_BK_or_HBL, invoice_type):
    if VS_or_BK_or_HBL == "VS":
        if invoice_type == "revenue":
            for row in context.table:
                index = int(row["No."])
                if "Bill to" in context.table.headings:
                    Pages.OEVSAccountingBillingBasedTab.VS.revenue(index).bill_to_autocomplete.input(row["Bill to"])
        elif invoice_type == "cost":
            for row in context.table:
                index = int(row["No."])
                if "Bill to" in context.table.headings:
                    Pages.OEVSAccountingBillingBasedTab.VS.cost(index).bill_to_autocomplete.input(row["Bill to"])
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif VS_or_BK_or_HBL == "BK":
        if invoice_type == "revenue":
            for row in context.table:
                index = int(row["No."])
                if "Bill to" in context.table.headings:
                    Pages.OEVSAccountingBillingBasedTab.BK.revenue(index).bill_to_autocomplete.input(row["Bill to"])
        elif invoice_type == "cost":
            for row in context.table:
                index = int(row["No."])
                if "Bill to" in context.table.headings:
                    Pages.OEVSAccountingBillingBasedTab.BK.cost(index).bill_to_autocomplete.input(row["Bill to"])
                if "Cost Share" in context.table.headings:
                    input_data = transfer_data(row["Cost Share"])
                    Pages.OEVSAccountingBillingBasedTab.BK.cost(index).cost_share_checkbox.tick(input_data)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif VS_or_BK_or_HBL == "HBL":
        if invoice_type == "revenue":
            for row in context.table:
                index = int(row["No."])
                if "Bill to" in context.table.headings:
                    Pages.OEVSAccountingBillingBasedTab.HBL.revenue(index).bill_to_autocomplete.input(row["Bill to"])
        elif invoice_type == "cost":
            for row in context.table:
                index = int(row["No."])
                if "Bill to" in context.table.headings:
                    Pages.OEVSAccountingBillingBasedTab.HBL.cost(index).bill_to_autocomplete.input(row["Bill to"])
                if "Cost Share" in context.table.headings:
                    input_data = transfer_data(row["Cost Share"])
                    Pages.OEVSAccountingBillingBasedTab.HBL.cost(index).cost_share_checkbox.tick(input_data)
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@When("the user clicks 'Action -> Print / Mail' to OEVS {VS_or_BK_or_HBL} {invoice_type}({index})")
def step_impl(context, VS_or_BK_or_HBL, invoice_type, index):
    if VS_or_BK_or_HBL == "VS":
        if invoice_type == "revenue":
            Pages.OEVSAccountingBillingBasedTab.VS.revenue(int(index)).action_button.click()
            Pages.OEVSAccountingBillingBasedTab.VS.revenue(int(index)).action_print_mail_button.click()
        elif invoice_type == "cost":
            Pages.OEVSAccountingBillingBasedTab.VS.cost(int(index)).action_button.click()
            Pages.OEVSAccountingBillingBasedTab.VS.cost(int(index)).action_print_mail_button.click()
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif VS_or_BK_or_HBL == "BK":
        if invoice_type == "revenue":
            Pages.OEVSAccountingBillingBasedTab.BK.revenue(int(index)).action_button.click()
            Pages.OEVSAccountingBillingBasedTab.BK.revenue(int(index)).action_print_mail_button.click()
        elif invoice_type == "cost":
            Pages.OEVSAccountingBillingBasedTab.BK.cost(int(index)).action_button.click()
            Pages.OEVSAccountingBillingBasedTab.BK.cost(int(index)).action_print_mail_button.click()
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif VS_or_BK_or_HBL == "HBL":
        if invoice_type == "revenue":
            Pages.OEVSAccountingBillingBasedTab.HBL.revenue(int(index)).action_button.click()
            Pages.OEVSAccountingBillingBasedTab.HBL.revenue(int(index)).action_print_mail_button.click()
        elif invoice_type == "cost":
            Pages.OEVSAccountingBillingBasedTab.HBL.cost(int(index)).action_button.click()
            Pages.OEVSAccountingBillingBasedTab.HBL.cost(int(index)).action_print_mail_button.click()
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)

    sleep(4)
    Driver.switch_to(window_name="Invoice Print")


@When("the user goes back to OEVS Shipment '{shipment_name}'")
def step_impl(context, shipment_name):
    Driver.open(context._vp.get("shipment_url")[shipment_name])
    Pages.Common.spin_bar.gone()


@Then("the {block_unblock} bottom in OEVS {VS_or_BK_or_HBL} {invoice_type}({index}) should be invisible")
def step_impl(context, block_unblock, VS_or_BK_or_HBL, invoice_type, index):
    if VS_or_BK_or_HBL == "VS":
        if invoice_type == "revenue":
            Pages.OEVSAccountingBillingBasedTab.VS.revenue(int(index)).action_button.click()
            if block_unblock == "block":
                assert (
                    Pages.OEVSAccountingBillingBasedTab.VS.revenue(int(index)).action_block_button.is_visible() == False
                )
            elif block_unblock == "unblock":
                assert (
                    Pages.OEVSAccountingBillingBasedTab.VS.revenue(int(index)).action_unblock_button.is_visible()
                    == False
                )
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
            Pages.OEVSAccountingBillingBasedTab.VS.revenue(int(index)).action_button.click()
        elif invoice_type == "cost":
            Pages.OEVSAccountingBillingBasedTab.VS.cost(int(index)).action_button.click()
            if block_unblock == "block":
                assert Pages.OEVSAccountingBillingBasedTab.VS.cost(int(index)).action_block_button.is_visible() == False
            elif block_unblock == "unblock":
                assert (
                    Pages.OEVSAccountingBillingBasedTab.VS.cost(int(index)).action_unblock_button.is_visible() == False
                )
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
            Pages.OEVSAccountingBillingBasedTab.VS.cost(int(index)).action_button.click()
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif VS_or_BK_or_HBL == "BK":
        if invoice_type == "revenue":
            Pages.OEVSAccountingBillingBasedTab.BK.revenue(int(index)).action_button.click()
            if block_unblock == "block":
                assert (
                    Pages.OEVSAccountingBillingBasedTab.BK.revenue(int(index)).action_block_button.is_visible() == False
                )
            elif block_unblock == "unblock":
                assert (
                    Pages.OEVSAccountingBillingBasedTab.BK.revenue(int(index)).action_unblock_button.is_visible()
                    == False
                )
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
            Pages.OEVSAccountingBillingBasedTab.BK.revenue(int(index)).action_button.click()
        elif invoice_type == "cost":
            Pages.OEVSAccountingBillingBasedTab.BK.cost(int(index)).action_button.click()
            if block_unblock == "block":
                assert Pages.OEVSAccountingBillingBasedTab.BK.cost(int(index)).action_block_button.is_visible() == False
            elif block_unblock == "unblock":
                assert (
                    Pages.OEVSAccountingBillingBasedTab.BK.cost(int(index)).action_unblock_button.is_visible() == False
                )
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
            Pages.OEVSAccountingBillingBasedTab.BK.cost(int(index)).action_button.click()
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    elif VS_or_BK_or_HBL == "HBL":
        if invoice_type == "revenue":
            Pages.OEVSAccountingBillingBasedTab.HBL.revenue(int(index)).action_button.click()
            if block_unblock == "block":
                assert (
                    Pages.OEVSAccountingBillingBasedTab.HBL.revenue(int(index)).action_block_button.is_visible()
                    == False
                )
            elif block_unblock == "unblock":
                assert (
                    Pages.OEVSAccountingBillingBasedTab.HBL.revenue(int(index)).action_unblock_button.is_visible()
                    == False
                )
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
            Pages.OEVSAccountingBillingBasedTab.HBL.revenue(int(index)).action_button.click()
        elif invoice_type == "cost":
            Pages.OEVSAccountingBillingBasedTab.HBL.cost(int(index)).action_button.click()
            if block_unblock == "block":
                assert (
                    Pages.OEVSAccountingBillingBasedTab.HBL.cost(int(index)).action_block_button.is_visible() == False
                )
            elif block_unblock == "unblock":
                assert (
                    Pages.OEVSAccountingBillingBasedTab.HBL.cost(int(index)).action_unblock_button.is_visible() == False
                )
            else:
                assert False, "Syntax Error: {0}".format(context.step_name)
            Pages.OEVSAccountingBillingBasedTab.HBL.cost(int(index)).action_button.click()
        else:
            assert False, "Syntax Error: {0}".format(context.step_name)
    else:
        assert False, "Syntax Error: {0}".format(context.step_name)


@Then("The OEVS plus BK Accounting Billing Based page should show normally")
def step_impl(context):
    assert Pages.OEVSAccountingBillingBasedTab.BK.revenue.new_button.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.BK.revenue.new_five_button.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.BK.revenue.add_multiple_button.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.BK.revenue.copy_button.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.BK.revenue.copy_to_button.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.BK.revenue.delete_button.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.BK.revenue.load_from_template_button.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.BK.cost.new_button.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.BK.cost.new_five_button.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.BK.cost.add_multiple_button.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.BK.cost.copy_button.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.BK.cost.copy_to_button.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.BK.cost.delete_button.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.BK.cost.load_from_template_button.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.BK.HBLAmount.hbl_amount_label.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.BK.ShipmentProfit.profit_amount_label.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.BK.tool_button.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.BK.HBLAmount.include_draft_amount_checkbox.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.BK.Memo.memo_title_button.is_visible()


@Then("The OEVS plus HBL Accounting Billing Based page should show normally")
def step_impl(context):
    assert Pages.OEVSAccountingBillingBasedTab.HBL.revenue.new_button.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.HBL.revenue.new_five_button.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.HBL.revenue.add_multiple_button.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.HBL.revenue.copy_button.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.HBL.revenue.copy_to_button.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.HBL.revenue.delete_button.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.HBL.revenue.load_from_template_button.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.HBL.cost.new_button.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.HBL.cost.new_five_button.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.HBL.cost.add_multiple_button.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.HBL.cost.copy_button.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.HBL.cost.copy_to_button.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.HBL.cost.delete_button.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.HBL.cost.load_from_template_button.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.HBL.HBLAmount.hbl_amount_label.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.HBL.ShipmentProfit.profit_amount_label.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.HBL.tool_button.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.HBL.HBLAmount.include_draft_amount_checkbox.is_visible()
    assert Pages.OEVSAccountingBillingBasedTab.HBL.Memo.memo_title_button.is_visible()


@When("the user clicks save button in OEVS Accounting Billing Based")
def step_impl(context):
    if Pages.OEVSAccountingBillingBasedTab.save_button.is_enable():
        Pages.OEVSAccountingBillingBasedTab.save_button.click()
        Pages.Common.spin_bar.gone()
        sleep(2)
    else:
        Logger.getLogger().warning("The save button is not clickable")


@Then("the save button in OEVS shipment Accounting Billing Based should be disabled")
def step_impl(context):
    assert Pages.OEVSAccountingBillingBasedTab.save_button.is_disabled(), "The save button should be disabled"
