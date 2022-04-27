Feature: [OceanExport] Add OE HBL To Shipment

    the operator can add HB/L(s) to the shipment which has been created

    Background: Log in GoFreight with Operator
        Given the user is a 'Operator'

    @SFI @LOHAN
    Scenario: Add OE HBL with required fields only (For generic)
        Given the user has a OE Shipment
        When the user click OE 'Add HBL' button
        And the user enter 'OE HBL(1)' shipment datas as 'A' and save it
            | field | attribute | action | data |
        Then the shipment 'A' HBL(1) of 'Ocean Export' will be created

    @OLC
    Scenario: Add OE HBL with required fields only (For enterprise)
        Given the user has a OE Shipment
        When the user click OE 'Add HBL' button
        And the user enter 'OE HBL(1)' shipment datas as 'A' and save it
            | field    | attribute    | action | data             |
            | HB/L No. | input        | input  | OEHBL-{randN(6)} |
            | Sales    | autocomplete | input  | {randomSales}    |
        Then the shipment 'A' HBL(1) of 'Ocean Export' will be created
