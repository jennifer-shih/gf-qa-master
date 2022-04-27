@BugRegression
Feature: [Bug Regression] GQT-258

    Payment should be saved successfully even when we choose the invoice whose post date is later than today
    https://hardcoretech.atlassian.net/browse/GQT-258

    Scenario: Payment should be saved successfully
        When the user resets DB to HGL's latest one
        Given the user is a 'Super Admin'
        And the user is on 'New Trade Partner' page
        When the user input the trade partner profile
            | field      | attribute    | action | data        |
            | TP Type    | select       | select | AIR CARRIER |
            | Name       | input        | input  | TP_258      |
            | Print Name | input        | input  | TP_258      |
            | Country    | autocomplete | input  | TAIWAN      |
        And the user click save button

        Given the user has a TK MBL as 'A' with only required fields filled
        When the user click 'Accounting' tab of Truck
        And the user clicks TK MBL 'Create Invoice' button
        And the user input AR Billing Information
            | Bill to | Post Date |
            | TP_258  | {today}   |
        And the user add freights to AR
            | Freight code | Rate |
            | EXAM FEE     | 10   |
        And the user click save button
        And the user clicks TK MBL 'Create Invoice' button
        And the user input AR Billing Information
            | Bill to | Post Date |
            | TP_258  | {today+7} |
        And the user add freights to AR
            | Freight code | Rate |
            | FORKLIFT     | 20   |
        And the user click save button

        When the user browse to 'Receive Payment' page by navigator
        And the user input 'Receive Payment' information
            | field         | attribute    | action | data   |
            | Received From | autocomplete | input  | TP_258 |
        And the user input 'Receive Payment' 'Invoice Search' information and search
            | field    | attribute    | action | data   |
            | Customer | autocomplete | input  | TP_258 |
        And the user select invoices in Receive Payment Invoice List
            | index |
            | 1     |
        And the user clicks save button in 'Receive Payment'
        Then the data is saved successfully
        When the user input 'Receive Payment' 'Invoice Search' information and search
            | field    | attribute    | action | data   |
            | Customer | autocomplete | input  | TP_258 |
        And the user select invoices in Receive Payment Invoice List
            | index |
            | 2     |
        And the user clicks save button in 'Receive Payment'
        Then the data is saved successfully
