@SFI @LOHAN @OLC
Feature: [Warehouse] Create Shipping

    the operator can create a shipping

    Background: Log in GoFreight with Operator
        Given the user is a 'Operator'

    Scenario: The operator want to go to 'New Shipping' page of Warehouse
        Given the user is on 'Dashboard' page
        When the user browse to 'New Shipping' page by navigator
        Then 'New Shipping' page show normally

    Scenario: Generate a new receipt with required fields only and default value should be correct
        Given the user is on 'New Shipping' page
        When the user enter shipping basic datas as 'A'
            | field     | attribute    | action               | data                 |
            | Post Date | datepicker   | input                | {today+5}            |
            | Customer  | autocomplete | input and close memo | {randomTradePartner} |
            | Out Date  | datepicker   | input                | {today}              |
        And the user click WH 'Save' button
        Then the shipping 'A' will be created
