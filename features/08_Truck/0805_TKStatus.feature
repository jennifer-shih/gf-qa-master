Feature: [Truck] Check Status

     Background: Log in GoFreight with Operator
          Given the user is a 'Operator'
          And the user is on 'Truck New Shipment' page


     @SFI @LOHAN
     Scenario: Check Roles is correct (For generic)
          When the user enter 'TK MBL' shipment datas as 'A' and save it
               | field | attribute    | action | data       |
               | Sales | autocomplete | input  | sales_joey |
          And the user click 'Status' tab of Truck
          Then OP in TK Status is 'op_joey lee (op_joey)'
          And SALES in TK Status is 'sales_joey lee (sales_joey)'


     @OLC
     Scenario: Check Roles is correct (For enterprise)
          When the user enter 'TK MBL' shipment datas as 'A' and save it
               | field | attribute    | action | data      |
               | Sales | autocomplete | input  | sales_lcl |
          And the user click 'Status' tab of Truck
          Then OP in TK Status is 'op_lcl lee (op_lcl)'
          And SALES in TK Status is 'sales_lcl lee (sales_lcl)'
