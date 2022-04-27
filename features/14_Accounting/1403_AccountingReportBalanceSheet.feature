Feature: [Accounting] Accounting Report - Balance Sheet

     @SFI @LOHAN @OLC
     Scenario: The user want to go to 'Balance Sheet' page
          Given the user is a 'General Manager'
          And the user is on 'Dashboard' page
          When the user browse to 'Balance Sheet' page by navigator
          Then 'Balance Sheet' page show normally

     @SFI
     Scenario: The general manager try to download 'Balance Sheet' report
          Given the download file folder is 'download'
          And the user is a 'General Manager'
          Given the user is on 'Balance Sheet' page
          When the user enter 'Balance Sheet' info
               | field  | attribute  | action | data       |
               | As of  | datepicker | input  | 12-31-2018 |
               | Office | select     | select | All        |
          And the user click 'Balance Sheet' 'Print' button
          And the user click 'Download PDF' button
          Then the 'Balance Sheet' values should be correct
               | field                                      | value         |
               | TOTAL LIABILITIES AND STOCKHOLDERS' EQUITY | 11,175,065.93 |
          And the 'Balance Sheet' file should be saved in download folder (120 sec)
          When the user closes current tab
          And the user choose 'LAX' office for 'Balance Sheet'
          And the user click 'Balance Sheet' 'Print' button
          Then the 'Balance Sheet' values should be correct
               | field                                      | value        |
               | TOTAL LIABILITIES AND STOCKHOLDERS' EQUITY | 9,463,904.29 |
          When the user closes current tab
          And the user choose 'MEO' office for 'Balance Sheet'
          And the user click 'Balance Sheet' 'Print' button
          Then the 'Balance Sheet' values should be correct
               | field                                      | value        |
               | TOTAL LIABILITIES AND STOCKHOLDERS' EQUITY | 1,474,204.03 |

     @LOHAN
     Scenario: The general manager try to download 'Balance Sheet' report
          Given the download file folder is 'download'
          And the user is a 'General Manager'
          Given the user is on 'Balance Sheet' page
          When the user enter 'Balance Sheet' info
               | field  | attribute  | action | data       |
               | As of  | datepicker | input  | 01-31-2021 |
               | Office | select     | select | All        |
          And the user click 'Balance Sheet' 'Print' button
          And the user click 'Download PDF' button
          Then the 'Balance Sheet' values should be correct
               | field                                      | value         |
               | TOTAL LIABILITIES AND STOCKHOLDERS' EQUITY | 53,227,844.91 |
          And the 'Balance Sheet' file should be saved in download folder (120 sec)
          When the user closes current tab
          And the user choose 'NGB' office for 'Balance Sheet'
          And the user click 'Balance Sheet' 'Print' button
          Then the 'Balance Sheet' values should be correct
               | field                                      | value        |
               | TOTAL LIABILITIES AND STOCKHOLDERS' EQUITY | 3,097,635.55 |
          When the user closes current tab
          And the user choose 'SZX' office for 'Balance Sheet'
          And the user click 'Balance Sheet' 'Print' button
          Then the 'Balance Sheet' values should be correct
               | field                                      | value         |
               | TOTAL LIABILITIES AND STOCKHOLDERS' EQUITY | 38,988,291.77 |

     @OLC
     Scenario: The super admin try to download 'Balance Sheet' report
          Given the download file folder is 'download'
          And the user is a 'General Manager'
          Given the user is on 'Balance Sheet' page
          When the user enter 'Balance Sheet' info
               | field  | attribute  | action | data       |
               | As of  | datepicker | input  | 2021-08-01 |
               | Office | select     | select | All        |
          And the user click 'Balance Sheet' 'Print' button
          And the user click 'Download PDF' button
          Then the 'Balance Sheet' values should be correct
               | field                                      | value          |
               | TOTAL LIABILITIES AND STOCKHOLDERS' EQUITY | 166,246,902.52 |
          And the 'Balance Sheet' file should be saved in download folder (120 sec)
