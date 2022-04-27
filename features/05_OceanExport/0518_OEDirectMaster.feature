@SFI @LOHAN @OLC
Feature: [OceanExport] OE Direct Master

    User can create a OE shipment with direct master mode

    Background: Log in GoFreight with Operator
        Given the user is a 'Operator'

    Scenario: The operator can create a Direct Master OE Shipment without any error
        Given the user is on 'Ocean Export New Shipment' page
        When the user tick OE 'Direct Master' checkbox
        And the user click OE MBL 'More' button
        And the user enter 'OE MBL' shipment datas as 'A' and save it
            | field             | attribute    | action               | data                 |
            | MB/L No.          | input        | input                | HACO-{randN(6)}      |
            | B/L Type          | select       | random select        |                      |
            | Carrier Bkg. No.  | input        | input                | CBN-{randN(6)}       |
            | Carrier           | autocomplete | input                | OCEAN9191            |
            | Oversea Agent     | autocomplete | input and close memo | {randomTradePartner} |
            | Notify            | autocomplete | input                | {randomTradePartner} |
            | Customer Ref. No. | input        | input                | CRN-{randN(6)}       |
            | Customer          | autocomplete | input and close memo | {randomTradePartner} |
            | Consignee         | autocomplete | input                | {randomTradePartner} |
            | Sales Type        | select       | random select        |                      |
            | Cargo Type        | select       | random select        |                      |
            | ETD               | datepicker   | input                | {today+5}            |
        Then the shipment 'A' of 'Ocean Export' will be created
