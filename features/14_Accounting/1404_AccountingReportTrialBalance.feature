Feature: [Accounting] Accounting Report - Trial Balance

     @SFI @LOHAN @OLC
     Scenario: The user want to go to 'Trial Balance' page
          Given the user is a 'General Manager'
          And the user is on 'Dashboard' page
          When the user browse to 'Trial Balance' page by navigator
          Then 'Trial Balance' page show normally

     @SFI
     Scenario: The general manager try to download 'Trial Balance' report
          Given the download file folder is 'download'
          And the user is a 'General Manager'
          And the user is on 'Trial Balance' page
          When the user enter 'Trial Balance' info
               | field  | attribute         | action | data                    |
               | Period | period datepicker | input  | 12-01-2017 ~ 01-31-2018 |
               | Office | select            | select | All                     |
          And the user click 'Trial Balance' 'Print' button
          And the user click 'Download PDF' button
          Then the 'Trial Balance' values for 'All' office should be correct
               # ? KNOWN ISSUE GFACCT-1570 and others
               #    | field                   | value         |
               #    | Total Beginning Balance | 67,211,076.95 |
               #    | Total Debit             | 42,445,020.49 |
               #    | Total Credit            | 42,445,020.49 |
               #    | Total Balance           | 82,339,428.25 |
               | field                   | value         |
               | Total Beginning Balance | 67,211,076.96 |
               | Total Debit             | 42,852,456.49 |
               | Total Credit            | 42,852,456.49 |
               | Total Balance           | 82,339,428.26 |

          And the 'Trial Balance' file should be saved in download folder (120 sec)
          When the user closes current tab
          And the user choose 'LAX' office for 'Trial Balance'
          And the user click 'Trial Balance' 'Print' button
          Then the 'Trial Balance' values for 'LAX' office should be correct
               # ? KNOWN ISSUE
               #    | field                   | value         |
               #    | Total Beginning Balance | 59,193,309.31 |
               #    | Total Debit             | 37,722,449.71 |
               #    | Total Credit            | 37,722,449.71 |
               #    | Total Balance           | 71,003,858.35 |
               | field                   | value         |
               | Total Beginning Balance | 59,193,309.32 |
               | Total Debit             | 38,128,521.64 |
               | Total Credit            | 38,128,521.64 |
               | Total Balance           | 71,003,858.36 |
          When the user closes current tab
          And the user choose 'MEO' office for 'Trial Balance'
          And the user click 'Trial Balance' 'Print' button
          Then the 'Trial Balance' values for 'MEO' office should be correct
               # ? KNOWN ISSUE
               #    | field                   | value         |
               #    | Total Beginning Balance | 7,985,417.64  |
               #    | Total Debit             | 3,425,914.34  |
               #    | Total Credit            | 3,425,914.34  |
               #    | Total Balance           | 10,557,017.70 |
               | field                   | value         |
               | Total Beginning Balance | 7,985,417.64  |
               | Total Debit             | 3,427,278.41  |
               | Total Credit            | 3,427,278.41  |
               | Total Balance           | 10,557,017.70 |

     @LOHAN
     Scenario: The general manager try to download 'Trial Balance' report
          Given the download file folder is 'download'
          And the user is a 'General Manager'
          And the user is on 'Trial Balance' page
          When the user enter 'Trial Balance' info
               | field  | attribute         | action | data                    |
               | Period | period datepicker | input  | 12-01-2020 ~ 01-31-2021 |
               | Office | select            | select | All                     |
          And the user click 'Trial Balance' 'Print' button
          And the user click 'Download PDF' button
          Then the 'Trial Balance' values for 'All' office should be correct
               | field                   | value          |
               | Total Beginning Balance | 105,083,756.28 |
               | Total Debit             | 80,008.15      |
               | Total Credit            | 80,008.15      |
               | Total Balance           | 105,160,158.28 |
          And the 'Trial Balance' file should be saved in download folder (120 sec)
          When the user closes current tab
          And the user choose 'NGB' office for 'Trial Balance'
          And the user click 'Trial Balance' 'Print' button
          Then the 'Trial Balance' values for 'NGB' office should be correct
               | field                   | value        |
               | Total Beginning Balance | 6,187,188.20 |
               | Total Debit             | 0.00         |
               | Total Credit            | 0.00         |
               | Total Balance           | 6,187,188.20 |
          When the user closes current tab
          And the user choose 'SZX' office for 'Trial Balance'
          And the user click 'Trial Balance' 'Print' button
          Then the 'Trial Balance' values for 'SZX' office should be correct
               | field                   | value         |
               | Total Beginning Balance | 77,647,426.16 |
               | Total Debit             | 80,008.15     |
               | Total Credit            | 80,008.15     |
               | Total Balance           | 77,723,828.16 |

     @OLC
     Scenario: The general manager try to download 'Trial Balance' report
          Given the download file folder is 'download'
          And the user is a 'General Manager'
          And the user is on 'Trial Balance' page
          When the user enter 'Trial Balance' info
               | field  | attribute         | action | data                    |
               | Period | period datepicker | input  | 2021-05-01 ~ 2021-06-30 |
               | Office | select            | select | All                     |
          And the user click 'Trial Balance' 'Print' button
          And the user click 'Download PDF' button
          Then the 'Trial Balance' values for 'All' office should be correct
               | field                   | value            |
               | Total Beginning Balance | 1,231,684,359.44 |
               | Total Debit             | 745,899,529.88   |
               | Total Credit            | 745,899,529.88   |
               | Total Balance           | 1,542,753,304.62 |
          And the 'Trial Balance' file should be saved in download folder (120 sec)
