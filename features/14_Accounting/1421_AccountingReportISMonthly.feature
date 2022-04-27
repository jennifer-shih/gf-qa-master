@OLC
Feature: [Accounting] Accounting Report - Income Statement - Month By Month


  Scenario: The 'Income Statement' report during 2020-09-01 and 2020-09-30 is correct
    Given the download file folder is 'download'
    And the user is a 'General Manager'
    And the user is on 'Income Statement' page
    When the user enter 'Income Statement' info
      | field  | attribute         | action | data                    |
      | Type   | radio group       | click  | Standard                |
      | Period | period datepicker | input  | 2020-09-01 ~ 2020-09-30 |
      | Office | select            | select | QD                      |
    And the user click 'Income Statement' 'Print' button
    And the user click 'Download Excel' button
    Then the 'Income Statement' excel file should be saved in download folder (120 sec)
    And the 'Income Statement' excel file should be as same as 'excel/IS Monthly/Income_statement (20200901-20200930).xlsx'

  Scenario: The 'Income Statement' report during 2020-10-01 and 2020-10-31 is correct
    Given the download file folder is 'download'
    And the user is a 'General Manager'
    And the user is on 'Income Statement' page
    When the user enter 'Income Statement' info
      | field  | attribute         | action | data                    |
      | Type   | radio group       | click  | Standard                |
      | Period | period datepicker | input  | 2020-10-01 ~ 2020-10-31 |
      | Office | select            | select | QD                      |
    And the user click 'Income Statement' 'Print' button
    And the user click 'Download Excel' button
    Then the 'Income Statement' excel file should be saved in download folder (120 sec)
    And the 'Income Statement' excel file should be as same as 'excel/IS Monthly/Income_statement (20201001-20201031).xlsx'

  Scenario: The 'Income Statement' report during 2020-11-01 and 2020-11-30 is correct
    Given the download file folder is 'download'
    And the user is a 'General Manager'
    And the user is on 'Income Statement' page
    When the user enter 'Income Statement' info
      | field  | attribute         | action | data                    |
      | Type   | radio group       | click  | Standard                |
      | Period | period datepicker | input  | 2020-11-01 ~ 2020-11-30 |
      | Office | select            | select | QD                      |
    And the user click 'Income Statement' 'Print' button
    And the user click 'Download Excel' button
    Then the 'Income Statement' excel file should be saved in download folder (120 sec)
    And the 'Income Statement' excel file should be as same as 'excel/IS Monthly/Income_statement (20201101-20201130).xlsx'

  Scenario: The 'Income Statement' report during 2020-12-01 and 2020-12-31 is correct
    Given the download file folder is 'download'
    And the user is a 'General Manager'
    And the user is on 'Income Statement' page
    When the user enter 'Income Statement' info
      | field  | attribute         | action | data                    |
      | Type   | radio group       | click  | Standard                |
      | Period | period datepicker | input  | 2020-12-01 ~ 2020-12-31 |
      | Office | select            | select | QD                      |
    And the user click 'Income Statement' 'Print' button
    And the user click 'Download Excel' button
    Then the 'Income Statement' excel file should be saved in download folder (120 sec)
    And the 'Income Statement' excel file should be as same as 'excel/IS Monthly/Income_statement (20201201-20201231).xlsx'

  Scenario: The 'Income Statement' report during 2021-01-01 and 2021-01-31 is correct
    Given the download file folder is 'download'
    And the user is a 'General Manager'
    And the user is on 'Income Statement' page
    When the user enter 'Income Statement' info
      | field  | attribute         | action | data                    |
      | Type   | radio group       | click  | Standard                |
      | Period | period datepicker | input  | 2021-01-01 ~ 2021-01-31 |
      | Office | select            | select | QD                      |
    And the user click 'Income Statement' 'Print' button
    And the user click 'Download Excel' button
    Then the 'Income Statement' excel file should be saved in download folder (120 sec)
    And the 'Income Statement' excel file should be as same as 'excel/IS Monthly/Income_statement (20210101-20210131).xlsx'

  Scenario: The 'Income Statement' report during 2021-02-01 and 2021-02-28 is correct
    Given the download file folder is 'download'
    And the user is a 'General Manager'
    And the user is on 'Income Statement' page
    When the user enter 'Income Statement' info
      | field  | attribute         | action | data                    |
      | Type   | radio group       | click  | Standard                |
      | Period | period datepicker | input  | 2021-02-01 ~ 2021-02-28 |
      | Office | select            | select | QD                      |
    And the user click 'Income Statement' 'Print' button
    And the user click 'Download Excel' button
    Then the 'Income Statement' excel file should be saved in download folder (120 sec)
    And the 'Income Statement' excel file should be as same as 'excel/IS Monthly/Income_statement (20210201-20210228).xlsx'

  Scenario: The 'Income Statement' report during 2021-03-01 and 2021-03-31 is correct
    Given the download file folder is 'download'
    And the user is a 'General Manager'
    And the user is on 'Income Statement' page
    When the user enter 'Income Statement' info
      | field  | attribute         | action | data                    |
      | Type   | radio group       | click  | Standard                |
      | Period | period datepicker | input  | 2021-03-01 ~ 2021-03-31 |
      | Office | select            | select | QD                      |
    And the user click 'Income Statement' 'Print' button
    And the user click 'Download Excel' button
    Then the 'Income Statement' excel file should be saved in download folder (120 sec)
    And the 'Income Statement' excel file should be as same as 'excel/IS Monthly/Income_statement (20210301-20210331).xlsx'

  Scenario: The 'Income Statement' report during 2021-04-01 and 2021-04-30 is correct
    Given the download file folder is 'download'
    And the user is a 'General Manager'
    And the user is on 'Income Statement' page
    When the user enter 'Income Statement' info
      | field  | attribute         | action | data                    |
      | Type   | radio group       | click  | Standard                |
      | Period | period datepicker | input  | 2021-04-01 ~ 2021-04-30 |
      | Office | select            | select | QD                      |
    And the user click 'Income Statement' 'Print' button
    And the user click 'Download Excel' button
    Then the 'Income Statement' excel file should be saved in download folder (120 sec)
    And the 'Income Statement' excel file should be as same as 'excel/IS Monthly/Income_statement (20210401-20210430).xlsx'

  Scenario: The 'Income Statement' report during 2021-05-01 and 2021-05-31 is correct
    Given the download file folder is 'download'
    And the user is a 'General Manager'
    And the user is on 'Income Statement' page
    When the user enter 'Income Statement' info
      | field  | attribute         | action | data                    |
      | Type   | radio group       | click  | Standard                |
      | Period | period datepicker | input  | 2021-05-01 ~ 2021-05-31 |
      | Office | select            | select | QD                      |
    And the user click 'Income Statement' 'Print' button
    And the user click 'Download Excel' button
    Then the 'Income Statement' excel file should be saved in download folder (120 sec)
    And the 'Income Statement' excel file should be as same as 'excel/IS Monthly/Income_statement (20210501-20210531).xlsx'

  Scenario: The 'Income Statement' report during 2021-06-01 and 2021-06-30 is correct
    Given the download file folder is 'download'
    And the user is a 'General Manager'
    And the user is on 'Income Statement' page
    When the user enter 'Income Statement' info
      | field  | attribute         | action | data                    |
      | Type   | radio group       | click  | Standard                |
      | Period | period datepicker | input  | 2021-06-01 ~ 2021-06-30 |
      | Office | select            | select | QD                      |
    And the user click 'Income Statement' 'Print' button
    And the user click 'Download Excel' button
    Then the 'Income Statement' excel file should be saved in download folder (120 sec)
    And the 'Income Statement' excel file should be as same as 'excel/IS Monthly/Income_statement (20210601-20210630).xlsx'

  Scenario: The 'Income Statement' report during 2021-07-01 and 2021-07-31 is correct
    Given the download file folder is 'download'
    And the user is a 'General Manager'
    And the user is on 'Income Statement' page
    When the user enter 'Income Statement' info
      | field  | attribute         | action | data                    |
      | Type   | radio group       | click  | Standard                |
      | Period | period datepicker | input  | 2021-07-01 ~ 2021-07-31 |
      | Office | select            | select | QD                      |
    And the user click 'Income Statement' 'Print' button
    And the user click 'Download Excel' button
    Then the 'Income Statement' excel file should be saved in download folder (120 sec)
    And the 'Income Statement' excel file should be as same as 'excel/IS Monthly/Income_statement (20210701-20210731).xlsx'

  Scenario: The 'Income Statement' report during 2021-08-01 and 2021-08-31 is correct
    Given the download file folder is 'download'
    And the user is a 'General Manager'
    And the user is on 'Income Statement' page
    When the user enter 'Income Statement' info
      | field  | attribute         | action | data                    |
      | Type   | radio group       | click  | Standard                |
      | Period | period datepicker | input  | 2021-08-01 ~ 2021-08-31 |
      | Office | select            | select | QD                      |
    And the user click 'Income Statement' 'Print' button
    And the user click 'Download Excel' button
    Then the 'Income Statement' excel file should be saved in download folder (120 sec)
    And the 'Income Statement' excel file should be as same as 'excel/IS Monthly/Income_statement (20210801-20210831).xlsx'

  Scenario: The 'Income Statement' report during 2021-09-01 and 2021-09-30 is correct
    Given the download file folder is 'download'
    And the user is a 'General Manager'
    And the user is on 'Income Statement' page
    When the user enter 'Income Statement' info
      | field  | attribute         | action | data                    |
      | Type   | radio group       | click  | Standard                |
      | Period | period datepicker | input  | 2021-09-01 ~ 2021-09-30 |
      | Office | select            | select | QD                      |
    And the user click 'Income Statement' 'Print' button
    And the user click 'Download Excel' button
    Then the 'Income Statement' excel file should be saved in download folder (120 sec)
    And the 'Income Statement' excel file should be as same as 'excel/IS Monthly/Income_statement (20210901-20210930).xlsx'
