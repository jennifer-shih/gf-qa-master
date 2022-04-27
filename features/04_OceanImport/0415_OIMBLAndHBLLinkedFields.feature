@SFI @LOHAN @OLC
Feature: [OceanImport] OI MBL And HBL Linked Fields

    the OI HBL fields link with MBL fields

    Background: Log in GoFreight with Operator
        Given the user is a 'Operator'

    Scenario: Entries should be fill to the new HBL
        Given the user is on 'Ocean Import New Shipment' page
        When the user input 'SBL-TEST' for MBL field 'Sub BL No.'
        Then new HBL field 'Sub BL No.' should be autofilled with 'SBL-TEST'
