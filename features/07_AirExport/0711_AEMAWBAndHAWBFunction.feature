Feature: [AirExport] AE MAWB and HAWB Function Test

    linked fields of AE M/HAWB and some features work no problem

    Background: Log in GoFreight with Operator
        Given the user is a 'Operator'

    @SFI @LOHAN @OLC
    Scenario: 'Customer', 'Bill To' should be the same values as 'Actual Shipper'
        Given the user has an AE Shipment without any HAWB
        When the user click AE 'Add HAWB' button
        And the user click AE HAWB(1) 'More' button
        And the user enter AE shipment 'A' HAWB(1) 'Shipment' datas
            | field          | attribute    | action               | data                 |
            | Actual Shipper | autocomplete | input and close memo | {randomTradePartner} |
        And the user click save button
        Then 'Customer', 'Bill To' should be the same values as 'Actual Shipper' for HAWB(1)

    @SFI @LOHAN @OLC
    Scenario: Input weight value in 2 ways
        Given the user has a AE MAWB with 1 HAWB as 'A' with only required fields filled
        When the user enter '100' for field 'Gross Weight (SHPR)' in AE 'new shipment' page for HAWB(1)
        And the user click 'Gross Weight (SHPR) LB' for AE HAWB(1)
        Then all 'Weight' fields for AE HAWB(1) should be autofilled with right numbers
        When the user click AE HAWB(1) 'Set Dimensions' button
        And the user input Length, Width, Height and PCS for AE shipment 'A' HAWB(1) 'Volume Weight'
            | Length           | Width            | Height           | PCS             |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
        Then the AE shipment 'A' HAWB(1) 'Volume Weight' data are correct
        And the AE shipment 'A' HAWB(1) summarized 'Volume Weight' data are correct
        When the user save AE 'Dimensions' settings
        And the user click save button
        Then 'Volume Weight' data in the 'New Shipment' page for AE shipment 'A' HAWB(1) are correct
        And all 'Weight' fields for AE HAWB(1) should be autofilled with right numbers

    @SFI @LOHAN @OLC
    Scenario: Copy button in More block is no problem
        Given the user has a AE MAWB with 1 HAWB as 'A' with only required fields filled
        When the user enter AE shipment 'A' HAWB(1) 'Shipment' datas
            | field                        | attribute | action | data                                        |
            | P.O. No.                     | tag input | input  | {randomNo(6)}                               |
            | Nature and Quantity of Goods | input     | input  | THIS IS HAWB : NATURE AND QUANTITY OF GOODS |
        And the user input information for AE shipment 'A' HAWB(1) 'Commodity'
            | Commodity Description | HTS Code         |
            | {randomCommodity}     | HTS{randomNo(6)} |
        And the user click 'Copy P.O.' button for AE HAWB(1)
        Then the 'Nature and Quantitfy of Goods' field for AE HAWB(1) are correct
        When the user click 'Copy Commodity' button for AE HAWB(1)
        Then the 'Nature and Quantitfy of Goods' field for AE HAWB(1) are correct
        When the user click 'Copy Commodity & HTS' button for AE HAWB(1)
        And the user click save button
        Then the 'Nature and Quantitfy of Goods' field for AE HAWB(1) are correct

    @SFI
    Scenario: Create 2nd HAWB and HAWB default value should be correct when having multiple HAWBs
        Given the user has a AE MAWB with 1 HAWB as 'A' with only required fields filled
        When the user expand AE MAWB block
        And the user enter AE MAWB 'Shipment' datas as 'A'
            | field                     | attribute    | action               | data                 |
            | AWB Date                  | datepicker   | input                | {today}              |
            | Consignee (Oversea Agent) | autocomplete | input and close memo | {randomTradePartner} |
            | Departure                 | autocomplete | input                | gru                  |
            | Destination               | autocomplete | input                | abq                  |
            | WT/VAL                    | radio group  | random click         |                      |
            | Other                     | radio group  | random click         |                      |
        And the user click save button
        And the user click AE 'Add HAWB' button
        And the user click AE HAWB(2) 'More' button
        And the user click save button
        Then AE HAWB(2) fileds should be same as MAWB
            | MAWB          | HAWB          |
            | AWB Date      | Booking Date  |
            | Oversea Agent | Oversea Agent |
            | Departure     | Departure     |
            | Destination   | Destination   |
            | D.V. Carriage | D.V. Carriage |
            | D.V. Customs  | D.V. Customs  |
            | Insurance     | Insurance     |
        And AE HAWB(2) fields should be
            | field           | value                     |
            | ITN NO.         | NO EEI 30.37(a)           |
            | Issuing Carrier | STRAIGHT FORWARDING, INC. |
            | WT/VAL          | PPD                       |
            | Other           | PPD                       |

    @LOHAN
    Scenario: Create 2nd HAWB and HAWB default value should be correct when having multiple HAWBs
        Given the user has a AE MAWB with 1 HAWB as 'A' with only required fields filled
        When the user expand AE MAWB block
        And the user enter AE MAWB 'Shipment' datas as 'A'
            | field                     | attribute    | action               | data                 |
            | AWB Date                  | datepicker   | input                | {today}              |
            | Consignee (Oversea Agent) | autocomplete | input and close memo | {randomTradePartner} |
            | Departure                 | autocomplete | input                | gru                  |
            | Destination               | autocomplete | input                | abq                  |
            | WT/VAL                    | radio group  | random click         |                      |
            | Other                     | radio group  | random click         |                      |
        And the user click save button
        And the user click AE 'Add HAWB' button
        And the user click AE HAWB(2) 'More' button
        And the user click save button
        Then AE HAWB(2) fileds should be same as MAWB
            | MAWB          | HAWB          |
            | AWB Date      | Booking Date  |
            | Oversea Agent | Oversea Agent |
            | Departure     | Departure     |
            | Destination   | Destination   |
            | D.V. Carriage | D.V. Carriage |
            | D.V. Customs  | D.V. Customs  |
            | Insurance     | Insurance     |
        And AE HAWB(2) fields should be
            | field           | value           |
            | ITN NO.         | NO EEI 30.37(a) |
            | Issuing Carrier | LHL             |
            | WT/VAL          | PPD             |
            | Other           | PPD             |

    @OLC
    Scenario: Create 2nd HAWB and HAWB default value should be correct when having multiple HAWBs
        Given the user has a AE MAWB with 1 HAWB as 'A' with only required fields filled
        When the user expand AE MAWB block
        And the user enter AE MAWB 'Shipment' datas as 'A'
            | field                     | attribute    | action               | data                 |
            | AWB Date                  | datepicker   | input                | {today}              |
            | Consignee (Oversea Agent) | autocomplete | input and close memo | {randomTradePartner} |
            | Departure                 | autocomplete | input                | gru                  |
            | Destination               | autocomplete | input                | abq                  |
            | WT/VAL                    | radio group  | random click         |                      |
            | Other                     | radio group  | random click         |                      |
        And the user click save button
        And the user click AE 'Add HAWB' button
        And the user click AE HAWB(2) 'More' button
        And the user click save button
        Then AE HAWB(2) fileds should be same as MAWB
            | MAWB          | HAWB          |
            | AWB Date      | Booking Date  |
            | Oversea Agent | Oversea Agent |
            | Departure     | Departure     |
            | Destination   | Destination   |
            | D.V. Carriage | D.V. Carriage |
            | D.V. Customs  | D.V. Customs  |
            | Insurance     | Insurance     |
        And AE HAWB(2) fields should be
            | field           | value                                        |
            | ITN NO.         | NO EEI 30.37(a)                              |
            | Issuing Carrier | 东方超捷国际货运代理(深圳)有限公司青岛分公司 |
            | WT/VAL          | PPD                                          |
            | Other           | PPD                                          |


    @SFI
    Scenario: Fill in 2nd HAWB data
        Given the user has a AE MAWB with 2 HAWB as 'A' with only required fields filled
        When the user click AE HAWB(2) 'More' button
        And the user enter AE shipment 'A' HAWB(2) 'Shipment' datas
            | field                                 | attribute | action | data                                                            |
            | P.O. No.                              | tag input | input  | {randomNo(6)}                                                   |
            | Mark                                  | input     | input  | THIS IS AIR EXPORT - HBL : MARK                                 |
            | Nature and Quantity of Goods          | input     | input  | THIS IS HAWB : NATURE AND QUANTITY OF GOODS                     |
            | Manifest Nature and Quantity of Goods | input     | input  | THIS IS AIR EXPORT - HAWB MENIFEST NATURE AND QUANTITY OF GOODS |
            | Handling Information                  | input     | input  | THIS IS AIR EXPORT - HAWB HANDLING INFORMATION                  |
        And the user input information for AE shipment 'A' HAWB(2) 'Commodity'
            | Commodity Description | HTS Code         |
            | {randomCommodity}     | HTS{randomNo(6)} |
        And the user click Air 'Save' button
        Then the shipment 'A' HAWB(2) in 'Air Export' will be created
        And the AE shipment 'A' HAWB(2) 'Commodity' data is saved

    @LOHAN @OLC
    Scenario: Fill in 2nd HAWB data
        Given the user has a AE MAWB with 2 HAWB as 'A' with only required fields filled
        When the user click AE HAWB(2) 'More' button
        And the user enter AE shipment 'A' HAWB(2) 'Shipment' datas
            | field                        | attribute | action | data                                           |
            | P.O. No.                     | tag input | input  | {randomNo(6)}                                  |
            | Mark                         | input     | input  | THIS IS AIR EXPORT - HBL : MARK                |
            | Nature and Quantity of Goods | input     | input  | THIS IS HAWB : NATURE AND QUANTITY OF GOODS    |
            | Handling Information         | input     | input  | THIS IS AIR EXPORT - HAWB HANDLING INFORMATION |
        And the user input information for AE shipment 'A' HAWB(2) 'Commodity'
            | Commodity Description | HTS Code         |
            | {randomCommodity}     | HTS{randomNo(6)} |
        And the user click Air 'Save' button
        Then the shipment 'A' HAWB(2) in 'Air Export' will be created
        And the AE shipment 'A' HAWB(2) 'Commodity' data is saved

    @SFI @LOHAN @OLC
    Scenario: Description should be autofilled with the same value after choosing charge item
        Given the user has a AE MAWB with 2 HAWB as 'A' with only required fields filled
        When the user input information for AE shipment 'A' HAWB(2) 'Other Charge'
            | Carrier/Agent | Collect/Prepaid | Charge Amount    |
            | CARRIER       | PREPAID         | {randInt(1,999)} |
            | AGENT         | COLLECT         | {randInt(1,999)} |
        And the user click Air 'Save' button
        Then the AE shipment 'A' HAWB(2) 'Other Charge' data is saved

    @SFI @LOHAN @OLC
    Scenario: Sum up package & weight is no problem
        Given the user has a AE MAWB with 2 HAWB as 'A' with only required fields filled
        When the user enter '100' for field 'Gross Weight (SHPR)' in AE 'new shipment' page for HAWB(1)
        And the user click 'Gross Weight (SHPR) LB' for AE HAWB(1)
        And the user click save button
        And the user enter '200' for field 'Gross Weight (SHPR)' in AE 'new shipment' page for HAWB(2)
        And the user click 'Gross Weight (SHPR) LB' for AE HAWB(2)
        Then all 'Weight' fields for AE HAWB(2) should be autofilled with right numbers
        When the user click AE HAWB(2) 'Set Dimensions' button
        And the user input Length, Width, Height and PCS for AE shipment 'A' HAWB(2) 'Volume Weight'
            | Length           | Width            | Height           | PCS             |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
        Then the AE shipment 'A' HAWB(2) 'Volume Weight' data are correct
        And the AE shipment 'A' HAWB(2) summarized 'Volume Weight' data are correct
        When the user save AE 'Dimensions' settings
        And the user click save button
        Then 'Volume Weight' data in the 'New Shipment' page for AE shipment 'A' HAWB(2) are correct
        And all 'Weight' fields for AE HAWB(2) should be autofilled with right numbers
        When the user expand AE MAWB block
        And the user click AE 'Sum Package & Weight' button
        Then the HAWBs weight should be sumed up in AE MAWB block
        And all 'Weight' fields for AE HAWB(2) should be autofilled with right numbers
