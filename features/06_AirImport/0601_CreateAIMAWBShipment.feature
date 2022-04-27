@SFI @LOHAN @OLC
Feature: [AirImport] Create AI Shipment

    the operator can create a shipment of Air Import

    Background: Log in GoFreight with Operator
        Given the user is a 'Operator'

    Scenario: The operator want to go to 'New Shipment' page of Air Import
        Given the user is on 'Dashboard' page
        When the user browse to 'New Shipment of Air Import' page by navigator
        Then 'New Shipment of Air Import' page show normally

    Scenario: Generate a new shipment with required fields only and default value should be correct
        Given the user is on 'Air Import New Shipment' page
        When the user enter AI MAWB 'Shipment' datas as 'A'
            | field    | attribute | action | data              |
            | MAWB No. | input     | input  | 911-{randomNo(7)} |
        And the user click Air 'Save' button
        Then the shipment 'A' of 'Air Import' will be created
        And the default pakage unit for AI MAWB is correct

    Scenario: Generate a new shipment
        Given the user is on 'Air Import New Shipment' page
        When the user click AI MAWB 'More' button
        And the user enter AI MAWB 'Shipment' datas as 'A'
            | field                | attribute    | action        | data                 |
            | MAWB No.             | input        | input         | 911-{randomNo(7)}    |
            | AWB Type             | select       | random select |                      |
            | Oversea Agent        | autocomplete | input         | {randomTradePartner} |
            | Co-loader            | autocomplete | input         | {randomTradePartner} |
            | Departure            | autocomplete | input         | gru                  |
            | Departure Date/Time  | datepicker   | input         | {today+1}            |
            | Flight No.           | input        | input         | FNO{randN(8)}        |
            | Destination          | autocomplete | input         | abq                  |
            | Arrival Date/Time    | datepicker   | input         | {today+2}            |
            | Freight Location     | autocomplete | input         | {randomTradePartner} |
            | Storage Start Date   | datepicker   | input         | {today+3}            |
            | Package              | input        | input         | {randInt(1,999)}     |
            | Gross Weight         | input        | input         | {randInt(1,999)}     |
            | Freight              | select       | random select |                      |
            | Incoterms            | select       | random select |                      |
            | Service Term From    | select       | random select |                      |
            | Service Term To      | select       | random select |                      |
            | Business Referred By | autocomplete | input         | {randomTradePartner} |
            | E-Commerce           | checkbox     | tick          | {randomOnOff}        |
        And the user click AI MAWB 'Set Dimensions' button
        And the user input Length, Width, Height and PCS for AI MAWB 'A' 'Volume Weight'
            | Length           | Width            | Height           | PCS             |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
        And the user save AI 'Dimensions' settings
        And the user click AI MAWB 'Connecting Flight' button
        And the user enter AI MAWB 'A' 'Route' datas
            | field                                     | attribute    | action | data                 |
            | Route Departure Departure Date/Time       | datepicker   | input  | {today+1}            |
            | Route Trans 1                             | autocomplete | input  | BBB                  |
            | Route Trans 1 Arrival Date/Time           | datepicker   | input  | {today+4}            |
            | Route Trans 1 Departure Date/Time         | datepicker   | input  | {today+5}            |
            | Route Trans 1 Flight No.                  | input        | input  | TRANS1_{randN(5)}    |
            | Route Trans 1 Carrier                     | autocomplete | input  | {randomTradePartner} |
            | Route Trans 2                             | autocomplete | input  | CCC                  |
            | Route Trans 2 Arrival Date/Time           | datepicker   | input  | {today+6}            |
            | Route Trans 2 Departure Date/Time         | datepicker   | input  | {today+7}            |
            | Route Trans 2 Flight No.                  | input        | input  | TRANS2_{randN(5)}    |
            | Route Trans 2 Carrier                     | autocomplete | input  | {randomTradePartner} |
            | Route Trans 3                             | autocomplete | input  | GGG                  |
            | Route Trans 3 Arrival Date/Time           | datepicker   | input  | {today+8}            |
            | Route Trans 3 Departure Date/Time         | datepicker   | input  | {today+9}            |
            | Route Trans 3 Flight No.                  | input        | input  | TRANS3_{randN(5)}    |
            | Route Trans 3 Carrier                     | autocomplete | input  | {randomTradePartner} |
            | Route Final Destination Arrival Date/Time | datepicker   | input  | {today+2}            |
        And the user save AI MAWB 'Route' settings
        And the user click Air 'Save' button
        Then the shipment 'A' of 'Air Import' will be created
        And the AI MAWB 'A' 'Volume Weight' data is saved
        And field 'Chargeable Weight' for AI MAWB should be autofilled with right numbers
        And the AI MAWB 'A' 'Route' data is saved
