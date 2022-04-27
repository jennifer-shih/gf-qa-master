@SFI @LOHAN @OLC
Feature: [Sales] Create Quotation

    Background: Log in GoFreight with Saleperson
        Given the user is a 'Salesperson'

    Scenario Outline: Create a quotation for '<shipping type>' is no problem
        Given the user is on 'New Quotation' page
        When the user close the favorite tool prompt
        And the user enter quotation data for '<shipping type>' as '<shipping type>' and save it
            | field    | attribute    | action | data         |
            | Customer | autocomplete | input  | customer9191 |
        Then the quotation '<shipping type>' will be created

        Examples:
            | shipping type |
            | Ocean Import  |
            | Ocean Export  |
            | Air Import    |
            | Air Export    |
            | Truck         |
            | Misc.         |
            | Warehouse     |
