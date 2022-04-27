Feature: [Truck] Create TK Shipment

     the operator can create a shipment of Truck

     Background: Log in GoFreight with Operator
          Given the user is a 'Operator'

     @SFI @LOHAN @OLC
     Scenario: The operator want to go to 'New Shipment' page of Truck
          Given the user is on 'Dashboard' page
          When the user browse to 'New Shipment of Truck' page by navigator
          Then 'New Shipment of Truck' page show normally

     @SFI
     Scenario: Generate a new shipment with required fields only and default value should be correct (For SFI)
          Given the user is on 'Truck New Shipment' page
          When the user enter 'TK MBL' shipment datas as 'A' and save it
               | field     | attribute    | action | data    |
               | Post Date | datepicker   | input  | {today} |
               | Office    | autocomplete | input  | LAX     |
          Then the shipment 'A' of 'Truck' will be created

     @LOHAN
     Scenario: Generate a new shipment with required fields only and default value should be correct (For LOHAN)
          Given the user is on 'Truck New Shipment' page
          When the user enter 'TK MBL' shipment datas as 'A' and save it
               | field     | attribute    | action | data    |
               | Post Date | datepicker   | input  | {today} |
               | Office    | autocomplete | input  | SZX     |
          Then the shipment 'A' of 'Truck' will be created

     @OLC
     Scenario: Generate a new shipment with required fields only and default value should be correct (For OLC)
          Given the user is on 'Truck New Shipment' page
          When the user enter 'TK MBL' shipment datas as 'A' and save it
               | field     | attribute    | action | data          |
               | Post Date | datepicker   | input  | {today}       |
               | Office    | autocomplete | input  | 拼箱部        |
               | Sales     | autocomplete | input  | {randomSales} |
          Then the shipment 'A' of 'Truck' will be created

     @SFI @LOHAN
     Scenario: Generate a new shipment and fill in quotation no. field (For generic)
          Given the user is on 'Truck New Shipment' page
          When the user enter 'TK MBL' shipment datas as 'A' and save it
               | field         | attribute    | action               | data         |
               | Post Date     | datepicker   | input                | {today}      |
               | Customer      | autocomplete | input and close memo | CUSTOMER9191 |
               | Quotation No. | autocomplete | input                | QT           |
          Then the shipment 'A' of 'Truck' will be created

     @OLC
     Scenario: Generate a new shipment and fill in quotation no. field (For OLC)
          Given the user is on 'Truck New Shipment' page
          When the user enter 'TK MBL' shipment datas as 'A' and save it
               | field         | attribute    | action               | data          |
               | Post Date     | datepicker   | input                | {today}       |
               | Customer      | autocomplete | input and close memo | CUSTOMER9191  |
               | Quotation No. | autocomplete | input                | QT            |
               | Sales         | autocomplete | input                | {randomSales} |
          Then the shipment 'A' of 'Truck' will be created

     @SFI @LOHAN @OLC
     Scenario: Generate a new shipment
          Given the user is on 'Truck New Shipment' page
          When the user click TK 'More' button
          And the user enter 'TK MBL' shipment datas as 'A' and save it
               | field                   | attribute    | action               | data                 |
               | Post Date               | datepicker   | input                | {today}              |
               | MB/L No.                | input        | input                | 555-{randomNo(5)}(M) |
               | HB/L No.                | input        | input                | 555-{randomNo(5)}(H) |
               | Vessel/Flight No.       | input        | input                | VSN{randomNo(5)}     |
               | Carrier Bkg. No.        | input        | input                | CBN{randomNo(5)}     |
               | Customer                | autocomplete | input and close memo | {randomTradePartner} |
               | Customer Ref. No.       | input        | input                | CRN{randomNo(5)}     |
               | Shipper                 | autocomplete | input                | {randomTradePartner} |
               | Consignee               | autocomplete | input                | {randomTradePartner} |
               | Trucker                 | autocomplete | input                | {randomTradePartner} |
               | Ship Type               | select       | random select        |                      |
               | Port of Loading         | autocomplete | input                | {randomPort}         |
               | Departure               | autocomplete | input                | AAF                  |
               | ETD                     | datepicker   | input                | {today+2}            |
               | Port of Discharge       | autocomplete | input                | {randomPort}         |
               | Destination             | autocomplete | input                | AOP                  |
               | ETA                     | datepicker   | input                | {today+5}            |
               | Final Destination       | autocomplete | input                | CAPDO                |
               | Final ETA               | datepicker   | input                | {today+7}            |
               | Empty Pickup            | autocomplete | input                | {randomTradePartner} |
               | Freight Pickup          | autocomplete | input                | {randomTradePartner} |
               | Delivery To             | autocomplete | input                | {randomTradePartner} |
               | Empty Return            | autocomplete | input                | {randomTradePartner} |
               | Package                 | input        | input                | {randN(3)}           |
               | Weight KG               | input        | input                | {randN(3)}           |
               | Measurement CBM         | input        | input                | {randN(3)}           |
               | Estimated Delivery Date | datepicker   | input                | {today+8}            |
               | Delivered               | checkbox     | tick                 | {randomOnOff}        |
               | E-Commerce              | checkbox     | tick                 | {randomOnOff}        |
          Then the shipment 'A' of 'Truck' will be created
