Feature: [AirExport] AE MAWB Function Test

    linked fields of AE MAWB and some features work no problem

    Background: Log in GoFreight with Operator
        Given the user is a 'Operator'

    @SFI @LOHAN
    Scenario: MAWB NO. should be autofilled with '911-' after choosing Carrier (For generic)
        Given the user is on 'Air Export New Shipment' page
        When the user enter AE MAWB 'Shipment' datas as 'A'
            | field   | attribute    | action | data                 |
            | Carrier | autocomplete | input  | {randomTradePartner} |
        Then 'HAWB NO.' should be autofilled with '911-'

    @OLC
    Scenario: MAWB NO. should be autofilled with '911-' after choosing Carrier (For enterprise)
        Given the user is on 'Air Export New Shipment' page
        When the user enter AE MAWB 'Shipment' datas as 'A'
            | field   | attribute    | action | data    |
            | Carrier | autocomplete | input  | AIR9191 |
        Then 'HAWB NO.' should be autofilled with '911-'

    @SFI @LOHAN @OLC
    Scenario: Auto-calculate gross amount and chargeable amount is no problem
        Given the user is on 'Air Export New Shipment' page
        When the user enter AE MAWB 'Shipment' datas as 'A'
            | field        | attribute | action | data             |
            | Gross Weight | input     | input  | {randInt(1,999)} |
            | Buying Rate  | input     | input  | {randInt(1,10)}  |
            | Selling Rate | input     | input  | {randInt(1,10)}  |
        And the user click save button
        Then amount should be autofilled with right numbers

    @SFI @LOHAN @OLC
    Scenario: Input 'Gross Weight' then 'Chargeable Weight' should be autofilled with the same value
        Given the user is on 'Air Export New Shipment' page
        When the user enter '100' for field 'Gross Weight' in AE 'new shipment' page for MAWB
        And the user click 'Gross Weight LB' for AE MAWB
        Then 'Chargeable Weight' value should be the same as 'Gross Weight' value for AE MAWB

    @SFI @LOHAN @OLC
    Scenario: Input 'Departure' and 'Destination' then those in 'Connecting Flight' should be autofilled with the same value
        Given the user is on 'Air Export New Shipment' page
        When the user enter AE MAWB 'Shipment' datas as 'A'
            | field       | attribute    | action | data |
            | Departure   | autocomplete | input  | gru  |
            | Destination | autocomplete | input  | abq  |
        And the user click save button
        Then 'Departure' value should be the same as 'Departure' value in 'Connecting Flight'
        And 'Destination' value should be the same as 'Destination' value in 'Connecting Flight'

    @SFI @LOHAN @OLC
    Scenario: Click cancel button sould not affect current 'Dimensions' value
        Given the user is on 'Air Export New Shipment' page
        When the user click AE MAWB 'Set Dimensions' button
        And the user input Length, Width, Height and PCS for AE MAWB 'A' 'Volume Weight'
            | Length           | Width            | Height           | PCS             |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
        And the user save AE 'Dimensions' settings
        And the user click AE MAWB 'Set Dimensions' button
        And the user cancel AE 'Dimensions' settings
        Then the AE 'A' 'Volume Weight' won't change
        And field 'Chargeable Weight' for AE MAWB should be autofilled with right numbers

    @SFI @LOHAN @OLC
    Scenario: Click cancel button sould not affect current 'Route' value
        Given the user is on 'Air Export New Shipment' page
        When the user click AE MAWB 'Connecting Flight' button
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
        And the user click AE MAWB 'Connecting Flight' button
        And the user cancel AE MAWB 'Route' settings
        Then the AE 'A' 'Route' won't change

    @SFI @LOHAN @OLC
    Scenario: Input multiple rows for 'Volume Weight' is no problem
        Given the user is on 'Air Export New Shipment' page
        When the user click AE MAWB 'Set Dimensions' button
        And the user input Length, Width, Height and PCS for AE MAWB 'A' 'Volume Weight'
            | Length           | Width            | Height           | PCS             |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
        Then the AE MAWB 'A' 'Volume Weight' data are correct
        And the AE MAWB 'A' summarized 'Volume Weight' data are correct
        When the user save AE 'Dimensions' settings
        Then 'Volume Weight' data in the 'New Shipment' page for AE MAWB 'A' are correct
        And field 'Chargeable Weight' for AE MAWB should be autofilled with right numbers

    @SFI @LOHAN @OLC
    Scenario: Copy button in More block is no problem
        Given the user is on 'Air Export New Shipment' page
        When the user expand MAWB 'More' block
        And the user enter AE MAWB 'A' 'More' datas
            | field                | attribute | action | data                                           |
            | P.O. No.             | tag input | input  | {randomNo(6)}                                  |
            | Mark                 | input     | input  | THIS IS AIR EXPORT - MBL : MARK                |
            | Handling Information | input     | input  | THIS IS AIR EXPORT - MAWB HANDLING INFORMATION |
        And the user input information for AE MAWB 'A' 'Commodity'
            | Commodity Description | HTS Code         |
            | {randomCommodity}     | HTS{randomNo(6)} |
        And the user click 'Copy P.O.' button for AE MAWB
        Then the 'Nature and Quantity of Goods' field are correct
        When the user click 'Copy Commodity' button for AE MAWB
        Then the 'Nature and Quantity of Goods' field are correct
        When the user click 'Copy Commodity & HTS' button for AE MAWB
        Then the 'Nature and Quantity of Goods' field are correct
