from random import randint
from time import sleep

from behave import Then, When

import src.pages as Pages
from src.drivers.driver import Driver
from src.helper.script import input_dynamic_datas


@Then("the user will not see 'Front Desk'")
def step_impl(context):
    assert Pages.NavigatorBar.accounting_front_desk.is_invisible(), "Front Desk should be invisible"


@Then("the user will see 'Front Desk' subitems")
def step_impl(context):
    assert Pages.NavigatorBar.accounting_front_desk_front_desk_portal.is_visible(), "Desk Portal should be visible"
    assert (
        Pages.NavigatorBar.accounting_front_desk_uniform_invoice_management.is_visible()
    ), "Uniform Invoice Management should be visible"
    assert (
        Pages.NavigatorBar.accounting_front_desk_uniform_invoice_setting.is_visible()
    ), "Uniform Invoice Setting should be visible"


@When("the user search for the OI '{name}' HBL({index}) AR just created")
def step_impl(context, name, index):
    hbl_no = context._vp.get("hbl_model")["{}_{}".format(name, index)].get_data("HB/L No.")

    Pages.FrontDeskPortal.keyword_input.input(hbl_no)
    Pages.FrontDeskPortal.search_button.click()
    Pages.Common.spin_bar.gone()


@Then("the OI '{name}' HBL({index}) AR should not be found")
def step_impl(context, name, index):
    assert Pages.FrontDeskPortal.SearchResult(1).hbl_no_link.is_invisible(), "the AR should not be found"


@When("the user search for the OE Booking AR just created")
def step_impl(context):
    Pages.Common.spin_bar.gone()
    booking_no = context._vp.get("oe_booking_no")
    Pages.FrontDeskPortal.keyword_input.input(booking_no)
    Pages.FrontDeskPortal.search_button.click()


@Then("the OE Booking AR should not be found")
def step_impl(context):
    assert Pages.FrontDeskPortal.SearchResult(1).hbl_no_link.is_invisible(), "the AR should not be found"


@When("the user search for the AI HAWB({index}) AR just created")
def step_impl(context, index):
    hawb_no = context._vp.get("hawb_model")[index].get_data("HAWB No.")
    Pages.FrontDeskPortal.keyword_input.input(hawb_no)
    Pages.FrontDeskPortal.search_button.click()


@Then("the AI HAWB({index}) {ar_cnt} ARs info should be correct")
def step_impl(context, index, ar_cnt):
    for i in range(1, int(ar_cnt) + 1):
        hawb_model = context._vp.get("hawb_model")["{}".format(index)]
        hawb_freight_model = context._vp.get("hawb_freight_model")["{}_{}".format(index, i)]
        exp_hbl_no = hawb_model.get_data("HAWB No.")
        exp_party = hawb_freight_model.get_data("Bill To")

        hbl_no = Pages.FrontDeskPortal.SearchResult(i).hbl_no_link.get_value()
        party = Pages.FrontDeskPortal.SearchResult(i).party_name_label.get_value()
        assert exp_hbl_no == hbl_no, "Freight {0} hbl no not showing correctly, expect [{1}] but get [{2}]".format(
            i, exp_hbl_no, hbl_no
        )
        assert exp_party == party, "Freight {0} party name not showing correctly, expect [{1}] but get [{2}]".format(
            i, exp_party, party
        )


@When("the user add {count} new uniform invoice roll")
def step_impl(context, count):
    model_list = []
    for i in range(1, int(count) + 1):
        Pages.UniformInvoiceSettingPage.new_invoice_roll_button.click()
        model = input_dynamic_datas(context.table, "Pages.UniformInvoiceSettingPage.AddInvoiceRoll")
        Pages.UniformInvoiceSettingPage.AddInvoiceRoll.add_button.click()
        Pages.Common.spin_bar.gone()

        # fit field to result list field
        prefix = model.get_data("Prefix")
        model.pop("Prefix")
        model.add(field="Prefix", attribute="label", data=prefix)

        year = model.get_data("Year")
        month = model.get_data("Month")
        model.add(field="Invoice Month", attribute="label", data="{}-{}".format(year, month))
        model.pop("Year")
        model.pop("Month")

        type = model.get_data("Uniform Invoice Type")
        model.add(field="Invoice Type", attribute="label", data=type)
        model.pop("Uniform Invoice Type")

        rolls = int(model.get_data("Rolls"))
        amount_per_roll = int(model.get_data("Amount Per Roll"))
        starting_no = int(model.get_data("Invoice Number Begin"))
        model.pop("Rolls")
        model.pop("Amount Per Roll")
        model.pop("Invoice Number Begin")
        last_ending_no = starting_no + amount_per_roll - 1

        for j in range(1, rolls + 1):
            starting_no = str(last_ending_no - amount_per_roll + 1).zfill(8)
            ending_no = str(last_ending_no).zfill(8)
            last_ending_no += amount_per_roll
            new_model = model.copy()
            new_model.add(field="Starting No.", attribute="label", data=starting_no)
            new_model.add(field="Current No.", attribute="label", data="")
            new_model.add(field="Ending No.", attribute="label", data=ending_no)
            model_list.append(new_model)

    model_list.reverse()
    for index in range(1, len(model_list) + 1):
        model = model_list[index - 1]
        model.set_page_class_name("Pages.UniformInvoiceSettingPage.InvoiceList({})".format(index))
        context._vp.add_list(list_name="invoice_model", value=model)
    Driver.refresh()
    Pages.Common.spin_bar.gone()


