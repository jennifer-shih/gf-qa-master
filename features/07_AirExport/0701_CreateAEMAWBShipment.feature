@SFI @LOHAN @OLC
Feature: [AirExport] Create AE Shipment

    the operator can create a shipment of Air Export

    Background: Log in GoFreight with Operator
        Given the user is a 'Operator'

    Scenario: The operator want to go to 'New Shipment' page of Air Export
        Given the user is on 'Dashboard' page
        When the user browse to 'New Shipment of Air Export' page by navigator
        Then 'New Shipment of Air Export' page show normally

    Scenario: Generate a new shipment with required fields only and default value should be correct
        Given the user is on 'Air Export New Shipment' page
        When the user enter AE MAWB 'Shipment' datas as 'A'
            | field               | attribute  | action | data      |
            | Departure Date/Time | datepicker | input  | {today+1} |
        And the user click Air 'Save' button
        Then the shipment 'A' of 'Air Export' will be created
        And the default issuing carrier agent is correct
        And the default ITN NO. is correct
        And the default shipper is correct
        And the default D.V. carriage is correct
        And the default D.V. customs is correct
        And the default insurance is correct
        And the default pakage unit for AE MAWB is correct
        And the default carrier agent in Other Charge(1) is correct
        And the default collect prepaid in Other Charge(1) is correct
        And the default charge item in Other Charge(1) is correct
        And the default description in Other Charge(1) is correct
        And the default carrier agent in Other Charge(2) is correct
        And the default collect prepaid in Other Charge(2) is correct
        And the default charge item in Other Charge(2) is correct
        And the default description in Other Charge(2) is correct

    Scenario: Generate a new shipment
        Given the user is on 'Air Export New Shipment' page
        When the user click AE MAWB 'More' button
        And the user enter AE MAWB 'Shipment' datas as 'A'
            | field                     | attribute    | action               | data                 |
            | Carrier                   | autocomplete | input                | AIR9191              |
            | AWB Type                  | select       | random select        |                      |
            | MAWB No.                  | input        | input                | 911-{randN(4)}       |
            | AWB Date                  | datepicker   | input                | {today}              |
            | Consignee (Oversea Agent) | autocomplete | input and close memo | {randomTradePartner} |
            | Notify                    | autocomplete | input and close memo | {randomTradePartner} |
            | Co-loader                 | autocomplete | input                | {randomTradePartner} |
            | Departure                 | autocomplete | input                | gru                  |
            | Departure Date/Time       | datepicker   | input                | {today+1}            |
            | Flight No.                | input        | input                | FNO{randN(6)}        |
            | Destination               | autocomplete | input                | abq                  |
            | Arrival Date/Time         | datepicker   | input                | {today+2}            |
            | Carrier's Spot No.        | input        | input                | CSNO{randN(6)}       |
            | WT/VAL                    | radio group  | random click         |                      |
            | Other                     | radio group  | random click         |                      |
            | Delivery To/Pier          | autocomplete | input                | {randomTradePartner} |
            | Package                   | input        | input                | {randInt(1,10)}      |
            | Gross Weight              | input        | input                | {randInt(1,999)}     |
            | Buying Rate               | input        | input                | {randInt(1,10)}      |
            | Selling Rate              | input        | input                | {randInt(1,10)}      |
            | Incoterms                 | select       | random select        |                      |
            | Service Term From         | select       | random select        |                      |
            | Service Term To           | select       | random select        |                      |
            | Business Referred By      | autocomplete | input                | {randomTradePartner} |
            | E-Commerce                | checkbox     | tick                 | {randomOnOff}        |
        And the user click AE MAWB 'Set Dimensions' button
        And the user input Length, Width, Height and PCS for AE MAWB 'A' 'Volume Weight'
            | Length           | Width            | Height           | PCS             |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
        And the user save AE 'Dimensions' settings
        And the user click AE MAWB 'Connecting Flight' button
        And the user enter AE MAWB 'A' 'Route' datas
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
        And the user save AE MAWB 'Route' settings
        And the user input information for AE MAWB 'A' 'Other Charge'
            | Charge Amount    |
            | {randInt(1,999)} |
            | {randInt(1,999)} |
        And the user expand MAWB 'More' block
        And the user enter AE MAWB 'A' 'More' datas
            | field                                | attribute | action | data                                           |
            | Prepaid Valuation                    | input     | input  | {randInt(1,999)}                               |
            | Prepaid Tax                          | input     | input  | {randInt(1,999)}                               |
            | Prepaid Currency Conversion Rates    | input     | input  | {randInt(1,999)}                               |
            | Collect Valuation                    | input     | input  | {randInt(1,999)}                               |
            | Collect Tax                          | input     | input  | {randInt(1,999)}                               |
            | Collect CC Charges in Dest. Currency | input     | input  | {randInt(1,999)}                               |
            | Collect Charges at Destination       | input     | input  | {randInt(1,999)}                               |
            | P.O. No.                             | tag input | input  | {randomNo(6)}                                  |
            | Mark                                 | input     | input  | THIS IS AIR EXPORT - MBL : MARK                |
            | Handling Information                 | input     | input  | THIS IS AIR EXPORT - MAWB HANDLING INFORMATION |
        And the user input information for AE MAWB 'A' 'Commodity'
            | Commodity Description | HTS Code         |
            | {randomCommodity}     | HTS{randomNo(6)} |
        And the user click Air 'Save' button
        Then the shipment 'A' of 'Air Export' will be created
        And the AE MAWB 'A' 'Volume Weight' data is saved
        And field 'Chargeable Weight' for AE MAWB should be autofilled with right numbers
        And the AE MAWB 'A' 'Route' data is saved
        And the AE MAWB 'A' 'Other Charge' data is saved
        And the AE MAWB 'A' 'Commodity' data is saved
