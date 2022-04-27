@SFI @LOHAN @OLC
Feature: [Warehouse] Create Receipt (Advanced)

    the operator can create a receipt and do more with dimension

    Background: Log in GoFreight with Operator
        Given the user is a 'Operator'

    Scenario: Copy a dimension linked to an OI HBL is no problem
        Given the user has a OI MBL with 1 HBL as 'A' with only required fields filled
        And the user is on 'New Receipt' page
        When the user enter 'others' receipt basic datas as 'A'
            | field              | attribute  | action | data            |
            | Received Date/Time | datepicker | input  | {today+1} 13:00 |
        And the user input receipt 'A' dimension datas
            | Length     | Width      | Height     | Dimension     | PKG        | Unit          | Sku PO        | Pallet     | Total PCS  | Act. Weight KGS |
            | {randN(2)} | {randN(2)} | {randN(2)} | random select | {randN(2)} | random select | SKU{randN(6)} | {randN(2)} | {randN(1)} | randN(3)        |
        And the user link dimension(1) in receipt to OI 'A' HBL(1)
        And the user copy WH receipt dimension(1)
        And the user click WH 'Save' button
        Then the 'others' receipt 'A' will be created
        And the 'others' receipt 'A' dimension data will be saved
        And the dimension(2) copied from dimension(1) in receipt 'A' should be the same except for field Lnkd, Date, BL BKG. No.

    Scenario: Copy a dimension linked to an AE HAWB is no problem
        Given the user has a AE MAWB with 1 HAWB as 'A' with only required fields filled
        And the user is on 'New Receipt' page
        When the user enter 'others' receipt basic datas as 'A'
            | field              | attribute  | action | data            |
            | Received Date/Time | datepicker | input  | {today+1} 13:00 |
        And the user input receipt 'A' dimension datas
            | Length     | Width      | Height     | Dimension     | PKG        | Unit          | Sku PO        | Pallet     | Total PCS  | Act. Weight KGS |
            | {randN(2)} | {randN(2)} | {randN(2)} | random select | {randN(2)} | random select | SKU{randN(6)} | {randN(2)} | {randN(1)} | randN(3)        |
        And the user link dimension(1) in receipt to AE 'A' HAWB(1)
        And the user copy WH receipt dimension(1)
        And the user click WH 'Save' button
        Then the 'others' receipt 'A' will be created
        And the 'others' receipt 'A' dimension data will be saved
        And the dimension(2) copied from dimension(1) in receipt 'A' should be the same except for field Lnkd, Date, BL BKG. No.

    Scenario: Copy a dimension linked to a TK MBL is no problem
        Given the user has a TK MBL as 'A' with only required fields filled
        And the user is on 'New Receipt' page
        When the user enter 'others' receipt basic datas as 'A'
            | field              | attribute  | action | data            |
            | Received Date/Time | datepicker | input  | {today+1} 13:00 |
        And the user input receipt 'A' dimension datas
            | Length     | Width      | Height     | Dimension     | PKG        | Unit          | Sku PO        | Pallet     | Total PCS  | Act. Weight KGS |
            | {randN(2)} | {randN(2)} | {randN(2)} | random select | {randN(2)} | random select | SKU{randN(6)} | {randN(2)} | {randN(1)} | randN(3)        |
        And the user link dimension(1) in receipt to TK 'A' MBL
        And the user copy WH receipt dimension(1)
        And the user click WH 'Save' button
        Then the 'others' receipt 'A' will be created
        And the 'others' receipt 'A' dimension data will be saved
        And the dimension(2) copied from dimension(1) in receipt 'A' should be the same except for field Lnkd, Date, BL BKG. No.

    Scenario: Copy a dimension linked to a MS MBL is no problem
        Given the user has a MS MBL as 'A' with only required fields filled
        And the user is on 'New Receipt' page
        When the user enter 'others' receipt basic datas as 'A'
            | field              | attribute  | action | data            |
            | Received Date/Time | datepicker | input  | {today+1} 13:00 |
        And the user input receipt 'A' dimension datas
            | Length     | Width      | Height     | Dimension     | PKG        | Unit          | Sku PO        | Pallet     | Total PCS  | Act. Weight KGS |
            | {randN(2)} | {randN(2)} | {randN(2)} | random select | {randN(2)} | random select | SKU{randN(6)} | {randN(2)} | {randN(1)} | randN(3)        |
        And the user link dimension(1) in receipt to MS 'A' MBL
        And the user copy WH receipt dimension(1)
        And the user click WH 'Save' button
        Then the 'others' receipt 'A' will be created
        And the 'others' receipt 'A' dimension data will be saved
        And the dimension(2) copied from dimension(1) in receipt 'A' should be the same except for field Lnkd, Date, BL BKG. No.

    Scenario: Unlink a dimension linked to an OI HBL is no problem
        Given the user has a OI MBL with 1 HBL as 'A' with only required fields filled
        And the user is on 'New Receipt' page
        When the user enter 'others' receipt basic datas as 'A'
            | field              | attribute  | action | data            |
            | Received Date/Time | datepicker | input  | {today+1} 13:00 |
        And the user input receipt 'A' dimension datas
            | Length     | Width      | Height     | Dimension     | PKG        | Unit          | Sku PO        | Pallet     | Total PCS  | Act. Weight KGS |
            | {randN(2)} | {randN(2)} | {randN(2)} | random select | {randN(2)} | random select | SKU{randN(6)} | {randN(2)} | {randN(1)} | randN(3)        |
        And the user link dimension(1) in receipt to OI 'A' HBL(1)
        And the user unlink WH receipt 'A' dimension(1)
        And the user click WH 'Save' button
        Then the 'others' receipt 'A' will be created
        And the 'others' receipt 'A' dimension data will be saved

    Scenario: Unlink a dimension linked to an AE HAWB is no problem
        Given the user has a AE MAWB with 1 HAWB as 'A' with only required fields filled
        And the user is on 'New Receipt' page
        When the user enter 'others' receipt basic datas as 'A'
            | field              | attribute  | action | data            |
            | Received Date/Time | datepicker | input  | {today+1} 13:00 |
        And the user input receipt 'A' dimension datas
            | Length     | Width      | Height     | Dimension     | PKG        | Unit          | Sku PO        | Pallet     | Total PCS  | Act. Weight KGS |
            | {randN(2)} | {randN(2)} | {randN(2)} | random select | {randN(2)} | random select | SKU{randN(6)} | {randN(2)} | {randN(1)} | randN(3)        |
        And the user link dimension(1) in receipt to AE 'A' HAWB(1)
        And the user unlink WH receipt 'A' dimension(1)
        And the user click WH 'Save' button
        Then the 'others' receipt 'A' will be created
        And the 'others' receipt 'A' dimension data will be saved

    Scenario: Unlink a dimension linked to a TK MBL is no problem
        Given the user has a TK MBL as 'A' with only required fields filled
        And the user is on 'New Receipt' page
        When the user enter 'others' receipt basic datas as 'A'
            | field              | attribute  | action | data            |
            | Received Date/Time | datepicker | input  | {today+1} 13:00 |
        And the user input receipt 'A' dimension datas
            | Length     | Width      | Height     | Dimension     | PKG        | Unit          | Sku PO        | Pallet     | Total PCS  | Act. Weight KGS |
            | {randN(2)} | {randN(2)} | {randN(2)} | random select | {randN(2)} | random select | SKU{randN(6)} | {randN(2)} | {randN(1)} | randN(3)        |
        And the user link dimension(1) in receipt to TK 'A' MBL
        And the user unlink WH receipt 'A' dimension(1)
        And the user click WH 'Save' button
        Then the 'others' receipt 'A' will be created
        And the 'others' receipt 'A' dimension data will be saved

    Scenario: Unlink a dimension linked to a MS MBL is no problem
        Given the user has a MS MBL as 'A' with only required fields filled
        And the user is on 'New Receipt' page
        When the user enter 'others' receipt basic datas as 'A'
            | field              | attribute  | action | data            |
            | Received Date/Time | datepicker | input  | {today+1} 13:00 |
        And the user input receipt 'A' dimension datas
            | Length     | Width      | Height     | Dimension     | PKG        | Unit          | Sku PO        | Pallet     | Total PCS  | Act. Weight KGS |
            | {randN(2)} | {randN(2)} | {randN(2)} | random select | {randN(2)} | random select | SKU{randN(6)} | {randN(2)} | {randN(1)} | randN(3)        |
        And the user link dimension(1) in receipt to MS 'A' MBL
        And the user unlink WH receipt 'A' dimension(1)
        And the user click WH 'Save' button
        Then the 'others' receipt 'A' will be created
        And the 'others' receipt 'A' dimension data will be saved

    Scenario: Unship a shipped dimension is no problem
        Given the user is on 'New Receipt' page
        When the user enter 'others' receipt basic datas as 'A'
            | field              | attribute  | action | data            |
            | Received Date/Time | datepicker | input  | {today+1} 13:00 |
        And the user input receipt 'A' dimension datas
            | Length     | Width      | Height     | Dimension     | PKG        | Unit          | Sku PO        | Pallet     | Total PCS  | Act. Weight KGS |
            | {randN(2)} | {randN(2)} | {randN(2)} | random select | {randN(2)} | random select | SKU{randN(6)} | {randN(2)} | {randN(1)} | randN(3)        |
        And the user check dimension(1) Shpd field
        And the user unshipped WH receipt 'A' dimension(1)
        And the user click WH 'Save' button
        Then the 'others' receipt 'A' will be created
        And the 'others' receipt 'A' dimension data will be saved