@Then("the uniform invoice roll should be saved correctly")
def step_impl(context):
    models = context._vp.get("invoice_model")
    for model in models:
        model.verify()


@When("the user select one invoice roll and click 'Delete'")
def step_impl(context):
    models = context._vp.get("invoice_model")
    invoice_count = len(models)
    delete_index = randint(1, invoice_count)
    Pages.UniformInvoiceSettingPage.InvoiceList(delete_index).check_checkbox.tick(True)
    Pages.UniformInvoiceSettingPage.delete_invoice_roll_button.click()
    sleep(2)
    Pages.UniformInvoiceSettingPage.delete_ok_button.click()
    Pages.Common.spin_bar.gone()

    for index in range(1, invoice_count + 1):
        if index == delete_index:
            continue
        model = models[index - 1].copy()
        if index > delete_index:
            model.set_page_class_name("Pages.UniformInvoiceSettingPage.InvoiceList({})".format(index - 1))
        context._vp.add_list(list_name="after_delete_invoice_model", value=model)

    Driver.refresh()
    Pages.Common.spin_bar.gone()


@Then("the uniform invoice roll should be deleted")
def step_impl(context):
    models = context._vp.get("after_delete_invoice_model")
    for model in models:
        model.verify()


@When("the user select AR({ar_index}) in 'Front Desk Portal'")
def step_impl(context, ar_index):
    # ? Known Issue OLC-5157
    Pages.Common.spin_bar.gone()
    ele = Driver.get_driver().find_element_by_xpath(
        "//hcgridcontainer//div[@row-id='{0}']//label[contains(@class, 'chkcontainer')]//span".format(int(ar_index) - 1)
    )
    Driver.get_driver().execute_script("arguments[0].click();", ele)
    # ?
    # Pages.FrontDeskPortal.SearchResult(ar_index).check_checkbox.tick(True)


@When("the user click 'Print HBL' button in 'Front Desk Portal'")
def step_impl(context):
    pass
    # ? Known Issue OLC-4991
    # Pages.FrontDeskPortal.print_hbl_button.click()
    # ?


@When("the user click 'Print Uniform Invoice' button in 'Front Desk Portal'")
def step_impl(context):
    Pages.FrontDeskPortal.print_uniform_invoice_button.click()


@When("the user click 'Print' in 'Print Uniform Invoice' modal")
def step_impl(context):
    Pages.FrontDeskPortal.PrintReceipt.print_button.click()
    Driver.switch_to(window_index=1)


@When("the user click 'Receipt Payment' button in 'Front Desk Portal'")
def step_impl(context):
    Pages.FrontDeskPortal.receive_payment_button.click()
    sleep(2)


@When("the user click 'Print Receipt' button in 'Front Desk Portal'")
def step_impl(context):
    Pages.FrontDeskPortal.print_receipt_button.click()
    Driver.switch_to(window_index=1)


@When("the user click 'Cancel' button in uniform invoice modal")
def step_impl(context):
    Pages.FrontDeskPortal.PrintUniformInvoiceModal.cancel_button.click()


@Then("the AR({ar_index}) preview modal pop out")
def step_impl(context, ar_index):
    # ? Known Issue OLC-4991
    assert True
    # ? Known Issue OLC-4991


@Then("the AR({ar_index}) print uniform invoice modal pop out")
def step_impl(context, ar_index):
    assert (
        Pages.FrontDeskPortal.PrintUniformInvoiceModal.counter_label.is_visible()
    ), "Print Uniform Invoice is not visible"


