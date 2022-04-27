@SFI @LOHAN @OLC
Feature: [OceanExport] Create OE Shipment

    the operator can create a shipment of Ocean Emport

    Background: Log in GoFreight with Operator
        Given the user is a 'Operator'

    Scenario: The operator want to go to 'New Shipment' page of Ocean Emport
        Given the user is on 'Dashboard' page
        When the user browse to 'New Shipment of Ocean Export' page by navigator
        Then 'New Shipment of Ocean Export' page show normally

    Scenario: Generate a new shipment with required fields only and default value should be correct
        Given the user is on 'Ocean Export New Shipment' page
        When the user enter 'OE MBL' shipment datas as 'A' and save it
            | field    | attribute    | action | data            |
            | MB/L No. | input        | input  | HACO-{randN(6)} |
            | Office   | autocomplete | input  | LAX             |
            | ETD      | datepicker   | input  | {today+5}       |
        Then the shipment 'A' of 'Ocean Export' will be created
