@BugRegression
Feature: [GQT-301] Run Trial balance report w/o input start date, the amount show incorrect

     The amount in trial balance report should be correct even without start date
     https://hardcoretech.atlassian.net/browse/GQT-301


     Scenario: The amount in trial balance report should be correct even without start date
          When the user resets DB to aws-deg-gofreight / fms / backup.sql.gz-20211227
          Given the user is a 'Super Admin'
          And the user is on 'Trial Balance' page
          When the user enter 'Trial Balance' info
               | field  | attribute         | action | data                    |
               | Period | period datepicker | input  | {blank} ~ 07-31-2021    |
               | Office | select            | select | All                     |
               | Format | radio group       | click  | Display Currency Detail |
          And the user click 'Trial Balance' 'Print' button
          Then the 'Trial Balance' values for 'All' office should be correct
               | field                      | value     |
               | GL No. 10100 Balance Debit | 52,487.39 |

          When the user clicks 'GL No. 10100' link in 'Trial Balance'
          Then the 'General Ledger Report' detail values for 'All' office should be correct
               | field         | value     |
               | Total Balance | 52,487.39 |
