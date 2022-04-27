@OLC_TPE
Feature: [Front Desk] Acceptance Test GQT_140

    the front desk setting is no problem

    Scenario: Setting config #2
        Given the user is a 'Super Admin'
        And the user is on 'Company Management' page
        And settings in 'Company Management' page are as listed below
            | field       | attribute    | action | data        |
            | Enable Tax  | checkbox     | tick   | {on}        |
            | Tax Billing | autocomplete | input  | AIR FREIGHT |
        And the user is on 'Office Management' page
        And settings in 'QD' 'Office Entry' page are as listed below
            | field      | attribute | action | data  |
            | Enable Tax | checkbox  | tick   | {off} |
        And the user is on 'Office Management' page
        And settings in 'TPE' 'Office Entry' page are as listed below
            | field                        | attribute          | action | data                       |
            | Enable Branch List           | checkbox           | tick   | {on}                       |
            | Branch List                  | tag input          | input  | TPE;TCH;KAO;KEE            |
            | Multiple POL & POD           | checkbox           | tick   | {on}                       |
            | Multiple Port Cut-Off dates  | checkbox           | tick   | {on}                       |
            | Location List                | multi autocomplete | input  | KEELUNG;KAOHSIUNG;TAICHUNG |
            | Enable Tax                   | checkbox           | tick   | {on}                       |
            | AR Tax Opt.                  | tag input          | input  | 應稅                       |
            | A/R - Tax value when P/C = P | select             | select | 應稅                       |
            | AR 0-Tax Opt.                | tag input          | input  | 免稅                       |
            | A/R - Tax value when P/C = C | select             | select | 免稅                       |
            | AR Exempt Opt.               | tag input          | input  | 收據;代收付                |
            | AP Tax Opt.                  | tag input          | input  | 應稅                       |
            | A/P - Tax value when P/C = P | select             | select | 應稅                       |
            | AP 0-Tax Opt.                | tag input          | input  | 零稅                       |
        And the user is on 'System Configuration' page
        And settings in 'TPE' 'System Configuration' page are as listed below
            | field                                                          | attribute | action | data                                        |
            | OE HBL Style                                                   | select    | select | ORIENTAL LOGISTICS GROUP LTD. TPE (OLC-TPE) |
            | OE HBL Booking Confirmation Style                              | select    | select | OLC TPE                                     |
            | Enable OE Vessel Freight List                                  | checkbox  | tick   | {on}                                        |
            | Enable Allocate FCL profits per shipment (others by CBM share) | checkbox  | tick   | {on}                                        |
            | Vessel Based (Merge/Split Bookings                             | checkbox  | tick   | {on}                                        |
            | Enable FCL/LCL                                                 | checkbox  | tick   | {on}                                        |
            | Enable Back Date                                               | checkbox  | tick   | {on}                                        |
            | Show Extra Agent in OE/Booking                                 | checkbox  | tick   | {on}                                        |
            | Enable auto-gen CNTR from booking                              | checkbox  | tick   | {on}                                        |
            | Enable Cost Share                                              | checkbox  | tick   | {on}                                        |
            | Enable Handle Agent at Container List                          | checkbox  | tick   | {on}                                        |
            | Enable copy existing hawb                                      | checkbox  | tick   | {on}                                        |
            | Enable Front Desk Portal                                       | checkbox  | tick   | {on}                                        |
        And the user is on 'Permission Management' page
        And settings in 'Permission Management' page are as listed below
            | User       | Uniform Invoice Edit Void/Valid |
            | op_tpe lee | Allow                           |
        And the user is on 'Dashboard' page

    Scenario: OLC QD AM won't see "Front Desk" #3
        Given the user is a 'Accounting Manager'
        When the user expand the navigator 'Accounting'
        Then the user will not see 'Front Desk'

    Scenario: OLC TPE OP can see "Front Desk" #4
        Given the user is a 'Operator' in 'TPE' office
        When the user expand the navigator 'Accounting'
        And the user expand the navigator 'Front Desk'
        Then the user will see 'Front Desk' subitems

    Scenario: Booking AR should not be found in 'Front Desk Portal' #5
        Given the user is a 'Operator' in 'TPE' office
        And the user has a OE Booking
        When the user click 'Accounting' tab of OE Booking
        And the user add freights to OE Booking AR
            | Bill To              | Freight Code  | Rate   | Tax  |
            | {randomTradePartner} | ocean freight | 111.11 | 應稅 |
        And the user click OE Booking Accounting 'Save' Button
        And the user browse to 'Front Desk Portal' page by navigator
        And the user search for the OE Booking AR just created
        Then the OE Booking AR should not be found

    Scenario: TPE OP won't see other office's AR due to invoice view permission can #7
        Given the user is a 'Operator' in 'QD' office
        And the user has a OI MBL with 1 HBL as 'A'
        When the user click 'Accounting' tab of OI
        And the user without tax permission add freights to OI 'A' HBL(1) AR
            | Bill To              | Freight Code  | Rate   |
            | {randomTradePartner} | OCEAN FREIGHT | 111.11 |
        And the user click OI Accounting 'Save' Button
        Given the user is a 'Operator' in 'TPE' office
        When the user browse to 'Front Desk Portal' page by navigator
        And the user search for the OI 'A' HBL(1) AR just created
        Then the OI 'A' HBL(1) AR should not be found

    Scenario: HBLs Preview #6, 8
        Given the user is a 'Operator' in 'TPE' office
        And the user created an AI Shipment with 1 of HAWB
        When the user click 'Accounting' tab of AI
        And the user add revenue freights to AI HAWB(1) AR
            | Bill To    | Freight Code | Rate   | Tax  |
            | OTHERS9191 | AIR FREIGHT  | 111.11 | 應稅 |
            | AIR9191    | AIR FREIGHT  | 222.11 | 免稅 |
        And the user click AI Accounting 'Save' Button
        And the user browse to 'Front Desk Portal' page by navigator
        And the user search for the AI HAWB(1) AR just created
        Then the AI HAWB(1) 2 ARs info should be correct
        When the user select AR(1) in 'Front Desk Portal'
        And the user click 'Print HBL' button in 'Front Desk Portal'
        Then the AR(1) preview modal pop out
        When the user click 'Print Uniform Invoice' button in 'Front Desk Portal'
        Then the AR(1) print uniform invoice modal pop out
        And the AR(1) print uniform invoice modal should have no freight listed
        When the user click 'Cancel' button in uniform invoice modal
        And the user click 'Print Receipt' button in 'Front Desk Portal'
        Then the AR(1) print receipt preview shows up
        And the AR(1) print receipt preview should have no freight listed
        When the user click 'Receipt Payment' button in 'Front Desk Portal'
        Then the AR(1) receipt payment modal should have 4 method to receive

    Scenario: HBLs detail viewing is no problem #9
        Given the user is a 'Operator' in 'TPE' office
        And the user has a OI MBL with 1 HBL as 'A'
        When the user click 'Accounting' tab of OI
        And the user add freights to OI 'A' HBL(1) AR
            | Bill To              | Freight Code  | Rate   | Tax  |
            | {randomTradePartner} | OCEAN FREIGHT | 111.11 | 應稅 |
            | {randomTradePartner} | OCEAN FREIGHT | 222.11 | 應稅 |
        And the user click OI Accounting 'Save' Button
        And the user browse to 'Front Desk Portal' page by navigator
        And the user search for the OI 'A' HBL(1) AR just created
        And the user select AR(1) in 'Front Desk Portal'
        Then the AR detail modal shows up
        When the user select AR(2) in 'Front Desk Portal'
        Then the AR summary detail modal shows up

    Scenario: OLC TPE OP can create and delete uniform invoice settings #10, 11
        Given the user is a 'Operator' in 'TPE' office
        When the user browse to 'Uniform Invoice Setting' page by navigator
        And the user add 2 new uniform invoice roll
            | field                | attribute   | action       | data            |
            | Prefix               | input       | input        | {randomNo(2)}   |
            | Year                 | select      | select       | {year}          |
            | Month                | select      | select       | {invoiceMonth}  |
            | Uniform Invoice Type | radio group | random click |                 |
            | Rolls                | input       | input        | {randInt(1, 2)} |
            | Amount Per Roll      | input       | input        | 100             |
            | Invoice Number Begin | input       | input        | {randN(8)}      |
        Then the uniform invoice roll should be saved correctly
        When the user select one invoice roll and click 'Delete'
        Then the uniform invoice roll should be deleted

    Scenario: HBLs AR works fine in Front Desk Portal and Uniform Invoice Management #12, 13, 14
        Given the user is a 'Operator' in 'TPE' office
        And the user created an AI Shipment with 1 of HAWB
        When the user click 'Accounting' tab of AI
        And the user add revenue freights to AI HAWB(1) AR
            | Bill To              | Freight Code | Rate   | Tax  |
            | {randomTradePartner} | AIR FREIGHT  | 111.11 | 應稅 |
            | {randomTradePartner} | AIR FREIGHT  | 222.11 | 免稅 |
        And the user click AI Accounting 'Save' Button
        And the user browse to 'Front Desk Portal' page by navigator
        And the user search for the AI HAWB(1) AR just created
        And the user select AR(1) in 'Front Desk Portal'
        And the user click 'Print Uniform Invoice' button in 'Front Desk Portal'
        And the user click 'Print' in 'Print Uniform Invoice' modal
        Then the 'Uniform Invoice Print' page will show
        When the user browse to 'Uniform Invoice Management' page by navigator
        And the user set AR(1) in 'Uniform Invoice Management' page to be 'Void'
        Then the AR(1) status in 'Uniform Invoice Management' should be 'Void'
        When the user set AR(1) in 'Uniform Invoice Management' page to be 'Valid'
        Then the AR(1) status in 'Uniform Invoice Management' should be 'Valid'
