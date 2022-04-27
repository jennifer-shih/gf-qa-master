@BugRegression
Feature: [Bug Regression] GQT-255

    Net Income value should be consistent in Income Statement and Balance Sheet
    https://hardcoretech.atlassian.net/browse/GQT-255

    Scenario: The value of 'NET INCOME/LOSS' should be consistent in Income Statement
        When the user resets DB to DEG's latest one
        Given the user is a 'Super Admin'
        When the user browse to 'Balance Sheet' page by navigator
        And the user enter 'Balance Sheet' info
            | field  | attribute  | action | data       |
            | As of  | datepicker | input  | 07-31-2020 |
            | Office | select     | select | All        |
        And the user click 'Balance Sheet' 'Print' button
        Then the 'Balance Sheet' values should be correct
            | field                      | value     |
            | NET INCOME FOR THIS PERIOD | 17,730.99 |
        When the user clicks 'NET INCOME FOR THIS PERIOD' link in 'Balance Sheet'
        Then the 'Income Statement' values should be correct
            | field           | value     |
            | NET INCOME/LOSS | 17,730.99 |
        When the user closes current tab

        When the user browse to 'Income Statement' page by navigator
        And the user enter 'Income Statement' info
            | field  | attribute         | action | data                    |
            | Type   | radio group       | click  | Standard                |
            | Period | period datepicker | input  | 08-01-2019 ~ 07-31-2020 |
            | Office | select            | select | All                     |
        And the user click 'Income Statement' 'Print' button
        Then the 'Income Statement' values should be correct
            | field           | value     |
            | NET INCOME/LOSS | 17,730.99 |
