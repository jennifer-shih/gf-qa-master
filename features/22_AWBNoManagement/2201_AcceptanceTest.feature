@OLC
Feature: [AWB No Management] Acceptance Test GQT_130

    the AWB no management setting is no problem

    Scenario: Disable "Setting Code Edit" then the user can create/edit 'AWB No. Management' page
        Given the user is a 'Super Admin'
        And the user is on 'Permission Management' page
        And settings in 'Permission Management' page are as listed below
            | User       | Setting Code Edit |
            | gm_lcl lee | Deny              |
        Given the user is a 'General Manager'
        And the user is on 'AWB No. Management' page
        When the user add AWB No. range in 'AWB No. Management'
            | Carrier | Begin No. | End No. | Remark | Prefix |
            | air9191 | 0000001   | 0000010 | test   | 911    |
        Then the user can NOT edit AWB No in 'AWB No. Management' page

    Scenario: OLC QD GM can set "AWB No. Management" and OP can create AE MAWB
        # Step 2
        Given the user is a 'Super Admin'
        And the user has a TP named 'AIR_TP_1' with below info
            | field      | attribute | action | data           |
            | TP Type    | select    | select | AIR CARRIER    |
            | Name       | input     | input  | AIR_TP_1       |
            | Print Name | input     | input  | AIR_TP_1 PRINT |
            | Office     | select    | select | QD             |
        And the user is on 'Permission Management' page
        And settings in 'Permission Management' page are as listed below
            | User       | Navigator Setting - AWB No. Management | Navigator Mawb No. Stock List | MAWB No Stock List Edit | MAWB No Stock List View | Trade Partner Edit | Setting Code Edit | Setting Code View |
            | gm_lcl lee | Allow                                  | Allow                         | Allow                   | Allow                   | Allow              | Allow             | Allow             |

        # Step 3
        Given the user is a 'General Manager'
        When the user browse to 'AWB No. Management' page by navigator
        And the user add AWB No. range in 'AWB No. Management'
            | Carrier  | Prefix | Begin No. | End No. | Remark |
            | AIR_TP_1 | QQQ    | 0000001   | 0000010 | TEST1  |
        Then 'AWB No. range' should be saved correctly

        # Step 4
        Given the user is a 'Operator'
        And the user is on 'Air Export New Shipment' page
        When the user enter AE MAWB 'Shipment' datas as 'A'
            | field               | attribute    | action | data      |
            | Departure Date/Time | datepicker   | input  | {today+1} |
            | Carrier             | autocomplete | input  | AIR_TP_1  |
        And the user click Air 'Save' button
        Then the shipment 'A' of 'Air Export' will be created
        And AE MAWB 'MAWB No.' should be 'QQQ-'

        # Step 5
        When the user clicks 'system generate' button in 'MAWB No.' and apply pupup dialog
        And the user click save button
        Then AE MAWB 'MAWB No.' should be 'QQQ-00000011'
        And the shipment 'A' of 'Air Export' will be created

        # Step 6
        When the user clear 'MAWB No.' in 'Air Export' shipment 'A'
        And the user click Air 'Save' button
        Then the shipment 'A' of 'Air Export' will be created

        # Step 7
        When the user enter AE MAWB 'Shipment' datas as 'A'
            | field    | attribute | action | data    |
            | MAWB No. | input     | input  | Test123 |
        And the user click Air 'Save' button
        Then the shipment 'A' of 'Air Export' will be created
        And the MAWB No field will show 'Invalid Format' warning

        # Step 8
        When the user click AE 'Add HAWB' button
        And the user enter AE shipment 'A' HAWB(1) 'Shipment' datas
            | field | attribute    | action | data      |
            | Sales | autocomplete | input  | sales_lcl |
        And the user click Air 'Save' button
        Then the shipment 'A' HAWB(1) in 'Air Export' will be created
