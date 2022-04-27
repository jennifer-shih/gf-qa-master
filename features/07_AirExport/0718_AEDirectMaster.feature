@SFI @LOHAN @OLC
Feature: [AirExport] AE Direct Master

    the operator can create a AE shipment with direct master mode

    Background: Log in GoFreight with Operator
        Given the user is a 'Operator'

    Scenario: The operator can create a Direct Master AE Shipment without any error
        Given the user is on 'Air Export New Shipment' page
        When the user tick AE 'Direct Master' checkbox
        And the user click AE MAWB 'More' button
        And the user enter AE MAWB 'Shipment' datas as 'A'
            | field               | attribute    | action               | data                 |
            | MAWB No.            | input        | input                | 911-{randN(4)}       |
            | Customer            | autocomplete | input and close memo | {randomTradePartner} |
            | Consignee           | autocomplete | input                | {randomTradePartner} |
            | Sales               | autocomplete | input                | sales_joey           |
            | Departure Date/Time | datepicker   | input                | {today+1}            |
        And the user click Air 'Save' button
        Then the shipment 'A' of 'Air Export' will be created
