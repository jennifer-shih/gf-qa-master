Feature: [AirImport] Add AI HAWB To Shipment

    the operator can add HAWB(s) to the shipment which has been created

    Background: Log in GoFreight with Operator
        Given the user is a 'Operator'

    @SFI @LOHAN
    Scenario: Add a HAWB to shipment with required fields only (For generic)
        Given the user has an AI Shipment without any HAWB
        When the user enter AI MAWB 'Shipment' datas as 'A'
            | field              | attribute    | action | data                 |
            | Freight Location   | autocomplete | input  | {randomTradePartner} |
            | Storage Start Date | datepicker   | input  | {today+3}            |
        And the user click AI 'Add HAWB' button
        And the user enter AI shipment 'A' HAWB(1) datas
            | field    | attribute | action | data              |
            | HAWB No. | input     | input  | 333-{randomNo(7)} |
        And the user click save button
        Then the freight location for AI HAWB(1) is the same as in MAWB
        And the storage start date for AI HAWB(1) is the same as in MAWB
        And the default pakage unit for AI HAWB(1) is correct

    @OLC
    Scenario: Add a HAWB to shipment with required fields only (For enterprise)
        Given the user has an AI Shipment without any HAWB
        When the user enter AI MAWB 'Shipment' datas as 'A'
            | field              | attribute    | action | data                 |
            | Freight Location   | autocomplete | input  | {randomTradePartner} |
            | Storage Start Date | datepicker   | input  | {today+3}            |
        And the user click AI 'Add HAWB' button
        And the user enter AI shipment 'A' HAWB(1) datas
            | field    | attribute    | action | data              |
            | HAWB No. | input        | input  | 333-{randomNo(7)} |
            | Sales    | autocomplete | input  | {randomSales}     |
        And the user click save button
        Then the freight location for AI HAWB(1) is the same as in MAWB
        And the storage start date for AI HAWB(1) is the same as in MAWB
        And the default pakage unit for AI HAWB(1) is correct

    @SFI @LOHAN @OLC
    Scenario: Fill in HAWB data
        Given the user has a AI MAWB with 0 HAWB as 'A' with only required fields filled
        When the user click AI 'Add HAWB' button
        And the user click AI HAWB(1) 'More' button
        And the user enter AI shipment 'A' HAWB(1) datas
            | field                         | attribute    | action               | data                                       |
            | HAWB No.                      | input        | input                | 333-{randomNo(7)}                          |
            | HSN                           | input        | input                | HSN{randomNo(6)}                           |
            | Shipper                       | autocomplete | input                | {randomTradePartner}                       |
            | Consignee                     | autocomplete | input and close memo | {randomTradePartner}                       |
            | Customs Broker                | autocomplete | input                | {randomTradePartner}                       |
            | Final Destination             | autocomplete | input                | usdhd                                      |
            | Final ETA                     | datepicker   | input                | {today+4}                                  |
            | Trucker                       | autocomplete | input                | {randomTradePartner}                       |
            | Last Free Day                 | datepicker   | input                | {today+12}                                 |
            | Freight                       | select       | random select        |                                            |
            | Sales Type                    | select       | random select        |                                            |
            | Package                       | input        | input                | {randInt(1,999)}                           |
            | Gross Weight                  | input        | input                | {randInt(1,999)}                           |
            | IT NO.                        | input        | input                | ITN{randN(6)}                              |
            | Class of Entry                | input        | input                | COE{randomNo(4)}                           |
            | IT Date                       | datepicker   | input                | {today+10}                                 |
            | IT Issued Location            | autocomplete | input                | 1901                                       |
            | Cargo Released To             | input        | input                | CARGO{randN(4)}                            |
            | C. Released Date              | datepicker   | input                | {today+11}                                 |
            | Door Delivered                | datepicker   | input                | {today+11}                                 |
            | Ship Type                     | select       | random select        |                                            |
            | Incoterms                     | select       | random select        |                                            |
            | Service Term From             | select       | random select        |                                            |
            | Service Term To               | select       | random select        |                                            |
            | E-Commerce                    | checkbox     | tick                 | {randomOnOff}                              |
            | Customer Reference / P.O. No. | tag input    | input                | {randomNo(6)}                              |
            | Mark                          | input        | input                | THis is Air Import - HAWB : MARK           |
            | Description                   | input        | input                | THis is Air Import - HAWB : DESCRIPTION    |
            | Remark                        | input        | input                | THis is Air Import - HAWB : REMARK SECTION |
        And the user click AI HAWB(1) 'Set Dimensions' button
        And the user input Length, Width, Height and PCS for AI shipment 'A' HAWB(1) 'Volume Weight'
            | Length           | Width            | Height           | PCS             |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
        And the user save AI 'Dimensions' settings
        And the user input information for AI shipment 'A' HAWB(1) 'Sub HAWB'
            | Sub HAWB     | Description / IT No.     | PCS        | PKG Unit | Amount     |
            | SUBHAWB TEXT | SUBHAWB TEXT_DESCRIPTION | {randN(2)} | tank     | {randN(3)} |
        And the user input information for AI shipment 'A' HAWB(1) 'Commodity'
            | Commodity Description | HTS Code         |
            | {randomCommodity}     | HTS{randomNo(6)} |
        And the user click Air 'Save' button
        Then the shipment 'A' HAWB(1) in 'Air Import' will be created
        And the AI shipment 'A' HAWB(1) 'Volume Weight' data is saved
        And the AI shipment 'A' HAWB(1) 'Sub HAWB' data is saved
        And the AI shipment 'A' HAWB(1) 'Commodity' data is saved

    @SFI @LOHAN @OLC
    Scenario: Add a HAWB to shipment and fill in quotation no. field
        Given the user has a AI MAWB with 0 HAWB as 'A' with only required fields filled
        When the user click AI 'Add HAWB' button
        And the user enter AI shipment 'A' HAWB(1) datas
            | field         | attribute    | action               | data              |
            | HAWB No.      | input        | input                | 111-{randomNo(6)} |
            | Customer      | autocomplete | input and close memo | CUSTOMER9191      |
            | Quotation No. | autocomplete | input                | QT                |
        And the user click Air 'Save' button
        Then the shipment 'A' HAWB(1) in 'Air Import' will be created
