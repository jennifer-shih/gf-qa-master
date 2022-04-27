@SFI @LOHAN @OLC
Feature: [Truck] Add TK Container

    the operator can create container and commodity in Container & Item tab

    Background: Log in GoFreight with Operator
        Given the user is a 'Operator'


    Scenario: Users can create a container and save data correctly
        Given the user has a TK MBL as 'A' with only required fields filled
        When the user click 'Container & Item' tab of Truck
        And the user add a tag 'ABC123' in P.O. No.
        And the user click 'New' button of 'Container List'
        And the user input datas in container(1)
            | field              | attribute  | action        | data                |
            | Container No.      | input      | input         | {randomContainerNo} |
            | TP/SZ              | select     | random select |                     |
            | Seal No.           | input      | input         | SN{randN(6)}        |
            | Pick Up No.        | input      | input         | PN{randN(6)}        |
            | PKG                | input      | input         | {randN(3)}          |
            | Weight             | input      | input         | {randN(3)}          |
            | Measurement        | input      | input         | {randN(3)}          |
            | Storage Start Date | datepicker | input         | {today+7}           |
            | Storage End Date   | datepicker | input         | {today+14}          |
            | LFD                | datepicker | input         | {today+21}          |
            | P.O. No.           | tag input  | input         | ABC123              |
        And the user click save button
        Then container(1) should be saved without any errors


    Scenario: Users can create a commodity and save data correctly
        Given the user has a TK MBL as 'A' with only required fields filled
        When the user click 'Container & Item' tab of Truck
        And the user click 'New' button of 'Commodity'
        And the user input data in commodity(1)
            | field                 | attribute | action | data              |
            | Commodity Description | input     | input  | {randomCommodity} |
            | HTS Code              | input     | input  | HTS{randN(4)}     |
        And the user click save button
        Then commodity(1) should be saved without any errors


# Scenario: Users can use 'P.O. No.' mapping by 'Container based'
#     Given the user has a TK shipment
#       And the user is at "Container & Item" tab
#       And there are one container in shipment
#      When the user add 'PONO123' in 'P.O. No.'
#       And

# Scenario: Users can use 'P.O. No.' mapping by 'Item based'
#     Given the user has a TK shipment
#       And the user is at "Container & Item" tab
#       And there are one
#      When the user add 'PONO123' in 'P.O. No.'
#       And
