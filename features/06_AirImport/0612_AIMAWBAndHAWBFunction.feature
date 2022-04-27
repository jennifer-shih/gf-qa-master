Feature: [AirImport] AI MAWB and HAWB Function Test

    linked fields of AI M/HAWB and some features work no problem

    Background: Log in GoFreight with Operator
        Given the user is a 'Operator'

    @SFI @LOHAN @OLC
    Scenario: 'Notify', 'Customer', 'Bill To', 'Delivery Location' should be the same values as 'Consignee'
        Given the user has an AI Shipment without any HAWB
        When the user click AI 'Add HAWB' button
        And the user click AI HAWB(1) 'More' button
        And the user enter AI shipment 'A' HAWB(1) datas
            | field     | attribute    | action               | data                 |
            | HAWB No.  | input        | input                | 333-{randomNo(7)}    |
            | HSN       | input        | input                | HSN{randomNo(6)}     |
            | Shipper   | autocomplete | input                | {randomTradePartner} |
            | Consignee | autocomplete | input and close memo | {randomTradePartner} |
        And the user click save button
        Then 'Notify', 'Customer', 'Bill To', 'Delivery Location' should be the same values as 'Consignee' for HAWB(1)

    @SFI @LOHAN @OLC
    Scenario: Input weight value in 2 ways
        Given the user has a AI MAWB with 1 HAWB as 'A' with only required fields filled
        When the user enter '100' for field 'Gross Weight' in AI 'new shipment' page for HAWB(1)
        And the user click 'Gross Weight LB' for AI HAWB(1)
        Then field 'Chargeable Weight' for AI HAWB(1) should be autofilled with right numbers
        When the user click AI HAWB(1) 'Set Dimensions' button
        And the user input Length, Width, Height and PCS for AI shipment 'A' HAWB(1) 'Volume Weight'
            | Length           | Width            | Height           | PCS             |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
        Then the AI shipment 'A' HAWB(1) 'Volume Weight' data are correct
        And the AI shipment 'A' HAWB(1) summarized 'Volume Weight' data are correct
        When the user save AI 'Dimensions' settings
        And the user click save button
        Then 'Volume Weight' data in the 'New Shipment' page for AI HAWB(1) are correct
        And field 'Chargeable Weight' for AI HAWB(1) should be autofilled with right numbers

    @SFI @LOHAN @OLC
    Scenario: Copy button in More block is no problem
        Given the user has a AI MAWB with 1 HAWB as 'A' with only required fields filled
        When the user enter AI shipment 'A' HAWB(1) datas
            | field                         | attribute | action | data                                       |
            | Customer Reference / P.O. No. | tag input | input  | {randomNo(6)}                              |
            | Mark                          | input     | input  | THis is Air Import - HAWB : MARK           |
            | Description                   | input     | input  | THis is Air Import - HAWB : DESCRIPTION    |
            | Remark                        | input     | input  | THis is Air Import - HAWB : REMARK SECTION |
        And the user input information for AI shipment 'A' HAWB(1) 'Commodity'
            | Commodity Description | HTS Code         |
            | {randomCommodity}     | HTS{randomNo(6)} |
        And the user click 'Copy P.O.' button for AI HAWB(1)
        Then the 'Description' field for AI HAWB(1) are correct
        When the user click 'Copy Commodity' button for AI HAWB(1)
        Then the 'Description' field for AI HAWB(1) are correct
        When the user click 'Copy Commodity & HTS' button for AI HAWB(1)
        Then the 'Description' field for AI HAWB(1) are correct

    @SFI @LOHAN @OLC
    Scenario: Create 2nd HAWB and HAWB default value should be correct when having multiple HAWBs
        Given the user has a AI MAWB with 1 HAWB as 'A' with only required fields filled
        When the user click AI 'Add HAWB' button
        And the user click AI HAWB(2) 'More' button
        And the user enter AI shipment 'A' HAWB(2) datas
            | field     | attribute    | action               | data                 |
            | HAWB No.  | input        | input                | 333-{randomNo(7)}    |
            | HSN       | input        | input                | HSN{randomNo(6)}     |
            | Shipper   | autocomplete | input                | {randomTradePartner} |
            | Consignee | autocomplete | input and close memo | {randomTradePartner} |
        And the user click save button
        Then the freight location for AI HAWB(2) is the same as in MAWB
        And the storage start date for AI HAWB(2) is the same as in MAWB
        And the default pakage unit for AI HAWB(2) is correct

    @SFI @LOHAN
    Scenario: Fill in 2nd HAWB data (For Generic)
        Given the user has a AI MAWB with 1 HAWB as 'A' with only required fields filled
        When the user click AI 'Add HAWB' button
        And the user click AI HAWB(2) 'More' button
        And the user enter AI shipment 'A' HAWB(2) datas
            | field                         | attribute | action | data                                       |
            | HAWB No.                      | input     | input  | 333-{randomNo(7)}                          |
            | E-Commerce                    | checkbox  | tick   | {randomOnOff}                              |
            | Customer Reference / P.O. No. | tag input | input  | {randomNo(6)}                              |
            | Mark                          | input     | input  | THis is Air Import - HAWB : MARK           |
            | Description                   | input     | input  | THis is Air Import - HAWB : DESCRIPTION    |
            | Remark                        | input     | input  | THis is Air Import - HAWB : REMARK SECTION |
        #   And the user close AI MAWB block
        And the user input information for AI shipment 'A' HAWB(2) 'Sub HAWB'
            | Sub HAWB     | Description / IT No.     | PCS        | PKG Unit | Amount     |
            | SUBHAWB TEXT | SUBHAWB TEXT_DESCRIPTION | {randN(2)} | tank     | {randN(3)} |
        And the user input information for AI shipment 'A' HAWB(2) 'Commodity'
            | Commodity Description | HTS Code         |
            | {randomCommodity}     | HTS{randomNo(6)} |
        And the user click Air 'Save' button
        Then the shipment 'A' HAWB(2) in 'Air Import' will be created
        And the AI shipment 'A' HAWB(2) 'Sub HAWB' data is saved
        And the AI shipment 'A' HAWB(2) 'Commodity' data is saved

    @OLC
    Scenario: Fill in 2nd HAWB data (For Enterprise)
        Given the user has a AI MAWB with 1 HAWB as 'A' with only required fields filled
        When the user click AI 'Add HAWB' button
        And the user click AI HAWB(2) 'More' button
        And the user enter AI shipment 'A' HAWB(2) datas
            | field                         | attribute    | action | data                                       |
            | HAWB No.                      | input        | input  | 333-{randomNo(7)}                          |
            | Sales                         | autocomplete | input  | {randomSales}                              |
            | E-Commerce                    | checkbox     | tick   | {randomOnOff}                              |
            | Customer Reference / P.O. No. | tag input    | input  | {randomNo(6)}                              |
            | Mark                          | input        | input  | THis is Air Import - HAWB : MARK           |
            | Description                   | input        | input  | THis is Air Import - HAWB : DESCRIPTION    |
            | Remark                        | input        | input  | THis is Air Import - HAWB : REMARK SECTION |
        #   And the user close AI MAWB block
        And the user input information for AI shipment 'A' HAWB(2) 'Sub HAWB'
            | Sub HAWB     | Description / IT No.     | PCS        | PKG Unit | Amount     |
            | SUBHAWB TEXT | SUBHAWB TEXT_DESCRIPTION | {randN(2)} | tank     | {randN(3)} |
        And the user input information for AI shipment 'A' HAWB(2) 'Commodity'
            | Commodity Description | HTS Code         |
            | {randomCommodity}     | HTS{randomNo(6)} |
        And the user click Air 'Save' button
        Then the shipment 'A' HAWB(2) in 'Air Import' will be created
        And the AI shipment 'A' HAWB(2) 'Sub HAWB' data is saved
        And the AI shipment 'A' HAWB(2) 'Commodity' data is saved

    @SFI @LOHAN @OLC
    Scenario: Sum up package & weight is no problem
        Given the user has a AI MAWB with 2 HAWB as 'A' with only required fields filled
        When the user enter '200' for field 'Gross Weight' in AI 'new shipment' page for HAWB(1)
        And the user click 'Gross Weight LB' for AI HAWB(1)
        Then field 'Chargeable Weight' for AI HAWB(1) should be autofilled with right numbers
        When the user click AI HAWB(1) 'Set Dimensions' button
        And the user input Length, Width, Height and PCS for AI shipment 'A' HAWB(1) 'Volume Weight'
            | Length           | Width            | Height           | PCS             |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
        Then the AI shipment 'A' HAWB(1) 'Volume Weight' data are correct
        And the AI shipment 'A' HAWB(1) summarized 'Volume Weight' data are correct
        When the user save AI 'Dimensions' settings
        And the user click save button
        Then 'Volume Weight' data in the 'New Shipment' page for AI HAWB(1) are correct
        And field 'Chargeable Weight' for AI HAWB(1) should be autofilled with right numbers

        When the user enter '200' for field 'Gross Weight' in AI 'new shipment' page for HAWB(2)
        And the user click 'Gross Weight LB' for AI HAWB(2)
        Then field 'Chargeable Weight' for AI HAWB(2) should be autofilled with right numbers
        When the user click AI HAWB(2) 'Set Dimensions' button
        And the user input Length, Width, Height and PCS for AI shipment 'A' HAWB(2) 'Volume Weight'
            | Length           | Width            | Height           | PCS             |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
            | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,200)} | {randInt(1,99)} |
        Then the AI shipment 'A' HAWB(2) 'Volume Weight' data are correct
        And the AI shipment 'A' HAWB(2) summarized 'Volume Weight' data are correct
        When the user save AI 'Dimensions' settings
        And the user click save button
        Then 'Volume Weight' data in the 'New Shipment' page for AI HAWB(2) are correct
        And field 'Chargeable Weight' for AI HAWB(2) should be autofilled with right numbers

        When the user expand AI MAWB block
        And the user click AI 'Sum Package & Weight' button
        Then the HAWBs weight should be sumed up in AI MAWB block
        And field 'Chargeable Weight' for AI MAWB should be autofilled with right numbers
