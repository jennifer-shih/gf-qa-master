@SFI @LOHAN @OLC
Feature: [OceanExport] OE HBL Tools Copy To

    User can copy a HBL to another MBL

    Background: Log in GoFreight with Operator
        Given the user is a 'Operator'

    Scenario: Copy a HBL to another shipment
        Given the user has a OE MBL with 1 HBL as 'A'
        And the user has a OE MBL with 0 HBL as 'B'
        When the user click OE 'A' HBL(1) 'Tools -> Copy To'
        And the user input 'B' to OE copy HBL to
        And the user click 'OK' button in OE 'Copy To' dialog
        Then the link of 'B' should show in OE 'Copy To' dialog
        When the user click the OE copied link
        Then the HBL(1) should copy from OE 'A' HBL(1)
            | field                   |
            | Actual Shipper          |
            | Customer                |
            | Bill To                 |
            | Consignee               |
            | Notify                  |
            | Customs Broker          |
            | Trucker                 |
            | HB/L Agent              |
            | Sales                   |
            | Forwarding Agent        |
            | Sub Agent B/L           |
            | Receiving Agent         |
            | Place of Receipt        |
            | Port of Discharge       |
            | ETA                     |
            | Place of Delivery (DEL) |
            | Final Destination       |
            | FBA FC                  |
            | Empty Pickup            |
            | Delivery To/Pier        |
            | Cargo Ready Date        |
            | Cargo Pickup            |
            | Ship Mode               |
            | Buying Freight          |
            | Selling Freight         |
            | Service Term From       |
            | Service Term To         |
            | Express B/L             |
            | Cargo Type              |
            | Sales Type              |
            | Early Return Date       |
            | Business Referred By    |
            | Stackable               |
            | Ship Type               |
            | Incoterms               |
            | E-Commerce              |
        And the OE HBL(1) should have 'COPY-1' as HBL NO.
