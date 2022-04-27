@SFI @LOHAN @OLC
Feature: [AirImport] AI Direct Master

    the operator can create a AI shipment with direct master mode

    Background: Log in GoFreight with Operator
        Given the user is a 'Operator'

    Scenario: The operator can create a Direct Master AI Shipment without any error
        Given the user is on 'Air Import New Shipment' page
        When the user tick AI 'Direct Master' checkbox
        And the user click AI MAWB 'More' button
        And the user enter AI MAWB 'Shipment' datas as 'A'
            | field     | attribute    | action               | data                 |
            | MAWB No.  | input        | input                | 911-{randomNo(7)}    |
            | Shipper   | autocomplete | input                | {randomTradePartner} |
            | Consignee | autocomplete | input and close memo | {randomTradePartner} |
            | Sales     | autocomplete | input                | {randomSales}        |
        And the user click Air 'Save' button
        Then the shipment 'A' of 'Air Import' will be created
