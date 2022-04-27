from behave import Then, When

import src.pages as Pages
from src.helper.timer import PatchDBTimer


@When("the user clicks 'Apply' button for '{patch_name}' on 'Patch DB' page")
def step_impl(context, patch_name):
    Pages.PatchDBPage.patch_apply_button(patch_name).click()
    Pages.PatchDBPage.proceed_button.click()


@Then("the success msg '{msg}' will show on 'Console' block in '{timeout}' sec")
def step_impl(context, msg, timeout):
    timer = PatchDBTimer(msg, int(timeout))
    timer.start()
    is_passed, text = timer.get_result()
    assert is_passed, f"Patch fail after {timeout} sec\n textarea: \n{text}"
