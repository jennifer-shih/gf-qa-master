@BugRegression
Feature: [Bug Regression] GQT-256

    The 'RETAINED EARNINGS' value until 2019/8/1 should be the same as the
    'NET INCOME FOR THIS PERIOD' value until 2019/7/31 in Balance Sheet.
    https://hardcoretech.atlassian.net/browse/GQT-256

    Scenario: The value of 'RETAINED EARNINGS' and 'NET INCOME FOR THIS PERIOD' should be consistent
        When the user resets DB to DEG's latest one
        Given the user is a 'Super Admin'
        When the user browse to 'Balance Sheet' page by navigator
        And the user enter 'Balance Sheet' info
            | field  | attribute  | action | data       |
            | As of  | datepicker | input  | 08-01-2019 |
            | Office | select     | select | All        |
        And the user click 'Balance Sheet' 'Print' button
        Then the 'Balance Sheet' values should be correct
            | field             | value    |
            | RETAINED EARNINGS | 2,786.36 |

        When the user closes current tab
        And the user browse to 'Balance Sheet' page by navigator
        And the user enter 'Balance Sheet' info
            | field  | attribute  | action | data       |
            | As of  | datepicker | input  | 07-31-2019 |
            | Office | select     | select | All        |
        And the user click 'Balance Sheet' 'Print' button
        Then the 'Balance Sheet' values should be correct
            | field                      | value    |
            | NET INCOME FOR THIS PERIOD | 2,786.36 |
