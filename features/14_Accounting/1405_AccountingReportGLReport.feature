Feature: [Accounting] Accounting Report - General Ledger Report

    @SFI @LOHAN
    Scenario: The user want to go to 'General Ledger Report' page
        Given the user is a 'General Manager'
        And the user is on 'Dashboard' page
        When the user browse to 'General Ledger Report' page by navigator
        Then 'General Ledger Report' page show normally

    @OLC
    Scenario: The user want to go to 'General Ledger Report' page
        Given the user is a 'Super Admin'
        And the user is on 'Dashboard' page
        When the user browse to 'General Ledger Report' page by navigator
        Then 'General Ledger Report' page show normally

    @SFI
    Scenario: The general manager try to download 'General Ledger Report' summary report
        Given the download file folder is 'download'
        And the user is a 'General Manager'
        And the user is on 'General Ledger Report' page
        When the user enter 'General Ledger Report' info
            | field       | attribute         | action | data                    |
            | Report Type | radio group       | click  | Summary                 |
            | Period      | period datepicker | input  | 12-01-2017 ~ 01-31-2018 |
            | Office      | select            | select | All                     |
        And the user click 'General Ledger Report' 'Print' button
        And the user click 'Download PDF' button
        And the user click 'Download Excel' button
        Then the 'General Ledger Report' summary values for 'All' office should be correct
            | field         | value         |
            | Total Balance | 15,128,351.30 |
        And the 'General Ledger Report' summary pdf file should be saved in download folder (120 sec)
        And the 'General Ledger Report' summary excel file should be saved in download folder (120 sec)
        When the user closes current tab
        And the user choose 'MEO' office for 'General Ledger Report'
        And the user click 'General Ledger Report' 'Print' button
        Then the 'General Ledger Report' summary values for 'MEO' office should be correct
            | field         | value        |
            | Total Balance | 2,571,600.06 |

    @SFI
    Scenario: The general manager try to download 'General Ledger Report' detail report
        Given the download file folder is 'download'
        And the user is a 'General Manager'
        And the user is on 'General Ledger Report' page
        When the user enter 'General Ledger Report' info
            | field               | attribute         | action | data                    |
            | Report Type         | radio group       | click  | Detail                  |
            | Period              | period datepicker | input  | 12-01-2017 ~ 01-31-2018 |
            | Office              | select            | select | All                     |
            | G/L No. Range Start | autocomplete      | input  | 50240                   |
        And the user click 'General Ledger Report' 'Print' button
        And the user click 'Download PDF' button
        And the user click 'Download Excel' button
        Then the 'General Ledger Report' detail values for 'All' office should be correct
            | field         | value     |
            | Total Balance | 39,551.95 |
            | Total Credit  | 13,137.53 |
        And the 'General Ledger Report' detail pdf file should be saved in download folder (120 sec)
        And the 'General Ledger Report' detail excel file should be saved in download folder (120 sec)
        When the user closes current tab
        And the user choose 'MEO' office for 'General Ledger Report'
        And the user click 'General Ledger Report' 'Print' button
        Then the 'General Ledger Report' detail values for 'MEO' office should be correct
            | field         | value     |
            | Total Balance | 12,973.92 |
            | Total Credit  | 0.00      |

    @SFI
    Scenario: The general manager try to download 'General Ledger Report' trade partner summary report
        Given the download file folder is 'download'
        And the user is a 'General Manager'
        And the user is on 'General Ledger Report' page
        When the user enter 'General Ledger Report' info
            | field               | attribute         | action | data                    |
            | Report Type         | radio group       | click  | Trade Partner Summary   |
            | Period              | period datepicker | input  | 12-01-2017 ~ 01-31-2018 |
            | Office              | select            | select | All                     |
            | G/L No. Range Start | autocomplete      | input  | 45601                   |
            | G/L No. Range End   | autocomplete      | input  | 45607                   |
        And the user click 'General Ledger Report' 'Print' button
        And the user click 'Download PDF' button
        And the user click 'Download Excel' button
        Then the 'General Ledger Report' tp summary values for 'All' office should be correct
            | field         | value        |
            | Total Balance | 2,692,116.81 |
        And the 'General Ledger Report' tp summary pdf file should be saved in download folder (120 sec)
        And the 'General Ledger Report' tp summary excel file should be saved in download folder (120 sec)
        When the user closes current tab
        And the user choose 'MEO' office for 'General Ledger Report'
        And the user enter 'General Ledger Report' info
            | field               | attribute    | action | data  |
            | G/L No. Range Start | autocomplete | input  | 10260 |
            | G/L No. Range End   | autocomplete | input  | 20410 |
        And the user click 'General Ledger Report' 'Print' button
        Then the 'General Ledger Report' tp summary values for 'MEO' office should be correct
            | field         | value        |
            | Total Balance | 1,047,736.60 |

    @SFI
    Scenario: The general manager try to download 'General Ledger Report' G&A expense report
        Given the download file folder is 'download'
        And the user is a 'General Manager'
        And the user is on 'General Ledger Report' page
        When the user enter 'General Ledger Report' info
            | field       | attribute         | action | data                    |
            | Report Type | radio group       | click  | G&A Expense             |
            | Period      | period datepicker | input  | 12-01-2017 ~ 01-31-2018 |
            | Office      | select            | select | All                     |
        And the user click 'General Ledger Report' 'Print' button
        And the user click 'Download PDF' button
        Then the 'General Ledger Report' A&G expense values for 'All' office should be correct
            | field         | value |
            | Total Balance | 0.00  |
        And the 'General Ledger Report' A&G expense pdf file should be saved in download folder (120 sec)
        When the user closes current tab
        And the user choose 'MEO' office for 'General Ledger Report'
        And the user click 'General Ledger Report' 'Print' button
        Then the 'General Ledger Report' A&G expense values for 'MEO' office should be correct
            | field         | value |
            | Total Balance | 0.00  |

    @LOHAN
    Scenario: The general manager try to download 'General Ledger Report' summary report
        Given the download file folder is 'download'
        And the user is a 'General Manager'
        And the user is on 'General Ledger Report' page
        When the user enter 'General Ledger Report' info
            | field       | attribute         | action | data                    |
            | Report Type | radio group       | click  | Summary                 |
            | Period      | period datepicker | input  | 07-01-2020 ~ 07-31-2020 |
            | Office      | select            | select | All                     |
        And the user click 'General Ledger Report' 'Print' button
        And the user click 'Download PDF' button
        And the user click 'Download Excel' button
        Then the 'General Ledger Report' summary values for 'All' office should be correct
            | field         | value        |
            | Total Balance | 6,273,285.42 |
        And the 'General Ledger Report' summary pdf file should be saved in download folder (120 sec)
        And the 'General Ledger Report' summary excel file should be saved in download folder (120 sec)
        When the user closes current tab
        And the user choose 'NGB' office for 'General Ledger Report'
        And the user click 'General Ledger Report' 'Print' button
        Then the 'General Ledger Report' summary values for 'NGB' office should be correct
            | field         | value |
            | Total Balance | 0.00  |

    @LOHAN
    Scenario: The general manager try to download 'General Ledger Report' detail report
        Given the download file folder is 'download'
        And the user is a 'General Manager'
        And the user is on 'General Ledger Report' page
        When the user enter 'General Ledger Report' info
            | field               | attribute         | action | data                    |
            | Report Type         | radio group       | click  | Detail                  |
            | Period              | period datepicker | input  | 07-01-2020 ~ 07-31-2020 |
            | Office              | select            | select | All                     |
            | G/L No. Range Start | autocomplete      | input  | 10202                   |
        And the user click 'General Ledger Report' 'Print' button
        And the user click 'Download PDF' button
        And the user click 'Download Excel' button
        Then the 'General Ledger Report' detail values for 'All' office should be correct
            | field         | value        |
            | Total Balance | -842,213.62  |
            | Total Credit  | 1,500,851.98 |
        And the 'General Ledger Report' detail pdf file should be saved in download folder (120 sec)
        And the 'General Ledger Report' detail excel file should be saved in download folder (120 sec)
        When the user closes current tab
        And the user choose 'NGB' office for 'General Ledger Report'
        And the user click 'General Ledger Report' 'Print' button
        Then the 'General Ledger Report' detail values for 'NGB' office should be correct
            | field         | value |
            | Total Balance | 0.00  |
            | Total Credit  | 0.00  |

    @LOHAN
    Scenario: The general manager try to download 'General Ledger Report' trade partner summary report
        Given the download file folder is 'download'
        And the user is a 'General Manager'
        And the user is on 'General Ledger Report' page
        When the user enter 'General Ledger Report' info
            | field               | attribute         | action | data                    |
            | Report Type         | radio group       | click  | Trade Partner Summary   |
            | Period              | period datepicker | input  | 07-01-2020 ~ 07-31-2020 |
            | Office              | select            | select | All                     |
            | G/L No. Range Start | autocomplete      | input  | 10520                   |
            | G/L No. Range End   | autocomplete      | input  | 45607                   |
        And the user click 'General Ledger Report' 'Print' button
        And the user click 'Download PDF' button
        And the user click 'Download Excel' button
        Then the 'General Ledger Report' tp summary values for 'All' office should be correct
            | field         | value        |
            | Total Balance | 4,161,655.06 |
        And the 'General Ledger Report' tp summary pdf file should be saved in download folder (120 sec)
        And the 'General Ledger Report' tp summary excel file should be saved in download folder (120 sec)
        When the user closes current tab
        And the user choose 'NGB' office for 'General Ledger Report'
        And the user click 'General Ledger Report' 'Print' button
        Then the 'General Ledger Report' tp summary values for 'NGB' office should be correct
            | field         | value        |
            | Total Balance | 2,506,945.80 |

    @LOHAN
    Scenario: The general manager try to download 'General Ledger Report' G&A expense report
        Given the download file folder is 'download'
        And the user is a 'General Manager'
        And the user is on 'General Ledger Report' page
        When the user enter 'General Ledger Report' info
            | field       | attribute         | action | data                    |
            | Report Type | radio group       | click  | G&A Expense             |
            | Period      | period datepicker | input  | 07-01-2020 ~ 07-31-2020 |
            | Office      | select            | select | All                     |
        And the user click 'General Ledger Report' 'Print' button
        And the user click 'Download PDF' button
        Then the 'General Ledger Report' A&G expense values for 'All' office should be correct
            | field         | value |
            | Total Balance | 0.00  |
        And the 'General Ledger Report' A&G expense pdf file should be saved in download folder (120 sec)
        When the user closes current tab
        And the user choose 'NGB' office for 'General Ledger Report'
        And the user click 'General Ledger Report' 'Print' button
        Then the 'General Ledger Report' A&G expense values for 'NGB' office should be correct
            | field         | value |
            | Total Balance | 0.00  |

    @OLC
    Scenario: The general manager try to download 'General Ledger Report' summary report
        Given the download file folder is 'download'
        And the user is a 'Super Admin'
        And the user is on 'General Ledger Report' page
        When the user enter 'General Ledger Report' info
            | field       | attribute         | action | data                    |
            | Report Type | radio group       | click  | Summary                 |
            | Period      | period datepicker | input  | 2021-07-01 ~ 2021-07-01 |
            | Office      | select            | select | All                     |
        And the user click 'General Ledger Report' 'Print' button
        And the user click 'Download PDF' button
        And the user click 'Download Excel' button
        Then the 'General Ledger Report' summary values for 'All' office should be correct
            | field         | value         |
            | Total Balance | 19,333,129.82 |
        And the 'General Ledger Report' summary pdf file should be saved in download folder (120 sec)
        And the 'General Ledger Report' summary excel file should be saved in download folder (120 sec)
        When the user closes current tab
        And the user choose 'TPE' office for 'General Ledger Report'
        And the user click 'General Ledger Report' 'Print' button
        Then the 'General Ledger Report' summary values for 'TPE' office should be correct
            | field         | value |
            | Total Balance | 0.00  |

    @OLC
    Scenario: The general manager try to download 'General Ledger Report' detail report
        Given the download file folder is 'download'
        And the user is a 'Super Admin'
        And the user is on 'General Ledger Report' page
        When the user enter 'General Ledger Report' info
            | field               | attribute         | action | data                    |
            | Report Type         | radio group       | click  | Detail                  |
            | Period              | period datepicker | input  | 2021-06-01 ~ 2021-06-01 |
            | Office              | select            | select | All                     |
            | G/L No. Range Start | autocomplete      | input  | 100201                  |
        And the user click 'General Ledger Report' 'Print' button
        And the user click 'Download PDF' button
        And the user click 'Download Excel' button
        Then the 'General Ledger Report' detail values for 'All' office should be correct
            | field         | value      |
            | Total Balance | 192,035.03 |
            | Total Credit  | 7,763.00   |
        And the 'General Ledger Report' detail pdf file should be saved in download folder (120 sec)
        And the 'General Ledger Report' detail excel file should be saved in download folder (120 sec)
        When the user closes current tab
        And the user choose 'TPE' office for 'General Ledger Report'
        And the user click 'General Ledger Report' 'Print' button
        Then the 'General Ledger Report' detail values for 'TPE' office should be correct
            | field         | value |
            | Total Balance | 0.00  |
            | Total Credit  | 0.00  |

    @OLC
    Scenario: The general manager try to download 'General Ledger Report' trade partner summary report
        Given the download file folder is 'download'
        And the user is a 'Super Admin'
        And the user is on 'General Ledger Report' page
        When the user enter 'General Ledger Report' info
            | field               | attribute         | action | data                    |
            | Report Type         | radio group       | click  | Trade Partner Summary   |
            | Period              | period datepicker | input  | 2021-07-01 ~ 2021-07-01 |
            | Office              | select            | select | All                     |
            | G/L No. Range Start | autocomplete      | input  | 100203                  |
            | G/L No. Range End   | autocomplete      | input  | 100206                  |
        And the user click 'General Ledger Report' 'Print' button
        And the user click 'Download PDF' button
        And the user click 'Download Excel' button
        Then the 'General Ledger Report' tp summary values for 'All' office should be correct
            | field         | value        |
            | Total Balance | 5,798,864.61 |
        And the 'General Ledger Report' tp summary pdf file should be saved in download folder (120 sec)
        And the 'General Ledger Report' tp summary excel file should be saved in download folder (120 sec)
        When the user closes current tab
        And the user choose 'TPE' office for 'General Ledger Report'
        And the user click 'General Ledger Report' 'Print' button
        Then the 'General Ledger Report' tp summary values for 'TPE' office should be correct
            | field         | value |
            | Total Balance | 0.00  |

    @OLC
    Scenario: The general manager try to download 'General Ledger Report' G&A expense report
        Given the download file folder is 'download'
        And the user is a 'Super Admin'
        And the user is on 'General Ledger Report' page
        When the user enter 'General Ledger Report' info
            | field       | attribute         | action | data                    |
            | Report Type | radio group       | click  | G&A Expense             |
            | Period      | period datepicker | input  | 2021-07-01 ~ 2021-07-31 |
            | Office      | select            | select | All                     |
        And the user click 'General Ledger Report' 'Print' button
        And the user click 'Download PDF' button
        Then the 'General Ledger Report' A&G expense values for 'All' office should be correct
            | field         | value        |
            | Total Balance | 1,745,991.25 |
        And the 'General Ledger Report' A&G expense pdf file should be saved in download folder (120 sec)
        When the user closes current tab
        And the user choose 'TPE' office for 'General Ledger Report'
        And the user click 'General Ledger Report' 'Print' button
        Then the 'General Ledger Report' A&G expense values for 'TPE' office should be correct
            | field         | value |
            | Total Balance | 0.00  |
