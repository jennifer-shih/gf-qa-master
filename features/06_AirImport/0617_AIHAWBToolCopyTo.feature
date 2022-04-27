@SFI @LOHAN @OLC
Feature: [AirImport] AI HAWB Tools Copy To

    User can copy a HAWB to another MAWB

    Background: Log in GoFreight with Operator
        Given the user is a 'Operator'

    Scenario: Copy a HAWB to another shipment
        Given the user has a AI MAWB with 1 HAWB as 'A'
        And the user has a AI MAWB with 0 HAWB as 'B'
        When the user click AI 'A' HAWB(1) 'Tools -> Copy To'
        And the user input 'B' to AI copy HAWB to
        And the user click 'OK' button in AI 'Copy To' dialog
        Then the link of 'B' should show in AI 'Copy To' dialog
        When the user click the AI copied link
        Then the HAWB(1) should copy from AI 'A' HAWB(1)
            | field                |
            | Quotation No.        |
            | HSN                  |
            | Shipper              |
            | Consignee            |
            | Notify               |
            | Customer             |
            | Bill To              |
            | Customs Broker       |
            | Sales                |
            | Freight Location     |
            | Final Destination    |
            | Delivery Location    |
            | Trucker              |
            | Freight              |
            | Sales Type           |
            | Package              |
            | Package Unit         |
            | Gross Weight         |
            | Gross Weight LB      |
            | Chargeable Weight    |
            | Chargeable Weight LB |
            | Volume Weight        |
            | Volume Measure       |
            | Class of Entry       |
            | Frt. Released        |
            | Released By          |
            | Cargo Released To    |
            | Door Delivered       |
            | Ship Type            |
            | Incoterms            |
            | Service Term From    |
            | Service Term To      |
            | E-Commerce           |
            | Display Unit         |
            | Mark                 |
            | Description          |
            | Remark               |
        And the AI HAWB(1) should have 'COPY-1' as HAWB NO.
