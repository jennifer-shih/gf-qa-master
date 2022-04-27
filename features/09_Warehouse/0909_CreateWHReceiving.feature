@SFI @LOHAN @OLC
Feature: [Warehouse] Create Receiving

    the operator can create a receiving

    Background: Log in GoFreight with Operator
        Given the user is a 'Operator'

    Scenario: The operator want to go to 'New Receiving' page of Warehouse
        Given the user is on 'Dashboard' page
        When the user browse to 'New Receiving' page by navigator
        Then 'New Receiving' page show normally

    Scenario: Generate a new receipt with required fields only and default value should be correct
        Given the user is on 'New Receiving' page
        When the user enter receiving basic datas as 'A'
            | field     | attribute    | action               | data                 |
            | Post Date | datepicker   | input                | {today+5}            |
            | Customer  | autocomplete | input and close memo | {randomTradePartner} |
            | In Date   | datepicker   | input                | {today}              |
        And the user click WH 'Save' button
        Then the receiving 'A' will be created
