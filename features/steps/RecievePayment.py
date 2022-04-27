from time import sleep

from behave import *

import src.pages as Pages
from src.helper.script import input_dynamic_datas


@When("the user input 'Receive Payment' information")
def step_impl(context):
    page_class_name = "Pages.ReceivePayment"
    input_dynamic_datas(context.table, page_class_name)


@When("the user input 'Receive Payment' 'Invoice Search' information and search")
def step_impl(context):
    page_class_name = "Pages.ReceivePayment.InvoiceSearch"

    # If the Invoice Search panel is not unfolded, click the 'Show More Invoice(s)' button
    if Pages.ReceivePayment.InvoiceSearch.search_button.is_invisible():
        Pages.ReceivePayment.InvoiceList.show_more_invoices_button.click()

    input_dynamic_datas(context.table, page_class_name)

    Pages.ReceivePayment.InvoiceSearch.search_button.click()
    sleep(5)


@When("the user select invoices in Receive Payment Invoice List")
def step_impl(context):
    for row in context.table:
        index = int(row["index"])
        Pages.ReceivePayment.InvoiceList(index).select_checkbox.tick(True)


@When("the user clicks save button in 'Receive Payment'")
def step_impl(context):
    Pages.ReceivePayment.save_button.click()
    sleep(3)

    if Pages.ReceivePayment.PopupMessage.message_element.is_visible():
        Pages.ReceivePayment.PopupMessage.proceed_button.click()
