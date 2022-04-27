@SFI @LOHAN
Feature: [Warehouse] Create Receipt - Automobile

    the operator can create a receipt (cargo type is Automobile)

    Background: Log in GoFreight with Operator
        Given the user is a 'Operator'

    Scenario: Generate a new receipt whose cargo type is automobile
        Given the user is on 'New Receipt' page
        When the user enter 'automobile' receipt basic datas as 'A'
            | field                    | attribute    | action               | data                                                               |
            | Received Date/Time       | datepicker   | input                | {today+1} 13:00                                                    |
            | Received By              | select       | random select        |                                                                    |
            | Truck B/L No.            | input        | input                | TK-{randomNo(6)}                                                   |
            | Location                 | input        | input                | {randomCity}                                                       |
            | Loaded Date/Time         | datepicker   | input                | {today+6} 16:00                                                    |
            | Maker                    | autocomplete | input                | {randomTradePartner}                                               |
            | Shipper                  | autocomplete | input and close memo | {randomTradePartner}                                               |
            | Consignee                | autocomplete | input                | {randomTradePartner}                                               |
            | Delivered Carrier        | input        | input                | {randomTradePartner}                                               |
            | Delivered By             | input        | input                | {randomTradePartner}                                               |
            | Amount                   | input        | input                | {randN(6)}                                                         |
            | Check No.                | input        | input                | CHK-{randN(4)}                                                     |
            | Cargo Type               | radio group  | click                | Automobile                                                         |
            | Hazardous Goods          | checkbox     | tick                 | {randomOnOff}                                                      |
            | Heat Treated Pallets     | checkbox     | tick                 | {randomOnOff}                                                      |
            | AM Vin No.               | autocomplete | input                | {randomVin}                                                        |
            | AM Tag No.               | input        | input                | tag{randN(6)}                                                      |
            | AM Customer              | autocomplete | input                | {randomTradePartner}                                               |
            | AM Maker                 | input        | input                | {randomTradePartner}                                               |
            | AM Year                  | input        | input                | 20{randN(2)}                                                       |
            | AM Model                 | input        | input                | {randomModel}                                                      |
            | AM Color                 | input        | input                | {randomColor}                                                      |
            | AM Engine No.            | input        | input                | EN-{randN(8)}                                                      |
            | AM Manufacture Year      | autocomplete | input                | {randInt(1900,2019)}                                               |
            | AM Manufacture Month     | autocomplete | input                | {randInt(1,12)}                                                    |
            | AM Title Received Status | checkbox     | tick                 | {randomOnOff}                                                      |
            | AM Condition             | input        | input                | CND-{randN(8)}                                                     |
            | AM Key                   | input        | input                | {randInt(0,10)}                                                    |
            | AM Fuel                  | input        | input                | F-{randN(2)}%                                                      |
            | AM Tire Size (Front)     | input        | input                | {randN(3)} / {randN(2)} / R{randN(2)}                              |
            | AM Tire Size (Rear)      | input        | input                | {randN(3)} / {randN(2)} / R{randN(2)}                              |
            | AM Mileage               | input        | input                | {randN(4)}                                                         |
            | AM W.STICKER             | radio group  | random click         |                                                                    |
            | AM Remote Control        | radio group  | random click         |                                                                    |
            | AM Headphone             | radio group  | random click         |                                                                    |
            | AM Owner's Manual        | radio group  | random click         |                                                                    |
            | AM CD Player             | radio group  | random click         |                                                                    |
            | AM CD Changer            | radio group  | random click         |                                                                    |
            | AM First Aid Kit         | radio group  | random click         |                                                                    |
            | AM Floor Mat             | radio group  | random click         |                                                                    |
            | AM Cigarette Lighter     | radio group  | random click         |                                                                    |
            | AM Cargo Net             | radio group  | random click         |                                                                    |
            | AM Ashtray               | radio group  | random click         |                                                                    |
            | AM Tools                 | radio group  | random click         |                                                                    |
            | AM Spare Tire            | radio group  | random click         |                                                                    |
            | AM Sun Roof              | radio group  | random click         |                                                                    |
            | P.O. No.                 | input        | input                | PO-{randomNo(6)}                                                   |
            | Remark                   | input        | input                | This is Warehouse Receipt on remark textarea for Automobile script |
        And the user input receipt 'A' dimension datas
            | Length     | Width      | Height     | Dimension     | PKG        | Unit          | Sku PO        | Pallet     | Total PCS  | Act. Weight KGS |
            | {randN(2)} | {randN(2)} | {randN(2)} | random select | {randN(2)} | random select | SKU{randN(6)} | {randN(2)} | {randN(1)} | randN(3)        |
            | {randN(2)} | {randN(2)} | {randN(2)} | random select | {randN(2)} | random select | SKU{randN(6)} | {randN(2)} | {randN(1)} | randN(3)        |
        And the user click WH 'Save' button
        Then the 'automobile' receipt 'A' will be created
        And the receipt 'A' total dimension is correct
        And the 'automobile' receipt 'A' dimension data will be saved

    Scenario: Link a automobile receipt to a HBL is no problem
        Given the user has a OI MBL with 1 HBL as 'A'
        And the user is on 'New Receipt' page
        When the user enter 'automobile' receipt basic datas as 'A'
            | field              | attribute    | action | data                 |
            | Received Date/Time | datepicker   | input  | {today+1} 13:00      |
            | Cargo Type         | radio group  | click  | Automobile           |
            | AM Vin No.         | autocomplete | input  | {randomVin}          |
            | AM Customer        | autocomplete | input  | {randomTradePartner} |
        And the user input receipt 'A' dimension datas
            | Length     | Width      | Height     | Dimension     | PKG        | Unit          | Sku PO        | Pallet     | Total PCS  | Act. Weight KGS |
            | {randN(2)} | {randN(2)} | {randN(2)} | random select | {randN(2)} | random select | SKU{randN(6)} | {randN(2)} | {randN(1)} | randN(3)        |
        And the user link dimension(1) in receipt to OI 'A' HBL(1)
