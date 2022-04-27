@OLC
Feature: [AWB No Management] Advanced Test GQT_131

     https://hardcoretech.atlassian.net/browse/GQT-131

     Scenario: Set permission for OLC-QD_GM and OLC-QD_OP
          Given the user is a 'Super Admin'
          And the user is on 'Permission Management' page
          And settings in 'Permission Management' page are as listed below
               | User       | Navigator Setting - AWB No. Management | Navigator Mawb No. Stock List | MAWB No Stock List Edit | MAWB No Stock List View | Trade Partner Edit | Setting Code Edit | Setting Code View |
               | gm_lcl lee | Allow                                  | Allow                         | Allow                   | Allow                   | Allow              | Allow             | Allow             |
          And settings in 'Permission Management' page are as listed below
               | User       | Navigator Mawb No. Stock List | MAWB No Stock List Edit | MAWB No Stock List View |
               | op_lcl lee | Allow                         | Allow                   | Allow                   |
          And the user has No.1~9 TP named 'AWB_AIR' with below info
               | field   | attribute | action | data        |
               | TP Type | select    | select | AIR CARRIER |
               | Office  | select    | select | QD          |


     Scenario: Setup limit for AWB# Management
          Given the user is a 'General Manager'
          And the user is on 'AWB No. Management' page
          When the user add AWB No. range in 'AWB No. Management'
               | Carrier   | Prefix | Begin No. | End No. | Remark |
               | AWB_AIR_5 | EEE    | 0000000   | 0001000 | test5  |
          Then save data fail message should show
               """
               The range of the serial numbers cannot be larger than 1000. Please edit and try again.
               """


     Scenario: Setup and Delete AWB# Management
          # 4. create awb no. range
          Given the user is a 'General Manager'
          And the user is on 'AWB No. Management' page
          When the user add AWB No. range in 'AWB No. Management'
               | Carrier   | Prefix | Begin No. | End No. | Remark |
               | AWB_AIR_6 | FFF    | 0000001   | 0000100 | TEST6  |
          Then the data is saved successfully
          And 'AWB No. range' should be saved correctly

          # 5. awb no. range can delete if it has not been used
          When the user selects AWB No. range
               | Carrier   | Prefix | Begin No. | End No. | Remark |
               | AWB_AIR_6 | FFF    | 0000001   | 0000100 | TEST6  |
          And the user clicks delete button on AWB No. Management
          Then popup msg should show
               """
               Are you sure to delete the selected AWB No. Range(s) permanently?
               """
          When the user clicks ok button
          Then AWB No. range should NOT be existed
               | Carrier   | Prefix | Begin No. | End No. | Remark |
               | AWB_AIR_6 | FFF    | 0000001   | 0000100 | TEST6  |


     Scenario: Setup, Apply, and Delete AWB#
          # 6. create awb no. range
          Given the user is a 'General Manager'
          And the user is on 'AWB No. Management' page
          When the user add AWB No. range in 'AWB No. Management'
               | Carrier   | Prefix | Begin No. | End No. | Remark |
               | AWB_AIR_7 | GGG    | 0000001   | 0000010 | TEST7  |
          Then the data is saved successfully
          And 'AWB No. range' should be saved correctly

          # 7. OP create AE shipment and apply AWB#
          Given the user is a 'Operator'
          And the user is on 'Air Export New Shipment' page
          When the user enter 'AE MAWB' shipment datas as 'A' and save it
               | field               | attribute    | action | data           |
               | Carrier             | autocomplete | input  | AWB_AIR_7      |
               | MAWB No.            | input        | input  | TMP-{randN(8)} |
               | Departure Date/Time | datepicker   | input  | {today+1}      |
          And the user clicks 'system generate' button in 'MAWB No.'
          Then popup msg should show
               """
               AWB No. already filled. Are you sure you want to generate a new one and replace current one?
               """
          When the user clicks ok button
          Then popup msg should show
               """
               Once you auto-generate AWB No., it will be assigned and non-reversible.Are you sure you want to continue?
               AWB No. Stock: 10
               """
          When the user clicks ok button
          And the user click save button
          Then the data is saved successfully
          And AE MAWB 'MAWB No.' should be 'GGG-00000011'

          # 8. GM cannot delete AWB#
          Given the user is a 'General Manager'
          And the user is on 'AWB No. Management' page
          Then AWB No. range(AWB_AIR_7) should be enabled/disabled
               | Checked  | Carrier | Begin No. | End No.  | Remark  |
               | disabled | enabled | disabled  | disabled | enabled |
          And 'AWB No. range' should be
               | Carrier   | Prefix | Begin No. | End No. | Latest Assigned No. | Remark |
               | AWB_AIR_7 | GGG    | 0000001   | 0000010 | 1                   | TEST7  |

          # 9. OP create AE MAWB from MAWB Stock List
          Given the user is a 'Operator'
          And the user is on 'MAWB Stock List' page
          When the user ticks 'MAWB Stock'
               | Carrier   | Prefix | MAWB No. | Status    |
               | AWB_AIR_7 | GGG    | 0000002  | AVAILABLE |
          And the user clicks 'Create MAWB' button
          And the user enter 'AE MAWB' shipment datas as 'A' and save it
               | field               | attribute  | action | data      |
               | Departure Date/Time | datepicker | input  | {today+1} |
          Given the user is a 'General Manager'
          And the user is on 'AWB No. Management' page
          Then 'AWB No. range' should be
               | Carrier   | Prefix | Begin No. | End No. | Latest Assigned No. | Remark |
               | AWB_AIR_7 | GGG    | 0000001   | 0000010 | 2                   | TEST7  |

          # 10. OP goes to AE MAWB by link in MAWB Stock List, and delete shipment
          Given the user is a 'Operator'
          And the user is on 'MAWB Stock List' page
          When the user clicks 'File No.' link in 'MAWB Stock List'
               | Carrier   | Prefix | MAWB No. | Status   |
               | AWB_AIR_7 | GGG    | 0000001  | ASSIGNED |
          And the user deletes AE MAWB
          Given the user is a 'General Manager'
          And the user is on 'AWB No. Management' page
          Then 'AWB No. range' should be
               | Carrier   | Prefix | Begin No. | End No. | Latest Assigned No. | Remark |
               | AWB_AIR_7 | GGG    | 0000001   | 0000010 | 2                   | TEST7  |

          # 11. check field disabled
          Then AWB No. range(AWB_AIR_7) should be enabled/disabled
               | Checked  | Carrier | Begin No. | End No.  | Remark  |
               | disabled | enabled | disabled  | disabled | enabled |

          # 12. GM create a AWB No. range
          Given the user is a 'General Manager'
          And the user is on 'AWB No. Management' page
          When the user add AWB No. range in 'AWB No. Management'
               | Carrier   | Prefix | Begin No. | End No. | Remark |
               | AWB_AIR_8 | HHH    | 0000001   | 0000010 | TEST8  |
          Then the data is saved successfully

          # 13. OP reserve AWB No., AWB No. Range CANNOT be edited
          Given the user is a 'Operator'
          And the user is on 'MAWB Stock List' page
          When the user ticks 'MAWB Stock'
               | Carrier   | Prefix | MAWB No. |
               | AWB_AIR_8 | HHH    | 0000001  |
          And the user clicks 'Reserve' button
          Given the user is a 'General Manager'
          And the user is on 'AWB No. Management' page
          Then AWB No. range(AWB_AIR_8) should be enabled/disabled
               | Checked  | Carrier | Begin No. | End No.  | Remark  |
               | disabled | enabled | disabled  | disabled | enabled |
          And 'AWB No. range' should be
               | Carrier   | Prefix | Begin No. | End No. | Latest Assigned No. | Remark |
               | AWB_AIR_8 | HHH    | 0000001   | 0000010 | 1                   | TEST8  |

          # 14. OP Unreserve AWB No., AWB No. Range still CANNOT be edited
          Given the user is a 'Operator'
          And the user is on 'MAWB Stock List' page
          When the user ticks 'MAWB Stock'
               | Carrier   | Prefix | MAWB No. |
               | AWB_AIR_8 | HHH    | 0000001  |
          And the user clicks 'Unreserve' button
          Given the user is a 'General Manager'
          And the user is on 'AWB No. Management' page
          Then AWB No. range(AWB_AIR_8) should be enabled/disabled
               | Checked  | Carrier | Begin No. | End No.  | Remark  |
               | disabled | enabled | disabled  | disabled | enabled |
          And 'AWB No. range' should be
               | Carrier   | Prefix | Begin No. | End No. | Latest Assigned No. | Remark |
               | AWB_AIR_8 | HHH    | 0000001   | 0000010 | 1                   | TEST8  |


     Scenario: Apply duplicate AWB# to shipment
          # 15. GM create duplicate AWB# range
          Given the user is a 'General Manager'
          And the user is on 'AWB No. Management' page
          When the user add AWB No. range in 'AWB No. Management'
               | Carrier   | Prefix | Begin No. | End No. | Remark  |
               | AWB_AIR_9 | III    | 0000001   | 0000002 | TEST9-1 |
          Then the data is saved successfully
          When the user add AWB No. range in 'AWB No. Management'
               | Carrier   | Prefix | Begin No. | End No. | Remark  |
               | AWB_AIR_9 | III    | 0000001   | 0000002 | TEST9-2 |
          Then the data is saved successfully

          # 16. OP create 2 shipments and assign AWB#
          Given the user is a 'Operator'
          And the user is on 'Air Export New Shipment' page
          When the user enter 'AE MAWB' shipment datas as 'A' and save it
               | field               | attribute    | action | data           |
               | Carrier             | autocomplete | input  | AWB_AIR_9      |
               | MAWB No.            | input        | input  | TMP-{randN(8)} |
               | Departure Date/Time | datepicker   | input  | {today+1}      |
          And the user clicks 'system generate' button in 'MAWB No.' and apply pupup dialog
          And the user click save button
          Then the data is saved successfully
          Given the user is on 'Air Export New Shipment' page
          When the user enter 'AE MAWB' shipment datas as 'A' and save it
               | field               | attribute    | action | data           |
               | Carrier             | autocomplete | input  | AWB_AIR_9      |
               | MAWB No.            | input        | input  | TMP-{randN(8)} |
               | Departure Date/Time | datepicker   | input  | {today+1}      |
          And the user clicks 'system generate' button in 'MAWB No.' and apply pupup dialog
          And the user click save button
          Then the data is saved successfully

          # 1st AWB No. range has be used and out of order. 2nd has be used 0 of AWB No.
          Given the user is a 'General Manager'
          And the user is on 'AWB No. Management' page
          Then 'AWB No. range' should be
               | Carrier   | Prefix | Begin No. | End No. | Latest Assigned No. | Remark  |
               | AWB_AIR_9 | III    | 0000001   | 0000002 | 2                   | TEST9-1 |
               | AWB_AIR_9 | III    | 0000001   | 0000002 |                     | TEST9-2 |

          # OP create 1 shipment and assign AWB#
          Given the user is a 'Operator'
          And the user is on 'Air Export New Shipment' page
          When the user enter 'AE MAWB' shipment datas as 'A' and save it
               | field               | attribute    | action | data           |
               | Carrier             | autocomplete | input  | AWB_AIR_9      |
               | MAWB No.            | input        | input  | TMP-{randN(8)} |
               | Departure Date/Time | datepicker   | input  | {today+1}      |
          And the user clicks 'system generate' button in 'MAWB No.' and apply pupup dialog
          And the user click save button
          And the user clicks ok button
          Then the data is saved successfully

          # 1st AWB No. range has be used and out of order. 2nd has be used 1 of AWB No.
          Given the user is a 'General Manager'
          And the user is on 'AWB No. Management' page
          Then 'AWB No. range' should be
               | Carrier   | Prefix | Begin No. | End No. | Latest Assigned No. | Remark  |
               | AWB_AIR_9 | III    | 0000001   | 0000002 | 2                   | TEST9-1 |
               | AWB_AIR_9 | III    | 0000001   | 0000002 | 1                   | TEST9-2 |


     Scenario: MAWB Stock List Test -- Preparation
          # 17. Setup AWB# Management for Carrier TP_1
          Given the user is a 'General Manager'
          And the user is on 'AWB No. Management' page
          When the user add AWB No. range in 'AWB No. Management'
               | Carrier   | Prefix | Begin No. | End No. | Remark |
               | AWB_AIR_1 | AAA    | 0000001   | 0000010 | TEST1  |
          Then 'AWB No. range' should be saved correctly

          # 18. Apply AWB# and go to MAWB Stock List check result
          Given the user is a 'Operator'
          And the user is on 'MAWB Stock List' page
          Then 'MAWB Stock List' should be
               | Status    | Prefix | Carrier   | MAWB No. | Created Date |
               | AVAILABLE | AAA    | AWB_AIR_1 | 0000001  | {now}        |
               | AVAILABLE | AAA    | AWB_AIR_1 | 0000002  | {now}        |
               | AVAILABLE | AAA    | AWB_AIR_1 | 0000003  | {now}        |
               | AVAILABLE | AAA    | AWB_AIR_1 | 0000004  | {now}        |
               | AVAILABLE | AAA    | AWB_AIR_1 | 0000005  | {now}        |
               | AVAILABLE | AAA    | AWB_AIR_1 | 0000006  | {now}        |
               | AVAILABLE | AAA    | AWB_AIR_1 | 0000007  | {now}        |
               | AVAILABLE | AAA    | AWB_AIR_1 | 0000008  | {now}        |
               | AVAILABLE | AAA    | AWB_AIR_1 | 0000009  | {now}        |
               | AVAILABLE | AAA    | AWB_AIR_1 | 0000010  | {now}        |


     Scenario: MAWB Stock List Test -- A. Available → Assigned
          # 19. A. Available → Assigned
          # 19.1 auto-gen MAWB No. without saving shipment, 'MAWB Stock' should be 'Available'
          Given the user is a 'Operator'
          And the user is on 'Air Export New Shipment' page
          When the user enter 'AE MAWB' shipment datas as 'A' and save it
               | field               | attribute    | action | data           |
               | Carrier             | autocomplete | input  | AWB_AIR_1      |
               | MAWB No.            | input        | input  | TMP-{randN(8)} |
               | Departure Date/Time | datepicker   | input  | {today+1}      |
          And the user clicks 'system generate' button in 'MAWB No.' and apply pupup dialog
          Then AE MAWB 'MAWB No.' should be 'AAA-00000011'
          When the user open new tab
          Given the user is on 'MAWB Stock List' page
          Then 'MAWB Stock List' should be
               | Status    | Carrier   | Prefix | MAWB No. |
               | AVAILABLE | AWB_AIR_1 | AAA    | 0000001  |

          # 19.2 after saving the shipment, 'MAWB Stock' should be 'Assigned'
          When the user switch to main window
          And the user click save button
          Then the data is saved successfully
          Given the user is on 'MAWB Stock List' page
          Then 'MAWB Stock List' should be
               | Status   | Carrier   | Prefix | MAWB No. |
               | ASSIGNED | AWB_AIR_1 | AAA    | 0000001  |
          When the user clicks 'File No.' link in 'MAWB Stock List'
               | Status   | Carrier   | Prefix | MAWB No. |
               | ASSIGNED | AWB_AIR_1 | AAA    | 0000001  |
          Then AE MAWB 'MAWB No.' should be 'AAA-00000011'


     Scenario: MAWB Stock List Test -- B. Assigned → Available
          # 20. B. Assigned → Available
          # 20.1 delete the shipment then File No. in MAWB No. should be empty
          # Given the user opens a new browser
          Given the user is a 'Operator'
          And the user is on 'MAWB Stock List' page
          When the user clicks 'File No.' link in 'MAWB Stock List'
               | Status   | Carrier   | Prefix | MAWB No. |
               | ASSIGNED | AWB_AIR_1 | AAA    | 0000001  |
          And the user deletes AE MAWB
          Given the user is on 'MAWB Stock List' page
          Then 'MAWB Stock List' should be
               | Status    | Carrier   | Prefix | MAWB No. | File No. |
               | AVAILABLE | AWB_AIR_1 | AAA    | 0000001  |          |

          # 20.2 AWB No. range 'Latest Assigned No' should still be 1
          Given the user is a 'General Manager'
          And the user is on 'AWB No. Management' page
          Then 'AWB No. range' should be
               | Carrier   | Prefix | Begin No. | End No. | Latest Assigned No. | Remark |
               | AWB_AIR_1 | AAA    | 0000001   | 0000010 | 1                   | TEST1  |

          # 21.1 use auto-gen to create another shipment, MAWB No. should be AAA-00000022
          Given the user is a 'Operator'
          And the user is on 'Air Export New Shipment' page
          When the user enter 'AE MAWB' shipment datas as 'A' and save it
               | field               | attribute    | action | data           |
               | Carrier             | autocomplete | input  | AWB_AIR_1      |
               | MAWB No.            | input        | input  | TMP-{randN(8)} |
               | Departure Date/Time | datepicker   | input  | {today+1}      |
          And the user clicks 'system generate' button in 'MAWB No.' and apply pupup dialog
          And the user click save button
          Then AE MAWB 'MAWB No.' should be 'AAA-00000022'

          # 21.2
          Given the user is on 'MAWB Stock List' page
          Then 'MAWB Stock List' should be
               | Status    | Carrier   | Prefix | MAWB No. |
               | AVAILABLE | AWB_AIR_1 | AAA    | 0000001  |
               | ASSIGNED  | AWB_AIR_1 | AAA    | 0000002  |

          # 21.3
          Given the user is a 'General Manager'
          And the user is on 'AWB No. Management' page
          Then 'AWB No. range' should be
               | Carrier   | Prefix | Begin No. | End No. | Latest Assigned No. | Remark |
               | AWB_AIR_1 | AAA    | 0000001   | 0000010 | 2                   | TEST1  |


     Scenario: MAWB Stock List Test -- C. Available → Reserved
          # 22. C. Available → Reserved
          # 22.1 OP click reserve button for 'MAWB No.'
          Given the user is a 'Operator'
          And the user is on 'MAWB Stock List' page
          When the user ticks 'MAWB Stock'
               | Carrier   | Prefix | MAWB No. | Status    |
               | AWB_AIR_1 | AAA    | 0000001  | AVAILABLE |
          And the user clicks 'Reserve' button
          When the user ticks 'MAWB Stock'
               | Carrier   | Prefix | MAWB No. | Status   |
               | AWB_AIR_1 | AAA    | 0000001  | RESERVED |
          Then 'Create MAWB' button is enabled
          And 'MAWB Stock List' should be
               | Status   | Carrier   | Prefix | MAWB No. | File No. |
               | RESERVED | AWB_AIR_1 | AAA    | 0000001  |          |

          # 22.2 AWB No. range 'Last Assigned No.' still be 2
          Given the user is a 'General Manager'
          And the user is on 'AWB No. Management' page
          Then 'AWB No. range' should be
               | Carrier   | Prefix | Begin No. | End No. | Latest Assigned No. | Remark |
               | AWB_AIR_1 | AAA    | 0000001   | 0000010 | 2                   | TEST1  |

          # 22.3 auto-gen awb no without saving
          Given the user is a 'Operator'
          And the user is on 'Air Export New Shipment' page
          When the user enter 'AE MAWB' shipment datas as 'A' and save it
               | field               | attribute    | action | data           |
               | Carrier             | autocomplete | input  | AWB_AIR_1      |
               | MAWB No.            | input        | input  | TMP-{randN(8)} |
               | Departure Date/Time | datepicker   | input  | {today+1}      |
          And the user clicks 'system generate' button in 'MAWB No.' and apply pupup dialog
          Then AE MAWB 'MAWB No.' should be 'AAA-00000033'
          When the user open new tab
          Given the user is on 'MAWB Stock List' page
          Then 'MAWB Stock List' should be
               | Status    | Carrier   | Prefix | MAWB No. |
               | AVAILABLE | AWB_AIR_1 | AAA    | 0000003  |
          Given the user is a 'General Manager'
          And the user is on 'AWB No. Management' page
          Then 'AWB No. range' should be
               | Carrier   | Prefix | Begin No. | End No. | Latest Assigned No. | Remark |
               | AWB_AIR_1 | AAA    | 0000001   | 0000010 | 3                   | TEST1  |


     Scenario: MAWB Stock List Test -- D. Reserved → Assigned
          # 23. D. Reserved → Assigned
          # 23.1
          # Given the user opens a new browser
          Given the user is a 'Operator'
          And the user is on 'MAWB Stock List' page
          When the user ticks 'MAWB Stock'
               | Carrier   | Prefix | MAWB No. | Status   |
               | AWB_AIR_1 | AAA    | 0000001  | RESERVED |
          Then 'Unreserve' button is enabled
          And 'Create MAWB' button is enabled
          And 'Reserve' button is disabled

          # 23.2
          When the user clicks 'Create MAWB' button
          Then AE MAWB 'MAWB No.' should be 'AAA-00000011'
          And AE MAWB 'Carrier' should be 'AWB_AIR_1'

          # 23.3
          When the user enter 'AE MAWB' shipment datas as 'A' and save it
               | field               | attribute  | action | data      |
               | Departure Date/Time | datepicker | input  | {today+1} |
          Then the data is saved successfully
          Given the user is on 'MAWB Stock List' page
          Then 'MAWB Stock List' should be
               | Status   | Carrier   | Prefix | MAWB No. |
               | ASSIGNED | AWB_AIR_1 | AAA    | 0000001  |

          # 23.4
          When the user ticks 'MAWB Stock'
               | Status   | Carrier   | Prefix | MAWB No. |
               | ASSIGNED | AWB_AIR_1 | AAA    | 0000002  |
          Then 'Reserve' button is disabled
          And 'Unreserve' button is disabled
          And 'Create MAWB' button is disabled

          # 23.5
          Given the user is a 'General Manager'
          And the user is on 'AWB No. Management' page
          Then 'AWB No. range' should be
               | Carrier   | Prefix | Begin No. | End No. | Latest Assigned No. | Remark |
               | AWB_AIR_1 | AAA    | 0000001   | 0000010 | 3                   | TEST1  |


     Scenario: MAWB Stock List Test -- E. Reserved → Available
          # 24. E. Reserved → Available
          Given the user is a 'Operator'
          And the user is on 'MAWB Stock List' page
          When the user ticks 'MAWB Stock'
               | Carrier   | Prefix | MAWB No. | Status    |
               | AWB_AIR_1 | AAA    | 0000003  | AVAILABLE |
          And the user clicks 'Reserve' button
          And the user ticks 'MAWB Stock'
               | Carrier   | Prefix | MAWB No. | Status   |
               | AWB_AIR_1 | AAA    | 0000003  | RESERVED |
          Then 'Create MAWB' button is enabled
          And 'Unreserve' button is enabled
          When the user clicks 'Unreserve' button
          Then 'MAWB Stock List' should be
               | Status    | Carrier   | Prefix | MAWB No. |
               | AVAILABLE | AWB_AIR_1 | AAA    | 0000003  |


     Scenario: MAWB Stock List Test -- Copy to new shipment
          # 25. Apply AWB# to shipment and copy to new shipment
          Given the user is a 'Operator'
          And the user is on 'MAWB Stock List' page
          When the user clicks 'File No.' link in 'MAWB Stock List'
               | Carrier   | Prefix | MAWB No. | Status   |
               | AWB_AIR_1 | AAA    | 0000002  | ASSIGNED |
          And the user copied AE MAWB
          Then AE MAWB 'MAWB No.' should be '{blank}'
          When the user enter 'AE MAWB' shipment datas as 'A' and save it
               | field    | attribute | action | data           |
               | MAWB No. | input     | input  | TMP-{randN(8)} |
          Then the data is saved successfully
