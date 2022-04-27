from behave import Then
from polling2 import TimeoutException, poll

import src.pages as Pages


@Then("popup msg should show")
def step_impl(context):
    exp_msg = context.text.replace(
        "\r", ""
    )  # Walkaround: in Windows OS, the newline escape character in doc string  will be regarded as '\r\n'

    # Wait until the given message is shown or timeout
    try:
        poll(
            target=Pages.Common.popup_modal_msg_label.get_value,
            check_success=lambda x: x == exp_msg,
            step=0.5,
            timeout=3,
        )
    except TimeoutException:
        assert False, f"Expect to show [{exp_msg}], but get [{Pages.Common.popup_modal_msg_label.get_value()}]"
