@OLC
Feature: [Accounting] Accounting Report - Balance Sheet - Month By Month

  Scenario: The 'Balance Sheet' report as of 2020-09-30 is correct
    Given the download file folder is 'download'
    And the user is a 'General Manager'
    And the user is on 'Balance Sheet' page
    When the user enter 'Balance Sheet' info
      | field  | attribute  | action | data       |
      | As of  | datepicker | input  | 2020-09-30 |
      | Office | select     | select | QD         |
    And the user click 'Balance Sheet' 'Print' button
    And the user click 'Download Excel' button
    Then the 'Balance Sheet' excel file should be saved in download folder (120 sec)
    And the 'Balance Sheet' excel file should be as same as 'excel/BS Monthly/Balance_sheet_2020-09-30.xlsx'

  Scenario: The 'Balance Sheet' report as of 2020-10-31 is correct
    Given the download file folder is 'download'
    And the user is a 'General Manager'
    And the user is on 'Balance Sheet' page
    When the user enter 'Balance Sheet' info
      | field  | attribute  | action | data       |
      | As of  | datepicker | input  | 2020-10-31 |
      | Office | select     | select | QD         |
    And the user click 'Balance Sheet' 'Print' button
    And the user click 'Download Excel' button
    Then the 'Balance Sheet' excel file should be saved in download folder (120 sec)
    And the 'Balance Sheet' excel file should be as same as 'excel/BS Monthly/Balance_sheet_2020-10-31.xlsx'

  Scenario: The 'Balance Sheet' report as of 2020-11-30 is correct
    Given the download file folder is 'download'
    And the user is a 'General Manager'
    And the user is on 'Balance Sheet' page
    When the user enter 'Balance Sheet' info
      | field  | attribute  | action | data       |
      | As of  | datepicker | input  | 2020-11-30 |
      | Office | select     | select | QD         |
    And the user click 'Balance Sheet' 'Print' button
    And the user click 'Download Excel' button
    Then the 'Balance Sheet' excel file should be saved in download folder (120 sec)
    And the 'Balance Sheet' excel file should be as same as 'excel/BS Monthly/Balance_sheet_2020-11-30.xlsx'

  Scenario: The 'Balance Sheet' report as of 2020-12-31 is correct
    Given the download file folder is 'download'
    And the user is a 'General Manager'
    And the user is on 'Balance Sheet' page
    When the user enter 'Balance Sheet' info
      | field  | attribute  | action | data       |
      | As of  | datepicker | input  | 2020-12-31 |
      | Office | select     | select | QD         |
    And the user click 'Balance Sheet' 'Print' button
    And the user click 'Download Excel' button
    Then the 'Balance Sheet' excel file should be saved in download folder (120 sec)
    And the 'Balance Sheet' excel file should be as same as 'excel/BS Monthly/Balance_sheet_2020-12-31.xlsx'

  Scenario: The 'Balance Sheet' report as of 2021-01-31 is correct
    Given the download file folder is 'download'
    And the user is a 'General Manager'
    And the user is on 'Balance Sheet' page
    When the user enter 'Balance Sheet' info
      | field  | attribute  | action | data       |
      | As of  | datepicker | input  | 2021-01-31 |
      | Office | select     | select | QD         |
    And the user click 'Balance Sheet' 'Print' button
    And the user click 'Download Excel' button
    Then the 'Balance Sheet' excel file should be saved in download folder (120 sec)
    And the 'Balance Sheet' excel file should be as same as 'excel/BS Monthly/Balance_sheet_2021-01-31.xlsx'

  Scenario: The 'Balance Sheet' report as of 2021-02-28 is correct
    Given the download file folder is 'download'
    And the user is a 'General Manager'
    And the user is on 'Balance Sheet' page
    When the user enter 'Balance Sheet' info
      | field  | attribute  | action | data       |
      | As of  | datepicker | input  | 2021-02-28 |
      | Office | select     | select | QD         |
    And the user click 'Balance Sheet' 'Print' button
    And the user click 'Download Excel' button
    Then the 'Balance Sheet' excel file should be saved in download folder (120 sec)
    And the 'Balance Sheet' excel file should be as same as 'excel/BS Monthly/Balance_sheet_2021-02-28.xlsx'

  Scenario: The 'Balance Sheet' report as of 2021-03-31 is correct
    Given the download file folder is 'download'
    And the user is a 'General Manager'
    And the user is on 'Balance Sheet' page
    When the user enter 'Balance Sheet' info
      | field  | attribute  | action | data       |
      | As of  | datepicker | input  | 2021-03-31 |
      | Office | select     | select | QD         |
    And the user click 'Balance Sheet' 'Print' button
    And the user click 'Download Excel' button
    Then the 'Balance Sheet' excel file should be saved in download folder (120 sec)
    And the 'Balance Sheet' excel file should be as same as 'excel/BS Monthly/Balance_sheet_2021-03-31.xlsx'

  Scenario: The 'Balance Sheet' report as of 2021-04-30 is correct
    Given the download file folder is 'download'
    And the user is a 'General Manager'
    And the user is on 'Balance Sheet' page
    When the user enter 'Balance Sheet' info
      | field  | attribute  | action | data       |
      | As of  | datepicker | input  | 2021-04-30 |
      | Office | select     | select | QD         |
    And the user click 'Balance Sheet' 'Print' button
    And the user click 'Download Excel' button
    Then the 'Balance Sheet' excel file should be saved in download folder (120 sec)
    And the 'Balance Sheet' excel file should be as same as 'excel/BS Monthly/Balance_sheet_2021-04-30.xlsx'

  Scenario: The 'Balance Sheet' report as of 2021-05-31 is correct
    Given the download file folder is 'download'
    And the user is a 'General Manager'
    And the user is on 'Balance Sheet' page
    When the user enter 'Balance Sheet' info
      | field  | attribute  | action | data       |
      | As of  | datepicker | input  | 2021-05-31 |
      | Office | select     | select | QD         |
    And the user click 'Balance Sheet' 'Print' button
    And the user click 'Download Excel' button
    Then the 'Balance Sheet' excel file should be saved in download folder (120 sec)
    And the 'Balance Sheet' excel file should be as same as 'excel/BS Monthly/Balance_sheet_2021-05-31.xlsx'

  Scenario: The 'Balance Sheet' report as of 2021-06-30 is correct
    Given the download file folder is 'download'
    And the user is a 'General Manager'
    And the user is on 'Balance Sheet' page
    When the user enter 'Balance Sheet' info
      | field  | attribute  | action | data       |
      | As of  | datepicker | input  | 2021-06-30 |
      | Office | select     | select | QD         |
    And the user click 'Balance Sheet' 'Print' button
    And the user click 'Download Excel' button
    Then the 'Balance Sheet' excel file should be saved in download folder (120 sec)
    And the 'Balance Sheet' excel file should be as same as 'excel/BS Monthly/Balance_sheet_2021-06-30.xlsx'

  Scenario: The 'Balance Sheet' report as of 2021-07-31 is correct
    Given the download file folder is 'download'
    And the user is a 'General Manager'
    And the user is on 'Balance Sheet' page
    When the user enter 'Balance Sheet' info
      | field  | attribute  | action | data       |
      | As of  | datepicker | input  | 2021-07-31 |
      | Office | select     | select | QD         |
    And the user click 'Balance Sheet' 'Print' button
    And the user click 'Download Excel' button
    Then the 'Balance Sheet' excel file should be saved in download folder (120 sec)
    And the 'Balance Sheet' excel file should be as same as 'excel/BS Monthly/Balance_sheet_2021-07-31.xlsx'

  Scenario: The 'Balance Sheet' report as of 2021-08-31 is correct
    Given the download file folder is 'download'
    And the user is a 'General Manager'
    And the user is on 'Balance Sheet' page
    When the user enter 'Balance Sheet' info
      | field  | attribute  | action | data       |
      | As of  | datepicker | input  | 2021-08-31 |
      | Office | select     | select | QD         |
    And the user click 'Balance Sheet' 'Print' button
    And the user click 'Download Excel' button
    Then the 'Balance Sheet' excel file should be saved in download folder (120 sec)
    And the 'Balance Sheet' excel file should be as same as 'excel/BS Monthly/Balance_sheet_2021-08-31.xlsx'

  Scenario: The 'Balance Sheet' report as of 2021-09-30 is correct
    Given the download file folder is 'download'
    And the user is a 'General Manager'
    And the user is on 'Balance Sheet' page
    When the user enter 'Balance Sheet' info
      | field  | attribute  | action | data       |
      | As of  | datepicker | input  | 2021-09-30 |
      | Office | select     | select | QD         |
    And the user click 'Balance Sheet' 'Print' button
    And the user click 'Download Excel' button
    Then the 'Balance Sheet' excel file should be saved in download folder (120 sec)
    And the 'Balance Sheet' excel file should be as same as 'excel/BS Monthly/Balance_sheet_2021-09-30.xlsx'
