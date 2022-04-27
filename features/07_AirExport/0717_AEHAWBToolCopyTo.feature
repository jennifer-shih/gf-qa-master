Feature: [AirExport] AE HAWB Tools Copy To

    User can copy a HAWB to another MAWB

    Background: Log in GoFreight with Operator
        Given the user is a 'Operator'

    @SFI
    Scenario: Copy a HAWB to another shipment (For SFI)
        Given the user has a AE MAWB with 1 HAWB as 'A'
        And the user has a AE MAWB with 0 HAWB as 'B'
        When the user click AE shipment 'A' HAWB(1) 'Tools -> Copy To'
        And the user input 'B' to AE copy HAWB to
        And the user click 'OK' button in AE 'Copy To' dialog
        Then the link of 'B' should show in AE 'Copy To' dialog
        When the user click the AE copied link
        Then the HAWB(1) should copy from AE shipment 'A' HAWB(1)
            | field                                 |
            | ITN No.                               |
            | Quotation                             |
            | Actual Shipper                        |
            | Customer                              |
            | Bill To                               |
            | Consignee                             |
            | Notify                                |
            | Oversea Agent                         |
            | Issuing Carrier/Agent                 |
            | Trucker                               |
            | Sales                                 |
            | Sub Agent AWB                         |
            | Cargo Pickup                          |
            | Delivery To/Pier                      |
            | Cargo Type                            |
            | Sales Type                            |
            | Ship Type                             |
            | D.V. Carriage                         |
            | D.V. Customs                          |
            | Insurance                             |
            | WT/VAL                                |
            | Other                                 |
            | Package                               |
            | Package Unit                          |
            | Gross Weight (SHPR)                   |
            | Gross Weight (SHPR) LB                |
            | Gross Weight (SHPR) Amount            |
            | Buying Rate                           |
            | Buying Rate Unit                      |
            | Gross Weight (CNEE)                   |
            | Gross Weight (CNEE) LB                |
            | Gross Weight (CNEE) Amount            |
            | Selling Rate                          |
            | Selling Rate Unit                     |
            | Chargeable Weight (SHPR)              |
            | Chargeable Weight (SHPR) LB           |
            | Chargeable Weight (SHPR) Amount       |
            | Volume Weight                         |
            | Volume Measure                        |
            | Chargeable Weight (CNEE)              |
            | Chargeable Weight (CNEE) LB           |
            | Chargeable Weight (CNEE) Amount       |
            | Incoterms                             |
            | Service Term From                     |
            | Service Term To                       |
            | L/C No.                               |
            | Rate                                  |
            | E-Commerce                            |
            | Display Unit                          |
            | Mark                                  |
            | Nature and Quantity of Goods          |
            | Manifest Nature and Quantity of Goods |
            | Handling Information                  |
        And the AE HAWB(1) should have 'COPY-1' as HAWB NO.

    @LOHAN @OLC
    Scenario: Copy a HAWB to another shipment (For LOHAN and OLC)
        Given the user has a AE MAWB with 1 HAWB as 'A'
        And the user has a AE MAWB with 0 HAWB as 'B'
        When the user click AE shipment 'A' HAWB(1) 'Tools -> Copy To'
        And the user input 'B' to AE copy HAWB to
        And the user click 'OK' button in AE 'Copy To' dialog
        Then the link of 'B' should show in AE 'Copy To' dialog
        When the user click the AE copied link
        Then the HAWB(1) should copy from AE shipment 'A' HAWB(1)
            | field                           |
            | ITN No.                         |
            | Quotation                       |
            | Actual Shipper                  |
            | Customer                        |
            | Bill To                         |
            | Consignee                       |
            | Notify                          |
            | Oversea Agent                   |
            | Issuing Carrier/Agent           |
            | Trucker                         |
            | Sales                           |
            | Sub Agent AWB                   |
            | Cargo Pickup                    |
            | Delivery To/Pier                |
            | Cargo Type                      |
            | Sales Type                      |
            | Ship Type                       |
            | D.V. Carriage                   |
            | D.V. Customs                    |
            | Insurance                       |
            | WT/VAL                          |
            | Other                           |
            | Package                         |
            | Package Unit                    |
            | Gross Weight (SHPR)             |
            | Gross Weight (SHPR) LB          |
            | Gross Weight (SHPR) Amount      |
            | Buying Rate                     |
            | Buying Rate Unit                |
            | Gross Weight (CNEE)             |
            | Gross Weight (CNEE) LB          |
            | Gross Weight (CNEE) Amount      |
            | Selling Rate                    |
            | Selling Rate Unit               |
            | Chargeable Weight (SHPR)        |
            | Chargeable Weight (SHPR) LB     |
            | Chargeable Weight (SHPR) Amount |
            | Volume Weight                   |
            | Volume Measure                  |
            | Chargeable Weight (CNEE)        |
            | Chargeable Weight (CNEE) LB     |
            | Chargeable Weight (CNEE) Amount |
            | Incoterms                       |
            | Service Term From               |
            | Service Term To                 |
            | L/C No.                         |
            | Rate                            |
            | E-Commerce                      |
            | Display Unit                    |
            | Mark                            |
            | Nature and Quantity of Goods    |
            | Handling Information            |
        And the AE HAWB(1) should have 'COPY-1' as HAWB NO.
