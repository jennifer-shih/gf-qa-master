@SFI
Feature: [Load And Link] Load And Link Test

  GQT-327
  https://hardcoretech.atlassian.net/browse/GQT-327


  Scenario: A HBL AR (Collect for Agent) links to a MBL DC
    # Step 1
    Given the user is a 'Operator'
    And the user has a OI MBL with 1 HBL as 'A' with only required fields filled

    # Step 2
    When the user goes to OI Accounting Tab
    And the user clicks OI HBL 'Create AR' button
    And the user input AR Billing Information
      | Bill to              |
      | {randomTradePartner} |
    And the user add freights to AR
      | Freight code | Type              | Rate |
      | ISF CHARGE   | Collect for Agent | 360  |
    And the user click save button

    # Step 3
    And the user clicks OI MBL 'Create DC' button
    And the user input DC Billing Information
      | Agent Name           |
      | {randomTradePartner} |
    And the user clicks 'Load and Link' button in DC entry
    And the user click save button

    # Step 4
    When the user goes to OI HBL AR(1)
    Then the values of freights in AR entry should be
      | index | Freight Code        | Amount | Status |
      | 1     | OI07ISF: ISF CHARGE | 360    | Linked |

    When the user goes back to the previous page
    And the user goes to OI MBL DC(1)
    Then the values of freights in DC entry should be
      | index | Freight Code        | Type                 | Amount | Status |
      | 1     | OI07ISF: ISF CHARGE | Credit (Origin Cost) | 360    | Linked |


  Scenario: A HBL AP (Pay for Agent) links to a MBL DC
    # Step 5
    Given the user is a 'Operator'
    And the user has a OI MBL with 1 HBL as 'A' with only required fields filled
    When the user goes to OI Accounting Tab
    And the user clicks OI HBL 'Create AP' button
    And the user input AP Billing Information
      | Vendor               |
      | {randomTradePartner} |
    And the user add freights to AP
      | Freight code | Type          | Rate |
      | ISF CHARGE   | Pay for Agent | 720  |
    And the user click save button

    # Step 6
    And the user clicks OI MBL 'Create DC' button
    And the user input DC Billing Information
      | Agent Name           |
      | {randomTradePartner} |
    And the user clicks 'Load and Link' button in DC entry
    And the user click save button

    # Step 7
    When the user goes to OI HBL AP(1)
    Then the values of freights in AP entry should be
      | index | Freight Code        | Amount | Status |
      | 1     | OI07ISF: ISF CHARGE | 720    | Linked |

    When the user goes back to the previous page
    And the user goes to OI MBL DC(1)
    Then the values of freights in DC entry should be
      | index | Freight Code        | Type                   | Amount | Status |
      | 1     | OI07ISF: ISF CHARGE | Debit (Origin Revenue) | 720    | Linked |


  Scenario: A HBL AR (Our Sales) can't link to a MBL DC if the agent amount is blank
    # Step 8
    Given the user is a 'Operator'
    And the user has a OI MBL with 1 HBL as 'A' with only required fields filled
    When the user goes to OI Accounting Tab
    And the user clicks OI HBL 'Create AR' button
    And the user input AR Billing Information
      | Bill to              |
      | {randomTradePartner} |
    And the user add freights to AR
      | Freight code | Type      | Rate |
      | ISF CHARGE   | Our Sales | 360  |
    And the user click save button

    # Step 9
    And the user clicks OI MBL 'Create DC' button
    And the user input DC Billing Information
      | Agent Name           |
      | {randomTradePartner} |
    Then the 'Load and Link' button should be disabled


  Scenario: A HBL AP (Our Cost) can't link to a MBL DC if the agent amount is blank
    # Step 10
    Given the user is a 'Operator'
    And the user has a OI MBL with 1 HBL as 'A' with only required fields filled
    When the user goes to OI Accounting Tab
    And the user clicks OI HBL 'Create AP' button
    And the user input AP Billing Information
      | Vendor               |
      | {randomTradePartner} |
    And the user add freights to AP
      | Freight code | Type     | Rate |
      | ISF CHARGE   | Our Cost | 720  |
    And the user click save button

    # Step 11
    And the user clicks OI MBL 'Create DC' button
    And the user input DC Billing Information
      | Agent Name           |
      | {randomTradePartner} |
    Then the 'Load and Link' button should be disabled
