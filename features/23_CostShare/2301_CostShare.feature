@OLC_TPE
Feature: [Vessel Schedule] Cost Share

     GQT-184
     https://hardcoretech.atlassian.net/browse/GQT-184

     Scenario: Cost Share enabling test
          # Step 2
          Given the user is a 'Super Admin'
          And the user is on 'Company Management' page
          And settings in 'Company Management' page are as listed below
               | field      | attribute | action | data |
               | Enable Tax | checkbox  | tick   | {on} |
          And the user is on 'Office Management' page
          And settings in 'QD' 'Office Entry' page are as listed below
               | field      | attribute | action | data  |
               | Enable Tax | checkbox  | tick   | {off} |
          And the user is on 'Office Management' page
          And settings in 'TPE' 'Office Entry' page are as listed below
               | field                        | attribute          | action | data                       |
               | Enable Branch List           | checkbox           | tick   | {on}                       |
               | Branch List                  | tag input          | input  | TPE;TCH;KAO;KEE            |
               | Multiple POL & POD           | checkbox           | tick   | {on}                       |
               | Multiple Port Cut-Off dates  | checkbox           | tick   | {on}                       |
               | Location List                | multi autocomplete | input  | KEELUNG;KAOHSIUNG;TAICHUNG |
               | Enable Tax                   | checkbox           | tick   | {on}                       |
               | AR Tax Opt.                  | tag input          | input  | 應稅                       |
               | A/R - Tax value when P/C = P | select             | select | 應稅                       |
               | AR 0-Tax Opt.                | tag input          | input  | 免稅                       |
               | A/R - Tax value when P/C = C | select             | select | 免稅                       |
               | AR Exempt Opt.               | tag input          | input  | 收據;代收付                |
               | AP Tax Opt.                  | tag input          | input  | 應稅                       |
               | A/P - Tax value when P/C = P | select             | select | 應稅                       |
               | AP 0-Tax Opt.                | tag input          | input  | 零稅                       |
          And the user is on 'System Configuration' page
          And settings in 'TPE' 'System Configuration' page are as listed below
               | field                                                          | attribute | action | data                                        |
               | OE HBL Style                                                   | select    | select | ORIENTAL LOGISTICS GROUP LTD. TPE (OLC-TPE) |
               | OE HBL Booking Confirmation Style                              | select    | select | OLC TPE                                     |
               | Enable OE Vessel Freight List                                  | checkbox  | tick   | {on}                                        |
               | Enable Allocate FCL profits per shipment (others by CBM share) | checkbox  | tick   | {on}                                        |
               | Vessel Based (Merge/Split Bookings)                            | checkbox  | tick   | {on}                                        |
               | Enable FCL/LCL                                                 | checkbox  | tick   | {on}                                        |
               | Enable Back Date                                               | checkbox  | tick   | {on}                                        |
               | Show Extra Agent in OE/Booking                                 | checkbox  | tick   | {on}                                        |
               | Enable auto-gen CNTR from booking                              | checkbox  | tick   | {on}                                        |
               | Enable Cost Share                                              | checkbox  | tick   | {on}                                        |
               | Enable Handle Agent at Container List                          | checkbox  | tick   | {on}                                        |
               | Enable copy existing hawb                                      | checkbox  | tick   | {on}                                        |
               | Enable Front Desk Portal                                       | checkbox  | tick   | {on}                                        |
          And the user is on 'Permission Management' page
          And settings in 'Permission Management' page are as listed below
               | User       | Uniform Invoice Edit Void/Valid |
               | op_tpe lee | Allow                           |

          # Step 3
          Given the user is a 'Operator' in 'TPE' office
          And the user has a OI MBL with 1 HBL as 'A' with only required fields filled
          When the user goes to OI Accounting Tab (Billing Based)
          Then there is no 'Cost Share' text in the web page

          Given the user has a OE MBL with 1 HBL as 'A' with only required fields filled
          When the user goes to OE Accounting Tab (Billing Based)
          Then there is no 'Cost Share' text in the web page

          Given the user has a OE Booking as 'A' with only required fields filled
          When the user goes to OEBK Accounting Tab (Billing Based)
          Then there is no 'Cost Share' text in the web page

          Given the user has a AI MAWB with 1 HAWB as 'A' with only required fields filled
          When the user goes to AI Accounting Tab (Billing Based)
          Then there is no 'Cost Share' text in the web page

          Given the user has a AE MAWB with 1 HAWB as 'A' with only required fields filled
          When the user goes to AE Accounting Tab (Billing Based)
          Then there is no 'Cost Share' text in the web page

          Given the user has a TK MBL as 'A' with only required fields filled
          When the user goes to TK Accounting Tab (Billing Based)
          Then there is no 'Cost Share' text in the web page

          Given the user has a MS MBL as 'A' with only required fields filled
          When the user goes to MS Accounting Tab (Billing Based)
          Then there is no 'Cost Share' text in the web page

          Given the user has a WH Receiving as 'A' with only required fields filled
          When the user goes to WH Receiving Accounting Tab (Billing Based)
          Then there is no 'Cost Share' text in the web page

          Given the user has a WH Shipping as 'A' with only required fields filled
          When the user goes to WH Shipping Accounting Tab (Billing Based)
          Then there is no 'Cost Share' text in the web page

     Scenario: Cost Share general test 1
          # Step 4
          Given the user is a 'Operator' in 'TPE' office
          And the user has a OEVS VS with 0 BK as 'A' with only required fields filled
          When the user click OEVS 'Add Booking' button
          And the user enter 'OEVS BK(1)' shipment datas as 'A' and save it
               | field | attribute | action | data |
          And the user enter OEVS BK(1) 'Container list' datas and save it
               | field       | attribute | action | data |
               | PKG         | input     | input  | 1    |
               | Weight      | input     | input  | 2500 |
               | Measurement | input     | input  | 3    |
          And the user click save button
          When the user click OEVS 'Add Booking' button
          And the user enter 'OEVS BK(2)' shipment datas as 'A' and save it
               | field | attribute | action | data |
          And the user enter OEVS BK(2) 'Container list' datas and save it
               | field       | attribute | action | data |
               | PKG         | input     | input  | 3    |
               | Weight      | input     | input  | 1700 |
               | Measurement | input     | input  | 3    |
          And the user click save button
          And the user goes to OEVS Accounting Tab (Invoice Based)
          Then there is no 'Cost Share' text in the web page
          When the user clicks OEVS VS 'Create AR' button
          Then there is no 'Cost Share' text in the web page
          When the user goes back to the previous page
          And the user clicks OEVS VS 'Create AP' button
          Then there is no 'Cost Share' text in the web page
          When the user goes back to the previous page
          And the user clicks OEVS VS 'Create DC' button
          Then there is no 'Cost Share' text in the web page
          When the user goes back to the previous page

          # Step 5
          And the user goes to OEVS Accounting Tab (Billing Based)
          And the user switch to BK(1) in OEVS
          And the user adds freights to OEVS BK revenue
               | Bill to  | Freight code | Volume | Rate |
               | RAIL9191 | FILM WRAP    | 1      | 100  |
          And the user adds freights to OEVS BK cost
               | Bill to  | Freight code | Volume | Rate |
               | RAIL9191 | FILM WRAP    | 1      | 200  |
          And the user clicks save button in OEBK Accounting Billing Based
          And the user switch to BK(2) in OEVS
          And the user adds freights to OEVS BK revenue
               | Bill to  | Freight code | Volume | Rate |
               | RAIL9191 | FILM WRAP    | 1      | 50   |
          And the user clicks save button in OEBK Accounting Billing Based
          And the user switch to BK(1) in OEVS
          Then the OEVS BK amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -100.00       |
          When the user switch to BK(2) in OEVS
          Then the OEVS BK amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | 50.00         |

          # Step 6
          When the user switch to BK(1) in OEVS
          And the user input freights information to OEVS BK cost
               | No. | Cost Share |
               | 1   | {on}       |
          And the user clicks save button in OEVS Accounting Billing Based
          Then the OEVS BK amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -100.00       |
          When the user switch to BK(2) in OEVS
          Then the OEVS BK amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | 50.00         |

          # Step 7
          When the user goes to OEVS Basic Tab
          Then 'Handle Agent' field should be visible in OEVS Container List
          When the user add continers to OEVS VS 'Container list'
               | Container No. | TP/SZ |
               | CON-20DC      | 20DC  |
               | CON-40GP      | 40GP  |
          And the user click save button
          When the user load BKs' information to the container(1) in OEVS
               | Booking No. |
               | 1           |
               | 2           |
          And the user goes to OEVS Accounting Tab (Billing Based)
          And the user switch to BK(1) in OEVS
          Then the OEVS BK amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | 0.00          |
          When the user switch to BK(2) in OEVS
          Then the OEVS BK amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -50.00        |

          # Step 8
          When the user goes to OEVS Basic Tab
          #? KNOWN ISSUE OLC-5074
          # The order of container shouldn't change
          And the user creates 1 MBL as 'B' from containers in OEVS
               | No. |
               | 2   |
          And the user goes to OE Accounting Tab (Billing Based)
          Then the OEVS BK amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | 0.00          |
          When the user switch to HBL(2) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -50.00        |

          # Step 9
          When the user switch to HBL(1) in OE
          And the user input freights information to OE HBL cost
               | No. | Cost Share |
               | 1   | {off}      |
          And the user clicks save button in OE Accounting Billing Based
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -100.00       |
          When the user switch to HBL(2) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | 50.00         |
          When the user switch to HBL(1) in OE
          And the user input freights information to OE HBL cost
               | No. | Cost Share |
               | 1   | {on}       |
          And the user clicks save button in OE Accounting Billing Based
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | 0.00          |
          When the user switch to HBL(2) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -50.00        |

          When the user refresh browser
          When the user switch to HBL(1) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | 0.00          |
          When the user switch to HBL(2) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -50.00        |

          # Step 10
          When the user click OE 'Add HBL' button
          And the user click save button

          And the user goes to OE Accounting Tab (Billing Based)
          And the user switch to HBL(1) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | 0.00          |
          When the user switch to HBL(2) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -50.00        |
          When the user switch to HBL(3) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | 0.00          |

          When the user goes to OE Container Tab
          And the user switch to HBL(3) in OE
          And the user enters datas to OE HBL 'Container List'
               | field                          | attribute   | action | data               |
               | Total Amount Source            | radio group | click  | Manual Input Total |
               | Manual Input Total PKG         | input       | input  | 2                  |
               | Manual Input Total Weight      | input       | input  | 5800               |
               | Manual Input Total Measurement | input       | input  | 1                  |
          And the user click save button

          And the user goes to OE Accounting Tab (Billing Based)
          And the user switch to HBL(1) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | 50.00         |
          When the user switch to HBL(2) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | 16.00         |
          When the user switch to HBL(3) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -116.00       |

          # Step 11
          When the user adds freights to OE HBL cost
               | Bill to     | Freight code | Volume | Rate |
               | TRUCKER9191 | FILM WRAP    | 1      | 500  |
          And the user input freights information to OE HBL cost
               | No. | Cost Share |
               | 1   | {on}       |
          And the user clicks save button in OE Accounting Billing Based
          And the user switch to HBL(1) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -75.00        |
          When the user switch to HBL(2) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -69.00        |
          When the user switch to HBL(3) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -406.00       |

          # Step 12
          When the user goes to OE Container Tab
          And the user expand OE MBL block
          And the user assign / unassign HBL to containers in OE shipment
               | Container No. | HBL No. | Assign |
               | 1             | 3       | {off}  |
          And the user goes to OE Accounting Tab (Billing Based)
          And the user switch to HBL(1) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | 0.00          |
          When the user switch to HBL(2) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -50.00        |
          When the user switch to HBL(3) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -500.00       |

          When the user goes to OE Container Tab
          And the user deletes containers in OE Container Tab
               | No. |
               | 1   |
          And the user goes to OE Accounting Tab (Billing Based)
          And the user switch to HBL(1) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -100.00       |
          When the user switch to HBL(2) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | 50.00         |
          When the user switch to HBL(3) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -500.00       |

          When the user goes to OE Container Tab
          And the user click 'Add' of OE MBL Container List
          And the user enters datas to OE MBL container(1)
               | field         | attribute | action | data     |
               | Container No. | input     | input  | CON-40DC |
               | TP/SZ         | select    | select | 40DC     |
          And the user click save button
          And the user assign / unassign HBL to containers in OE shipment
               | Container No. | HBL No. | Assign |
               | 1             | 1       | {on}   |
               | 1             | 2       | {on}   |
               | 1             | 3       | {on}   |
          And the user goes to OE Accounting Tab (Billing Based)
          And the user switch to HBL(1) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -75.00        |
          When the user switch to HBL(2) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -69.00        |
          When the user switch to HBL(3) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -406.00       |

          # Step 13
          Given the user has a OE Booking as 'C' with only required fields filled
          When the user enter OEBK 'Container List' datas
               | field               | attribute | action | data |
               | Booking PKG         | input     | input  | 1    |
               | Booking Weight      | input     | input  | 0    |
               | Booking Measurement | input     | input  | 13   |
          And the user links the OEBK to the shipment 'B'
          And the user click save button
          And the user goes to OEBK Accounting Tab (Billing Based)
          When the user adds freights to OEBK cost
               | Bill to              | Freight code | Volume | Rate |
               | {randomTradePartner} | FILM WRAP    | 1      | 1000 |
          And the user clicks save button in OEBK Accounting Billing Based
          Then the OEBK amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -1,455.00     |

          # Step 14
          When the user goes back to OE Shipment 'B'
          And the user goes to OE Accounting Tab (Billing Based)
          And the user switch to HBL(1) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -5.00         |
          When the user switch to HBL(2) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -55.00        |
          When the user switch to HBL(3) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -35.00        |
          When the user switch to HBL(4) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -1,455.00     |

          # Step 15
          When the user goes back to OEBK 'C'
          And the user goes to OEBK Accounting Tab (Billing Based)
          And the user input freights information to OEBK cost
               | No. | Cost Share |
               | 1   | {on}       |
          And the user clicks save button in OEBK Accounting Billing Based
          Then the OEBK amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -1105.00      |

          When the user goes back to OE Shipment 'B'
          And the user goes to OE Accounting Tab (Billing Based)
          And the user switch to HBL(1) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -155.00       |
          When the user switch to HBL(2) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -205.00       |
          When the user switch to HBL(3) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -85.00        |
          When the user switch to HBL(4) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -1,105.00     |
          And values in OEVS BK revenue should be correct
               | No. | Cost Share |
               | 1   | {on}       |

          # Step 16
          When the user goes to OE Container Tab
          And the user click 'Add' of OE MBL Container List
          And the user enters datas to OE MBL container(1)
               | field         | attribute | action | data     |
               | Container No. | input     | input  | CON-53HC |
               | TP/SZ         | select    | select | 53HC     |
          And the user click save button
          And the user assign / unassign HBL to containers in OE shipment
               | Container No. | HBL No. | Assign |
               | 1             | 1       | {on}   |
               | 1             | 2       | {on}   |
               | 2             | 1       | {off}  |
               | 2             | 2       | {off}  |
          And the user goes to OE Accounting Tab (Billing Based)
          And the user switch to HBL(1) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | 0.00          |
          When the user switch to HBL(2) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -50.00        |
          When the user switch to HBL(3) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -107.14       |
          When the user switch to HBL(4) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -1,392.86     |

          # Step 17
          When the user goes to OE Container Tab
          And the user click 'More' button of OE MBL container(1)
          And the user enters datas to OE MBL container(1)
               | field        | attribute    | action | data         |
               | Handle Agent | autocomplete | input  | OVERSEAS9191 |
          And the user click 'More' button of OE MBL container(2)
          And the user enters datas to OE MBL container(2)
               | field        | attribute    | action | data         |
               | Handle Agent | autocomplete | input  | OVERSEAS9191 |
          And the user click save button

          And the user goes to OE Accounting Tab (Billing Based)
          And the user switch to HBL(1) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -155.00       |
          When the user switch to HBL(2) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -205.00       |
          When the user switch to HBL(3) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -85.00        |
          When the user switch to HBL(4) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -1,105.00     |

          # Step 18
          When the user goes to OE Container Tab
          And the user click 'More' button of OE MBL container(1)
          And the user enters datas to OE MBL container(1)
               | field        | attribute    | action | data         |
               | Handle Agent | autocomplete | input  | TERMINAL9191 |
          And the user click save button

          And the user goes to OE Accounting Tab (Billing Based)
          And the user switch to HBL(1) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | 0.00          |
          When the user switch to HBL(2) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -50.00        |
          When the user switch to HBL(3) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -107.14       |
          When the user switch to HBL(4) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -1,392.86     |


     Scenario: Cost Share general test 2
          # Step 19
          Given the user is a 'Operator' in 'TPE' office
          And the user has a OEVS VS with 4 BK as 'A' with only required fields filled
          When the user create a HBL by '1 to 1' from OEVS BK(1)
          And the user create a HBL by 'Merge' from OEVS BK(2, 3)
          And the user create 2 HBL by 'Split' from OEVS BK(4)

          And the user goes to OEVS Accounting Tab (Billing Based)
          And the user switch to HBL(1) in OEVS
          And the user adds freights to OEVS HBL cost
               | Bill to              | Freight code | Volume | Rate |
               | {randomTradePartner} | FILM WRAP    | 1      | 100  |
          And the user clicks save button in OEVS Accounting Billing Based
          # KNOWN ISSUE: the order of HBLs should be the same as the order that they are created
          And the user switch to HBL(3) in OEVS
          And the user adds freights to OEVS HBL revenue
               | Bill to              | Freight code | Volume | Rate |
               | {randomTradePartner} | FILM WRAP    | 1      | 500  |
          And the user adds freights to OEVS HBL cost
               | Bill to              | Freight code | Volume | Rate |
               | {randomTradePartner} | FILM WRAP    | 1      | 300  |
          And the user input freights information to OEVS HBL cost
               | No. | Cost Share |
               | 1   | {on}       |
          And the user clicks save button in OEVS Accounting Billing Based
          And the user switch to HBL(2) in OEVS
          And the user adds freights to OEVS HBL revenue
               | Bill to              | Freight code | Volume | Rate |
               | {randomTradePartner} | FILM WRAP    | 1      | 400  |
          And the user clicks save button in OEVS Accounting Billing Based
          And the user switch to HBL(4) in OEVS
          And the user adds freights to OEVS HBL cost
               | Bill to              | Freight code | Volume | Rate |
               | {randomTradePartner} | FILM WRAP    | 1      | 45   |
          And the user clicks save button in OEVS Accounting Billing Based

          # Step 20
          When the user goes to OEVS Basic Tab
          And the user add continers to OEVS VS 'Container list'
               | Container No. | Handle Agent | TP/SZ |
               | CON-12RF      | AIR9191      | 12RF  |
               | CON-20GP      | TERMINAL9191 | 20GP  |
               | CON-53FT      | AIR9191      | 53FT  |
          And the user click save button
          And the user switch to HBL(1) in OEVS
          And the user load HBLs' information to the container(1) in OEVS
               | HBL No. |
               | 1       |
          And the user load HBLs' information to the container(1) in OEVS
               | HBL No. |
               | 2       |
          And the user load HBLs' information to the container(1) in OEVS
               | HBL No. |
               | 1       |
               | 2       |

          When the user goes to OEVS Accounting Tab (Billing Based)
          And the user switch to HBL(1) in OEVS
          Then the OEVS HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -100.00       |
          When the user switch to HBL(3) in OEVS
          Then the OEVS HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | 200.00        |
          When the user switch to HBL(2) in OEVS
          Then the OEVS HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | 400.00        |
          When the user switch to HBL(4) in OEVS
          Then the OEVS HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -45.00        |

          # Step 21
          When the user goes to OEVS Basic Tab
          #？ KNOWN ISSUE OLC-5074  每次Container的順序可能不一樣
          And the user inputs containers information to OEVS VS
               | Container No. | Handle Agent |
               | CON-20GP      | AIR9191      |
          And the user click save button

          And the user goes to OEVS Accounting Tab (Billing Based)
          And the user switch to HBL(1) in OEVS
          Then the OEVS HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -100.00       |
          When the user switch to HBL(3) in OEVS
          Then the OEVS HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | 200.00        |
          When the user switch to HBL(2) in OEVS
          Then the OEVS HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | 400.00        |
          When the user switch to HBL(4) in OEVS
          Then the OEVS HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -45.00        |

          # Step 22
          When the user goes to OEVS Basic Tab
          And the user switch to HBL(1) in OEVS
          And the user enter OEVS HBL 'Container List' datas
               | field                    | attribute | action | data |
               | Manual Input Measurement | input     | input  | 2.5  |
          And the user click save button
          And the user switch to HBL(2) in OEVS
          And the user enter OEVS HBL 'Container List' datas
               | field                    | attribute | action | data |
               | Manual Input Measurement | input     | input  | 2.5  |
          And the user click save button
          And the user switch to HBL(3) in OEVS
          And the user enter OEVS HBL 'Container List' datas
               | field                    | attribute | action | data |
               | Manual Input Measurement | input     | input  | 2.5  |
          And the user click save button
          And the user switch to HBL(4) in OEVS
          And the user enter OEVS HBL 'Container List' datas
               | field                    | attribute | action | data |
               | Manual Input Measurement | input     | input  | 2.5  |
          And the user click save button

          And the user goes to OEVS Accounting Tab (Billing Based)
          And the user switch to HBL(1) in OEVS
          Then the OEVS HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -175.00       |
          When the user switch to HBL(3) in OEVS
          Then the OEVS HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | 425.00        |
          When the user switch to HBL(2) in OEVS
          Then the OEVS HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | 325.00        |
          When the user switch to HBL(4) in OEVS
          Then the OEVS HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -120.00       |

          # Step 23
          When the user goes to OEVS Basic Tab
          And the user creates 1 MBL as 'B' from containers in OEVS
               | Container No. |
               | CON-12RF      |
               | CON-20GP      |
          And the user goes to OE Accounting Tab (Billing Based)
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -250.00       |
          When the user switch to HBL(2) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | 350.00        |
          When the user closes current tab

          And the user creates 1 MBL as 'C' from containers in OEVS
               | Container No. |
               | CON-53FT      |
          And the user goes to OE Accounting Tab (Billing Based)
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | 400.00        |
          When the user switch to HBL(2) in OE
          Then the OE HBL amounts and profits should show correctly in Billing Based
               | Profit Amount |
               | -45.00        |

     Scenario: Cost Share disabling test
          # Step 24
          Given the user is a 'Super Admin'
          And the user is on 'System Configuration' page
          And settings in 'TPE' 'System Configuration' page are as listed below
               | field             | attribute | action | data  |
               | Enable Cost Share | checkbox  | tick   | {off} |

          # Step 25
          Given the user is a 'Operator' in 'TPE' office
          And the user has a OI MBL with 1 HBL as 'A' with only required fields filled
          When the user goes to OI Accounting Tab (Billing Based)
          Then there is no 'Cost Share' text in the web page

          Given the user has a OE MBL with 1 HBL as 'A' with only required fields filled
          When the user goes to OE Accounting Tab (Billing Based)
          Then there is no 'Cost Share' text in the web page

          Given the user has a OE Booking as 'A' with only required fields filled
          When the user goes to OEBK Accounting Tab (Billing Based)
          Then there is no 'Cost Share' text in the web page

          Given the user has a OEVS VS with 1 BK as 'A' with only required fields filled
          When the user goes to OEVS Accounting Tab (Billing Based)
          Then there is no 'Cost Share' text in the web page

          Given the user has a OEVS VS with 1 BK as 'A' with only required fields filled
          When the user create a HBL by '1 to 1' from OEVS BK(1)
          And the user goes to OEVS Accounting Tab (Billing Based)
          Then there is no 'Cost Share' text in the web page

          Given the user has a AI MAWB with 1 HAWB as 'A' with only required fields filled
          When the user goes to AI Accounting Tab (Billing Based)
          Then there is no 'Cost Share' text in the web page

          Given the user has a AE MAWB with 1 HAWB as 'A' with only required fields filled
          When the user goes to AE Accounting Tab (Billing Based)
          Then there is no 'Cost Share' text in the web page

          Given the user has a TK MBL as 'A' with only required fields filled
          When the user goes to TK Accounting Tab (Billing Based)
          Then there is no 'Cost Share' text in the web page

          Given the user has a MS MBL as 'A' with only required fields filled
          When the user goes to MS Accounting Tab (Billing Based)
          Then there is no 'Cost Share' text in the web page

          Given the user has a WH Receiving as 'A' with only required fields filled
          When the user goes to WH Receiving Accounting Tab (Billing Based)
          Then there is no 'Cost Share' text in the web page

          Given the user has a WH Shipping as 'A' with only required fields filled
          When the user goes to WH Shipping Accounting Tab (Billing Based)
          Then there is no 'Cost Share' text in the web page
