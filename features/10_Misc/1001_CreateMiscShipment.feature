Feature: [Misc] Create Misc Shipment

     the operator can create a shipment of Misc

     Background: Log in GoFreight with Operator
          Given the user is a 'Operator'

     @SFI @LOHAN @OLC
     Scenario: The operator want to go to 'New Operation' page of Misc
          Given the user is on 'Dashboard' page
          When the user browse to 'New Operation of Misc' page by navigator
          Then 'New Operation of Misc' page show normally

     @SFI @LOHAN
     Scenario: Generate a new operation with required fields only and default value should be correct (For generic)
          Given the user is on 'Misc New Operation' page
          When the user enter 'MS MBL' new shipment page as 'A' and save it
          Then the shipment 'A' of 'Misc' will be created

     @OLC
     Scenario: Generate a new operation with required fields only and default value should be correct (For enterprise)
          Given the user is on 'Misc New Operation' page
          When the user enter 'MS MBL' shipment datas as 'A' and save it
               | field     | attribute    | action | data          |
               | Post Date | datepicker   | input  | {today}       |
               | Office    | autocomplete | input  | QD            |
               | Sales     | autocomplete | input  | {randomSales} |
          Then the shipment 'A' of 'Misc' will be created

     @SFI @LOHAN
     Scenario: Generate a new operation and fill in quotation no. field (For generic)
          Given the user is on 'Misc New Operation' page
          When the user enter 'MS MBL' shipment datas as 'A' and save it
               | field         | attribute    | action               | data         |
               | Post Date     | datepicker   | input                | {today}      |
               | Customer      | autocomplete | input and close memo | CUSTOMER9191 |
               | Quotation No. | autocomplete | input                | QT           |
          Then the shipment 'A' of 'Misc' will be created

     @OLC
     Scenario: Generate a new operation and fill in quotation no. field (For enterprise)
          Given the user is on 'Misc New Operation' page
          When the user enter 'MS MBL' shipment datas as 'A' and save it
               | field         | attribute    | action               | data          |
               | Post Date     | datepicker   | input                | {today}       |
               | Customer      | autocomplete | input and close memo | CUSTOMER9191  |
               | Quotation No. | autocomplete | input                | QT            |
               | Sales         | autocomplete | input                | {randomSales} |
          Then the shipment 'A' of 'Misc' will be created

     @SFI @LOHAN @OLC
     Scenario: Generate a new operation
          Given the user is on 'Misc New Operation' page
          When the user click MS 'More' button
          And the user enter 'MS MBL' shipment datas as 'A' and save it
               | field             | attribute    | action               | data                 |
               | Post Date         | datepicker   | input                | {today}              |
               | MB/L No.          | input        | input                | 555-{randomNo(5)}(M) |
               | HB/L No.          | input        | input                | 555-{randomNo(5)}(H) |
               | Vessel/Flight No. | input        | input                | VSN{randomNo(5)}     |
               | Customer          | autocomplete | input and close memo | {randomTradePartner} |
               | Customer Ref. No. | input        | input                | CRN{randomNo(5)}     |
               | Shipper           | autocomplete | input                | {randomTradePartner} |
               | Consignee         | autocomplete | input                | {randomTradePartner} |
               | Trucker           | autocomplete | input                | {randomTradePartner} |
               | Oversea Agent     | autocomplete | input                | {randomTradePartner} |
               | Sales             | autocomplete | input                | {randomSale}         |
               | Ship Type         | select       | random select        |                      |
               | Service Term From | select       | random select        |                      |
               | Service Term To   | select       | random select        |                      |
               | Port of Loading   | autocomplete | input                | {randomPort}         |
               | Departure         | autocomplete | input                | AAF                  |
               | ETD               | datepicker   | input                | {today+2}            |
               | Port of Discharge | autocomplete | input                | {randomPort}         |
               | Destination       | autocomplete | input                | AOP                  |
               | ETA               | datepicker   | input                | {today+5}            |
               | Final Destination | autocomplete | input                | CAPDO                |
               | Final ETA         | datepicker   | input                | {today+7}            |
               | Empty Pickup      | autocomplete | input                | {randomTradePartner} |
               | Freight Pickup    | autocomplete | input                | {randomTradePartner} |
               | Delivery To       | autocomplete | input                | {randomTradePartner} |
               | Empty Return      | autocomplete | input                | {randomTradePartner} |
               | Package           | input        | input                | {randN(3)}           |
               | Package Unit      | autocomplete | input                | {randomUnit}         |
               | Weight KG         | input        | input                | {randN(3)}           |
               | Measurement CBM   | input        | input                | {randN(3)}           |
               | E-Commerce        | checkbox     | tick                 | {randomOnOff}        |
          Then the shipment 'A' of 'Misc' will be created
