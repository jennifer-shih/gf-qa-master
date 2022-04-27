from behave import Then, When

import src.pages as Pages
from src.drivers.driver import Driver
from src.helper.function import get_quotation_no
from src.helper.script import input_dynamic_datas


@When("the user close the favorite tool prompt")
def step_impl(context):
    Pages.SalesQuotPage.remove_prompt_button.click()


@When("the user enter quotation data for '{shipping_type}' as '{name}' and save it")
def step_impl(context, name, shipping_type):
    current_page_class_name = "Pages.SalesQuotPage"
    Pages.SalesQuotPage.shipping_type_select.select(shipping_type)
    model = input_dynamic_datas(context.table, current_page_class_name)
    model.add(field="Shipping Type", attribute="select", data=shipping_type)

    office = Pages.SalesQuotPage.office_autocomplete.get_value()
    if not model.has_key("Office"):
        model.add(field="Office", attribute="autocomplete", data=office)
    quote_no = get_quotation_no(office.split("-")[0].strip())
    model.add(field="quote_no", attribute="input", data=quote_no)
    context._vp.add_dict(dict_name="quotation_model", value={name: model})

    Pages.SalesQuotPage.save_button.click()
    assert Pages.Common.save_msg.is_visible(timeout=30) is True


@Then("the quotation '{name}' will be created")
def step_impl(context, name):
    model = context._vp.get("quotation_model")[name]

    # refresh page
    Driver.refresh()
    Pages.Common.spin_bar.gone(timeout=10)

    model.verify()
