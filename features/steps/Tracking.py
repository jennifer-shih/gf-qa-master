from behave import Then

import src.pages as Pages


@Then("the user {can_or_cannot} see 'Tracking User Management' on the navigator")
def step_impl(context, can_or_cannot):
    if can_or_cannot == "can":
        assert (
            Pages.NavigatorBar.settings_tracking_user_management.is_visible()
        ), "Tracking User Management should be visible"
    elif can_or_cannot == "can NOT":
        assert (
            Pages.NavigatorBar.settings_tracking_user_management.is_invisible()
        ), "Tracking User Management should be invisible"
