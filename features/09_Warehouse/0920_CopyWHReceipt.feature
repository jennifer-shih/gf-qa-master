Feature: [Warehouse] Copy Receipt

    the operator can copy a receipt

    Background: Log in GoFreight with Operator and create an OI hbl
        Given the user is a 'Operator'
        And the user has a OI MBL with 1 HBL as 'A' with only required fields filled

    @SFI @LOHAN @OLC
    Scenario: The operator copy a 'others' receipt
        Given the user has a WH 'others' receipt as 'A' having 4 dimensions
        And the dimension(2) in receipt is shipped
        And the dimension(3) in receipt is linked to OI 'A' HBL(1)
        And the dimension(4) in receipt is shipped
        And the dimension(4) in receipt is linked to OI 'A' HBL(1)
        When the user click WH receipt 'A' 'Tools -> Copy'
        And the user click WH 'Save' button
        Then the receipt should be copied from receipt 'A'
            | field                |
            | Received By          |
            | Truck B/L No.        |
            | Location             |
            | Loaded Date/Time     |
            | Maker                |
            | Shipper              |
            | Consignee            |
            | Delivered Carrier    |
            | Delivered By         |
            | Amount               |
            | Check No.            |
            | Cargo Type           |
            | Office               |
            | Hazardous Goods      |
            | Heat Treated Pallets |
            | P.O. No.             |
            | Remark               |

    @SFI @LOHAN
    Scenario: The operator copy an 'automobile' receipt
        Given the user has a WH 'automobile' receipt as 'A' having 4 dimensions
        And the dimension(2) in receipt is shipped
        And the dimension(3) in receipt is linked to OI 'A' HBL(1)
        And the dimension(4) in receipt is shipped
        And the dimension(4) in receipt is linked to OI 'A' HBL(1)
        When the user click WH receipt 'A' 'Tools -> Copy'
        Then the receipt should be copied from receipt 'A'
            | field                |
            | Received By          |
            | Truck B/L No.        |
            | Location             |
            | Loaded Date/Time     |
            | Maker                |
            | Shipper              |
            | Consignee            |
            | Delivered Carrier    |
            | Delivered By         |
            | Amount               |
            | Check No.            |
            | Cargo Type           |
            | Office               |
            | Hazardous Goods      |
            | Heat Treated Pallets |
            | P.O. No.             |
            | Remark               |
        And the 'automobile' receipt has empty Vin No. and Customer
        When the user enter 'automobile' receipt basic datas as 'B'
            | field       | attribute    | action | data                 |
            | AM Vin No.  | autocomplete | input  | {randomVin}          |
            | AM Customer | autocomplete | input  | {randomTradePartner} |
        And the user click WH 'Save' button
        Then none of automobile feilds in receipt 'B' should be copied from receipt 'A'
