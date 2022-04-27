Feature: [OceanImport] Create OI Shipment

     the operator can create a shipment of Ocean Import

     Background: Log in GoFreight with Operator
          Given the user is a 'Operator'

     @SFI @LOHAN @OLC
     Scenario: The operator want to go to 'New Shipment' page of Ocean Import
          Given the user is on 'Dashboard' page
          When the user browse to 'New Shipment of Ocean Import' page by navigator
          Then 'New Shipment of Ocean Import' page show normally


     @SFI
     Scenario: Generate a new shipment with required fields only and default value should be correct (For SFI)
          Given the user is on 'Ocean Import New Shipment' page
          When the user enter 'OI MBL' shipment datas as 'A' and save it
               | field    | attribute    | action | data            |
               | MB/L No. | input        | input  | HACO-{randN(6)} |
               | Office   | autocomplete | input  | LAX             |
               | ETA      | datepicker   | input  | {today+5}       |
          Then the shipment 'A' of 'Ocean Import' will be created


     @LOHAN
     Scenario: Generate a new shipment with required fields only and default value should be correct (For LOHAN)
          Given the user is on 'Ocean Import New Shipment' page
          When the user enter 'OI MBL' shipment datas as 'A' and save it
               | field    | attribute    | action | data            |
               | MB/L No. | input        | input  | HACO-{randN(6)} |
               | Office   | autocomplete | input  | SZX             |
               | ETA      | datepicker   | input  | {today+5}       |
          Then the shipment 'A' of 'Ocean Import' will be created


     @OLC
     Scenario: Generate a new shipment with required fields only and default value should be correct (For OLC)
          Given the user is on 'Ocean Import New Shipment' page
          When the user enter 'OI MBL' shipment datas as 'A' and save it
               | field    | attribute    | action | data            |
               | MB/L No. | input        | input  | HACO-{randN(6)} |
               | Office   | autocomplete | input  | 拼箱部          |
               | ETA      | datepicker   | input  | {today+5}       |
          Then the shipment 'A' of 'Ocean Import' will be created


     @SFI @LOHAN @OLC
     Scenario: Generate a new shipment
          Given the user is on 'Ocean Import New Shipment' page
          When the user click OI MBL 'More' button
          And the user enter 'OI MBL' shipment datas as 'A' and save it
               | field                  | attribute    | action        | data                 |
               | MB/L No.               | input        | input         | HACO-{randN(6)}      |
               | B/L Type               | select       | random select |                      |
               | Oversea Agent          | autocomplete | input         | {randomTradePartner} |
               | Carrier                | autocomplete | input         | OCEAN9191            |
               | Forwarding Agent       | autocomplete | input         | {randomTradePartner} |
               | Co-loader              | autocomplete | input         | {randomTradePartner} |
               | Agent Ref No.          | input        | input         | AGE{randN(6)}        |
               | Sub B/L No.            | input        | input         | SBL{randomNo(6)}     |
               | Vessel                 | autocomplete | input         | {randomVessel}       |
               | Voyage                 | input        | input         | VY{randomNo(6)}      |
               | CY Location            | autocomplete | input         | {randomTradePartner} |
               | CFS Location           | autocomplete | input         | {randomTradePartner} |
               | Port of Loading        | autocomplete | input         | {randomPort}         |
               | ETD                    | datepicker   | input         | {today+1}            |
               | Port of Discharge      | autocomplete | input         | {randomPort}         |
               | ETA                    | datepicker   | input         | {today+2}            |
               | Place of Delivery      | autocomplete | input         | {randomPort}         |
               | Place of Delivery ETA  | datepicker   | input         | {today+3}            |
               | Final Destination      | autocomplete | input         | {randomPort}         |
               | Final ETA              | datepicker   | input         | {today+4}            |
               | Freight                | select       | random select |                      |
               | Ship Mode              | select       | random select |                      |
               | OB/L Type              | select       | random select |                      |
               | OB/L Received          | checkbox     | tick          | {on}                 |
               | Telex release received | checkbox     | tick          | {on}                 |
               | Released Date          | checkbox     | tick          | {on}                 |
               | Business Referred By   | autocomplete | input         | {randomTradePartner} |
               | Place of Receipt       | autocomplete | input         | {randomPort}         |
               | Place of Receipt ETD   | datepicker   | input         | {today+5}            |
               | Return Location        | autocomplete | input         | {randomTradePartner} |
               | IT No.                 | input        | input         | IT{randomNo(4)}      |
               | IT Date                | datepicker   | input         | {today+9}            |
               | IT Issued Location     | autocomplete | input         | 3074                 |
               | E-Commerce             | checkbox     | tick          | {on}                 |
          Then the shipment 'A' of 'Ocean Import' will be created
