@SFI @LOHAN @OLC
Feature: [Warehouse] Create Receipt

    the operator can create a receipt

    Background: Log in GoFreight with Operator
        Given the user is a 'Operator'

    Scenario: The operator want to go to 'New Receipt' page of Warehouse
        Given the user is on 'Dashboard' page
        When the user browse to 'New Receipt' page by navigator
        Then 'New Receipt' page show normally

    Scenario: Generate a new receipt with required fields only and default value should be correct
        Given the user is on 'New Receipt' page
        When the user enter 'others' receipt basic datas as 'A'
            | field              | attribute  | action | data            |
            | Received Date/Time | datepicker | input  | {today+1} 13:00 |
        And the user click WH 'Save' button
        Then the 'others' receipt 'A' will be created
