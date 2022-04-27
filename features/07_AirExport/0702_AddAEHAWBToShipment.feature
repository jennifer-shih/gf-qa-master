Feature: [AirExport] Add AE HAWB To Shipment

    the operator can add HAWB(s) to the shipment which has been created

    Background: Log in GoFreight with Operator
        Given the user is a 'Operator'

    @SFI
    Scenario: Add a HAWB to shipment and the default value should be correct (SFI)
        Given the user has an AE Shipment without any HAWB
        When the user fills in AE MAWB 'Basic' data as 'A'
            | field                     | attribute    | action               | data                 |
            | AWB Date                  | datepicker   | input                | {today}              |
            | Consignee (Oversea Agent) | autocomplete | input and close memo | {randomTradePartner} |
            | Departure                 | autocomplete | input                | gru                  |
            | Destination               | autocomplete | input                | abq                  |
            | WT/VAL                    | radio group  | random click         |                      |
            | Other                     | radio group  | random click         |                      |
        And the user click AE 'Add HAWB' button
        And the user click save button
        Then AE HAWB(1) fileds should be same as MAWB
            | MAWB          | HAWB          |
            | AWB Date      | Booking Date  |
            | Oversea Agent | Oversea Agent |
            | Departure     | Departure     |
            | Destination   | Destination   |
            | D.V. Carriage | D.V. Carriage |
            | D.V. Customs  | D.V. Customs  |
            | Insurance     | Insurance     |
        And AE HAWB(1) fields should be
            | field           | value                     |
            | ITN NO.         | NO EEI 30.37(a)           |
            | Issuing Carrier | STRAIGHT FORWARDING, INC. |
            | WT/VAL          | PPD                       |
            | Other           | PPD                       |

    @LOHAN
    Scenario: Add a HAWB to shipment and the default value should be correct (LOHAN)
        Given the user has an AE Shipment without any HAWB
        When the user fills in AE MAWB 'Basic' data as 'A'
            | field                     | attribute    | action               | data                 |
            | AWB Date                  | datepicker   | input                | {today}              |
            | Consignee (Oversea Agent) | autocomplete | input and close memo | {randomTradePartner} |
            | Departure                 | autocomplete | input                | gru                  |
            | Destination               | autocomplete | input                | abq                  |
            | WT/VAL                    | radio group  | random click         |                      |
            | Other                     | radio group  | random click         |                      |
        And the user click AE 'Add HAWB' button
        And the user click save button
        Then AE HAWB(1) fileds should be same as MAWB
            | MAWB          | HAWB          |
            | AWB Date      | Booking Date  |
            | Oversea Agent | Oversea Agent |
            | Departure     | Departure     |
            | Destination   | Destination   |
            | D.V. Carriage | D.V. Carriage |
            | D.V. Customs  | D.V. Customs  |
            | Insurance     | Insurance     |
        And AE HAWB(1) fields should be
            | field           | value           |
            | ITN NO.         | NO EEI 30.37(a) |
            | Issuing Carrier | LHL             |
            | WT/VAL          | PPD             |
            | Other           | PPD             |

    @OLC
    Scenario: Add a HAWB to shipment and the default value should be correct (OLC)
        Given the user has an AE Shipment without any HAWB
        When the user fills in AE MAWB 'Basic' data as 'A'
            | field                     | attribute    | action               | data                 |
            | AWB Date                  | datepicker   | input                | {today}              |
            | Consignee (Oversea Agent) | autocomplete | input and close memo | {randomTradePartner} |
            | Departure                 | autocomplete | input                | gru                  |
            | Destination               | autocomplete | input                | abq                  |
            | WT/VAL                    | radio group  | random click         |                      |
            | Other                     | radio group  | random click         |                      |
        And the user click AE 'Add HAWB' button
        And the user enter 'AE HAWB(1)' shipment datas as 'A' and save it
            | field | attribute    | action | data          |
            | Sales | autocomplete | input  | {randomSales} |
        Then AE HAWB(1) fileds should be same as MAWB
            | MAWB          | HAWB          |
            | AWB Date      | Booking Date  |
            | Oversea Agent | Oversea Agent |
            | Departure     | Departure     |
            | Destination   | Destination   |
            | D.V. Carriage | D.V. Carriage |
            | D.V. Customs  | D.V. Customs  |
            | Insurance     | Insurance     |
        And AE HAWB(1) fields should be
            | field           | value                                        |
            | ITN NO.         | NO EEI 30.37(a)                              |
            | Issuing Carrier | 东方超捷国际货运代理(深圳)有限公司青岛分公司 |
            | WT/VAL          | PPD                                          |
            | Other           | PPD                                          |


    @SFI
    Scenario: Fill in HAWB data (For SFI)
        Given the user has a AE MAWB with 1 HAWB as 'A' with only required fields filled
        When the user click AE HAWB(1) 'More' button
        And the user enter AE shipment 'A' HAWB(1) 'Shipment' datas
            | field                                 | attribute    | action               | data                                                            |
            | Actual Shipper                        | autocomplete | input and close memo | {randomTradePartner}                                            |
            | Consignee                             | autocomplete | input                | {randomTradePartner}                                            |
            | Notify                                | autocomplete | input                | {randomTradePartner}                                            |
            | Trucker                               | autocomplete | input                | {randomTradePartner}                                            |
            | Cargo Pickup                          | autocomplete | input                | {randomTradePartner}                                            |
            | Delivery To/Pier                      | autocomplete | input                | {randomTradePartner}                                            |
            | Cargo Type                            | select       | random select        |                                                                 |
            | Sales Type                            | select       | random select        |                                                                 |
            | Ship Type                             | select       | random select        |                                                                 |
            | WT/VAL                                | radio group  | random click         |                                                                 |
            | Other                                 | radio group  | random click         |                                                                 |
            | Incoterms                             | select       | random select        |                                                                 |
            | Service Term From                     | select       | random select        |                                                                 |
            | Service Term To                       | select       | random select        |                                                                 |
            | Package                               | input        | input                | {randInt(1,10)}                                                 |
            | Buying Rate                           | input        | input                | {randInt(1,10)}                                                 |
            | Selling Rate                          | input        | input                | {randInt(1,10)}                                                 |
            | Volume Weight                         | input        | input                | {randInt(1,999)}                                                |
            | Gross Weight (SHPR)                   | input        | input                | {randInt(1,999)}                                                |
            | L/C NO.                               | input        | input                | LC{randN(6)}                                                    |
            | L/C Issue Bank                        | input        | input                | LCB{randN(6)}                                                   |
            | L/C Issue Date                        | datepicker   | input                | {today+10}                                                      |
            | Customer Ref. No.                     | input        | input                | CR{randN(6)}                                                    |
            | Agent Ref. No.                        | input        | input                | AN{randN(6)}                                                    |
            | Export Ref. No.                       | input        | input                | EX{randN(6)}                                                    |
            | Rate                                  | select       | random select        |                                                                 |
            | E-Commerce                            | checkbox     | tick                 | {randomOnOff}                                                   |
            | P.O. No.                              | tag input    | input                | {randomNo(6)}                                                   |
            | Mark                                  | input        | input                | THIS IS AIR EXPORT - HBL : MARK                                 |
            | Nature and Quantity of Goods          | input        | input                | THIS IS HAWB : NATURE AND QUANTITY OF GOODS                     |
            | Manifest Nature and Quantity of Goods | input        | input                | THIS IS AIR EXPORT - HAWB MENIFEST NATURE AND QUANTITY OF GOODS |
            | Handling Information                  | input        | input                | THIS IS AIR EXPORT - HAWB HANDLING INFORMATION                  |
        And the user input information for AE shipment 'A' HAWB(1) 'Commodity'
            | Commodity Description | HTS Code         |
            | {randomCommodity}     | HTS{randomNo(6)} |
        And the user input information for AE shipment 'A' HAWB(1) 'Other Charge'
            | Carrier/Agent | Collect/Prepaid | Charge Amount    |
            | CARRIER       | PREPAID         | {randInt(1,999)} |
            | AGENT         | COLLECT         | {randInt(1,999)} |
        And the user expand HAWB(1) 'More' block
        And the user enter AE shipment 'A' HAWB(1) 'More' datas
            | field                                | attribute | action | data             |
            | Prepaid Valuation                    | input     | input  | {randInt(1,999)} |
            | Prepaid Tax                          | input     | input  | {randInt(1,999)} |
            | Prepaid Currency Conversion Rates    | input     | input  | {randInt(1,999)} |
            | Collect Valuation                    | input     | input  | {randInt(1,999)} |
            | Collect Tax                          | input     | input  | {randInt(1,999)} |
            | Collect CC Charges in Dest. Currency | input     | input  | {randInt(1,999)} |
            | Collect Charges at Destination       | input     | input  | {randInt(1,999)} |
        And the user click Air 'Save' button
        Then the shipment 'A' HAWB(1) in 'Air Export' will be created
        And the AE shipment 'A' HAWB(1) 'Other Charge' data is saved
        And the AE shipment 'A' HAWB(1) 'Commodity' data is saved

    @LOHAN @OLC
    Scenario: Fill in HAWB data (For LOHAN, OLC)
        Given the user has a AE MAWB with 1 HAWB as 'A' with only required fields filled
        When the user click AE HAWB(1) 'More' button
        And the user enter AE shipment 'A' HAWB(1) 'Shipment' datas
            | field                        | attribute    | action               | data                                           |
            | Actual Shipper               | autocomplete | input and close memo | {randomTradePartner}                           |
            | Consignee                    | autocomplete | input                | {randomTradePartner}                           |
            | Notify                       | autocomplete | input                | {randomTradePartner}                           |
            | Trucker                      | autocomplete | input                | {randomTradePartner}                           |
            | Cargo Pickup                 | autocomplete | input                | {randomTradePartner}                           |
            | Delivery To/Pier             | autocomplete | input                | {randomTradePartner}                           |
            | Cargo Type                   | select       | random select        |                                                |
            | Sales Type                   | select       | random select        |                                                |
            | Ship Type                    | select       | random select        |                                                |
            | WT/VAL                       | radio group  | random click         |                                                |
            | Other                        | radio group  | random click         |                                                |
            | Incoterms                    | select       | random select        |                                                |
            | Service Term From            | select       | random select        |                                                |
            | Service Term To              | select       | random select        |                                                |
            | Package                      | input        | input                | {randInt(1,10)}                                |
            | Buying Rate                  | input        | input                | {randInt(1,10)}                                |
            | Selling Rate                 | input        | input                | {randInt(1,10)}                                |
            | Volume Weight                | input        | input                | {randInt(1,999)}                               |
            | Gross Weight (SHPR)          | input        | input                | {randInt(1,999)}                               |
            | L/C NO.                      | input        | input                | LC{randN(6)}                                   |
            | L/C Issue Bank               | input        | input                | LCB{randN(6)}                                  |
            | L/C Issue Date               | datepicker   | input                | {today+10}                                     |
            | Customer Ref. No.            | input        | input                | CR{randN(6)}                                   |
            | Agent Ref. No.               | input        | input                | AN{randN(6)}                                   |
            | Export Ref. No.              | input        | input                | EX{randN(6)}                                   |
            | Rate                         | select       | random select        |                                                |
            | E-Commerce                   | checkbox     | tick                 | {randomOnOff}                                  |
            | P.O. No.                     | tag input    | input                | {randomNo(6)}                                  |
            | Mark                         | input        | input                | THIS IS AIR EXPORT - HBL : MARK                |
            | Nature and Quantity of Goods | input        | input                | THIS IS HAWB : NATURE AND QUANTITY OF GOODS    |
            | Handling Information         | input        | input                | THIS IS AIR EXPORT - HAWB HANDLING INFORMATION |
        And the user input information for AE shipment 'A' HAWB(1) 'Commodity'
            | Commodity Description | HTS Code         |
            | {randomCommodity}     | HTS{randomNo(6)} |
        And the user input information for AE shipment 'A' HAWB(1) 'Other Charge'
            | Carrier/Agent | Collect/Prepaid | Charge Amount    |
            | CARRIER       | PREPAID         | {randInt(1,999)} |
            | AGENT         | COLLECT         | {randInt(1,999)} |
        And the user expand HAWB(1) 'More' block
        And the user enter AE shipment 'A' HAWB(1) 'More' datas
            | field                                | attribute | action | data             |
            | Prepaid Valuation                    | input     | input  | {randInt(1,999)} |
            | Prepaid Tax                          | input     | input  | {randInt(1,999)} |
            | Prepaid Currency Conversion Rates    | input     | input  | {randInt(1,999)} |
            | Collect Valuation                    | input     | input  | {randInt(1,999)} |
            | Collect Tax                          | input     | input  | {randInt(1,999)} |
            | Collect CC Charges in Dest. Currency | input     | input  | {randInt(1,999)} |
            | Collect Charges at Destination       | input     | input  | {randInt(1,999)} |
        And the user click Air 'Save' button
        Then the shipment 'A' HAWB(1) in 'Air Export' will be created
        And the AE shipment 'A' HAWB(1) 'Other Charge' data is saved
        And the AE shipment 'A' HAWB(1) 'Commodity' data is saved

    @SFI @LOHAN @OLC
    Scenario: 'Volume Weight' is no problem
        Given the user has a AE MAWB with 1 HAWB as 'A' with only required fields filled
        When the user click AE HAWB(1) 'Set Dimensions' button
        And the user input Length, Width, Height and PCS for AE shipment 'A' HAWB(1) 'Volume Weight'
            | Length           | Width            | Height           | PCS             |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
        And the user save AE 'Dimensions' settings
        And the user click Air 'Save' button
        Then the AE shipment 'A' HAWB(1) 'Volume Weight' data is saved

    @SFI @LOHAN @OLC
    Scenario: Add a HAWB to shipment and fill in quotation no. field
        Given the user has a AE MAWB with 1 HAWB as 'A' with only required fields filled
        When the user click AE 'Add HAWB' button
        And the user enter AE shipment 'A' HAWB(2) 'Shipment' datas
            | field         | attribute    | action               | data         |
            | Customer      | autocomplete | input and close memo | CUSTOMER9191 |
            | Quotation No. | autocomplete | input                | QT           |
        And the user click Air 'Save' button
        Then the shipment 'A' HAWB(2) in 'Air Export' will be created