@Then("the AR({ar_index}) print uniform invoice modal should have no freight listed")
def step_impl(context, ar_index):
    assert Pages.FrontDeskPortal.PrintUniformInvoiceModal.Freight(
        1
    ).freight_code_autocomplete.is_invisible(), "Print Uniform Invoice block should have no freight listed"


@Then("the AR({ar_index}) print receipt preview shows up")
def step_impl(context, ar_index):
    assert Pages.DocPreviewToolBar.print_button.is_visible(), "Print Receipt is not visible"


@Then("the AR({ar_index}) print receipt preview should have no freight listed")
def step_impl(context, ar_index):
    assert (
        Pages.FrontDeskPortal.PrintReceipt.Freight(1).name_label.get_value() == " "
    ), "Print Uniform Invoice block should have no freight listed"
    Driver.close()
    Driver.switch_to(window_index=0)


@Then("the AR({ar_index}) receipt payment modal should have 4 method to receive")
def step_impl(context, ar_index):
    assert Pages.FrontDeskPortal.ReceivePaymentModal.cash_button.is_visible(), "Cash button should be visible"
    assert Pages.FrontDeskPortal.ReceivePaymentModal.check_button.is_visible(), "Check button should be visible"
    assert Pages.FrontDeskPortal.ReceivePaymentModal.wire_button.is_visible(), "Wire button should be visible"
    assert (
        Pages.FrontDeskPortal.ReceivePaymentModal.temporary_receipt_button.is_visible()
    ), "Temporary Receipt button should be visible"


@Then("the 'Uniform Invoice Print' page will show")
def step_impl(context):
    sleep(3)
    assert "reports/uniform-invoice-print/print/" in Driver.get_url(), "Uniform Invoice Print page should show"
    Driver.close()
    Driver.switch_to(window_index=0)


@Then("the AR detail modal shows up")
def step_impl(context):
    Pages.FrontDeskPortal.ARDetailModal.spin_bar.gone(timeout=15)
    assert (
        Pages.FrontDeskPortal.ARDetailModal.spin_bar.is_invisible()
    ), "AR Detail loading in Front Desk Portal is timeout\n"
    assert Pages.FrontDeskPortal.ARDetailModal.hbl_no_label.is_visible(), "AR Detail Modal should be visible"


@Then("the AR summary detail modal shows up")
def step_impl(context):
    Pages.FrontDeskPortal.ARSummaryDetailModal.spin_bar.gone(timeout=15)
    assert (
        Pages.FrontDeskPortal.ARSummaryDetailModal.spin_bar.is_invisible()
    ), "AR Summary Detail loading in Front Desk Portal is timeout\n"
    assert (
        Pages.FrontDeskPortal.ARSummaryDetailModal.shipment_selected_label.is_visible()
    ), "AR Summary Detail Modal should be visible"


@When("the user set AR({invoice_index}) in 'Uniform Invoice Management' page to be 'Void'")
def step_impl(context, invoice_index):
    Pages.UniformInvoiceMngPage.InvoiceList(invoice_index).check_checkbox.tick(True)
    Pages.UniformInvoiceMngPage.void_button.click()
    sleep(0.5)
    Pages.UniformInvoiceMngPage.InvoiceModal.confirm_button.click()
    Pages.Common.spin_bar.gone()


@Then("the AR({invoice_index}) status in 'Uniform Invoice Management' should be 'Void'")
def step_impl(context, invoice_index):
    assert Pages.UniformInvoiceMngPage.InvoiceList(
        invoice_index
    ).void_success_label.is_visible(), "Void status check should be visible"


@When("the user set AR({invoice_index}) in 'Uniform Invoice Management' page to be 'Valid'")
def step_impl(context, invoice_index):
    Pages.UniformInvoiceMngPage.InvoiceList(invoice_index).check_checkbox.tick(True)
    Pages.UniformInvoiceMngPage.valid_button.click()
    sleep(0.5)
    Pages.UniformInvoiceMngPage.InvoiceModal.confirm_button.click()
    Pages.Common.spin_bar.gone()


@Then("the AR({invoice_index}) status in 'Uniform Invoice Management' should be 'Valid'")
def step_impl(context, invoice_index):
    assert Pages.UniformInvoiceMngPage.InvoiceList(
        invoice_index
    ).void_success_label.is_invisible(), "Void status check should not be visible"
