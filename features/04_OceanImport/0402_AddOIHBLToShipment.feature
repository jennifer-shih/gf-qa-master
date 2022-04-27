@SFI @LOHAN @OLC
Feature: [OceanImport] Add OI HBL To Shipment

    the operator can add HB/L(s) to the shipment which has been created

    Background: Log in GoFreight with Operator
        Given the user is a 'Operator'


    Scenario: Add a HB/L to shipment
        Given the user has a OI MBL with 0 HBL as 'A' with only required fields filled
        When the user click OI 'Add HBL' button
        And the user click OI HBL(1) 'More' button
        And the user enter 'OI HBL(1)' shipment datas as 'A' and save it
            | field                   | attribute        | action                  | data                 |
            | HB/L No.                | input            | input                   | 111-{randomNo(6)}    |
            | AMS No.                 | input            | input                   | AMS{randN(6)}        |
            | ISF No.                 | input            | input                   | ISF{randN(6)}        |
            | ISF Filing by 3rd Party | checkbox         | tick                    | {randomOnOff}        |
            | Shipper                 | autocomplete     | input                   | {randomTradePartner} |
            | Consignee               | autocomplete     | input and close memo    | {randomTradePartner} |
            | Customs Broker          | autocomplete     | input                   | {randomTradePartner} |
            | Trucker                 | autocomplete     | input                   | {randomTradePartner} |
            | Available               | datepicker       | input                   | {today+5}            |
            | Freight                 | select           | random select           |                      |
            | LFD                     | datepicker       | input                   | {today+6}            |
            | Rail                    | check select     | random_check_and_select |                      |
            | G.O Date                | datepicker       | input                   | {today+7}            |
            | Expiry Date             | datepicker       | input                   | {today+9}            |
            | Sales Type              | select           | random select           |                      |
            | Incoterms               | select           | random select           |                      |
            | Cargo Type              | select           | random select           |                      |
            | Door Move               | checkbox         | tick                    | {randomOnOff}        |
            | C.Clearance             | checkbox         | tick                    | {randomOnOff}        |
            | C.Hold                  | checkbox         | tick                    | {randomOnOff}        |
            | C. Released Date        | datepicker       | input                   | {today+8}            |
            | Business Referred By    | autocomplete     | input                   | {randomTradePartner} |
            | OB/L Received           | check datepicker | tick                    | {on}                 |
            | ROR                     | checkbox         | tick                    | {randomOnOff}        |
            | Frt. Released           | check datepicker | tick and close memo     |                      |
            | Door Delivered          | datepicker       | input                   | {today+10}           |
            | L/C No.                 | input            | input                   | LC{randN(6)}         |
            | Ship Type               | select           | random select           |                      |
            | S/C No.                 | input            | input                   | SCNO{randN(6)}       |
            | Name Account            | input            | input                   | NA{randN(6)}         |
            | Group Comm              | input            | input                   | GC{randN(6)}         |
            | Line Code               | input            | input                   | LC{randN(6)}         |
            | E-Commerce              | checkbox         | tick                    | {randomOnOff}        |
        Then the shipment 'A' HBL(1) of 'Ocean Import' will be created


    Scenario: Add another HB/L to shipment
        Given the user has a OI MBL with 1 HBL as 'A' with only required fields filled
        When the user click OI 'Add HBL' button
        And the user click OI HBL(2) 'More' button
        And the user enter 'OI HBL(2)' shipment datas as 'A' and save it
            | field                   | attribute        | action                  | data                 |
            | HB/L No.                | input            | input                   | 111-{randomNo(6)}    |
            | AMS No.                 | input            | input                   | AMS{randN(6)}        |
            | ISF No.                 | input            | input                   | ISF{randN(6)}        |
            | ISF Filing by 3rd Party | checkbox         | tick                    | {randomOnOff}        |
            | Shipper                 | autocomplete     | input                   | {randomTradePartner} |
            | Consignee               | autocomplete     | input and close memo    | {randomTradePartner} |
            | Customs Broker          | autocomplete     | input                   | {randomTradePartner} |
            | Trucker                 | autocomplete     | input                   | {randomTradePartner} |
            | Available               | datepicker       | input                   | {today+5}            |
            | Freight                 | select           | random select           |                      |
            | LFD                     | datepicker       | input                   | {today+6}            |
            | Rail                    | check select     | random_check_and_select |                      |
            | G.O Date                | datepicker       | input                   | {today+7}            |
            | Expiry Date             | datepicker       | input                   | {today+9}            |
            | Sales Type              | select           | random select           |                      |
            | Incoterms               | select           | random select           |                      |
            | Cargo Type              | select           | random select           |                      |
            | Door Move               | checkbox         | tick                    | {randomOnOff}        |
            | C.Clearance             | checkbox         | tick                    | {randomOnOff}        |
            | C.Hold                  | checkbox         | tick                    | {randomOnOff}        |
            | C. Released Date        | datepicker       | input                   | {today+8}            |
            | Business Referred By    | autocomplete     | input                   | {randomTradePartner} |
            | OB/L Received           | check datepicker | tick                    | {on}                 |
            | ROR                     | checkbox         | tick                    | {randomOnOff}        |
            | Frt. Released           | check datepicker | tick and close memo     |                      |
            | Door Delivered          | datepicker       | input                   | {today+10}           |
            | L/C No.                 | input            | input                   | LC{randN(6)}         |
            | Ship Type               | select           | random select           |                      |
            | S/C No.                 | input            | input                   | SCNO{randN(6)}       |
            | Name Account            | input            | input                   | NA{randN(6)}         |
            | Group Comm              | input            | input                   | GC{randN(6)}         |
            | Line Code               | input            | input                   | LC{randN(6)}         |
            | E-Commerce              | checkbox         | tick                    | {randomOnOff}        |
        Then the shipment 'A' HBL(2) of 'Ocean Import' will be created


    Scenario: Add a HB/L to new shipment and fill in quotation no. field
        Given the user has a OI MBL with 0 HBL as 'A' with only required fields filled
        When the user click OI 'Add HBL' button
        And the user enter 'OI HBL(1)' shipment datas as 'A' and save it
            | field         | attribute    | action               | data              |
            | HB/L No.      | input        | input                | 111-{randomNo(6)} |
            | Customer      | autocomplete | input and close memo | CUSTOMER9191      |
            | Quotation No. | autocomplete | input                | QT                |
        Then the shipment 'A' HBL(1) of 'Ocean Import' will be created


    Scenario: Add OI HBL with required fields only
        Given the user has a OI MBL with 0 HBL as 'A' with only required fields filled
        When the user click OI 'Add HBL' button
        And the user enter 'OI HBL(1)' shipment datas as 'A' and save it
            | field    | attribute    | action               | data              |
            | HB/L No. | input        | input                | 111-{randomNo(6)} |
            | Customer | autocomplete | input and close memo | CUSTOMER9191      |
        Then the shipment 'A' HBL(1) of 'Ocean Import' will be created
