@SFI @LOHAN @OLC
Feature: [OceanImport] OI MBL Linked Fields

    linked fields of OI MBL work no problem

    Background: Log in GoFreight with Operator
        Given the user is a 'Operator'

    Scenario: Select 'Carrier' then 'B/L Acct. Carrier' should be autofilled with the same value
        Given the user is on 'Ocean Import New Shipment' page
        When the user select 'OCEAN9191' for field 'Carrier'
        Then 'BL Acct. Carrier' should be autofilled with 'OCEAN9191'

    Scenario: Select 'ETA' then 'Post Date' should be autofilled with the same value
        Given the user is on 'Ocean Import New Shipment' page
        When the user create a shipment that 'ETA' is 'today'
        Then 'Post Date' should be autofilled with 'today'

    Scenario Outline: Select specific 'Ship Mode'(LCL/FAK) then 'Service Term' should be changed to 'CFS'
        Given the user is on 'Ocean Import New Shipment' page
        When the user switch 'Ship Mode' to <ship mode>
        Then 'Service Term From' and 'Service Term To' should be change to 'CFS'
        Examples:
            | ship mode |
            | LCL       |
            | FAK       |

    Scenario Outline: Different 'OBL Type' should match specific 'Received'
        Given the user is on 'Ocean Import New Shipment' page
        When the user switch 'OBL Type' to <obl type>
        Then 'Received' field should change to <received>
        Examples: <obl type>-<received>
            | obl type                | received               |
            | EXPRESS BILL OF LADING  | Telex release received |
            | ORIGINAL BILL OF LADING | OB/L Received          |
            | SEAWAY BILL             | Telex release received |
