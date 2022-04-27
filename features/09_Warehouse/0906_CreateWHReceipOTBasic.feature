@SFI @LOHAN @OLC
Feature: [Warehouse] Create Receipt - Other

    the operator can create a receipt (cargo type is other)

    Background: Log in GoFreight with Operator
        Given the user is a 'Operator'

    Scenario: The storage day is no problem
        Given the user is on 'New Receipt' page
        When the user enter 'others' receipt basic datas as 'A'
            | field            | attribute  | action | data            |
            | Loaded Date/Time | datepicker | input  | {today+5} 16:00 |
        Then the storage day is correct

    Scenario: Generate a new receipt whose cargo type is other
        Given the user is on 'New Receipt' page
        When the user enter 'others' receipt basic datas as 'A'
            | field                | attribute    | action               | data                                                               |
            | Received Date/Time   | datepicker   | input                | {today+1} 13:00                                                    |
            | Received By          | select       | random select        |                                                                    |
            | Truck B/L No.        | input        | input                | TK-{randomNo(6)}                                                   |
            | Location             | input        | input                | {randomCity}                                                       |
            | Loaded Date/Time     | datepicker   | input                | {today+6} 16:00                                                    |
            | Maker                | autocomplete | input                | {randomTradePartner}                                               |
            | Shipper              | autocomplete | input and close memo | {randomTradePartner}                                               |
            | Consignee            | autocomplete | input                | {randomTradePartner}                                               |
            | Delivered Carrier    | input        | input                | {randomTradePartner}                                               |
            | Delivered By         | input        | input                | {randomTradePartner}                                               |
            | Amount               | input        | input                | {randN(6)}                                                         |
            | Check No.            | input        | input                | CHK-{randN(4)}                                                     |
            | Hazardous Goods      | checkbox     | tick                 | {randomOnOff}                                                      |
            | Heat Treated Pallets | checkbox     | tick                 | {randomOnOff}                                                      |
            | Commodity            | input        | input                | THIS IS WAREHOUSE RECEIPT ON COMMODITY TEXTAREA                    |
            | P.O. No.             | input        | input                | PO-{randomNo(6)}                                                   |
            | Remark               | input        | input                | THIS IS WAREHOUSE RECEIPT ON REMARK TEXTAREA FOR AUTOMOBILE SCRIPT |
        And the user input receipt 'A' dimension datas
            | Length     | Width      | Height     | Dimension     | PKG        | Unit          | Sku PO        | Pallet     | Total PCS  | Act. Weight KGS |
            | {randN(2)} | {randN(2)} | {randN(2)} | random select | {randN(2)} | random select | SKU{randN(6)} | {randN(2)} | {randN(1)} | randN(3)        |
            | {randN(2)} | {randN(2)} | {randN(2)} | random select | {randN(2)} | random select | SKU{randN(6)} | {randN(2)} | {randN(1)} | randN(3)        |
        And the user click WH 'Save' button
        Then the 'others' receipt 'A' will be created
        And the receipt 'A' total dimension is correct
        And the 'others' receipt 'A' dimension data will be saved

    Scenario: Link a others receipt to a HBL is no problem
        Given the user has a OI MBL with 1 HBL as 'A' with only required fields filled
        And the user is on 'New Receipt' page
        When the user enter 'others' receipt basic datas as 'A'
            | field              | attribute  | action | data            |
            | Received Date/Time | datepicker | input  | {today+1} 13:00 |
        And the user input receipt 'A' dimension datas
            | Length     | Width      | Height     | Dimension     | PKG        | Unit          | Sku PO        | Pallet     | Total PCS  | Act. Weight KGS |
            | {randN(2)} | {randN(2)} | {randN(2)} | random select | {randN(2)} | random select | SKU{randN(6)} | {randN(2)} | {randN(1)} | randN(3)        |
        And the user link dimension(1) in receipt to OI 'A' HBL(1)
