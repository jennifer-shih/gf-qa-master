@MASCOT
Feature: [Accounting Wizard] Accounting Wizard Acceptance Test in Air Import module

    Accounting Wiazrd acceptance test in AI module, look up ticket GQT-161 for detail


    Scenario: If 'Accounting Wizard' function is on, then user can switch 'accounting mode'
        # Step 2
        Given the user is a 'Super Admin'
        And the user is on 'Company Management' page
        And settings in 'Company Management' page are as listed below
            | field                           | attribute   | action | data      |
            | Enable Accounting Wizard        | checkbox    | tick   | {on}      |
            | Accounting Wizard Billing Style | radio group | click  | Separated |
        And the user is on 'System Configuration' page
        And settings in 'LA' 'System Configuration' page are as listed below
            | field                                         | attribute | action | data                     |
            | Accounting Wizard Print Invoice TP Name style | select    | select | System Decide Print Name |

        # Step 3
        And the user is a 'Operator'
        When the user is in New Air Import Shipment page
        And the user enter 'AI MAWB' shipment datas as 'A' and save it
            | field    | attribute    | action | data            |
            | MAWB No. | input        | input  | HACO-{randN(6)} |
            | Office   | autocomplete | input  | LA              |
        Then 'Accounting Mode' switch should show on 'Accounting' tab
        When the user click AI 'Add HAWB' button
        And the user enter 'AI HAWB(1)' shipment datas as 'A' and save it
            | field    | attribute    | action | data           |
            | HAWB No. | input        | input  | ASS-{randN(6)} |
            | Sales    | autocomplete | input  | {randomSales}  |
        Then 'Accounting Mode' switch should show on 'Accounting' tab
        When the user goes to AI Accounting Tab (Billing Based)
        Then The AI Accounting Billing Based page should show normally

    Scenario: The user create some AR/AP in AI, and the statistical data show correctly in both 'Billing Based' and 'Invoice Based'
        # Step 4
        Given the user is a 'Operator'
        And the user has a AI MAWB with 1 HAWB as 'A' with only required fields filled
        When the user goes to AI Accounting Tab (Invoice Based)
        And the user clicks AI MAWB 'Create AR' button
        And the user input AR Billing Information
            | Bill to              |
            | {randomTradePartner} |
        And the user add freights to AR
            | Freight code | Rate |
            | AQI EXAM     | 10   |
        And the user click save button
        And the user clicks AI HAWB 'Create AP' button
        And the user input AP Billing Information
            | Vendor               |
            | {randomTradePartner} |
        And the user add freights to AP
            | Freight code               | Rate |
            | CONTAINER IMBALANCE CHARGE | 20   |
        And the user click save button
        And the user refresh browser
        Then the AI MAWB amounts and profits should show correctly in Invoice Based
            | Revenue | Cost | Balance | Total Profit Amount |
            | 10.00   | 0.00 | 10.00   | -10.00              |
        And the AI HAWB amounts and profits should show correctly in Invoice Based
            | Revenue | Cost  | Balance | HAWB Profit Amount |
            | 0.00    | 20.00 | -20.00  | -10.00             |
        When the user goes to AI Accounting Tab (Billing Based)
        Then the AI MAWB amounts and profits should show correctly in Billing Based
            | MAWB Revenue | MAWB Cost | MAWB Amount | Total Profit Amount |
            | 10.00        | 0.00      | 10.00       | -10.00              |
        And the AI HAWB amounts and profits should show correctly in Billing Based
            | HAWB Revenue | HAWB Cost | HAWB Amount | Profit Amount |
            | 0.00         | 20.00     | -20.00      | -10.00        |

        # Step 5
        When the user goes to AI Accounting Tab (Invoice Based)
        And the user clicks AI MAWB 'Create AP' button
        And the user input AP Billing Information
            | Vendor               |
            | {randomTradePartner} |
        And the user add freights to AP
            | Freight code  | Rate |
            | APHIS         | 100  |
            | ALL IN CHARGE | 200  |
        And the user click save button
        And the user clicks AI HAWB 'Create AR' button
        And the user input AR Billing Information
            | Bill to              |
            | {randomTradePartner} |
        And the user add freights to AR
            | Freight code      | Rate |
            | APHIS             | 100  |
            | ALL IN CHARGE     | 200  |
            | Loading&Receiving | 300  |
        And the user click save button
        And the user refresh browser
        Then the AI MAWB amounts and profits should show correctly in Invoice Based
            | Revenue | Cost   | Balance | Total Profit Amount |
            | 10.00   | 300.00 | -290.00 | 290.00              |
        And the AI HAWB amounts and profits should show correctly in Invoice Based
            | Revenue | Cost  | Balance | HAWB Profit Amount |
            | 600.00  | 20.00 | 580.00  | 290.00             |
        When the user goes to AI Accounting Tab (Billing Based)
        Then the AI MAWB amounts and profits should show correctly in Billing Based
            | MAWB Revenue | MAWB Cost | MAWB Amount | Total Profit Amount |
            | 10.00        | 300.00    | -290.00     | 290.00              |
        And the AI HAWB amounts and profits should show correctly in Billing Based
            | HAWB Revenue | HAWB Cost | HAWB Amount | Profit Amount |
            | 600.00       | 20.00     | 580.00      | 290.00        |

        # Step 6
        When the user delete all freights in AI MAWB revenue Billing Based
        And the user delete all freights in AI MAWB cost Billing Based
        And the user delete all freights in AI HAWB revenue Billing Based
        And the user delete all freights in AI HAWB cost Billing Based
        And the user clicks save button in AI Accounting Billing Based
        Then AI MAWB has no invoice in Billing Based
        And AI HAWB has no invoice in Billing Based
        When the user goes to AI Accounting Tab (Invoice Based)
        Then AI MAWB has no invoice in Invoice Based
        And AI HAWB has no invoice in Invoice Based

    Scenario: Blocking, draft, and DC supporting test
        # Step 7
        Given the user is a 'Operator'
        And the user has a AI MAWB with 1 HAWB as 'A' with only required fields filled
        When the user goes to AI Accounting Tab (Invoice Based)
        And the user clicks AI MAWB 'Create AR' button
        And the user input AR Billing Information
            | Bill to       |
            | WAREHOUSE9191 |
        And the user add freights to AR
            | Freight code | Rate |
            | APHIS        | 10   |
        And the user clicks 'Save as Draft' button
        And the user clicks AI MAWB 'Create AP' button
        And the user input AP Billing Information
            | Vendor        |
            | WAREHOUSE9191 |
        And the user click save button
        And the user clicks AI HAWB 'Create AR' button
        And the user input AR Billing Information
            | Bill to       |
            | WAREHOUSE9191 |
        And the user add freights to AR
            | Freight code      | Rate |
            | APHIS             | 10   |
            | ALL IN CHARGE     | 20   |
            | Loading&Receiving | 30   |
            | CCAM              | 40   |
            | Chassis Charge    | 50   |
        And the user click save button
        And the user clicks AI HAWB 'Create DC' button
        And the user input DC Billing Information
            | Agent Name    |
            | WAREHOUSE9191 |
        And the user add freights to DC
            | Freight code | Type                   | Rate |
            | APHIS        | Debit (Origin Revenue) | 100  |
        And the user click save button
        And the user clicks AI HAWB 'Create DC' button
        And the user input DC Billing Information
            | Agent Name    |
            | WAREHOUSE9191 |
        And the user add freights to DC
            | Freight code | Type                 | Rate |
            | CUS          | Credit (Origin Cost) | 200  |
        And the user click save button
        Then the AI MAWB amounts and profits should show correctly in Invoice Based
            | Revenue | Cost | Balance | Total Profit Amount |
            | 10.00   | 0.00 | 0.00    | 50.00               |
        And the AI HAWB amounts and profits should show correctly in Invoice Based
            | Revenue | Cost   | Balance | HAWB Profit Amount |
            | 250.00  | 200.00 | 50.00   | 50.00              |
        When the user unchecks AI Accounting (Invoice Based) MAWB 'Include Draft Amount' checkbox
        Then the AI MAWB amounts and profits should show correctly in Invoice Based
            | Revenue | Cost | Balance | Total Profit Amount |
            | 0.00    | 0.00 | 0.00    | 50.00               |
        When the user unchecks AI Accounting (Invoice Based) HAWB 'Include Draft Amount' checkbox
        Then the AI HAWB amounts and profits should show correctly in Invoice Based
            | Revenue | Cost   | Balance | HAWB Profit Amount |
            | 250.00  | 200.00 | 50.00   | 50.00              |
        When the user goes to AI Accounting Tab (Billing Based)
        And the user checks AI Accounting (Billing Based) MAWB 'Include Draft Amount' checkbox
        Then the AI MAWB amounts and profits should show correctly in Billing Based
            | MAWB Revenue | MAWB Cost | MAWB Amount | Total Profit Amount |
            | 10.00        | 0.00      | 10.00       | 50.00               |
        When the user checks AI Accounting (Billing Based) HAWB 'Include Draft Amount' checkbox
        Then the AI HAWB amounts and profits should show correctly in Billing Based
            | HAWB Revenue | HAWB Cost | HAWB Amount | Profit Amount |
            | 150.00       | 0.00      | 150.00      | 50.00         |
        When the user unchecks AI Accounting (Billing Based) MAWB 'Include Draft Amount' checkbox
        Then the AI MAWB amounts and profits should show correctly in Billing Based
            | MAWB Revenue | MAWB Cost | MAWB Amount | Total Profit Amount |
            | 0.00         | 0.00      | 0.00        | 50.00               |
        When the user unchecks AI Accounting (Billing Based) HAWB 'Include Draft Amount' checkbox
        Then the AI HAWB amounts and profits should show correctly in Billing Based
            | HAWB Revenue | HAWB Cost | HAWB Amount | Profit Amount |
            | 150.00       | 0.00      | 150.00      | 50.00         |

        # Step 8
        When the user blocks AI HAWB revenue(1) in Accounting Billing Based
        Then AI HAWB revenues listed below should be uneditable in Accounting Billing Based
            | No. |
            | 1   |
            | 2   |
            | 3   |
            | 4   |
            | 5   |

    Scenario: Special value test
        # Step 9
        Given the user is a 'Operator'
        And the user has a AI MAWB with 1 HAWB as 'A' with only required fields filled
        When the user goes to AI Accounting Tab (Billing Based)
        When the user adds freights to AI MAWB revenue
            | Bill to     | Freight code | Volume | Rate |
            | SHIPPER9191 | APHIS        | 9.293  | 165  |
        And the user clicks save button in AI Accounting Billing Based
        Then values in AI MAWB revenue should be correct
            | No. | Amount  |
            | 1   | 1533.35 |
        When the user adds freights to AI HAWB revenue
            | Bill to     | Freight code | Volume | Rate |
            | SHIPPER9191 | APHIS        | 9.293  | 165  |
        And the user clicks save button in AI Accounting Billing Based
        Then values in AI HAWB revenue should be correct
            | No. | Amount  |
            | 1   | 1533.35 |

    Scenario: Creation, deletion, editing, and order test in accounting wizard
        # Step 10
        Given the user is a 'Operator'
        And the user has a AI MAWB with 1 HAWB as 'A' with only required fields filled
        When the user goes to AI Accounting Tab (Billing Based)
        When the user adds freights to AI MAWB revenue
            | Bill to     | Freight code      | Volume | Rate |
            | TRUCKER9191 | APHIS             | 1      | 1    |
            | TRUCKER9191 | APHIS             | 1      | 2    |
            | TRUCKER9191 | ALL IN CHARGE     | 1      | 3    |
            | TRUCKER9191 | ALL IN CHARGE     | 1      | 4    |
            | TRUCKER9191 | Loading&Receiving | 1      | 5    |
            | TRUCKER9191 | Loading&Receiving | 1      | 6    |
            | TRUCKER9191 | CCAM              | 1      | 7    |
            | TRUCKER9191 | CCAM              | 1      | 8    |
            | TRUCKER9191 | Chassis Charge    | 1      | 9    |
            | TRUCKER9191 | Chassis Charge    | 1      | 10   |
        And the user clicks save button in AI Accounting Billing Based
        Then values in AI MAWB revenue should be correct
            | No. | Amount |
            | 1   | 1      |
            | 2   | 2      |
            | 3   | 3      |
            | 4   | 4      |
            | 5   | 5      |
            | 6   | 6      |
            | 7   | 7      |
            | 8   | 8      |
            | 9   | 9      |
            | 10  | 10     |

        # Step 11
        When the user adds freights to AI MAWB revenue
            | Bill to  | Freight code      | Volume | Rate |
            | RAIL9191 | APHIS             | 1      | 1    |
            | RAIL9191 | APHIS             | 1      | 2    |
            | RAIL9191 | ALL IN CHARGE     | 1      | 3    |
            | RAIL9191 | ALL IN CHARGE     | 1      | 4    |
            | RAIL9191 | Loading&Receiving | 1      | 5    |
            | RAMP9191 | Loading&Receiving | 1      | 1    |
            | RAMP9191 | CCAM              | 1      | 2    |
            | RAMP9191 | CCAM              | 1      | 3    |
            | RAMP9191 | Chassis Charge    | 1      | 4    |
            | RAMP9191 | Chassis Charge    | 1      | 5    |
        And the user adds freights to AI MAWB cost
            | Bill to  | Freight code      | Volume | Rate |
            | RAIL9191 | APHIS             | 1      | 1    |
            | RAIL9191 | APHIS             | 1      | 2    |
            | RAIL9191 | ALL IN CHARGE     | 1      | 3    |
            | RAIL9191 | ALL IN CHARGE     | 1      | 4    |
            | RAIL9191 | Loading&Receiving | 1      | 5    |
            | RAMP9191 | Loading&Receiving | 1      | 1    |
            | RAMP9191 | CCAM              | 1      | 2    |
            | RAMP9191 | CCAM              | 1      | 3    |
            | RAMP9191 | Chassis Charge    | 1      | 4    |
            | RAMP9191 | Chassis Charge    | 1      | 5    |
        And the user clicks save button in AI Accounting Billing Based
        Then values in AI MAWB revenue should be correct
            | No. | Amount |
            | 11  | 1      |
            | 12  | 2      |
            | 13  | 3      |
            | 14  | 4      |
            | 15  | 5      |
            | 16  | 1      |
            | 17  | 2      |
            | 18  | 3      |
            | 19  | 4      |
            | 20  | 5      |
        Then values in AI MAWB cost should be correct
            | No. | Amount |
            | 1   | 1      |
            | 2   | 2      |
            | 3   | 3      |
            | 4   | 4      |
            | 5   | 5      |
            | 6   | 1      |
            | 7   | 2      |
            | 8   | 3      |
            | 9   | 4      |
            | 10  | 5      |

        # Step 12
        When the user deletes freights in AI MAWB revenue
            | No. |
            | 5   |
            | 6   |
            | 7   |
        And the user adds freights to AI MAWB cost
            | Bill to  | Freight code | Volume | Rate |
            | RAIL9191 | APHIS        | 1      | 100  |
            | RAMP9191 | CCAM         | 1      | 200  |
        And the user clicks save button in AI Accounting Billing Based
        And the user changes currency of freights in AI MAWB revenue
            | No. | Currency |
            | 8   | GBP      |
            | 9   | GBP      |
            | 10  | GBP      |
            | 11  | GBP      |
            | 12  | GBP      |
            | 13  | EUR      |
            | 14  | EUR      |
            | 15  | EUR      |
            | 16  | EUR      |
            | 17  | EUR      |
        And the user clicks save button in AI Accounting Billing Based
        Then values in AI MAWB revenue should be correct
            | No. | Currency | Amount |
            | 1   |          | 1      |
            | 2   |          | 2      |
            | 3   |          | 3      |
            | 4   |          | 4      |
            | 5   |          | 8      |
            | 6   |          | 9      |
            | 7   |          | 10     |
            | 8   | GBP      | 1      |
            | 9   | GBP      | 2      |
            | 10  | GBP      | 3      |
            | 11  | GBP      | 4      |
            | 12  | GBP      | 5      |
            | 13  | EUR      | 1      |
            | 14  | EUR      | 2      |
            | 15  | EUR      | 3      |
            | 16  | EUR      | 4      |
            | 17  | EUR      | 5      |
        And values in AI MAWB cost should be correct
            | No. | Amount |
            | 1   | 1      |
            | 2   | 2      |
            | 3   | 3      |
            | 4   | 4      |
            | 5   | 5      |
            | 6   | 100    |
            | 7   | 1      |
            | 8   | 2      |
            | 9   | 3      |
            | 10  | 4      |
            | 11  | 5      |
            | 12  | 200    |

        # Step 13
        When the user delete all freights in AI MAWB revenue Billing Based
        And the user delete all freights in AI MAWB cost Billing Based
        And the user clicks save button in AI Accounting Billing Based
        Then AI MAWB has no invoice in Billing Based

    Scenario: Freights' order, and 'copy to' function test
        # Step 14
        Given the user is a 'Operator'
        And the user has a AI MAWB with 1 HAWB as 'A' with only required fields filled
        When the user goes to AI Accounting Tab (Billing Based)
        And the user adds freights to AI HAWB cost
            | Bill to  | Freight code      | Volume | Rate |
            | RAIL9191 | APHIS             | 1      | 1    |
            | RAIL9191 | APHIS             | 1      | 2    |
            | RAIL9191 | ALL IN CHARGE     | 1      | 3    |
            | RAIL9191 | ALL IN CHARGE     | 1      | 4    |
            | RAIL9191 | Loading&Receiving | 1      | 5    |
            | RAIL9191 | Loading&Receiving | 1      | 6    |
            | RAIL9191 | CCAM              | 1      | 7    |
            | RAIL9191 | CCAM              | 1      | 8    |
            | RAIL9191 | Chassis Charge    | 1      | 9    |
            | RAIL9191 | Chassis Charge    | 1      | 10   |
        And the user clicks save button in AI Accounting Billing Based
        Then values in AI HAWB cost should be correct
            | No. | Amount |
            | 1   | 1      |
            | 2   | 2      |
            | 3   | 3      |
            | 4   | 4      |
            | 5   | 5      |
            | 6   | 6      |
            | 7   | 7      |
            | 8   | 8      |
            | 9   | 9      |
            | 10  | 10     |

        # Step 15
        When the user copys freights from AI HAWB cost to HAWB revenue
            | No. |
            | 1   |
            | 2   |
            | 3   |
            | 4   |
            | 5   |
            | 6   |
            | 7   |
            | 8   |
            | 9   |
            | 10  |
        And the user input freights information to AI HAWB revenue
            | No. | Bill to     |
            | 1   | SHIPPER9191 |
            | 2   | SHIPPER9191 |
            | 3   | SHIPPER9191 |
            | 4   | SHIPPER9191 |
            | 5   | SHIPPER9191 |
            | 6   | SHIPPER9191 |
            | 7   | SHIPPER9191 |
            | 8   | SHIPPER9191 |
            | 9   | SHIPPER9191 |
            | 10  | SHIPPER9191 |
        And the user clicks save button in AI Accounting Billing Based
        And the user changes currency of freights in AI HAWB revenue
            | No. | Currency |
            | 1   | EUR      |
        And the user deletes freights in AI HAWB revenue
            | No. |
            | 2   |
            | 3   |
        And the user adds freights to AI HAWB revenue
            | Bill to  | Freight code | Volume | Rate |
            | RAIL9191 | APHIS        | 1      | 11   |
        And the user deletes freights in AI HAWB cost
            | No. |
            | 1   |
        And the user adds freights to AI HAWB cost
            | Bill to  | Freight code | Volume | Rate |
            | RAIL9191 | APHIS        | 1      | 11   |
        And the user clicks save button in AI Accounting Billing Based
        Then values in AI HAWB revenue should be correct
            | No. | Currency | Amount |
            | 1   | EUR      | 1      |
            | 2   |          | 4      |
            | 3   |          | 5      |
            | 4   |          | 6      |
            | 5   |          | 7      |
            | 6   |          | 8      |
            | 7   |          | 9      |
            | 8   |          | 10     |
            | 9   |          | 11     |
        Then values in AI HAWB cost should be correct
            | No. | Amount |
            | 1   | 2      |
            | 2   | 3      |
            | 3   | 4      |
            | 4   | 5      |
            | 5   | 6      |
            | 6   | 7      |
            | 7   | 8      |
            | 8   | 9      |
            | 9   | 10     |
            | 10  | 11     |

    Scenario Outline: AI invoice Print style test
        # Step 16
        Given the company set 'Invoice Accounting Wizard Form Style' to '<style>' in 'Company Management' page
        And the user is a 'Operator'
        And the user has a AI MAWB with 1 HAWB as 'A' with only required fields filled
        When the user goes to AI Accounting Tab (Billing Based)
        And the user adds freights to AI MAWB revenue
            | Bill to  | Freight code | Volume | Rate |
            | RAIL9191 | APHIS        | 1      | 1    |
        And the user clicks save button in AI Accounting Billing Based
        When the user clicks 'Action -> Print / Mail' to AI MAWB revenue(1)
        Then the AR form should be in '<style>' style
        When the user closes current tab
        Examples:
            | style    |
            | Default  |
            | OLC      |
            | Vinworld |

    Scenario: Permission test
        # Step 17, 18
        Given the user is a 'Super Admin'
        When the user browse to the Permission Management page by navigator
        Given settings in 'Permission Management' page are as listed below
            | User        | Invoice Block/Unblock Button Visible | Invoice Delete | Invoice Edit | Invoice Unblock | Invoice AR View | Invoice AP View |
            | op_joey lee | Inherit                              | Inherit        | Inherit      | Inherit         | Inherit         | Inherit         |

        Given the user is a 'Operator'
        And the user has a AI MAWB with 1 HAWB as 'A' with only required fields filled
        When the user goes to AI Accounting Tab (Billing Based)
        And the user adds freights to AI MAWB revenue
            | Bill to  | Freight code | Volume | Rate |
            | RAIL9191 | APHIS        | 1      | 10   |
            | CY9191   | Delivery Fee | 1      | 20   |
        And the user adds freights to AI MAWB cost
            | Bill to       | Freight code    | Volume | Rate |
            | WAREHOUSE9191 | Fuel Sur Charge | 1      | 30   |
        And the user clicks save button in AI Accounting Billing Based
        And the user blocks AI MAWB revenue(1) in Accounting Billing Based

        Given the user is a 'Super Admin'
        When the user browse to the Permission Management page by navigator
        Given settings in 'Permission Management' page are as listed below
            | User        | Invoice Block/Unblock Button Visible | Invoice Delete | Invoice Edit | Invoice Unblock |
            | op_joey lee | Deny                                 | Deny           | Deny         | Deny            |

        Given the user is a 'Operator'
        When the user goes back to AI Shipment 'A'
        And the user goes to AI Accounting Tab (Billing Based)
        Then the unblock bottom in AI MAWB revenue(1) should be invisible
        And the block bottom in AI MAWB revenue(2) should be invisible
        When the user changes currency of freights in AI MAWB revenue
            | No. | Currency |
            | 2   | EUR      |
        # ? KNOWN ISSUE OLC-5051
        #  Then the save button in AI shipment Accounting Billing Based should be disabled
        When the user refresh browser
        And the user deletes freights in AI MAWB revenue
            | No. |
            | 2   |
        # ? KNOWN ISSUE OLC-5051
        #  Then the save button in AI shipment Accounting Billing Based should be disabled
        When the user refresh browser

        Given the user is a 'Super Admin'
        When the user browse to the Permission Management page by navigator
        Given settings in 'Permission Management' page are as listed below
            | User        | Invoice AR View | Invoice AP View |
            | op_joey lee | Deny            | Deny            |

        Given the user is a 'Operator'
        When the user goes back to AI Shipment 'A'
        And the user goes to AI Accounting Tab (Billing Based)
        Then AI MAWB has no invoice in Billing Based

        # Set the permission back to original
        Given the user is a 'Super Admin'
        When the user browse to the Permission Management page by navigator
        Given settings in 'Permission Management' page are as listed below
            | User        | Invoice Block/Unblock Button Visible | Invoice Delete | Invoice Edit | Invoice Unblock | Invoice AR View | Invoice AP View |
            | op_joey lee | Inherit                              | Inherit        | Inherit      | Inherit         | Inherit         | Inherit         |

    Scenario: If 'Accounting Wizard' function is off, then user cannot switch 'accounting mode'
        # Step 19, 20
        Given the user is a 'Super Admin'
        And the user is on 'Company Management' page
        And settings in 'Company Management' page are as listed below
            | field                    | attribute | action | data  |
            | Enable Accounting Wizard | checkbox  | tick   | {off} |
        And the user is a 'Operator'
        When the user is in New Air Import Shipment page
        And the user enter 'AI MAWB' shipment datas as 'A' and save it
            | field    | attribute    | action | data            |
            | MAWB No. | input        | input  | HACO-{randN(6)} |
            | Office   | autocomplete | input  | LA              |
        Then 'Accounting Mode' switch should not show on 'Accounting' tab
        When the user click AI 'Add HAWB' button
        And the user enter 'AI HAWB(1)' shipment datas as 'A' and save it
            | field    | attribute    | action | data           |
            | HAWB No. | input        | input  | 111-{randN(6)} |
            | Sales    | autocomplete | input  | {randomSales}  |
        Then 'Accounting Mode' switch should not show on 'Accounting' tab