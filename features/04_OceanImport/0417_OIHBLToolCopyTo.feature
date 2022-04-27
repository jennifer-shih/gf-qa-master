@SFI @LOHAN @OLC
Feature: [OceanImport] OI HBL Tools Copy To

    User can copy a HBL to another MBL

    Background: Log in GoFreight with Operator
        Given the user is a 'Operator'

    Scenario: Copy a HBL to another shipment
        Given the user has a OI MBL with 1 HBL as 'A'
        And the user has a OI MBL with 0 HBL as 'B'
        When the user click OI 'A' HBL(1) 'Tools -> Copy To'
        And the user input 'B' to OI copy HBL to
        And the user click 'OK' button in OI 'Copy To' dialog
        Then the link of 'B' should show in OI 'Copy To' dialog
        When the user click the OI copied link
        Then the HBL(1) should copy from OI 'A' HBL(1)
            | field                |
            | Shipper              |
            | Consignee            |
            | Notify               |
            | Customer             |
            | Bill To              |
            | OP                   |
            | Forwarding Agent     |
            | Customs Broker       |
            | Trucker              |
            | CY/CFS Location      |
            | Available            |
            | Place of Delivery    |
            | Final Destination    |
            | Delivery Location    |
            | Ship Mode            |
            | Freight              |
            | Rail Check           |
            | Rail                 |
            | Expiry Date          |
            | Express B/L          |
            | Sales Type           |
            | Incoterms            |
            | Cargo Type           |
            | Door Move            |
            | C.Clearance          |
            | Service Term From    |
            | Service Term To      |
            | Business Referred By |
            | ROR                  |
            | Ship Type            |
            | S/C No.              |
            | Name Account         |
            | Group Comm           |
            | Line Code            |
            | E-Commerce           |
        And the OI HBL(1) should have 'COPY-1' as HBL NO.
