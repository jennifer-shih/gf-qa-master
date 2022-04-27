@SFI
Feature: [Load And Link] Load And Link > Match Test

    GQT-331
    https://hardcoretech.atlassian.net/browse/GQT-331


    Scenario: A HBL AR (Our Sales) matches a MBL DC
        # Step 1
        Given the user is a 'Operator'
        And the user has a OI MBL with 0 HBL as 'A' with only required fields filled

        # Step 2
        When the user goes to OI Accounting Tab
        And the user clicks OI MBL 'Create AR' button
        And the user input AR Billing Information
            | Bill to |
            | AIR9191 |
        And the user add freights to AR
            | Freight code | Type      | Rate |
            | DUTY         | Our Sales | 360  |
        And the user click save button

        # Step 3
        And the user clicks OI MBL 'Create DC' button
        And the user input DC Billing Information
            | Agent Name |
            | AIR9191    |
        And the user add freights to DC
            | Freight code | Type                 | Rate |
            | DUTY         | Credit (Origin Cost) | 360  |
        And the user click save button

        # Step 4
        When the user goes to OI MBL AR(1)
        Then the values of freights in AR entry should be
            | index | Freight Code   | Amount | Status  |
            | 1     | OI13DUTY: DUTY | 360    | Matched |

        When the user goes back to the previous page
        And the user goes to OI MBL DC(1)
        Then the values of freights in DC entry should be
            | index | Freight Code   | Type                 | Amount | Status  |
            | 1     | OI13DUTY: DUTY | Credit (Origin Cost) | 360    | Matched |


    Scenario: A HBL AP (Our Cost) matches a MBL DC
        # Step 5
        Given the user is a 'Operator'
        And the user has a OI MBL with 0 HBL as 'A' with only required fields filled
        When the user goes to OI Accounting Tab
        And the user clicks OI MBL 'Create AP' button
        And the user input AP Billing Information
            | Vendor  |
            | AIR9191 |
        And the user add freights to AP
            | Freight code | Type     | Rate |
            | DUTY         | Our Cost | 720  |
        And the user click save button

        # Step 6
        And the user clicks OI MBL 'Create DC' button
        And the user input DC Billing Information
            | Agent Name |
            | AIR9191    |
        And the user add freights to DC
            | Freight code | Type                   | Rate |
            | DUTY         | Debit (Origin Revenue) | 720  |
        And the user click save button

        # Step 7
        When the user goes to OI MBL AP(1)
        Then the values of freights in AP entry should be
            | index | Freight Code   | Amount | Status  |
            | 1     | OI13DUTY: DUTY | 720    | Matched |

        When the user goes back to the previous page
        And the user goes to OI MBL DC(1)
        Then the values of freights in DC entry should be
            | index | Freight Code   | Type                   | Amount | Status  |
            | 1     | OI13DUTY: DUTY | Debit (Origin Revenue) | 720    | Matched |


    Scenario: A HBL AR (Our Sales) matches a MBL DC
        # Step 8
        Given the user is a 'Operator'
        And the user has a OI MBL with 0 HBL as 'A' with only required fields filled
        When the user goes to OI Accounting Tab
        And the user clicks OI MBL 'Create AR' button
        And the user input AR Billing Information
            | Bill to |
            | AIR9191 |
        And the user add freights to AR
            | Freight code | Type      | Rate |
            | DUTY         | Our Sales | 360  |
        And the user click save button

        # Step 9
        And the user clicks OI MBL 'Create DC' button
        And the user input DC Billing Information
            | Agent Name |
            | AIR9191    |
        And the user add freights to DC
            | Freight code  | Type                 | Rate |
            | FORK LIFT FEE | Credit (Origin Cost) | 360  |
        And the user click save button

        # Step 10
        When the user goes to OI MBL AR(1)
        Then the values of freights in AR entry should be
            | index | Freight Code   | Amount | Status   |
            | 1     | OI13DUTY: DUTY | 360    | No Match |

        When the user goes back to the previous page
        And the user goes to OI MBL DC(1)
        Then the values of freights in DC entry should be
            | index | Freight Code              | Type                 | Amount | Status   |
            | 1     | OI17FORKLI: FORK LIFT FEE | Credit (Origin Cost) | 360    | No Match |


    Scenario: A HBL AP (Our Cost) matches a MBL DC
        # Step 11
        Given the user is a 'Operator'
        And the user has a OI MBL with 0 HBL as 'A' with only required fields filled
        When the user goes to OI Accounting Tab
        And the user clicks OI MBL 'Create AP' button
        And the user input AP Billing Information
            | Vendor  |
            | AIR9191 |
        And the user add freights to AP
            | Freight code | Type     | Rate |
            | DUTY         | Our Cost | 720  |
        And the user click save button

        # Step 12
        And the user clicks OI MBL 'Create DC' button
        And the user input DC Billing Information
            | Agent Name |
            | AIR9191    |
        And the user add freights to DC
            | Freight code  | Type                   | Rate |
            | FORK LIFT FEE | Debit (Origin Revenue) | 720  |
        And the user click save button

        # Step 13
        When the user goes to OI MBL AP(1)
        Then the values of freights in AP entry should be
            | index | Freight Code   | Amount | Status   |
            | 1     | OI13DUTY: DUTY | 720    | No Match |

        When the user goes back to the previous page
        And the user goes to OI MBL DC(1)
        Then the values of freights in DC entry should be
            | index | Freight Code              | Type                   | Amount | Status   |
            | 1     | OI17FORKLI: FORK LIFT FEE | Debit (Origin Revenue) | 720    | No Match |
