from behave import Given

import src.pages as Pages
from config import globalparameter as gl
from src.drivers.driver import Driver


@Given("the user is at HBL({hbl_no}) Booking entry")
def step_impl(context, hbl_no):
    Driver.open(gl.URL.OE_BOOKING_LIST)
    Pages.Common.spin_bar.gone()
    # There is a bug on GoFreight "Config" that before reset DB, first time in the page wil show correct table column order, but second time will be the error one.
    Driver.refresh()
    Pages.Common.spin_bar.gone()
    #
    Pages.OEBookingListPage.filter_button.click()
    Pages.OEBookingListPage.Filter.keyword_input.input(hbl_no)
    Pages.OEBookingListPage.Filter.apply_filters_button.click()
    Pages.Common.spin_bar.gone()
    Pages.OEBookingListPage.Row(1).booking_no_link.click()
    Pages.Common.spin_bar.gone()
