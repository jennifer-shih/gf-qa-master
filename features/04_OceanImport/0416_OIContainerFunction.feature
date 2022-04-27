Feature: [OceanImport] OI Container Function

     check the OI Container tab function is working perfectly

     Background: Log in GoFreight with Operator
          Given the user is a 'Operator'
          # use operator account log in
          And the user has a OI Shipment with two HBLs
               # browser to shipment and check the count of HBL, if count of HBL not equal to two, create an OI shipment with two HBL
               | HBL No. |
               | CNTR_H1 |
               | CNTR_H2 |
          And the user is on 'Container and Item of Ocean Import' page
     # browser to the shipment and switch to container tab

     @SFI @LOHAN @OLC
     Scenario: Default value(unit) of MBL container
          Then fields should be default value
               # check fields in current page
               | field       | attribute | default value           |
               | PKG         | select    | {companyDefaultPackage} |
               | Weight      | select    | KG                      |
               | Measurement | select    | CBM                     |

     @SFI @LOHAN @OLC
     Scenario: Unit exchangiing of MBL container
          When the user add a container and input Weight(KG), Measurement(CBM)
          # user click Add button of MBL Container List, and input Weight, Measurement
          Then the fields should be exchanged and show below fields
               # check the exchange value below Weithgt and Measurement fields
               | field       | value | exchange to   |
               | Weight      | 100   | 220.462 LB    |
               | Measurement | 200   | 3,531.466 CFT |


     @SFI @LOHAN
     Scenario: Users can manually input total value(PKG, Weight, Measurement) when tick 'Input total number'
          When the user tick 'Input total number'
          Then the user can input Total PKG, Total Weight, Total Measurement by itself and save without any errors

     @OLC
     Scenario: Users can manually input total value(PKG, Weight, Measurement) when tick 'Manual Input'
          When the user tick 'Manual Input'
          Then the user can input Total PKG, Total Weight, Total Measurement by itself and save without any errors



     @SFI @LOHAN
     Scenario: Assign container to HBL
          Given the user unselect 'Input total number' of Total option
          And the shipment has two containers
               # 先click add 兩次，再輸入兩個container 的info，就不會因為先建的container, index卻比較後面
               | Container No. | PKG | Weight | Measurement |
               | AAAU1234566   | 10  | 20     | 30          |
               | AAAU1234571   | 100 | 200    | 300         |
          When assign container(1) to HBL(1)
          And assign container(2) to HBL(2)
          Then container adv should show values
               | HB/L No. | PKG | Weight | Measurement |
               | CNTR_H1  | 10  | 20     | 30          |
               | CNTR_H2  | 100 | 200    | 300         |

     @OLC
     Scenario: Assign container to HBL
          Given the user select 'Container Total' of Total option
          And the shipment has two containers
               # 先click add 兩次，再輸入兩個container 的info，就不會因為先建的container, index卻比較後面
               | Container No. | PKG | Weight | Measurement |
               | AAAU1234566   | 10  | 20     | 30          |
               | AAAU1234571   | 100 | 200    | 300         |
          When assign container(1) to HBL(1)
          And assign container(2) to HBL(2)
          Then container adv should show values
               | HB/L No. | PKG | Weight | Measurement |
               | CNTR_H1  | 10  | 20     | 30          |
               | CNTR_H2  | 100 | 200    | 300         |
