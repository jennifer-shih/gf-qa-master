Feature: [Truck] create AR/AP/DC

    Background: Log in GoFreight with Accounting Manager
        Given the user is a 'Operator'


    @SFI
    Scenario: The user can create 2 ARs (For SFI)
        Given the user has a TK MBL as 'A' with only required fields filled
        When the user click 'Accounting' tab of Truck
        And the user click 'Create Invoice' button
        And the user input AR Billing Information
            | Bill to              | Invoice Date | Due Date  |
            | {randomTradePartner} | {today}      | {today+7} |
        And the user add freights to AR
            | Freight code  | Rate   |
            | warehouse fee | 111.11 |
            | new box       | 222.22 |
        And the user click save button
        Then the TK AR(1) should be created
            | Revenue | Cost | Balance | Date    |
            | 333.33  | 0.00 | 333.33  | {today} |

        When the user click 'Create Invoice' button
        And the user input AR Billing Information
            | Bill to              | Invoice Date | Due Date  |
            | {randomTradePartner} | {today+3}    | {today+7} |
        And the user add freights to AR
            | Freight code  | Rate   |
            | warehouse fee | 111.11 |
            | new box       | 222.22 |
        And the user click save button
        Then the TK AR(2) should be created
            | Revenue | Cost | Balance | Date      |
            | 333.33  | 0.00 | 333.33  | {today+3} |


    @LOHAN
    Scenario: The user can create 2 ARs (For LOHAN)
        Given the user has a TK MBL as 'A' with only required fields filled
        When the user click 'Accounting' tab of Truck
        And the user click 'Create Invoice' button
        And the user input AR Billing Information
            | Bill to              | Invoice Date | Due Date  |
            | {randomTradePartner} | {today}      | {today+7} |
        And the user add freights to AR
            | Freight code | Rate   |
            | Admini Fee   | 111.11 |
            | CFS          | 222.22 |
        And the user click save button
        Then the TK AR(1) should be created
            | Revenue | Cost | Balance | Date    |
            | 333.33  | 0.00 | 333.33  | {today} |

        When the user click 'Create Invoice' button
        And the user input AR Billing Information
            | Bill to              | Invoice Date | Due Date  |
            | {randomTradePartner} | {today+3}    | {today+7} |
        And the user add freights to AR
            | Freight code | Rate   |
            | Admini Fee   | 111.11 |
            | CFS          | 222.22 |
        And the user click save button
        Then the TK AR(2) should be created
            | Revenue | Cost | Balance | Date      |
            | 333.33  | 0.00 | 333.33  | {today+3} |


    @OLC
    Scenario: The user can create 2 ARs (For OLC)
        Given the user has a TK MBL as 'A' with only required fields filled
        When the user click 'Accounting' tab of Truck
        And the user click 'Create Invoice' button
        And the user input AR Billing Information
            | Bill to              | Invoice Date | Due Date  |
            | {randomTradePartner} | {today}      | {today+7} |
        And the user add freights to AR
            | Freight code  | Rate   |
            | Agent Fee     | 111.11 |
            | Net Pay Taxes | 222.22 |
        And the user click save button
        Then the TK AR(1) should be created
            | Revenue | Cost | Balance | Date    |
            | 333.33  | 0.00 | 333.33  | {today} |

        When the user click 'Create Invoice' button
        And the user input AR Billing Information
            | Bill to              | Invoice Date | Due Date  |
            | {randomTradePartner} | {today+3}    | {today+7} |
        And the user add freights to AR
            | Freight code  | Rate   |
            | Agent Fee     | 111.11 |
            | Net Pay Taxes | 222.22 |
        And the user click save button
        Then the TK AR(2) should be created
            | Revenue | Cost | Balance | Date      |
            | 333.33  | 0.00 | 333.33  | {today+3} |
