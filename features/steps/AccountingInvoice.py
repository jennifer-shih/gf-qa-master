from time import sleep

from behave import *

import src.pages as Pages
from src.helper.transfer import transfer_data


@When("the user input AR Billing Information")
def step_impl(context):
    for row in context.table:
        Pages.AREntry.bill_to_autocomplete.input(transfer_data(row["Bill to"]))
        if "Invoice Date" in context.table.headings:
            Pages.AREntry.invoice_date_datepicker.input(transfer_data(row["Invoice Date"]))
        if "Due Date" in context.table.headings:
            Pages.AREntry.due_date_datepicker.input(transfer_data(row["Due Date"]))


@When("the user add freights to AR")
def step_impl(context):
    freight_index = 1
    for row in context.table:
        Pages.AREntry.new_freight_button.click()
        if "Freight code" in context.table.headings:
            Pages.AREntry.freight(freight_index).freight_code_autocomplete.input(row["Freight code"], loading_timeout=4)
        if "Type" in context.table.headings:
            Pages.AREntry.freight(freight_index).type_select.select(row["Type"])
        if "Rate" in context.table.headings:
            Pages.AREntry.freight(freight_index).rate_input.input(row["Rate"])
        freight_index += 1


@When("the user input DC Billing Information")
def step_impl(context):
    for row in context.table:
        Pages.DCNoteEntry.agent_name_autocomplete.input(transfer_data(row["Agent Name"]))
        if "Invoice Date" in context.table.headings:
            Pages.AREntry.invoice_date_datepicker.input(transfer_data(row["Invoice Date"]))
        if "Due Date" in context.table.headings:
            Pages.AREntry.due_date_datepicker.input(transfer_data(row["Due Date"]))


@When("the user add freights to DC")
def step_impl(context):
    freight_index = 1
    for row in context.table:
        Pages.DCNoteEntry.new_freight_button.click()
        Pages.DCNoteEntry.freight(freight_index).freight_code_autocomplete.input(row["Freight code"], loading_timeout=4)
        Pages.DCNoteEntry.freight(freight_index).type_select.select(row["Type"])
        Pages.DCNoteEntry.freight(freight_index).rate_input.input(row["Rate"])


@When("the user input AP Billing Information")
def step_impl(context):
    for row in context.table:
        Pages.APEntry.vendor_autocomplete.input(transfer_data(row["Vendor"]))
        if "Invoice Date" in context.table.headings:
            Pages.AREntry.invoice_date_datepicker.input(transfer_data(row["Invoice Date"]))
        if "Due Date" in context.table.headings:
            Pages.AREntry.due_date_datepicker.input(transfer_data(row["Due Date"]))


@When("the user add freights to AP")
def step_impl(context):
    freight_index = 1
    for row in context.table:
        Pages.APEntry.new_freight_button.click()
        Pages.APEntry.freight(freight_index).freight_code_autocomplete.input(row["Freight code"], loading_timeout=4)
        Pages.APEntry.freight(freight_index).rate_input.input(row["Rate"])
        if "Type" in context.table.headings:
            Pages.APEntry.freight(freight_index).type_select.select(row["Type"])
        freight_index += 1


@When("the user clicks 'Save as Draft' button")
def step_impl(context):
    Pages.AREntry.save_as_draft_button.click()
    Pages.Common.spin_bar.gone()
    sleep(2)


@When("the user clicks 'Load and Link' button in DC entry")
def step_impl(context):
    Pages.DCNoteEntry.load_and_link_button.click()


@Then("the values of freights in AR entry should be")
def step_impl(context):
    for row in context.table:
        index = int(row["index"])
        if "Freight Code" in context.table.headings and row["Freight Code"]:
            assert row["Freight Code"] == Pages.AREntry.freight(index).freight_code_autocomplete.get_value()
        if "Amount" in context.table.headings and row["Amount"]:
            assert row["Amount"] == Pages.AREntry.freight(index).amount_label.get_value()
        if "Status" in context.table.headings and row["Status"]:
            assert row["Status"] == Pages.AREntry.freight(index).status_status_icon.get_value()


@Then("the values of freights in DC entry should be")
def step_impl(context):
    for row in context.table:
        index = int(row["index"])
        if "Freight Code" in context.table.headings and row["Freight Code"]:
            assert row["Freight Code"] == Pages.DCNoteEntry.freight(index).freight_code_autocomplete.get_value()
        if "Type" in context.table.headings and row["Type"]:
            assert row["Type"] == Pages.DCNoteEntry.freight(index).type_select.get_value()
        if "Amount" in context.table.headings and row["Amount"]:
            assert row["Amount"] == Pages.DCNoteEntry.freight(index).amount_label.get_value()
        if "Status" in context.table.headings and row["Status"]:
            assert row["Status"] == Pages.DCNoteEntry.freight(index).status_status_icon.get_value()


@Then("the values of freights in AP entry should be")
def step_impl(context):
    for row in context.table:
        index = int(row["index"])
        if "Freight Code" in context.table.headings and row["Freight Code"]:
            assert row["Freight Code"] == Pages.APEntry.freight(index).freight_code_autocomplete.get_value()
        if "Amount" in context.table.headings and row["Amount"]:
            assert row["Amount"] == Pages.APEntry.freight(index).amount_label.get_value()
        if "Status" in context.table.headings and row["Status"]:
            assert row["Status"] == Pages.APEntry.freight(index).status_status_icon.get_value()


@Then("the 'Load and Link' button should be disabled")
def step_impl(context):
    assert Pages.DCNoteEntry.load_and_link_button.is_disable()
