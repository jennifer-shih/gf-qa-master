@SFI @LOHAN @OLC
Feature: [AirImport] AI MAWB Function Test

    linked fields of AI MAWB and some features work no problem

    Background: Log in GoFreight with Operator
        Given the user is a 'Operator'

    Scenario: Input 'Gross Weight' then 'Chargeable Weight' should be autofilled with the same value
        Given the user is on 'Air Import New Shipment' page
        When the user enter '100' for field 'Gross Weight' in AI 'new shipment' page for MAWB
        And the user click 'Gross Weight LB' for AI MAWB
        Then 'Chargeable Weight' value should be the same as 'Gross Weight' value for AI MAWB

    Scenario: Input 'Departure' and 'Destination' then those in 'Connecting Flight' should be autofilled with the same value
        Given the user is on 'Air Import New Shipment' page
        When the user enter AI MAWB 'Shipment' datas as 'A'
            | field       | attribute    | action | data |
            | Departure   | autocomplete | input  | gru  |
            | Destination | autocomplete | input  | abq  |
        And the user click save button
        Then 'Departure' value should be the same as 'Departure' value in 'Connecting Flight'
        And 'Destination' value should be the same as 'Destination' value in 'Connecting Flight'

    Scenario: Click cancel button sould not affect current 'Dimensions' value
        Given the user is on 'Air Import New Shipment' page
        When the user click AI MAWB 'Set Dimensions' button
        And the user input Length, Width, Height and PCS for AI MAWB 'A' 'Volume Weight'
            | Length           | Width            | Height           | PCS             |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
        And the user save AI 'Dimensions' settings
        And the user click AI MAWB 'Set Dimensions' button
        And the user cancel AI 'Dimensions' settings
        Then the AI shipment 'A' 'Volume Weight' won't change
        And field 'Chargeable Weight' for AI MAWB should be autofilled with right numbers

    Scenario: Click cancel button sould not affect current 'Route' value
        Given the user is on 'Air Import New Shipment' page
        When the user click AI MAWB 'Connecting Flight' button
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
        And the user click AI MAWB 'Connecting Flight' button
        And the user cancel AI MAWB 'Route' settings
        Then the AI shipment 'A' 'Route' won't change

    Scenario: Input multiple rows for 'Volume Weight' is no problem
        Given the user is on 'Air Import New Shipment' page
        When the user click AI MAWB 'Set Dimensions' button
        And the user input Length, Width, Height and PCS for AI MAWB 'A' 'Volume Weight'
            | Length           | Width            | Height           | PCS             |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
        Then the AI MAWB 'A' 'Volume Weight' data are correct
        And the AI MAWB 'A' summarized 'Volume Weight' data are correct
        When the user save AI 'Dimensions' settings
        Then 'Volume Weight' data in the 'New Shipment' page for AI MAWB are correct
        And field 'Chargeable Weight' for AI MAWB should be autofilled with right numbers
