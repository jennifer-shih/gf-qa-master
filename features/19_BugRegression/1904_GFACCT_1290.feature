@BugRegression
Feature: [GFACCT-1290] Show 500 error page when the period set without start date

     Genral Ledger Detail Report without start date or end date should show normally
     https://hardcoretech.atlassian.net/browse/GFACCT-1290


     Scenario: General Ledger Report in 'Detail' mode without 'start date' or 'end date' should be OK
          # When the user resets DB to AECL's latest one
          Given the user is a 'Super Admin'
          And the user is on 'Profile' page
          When the user set language to 'English'
          Given the user is on 'General Ledger Report' page

          When the user enter 'General Ledger Report' info
               | field       | attribute         | action | data                 |
               | Report Type | radio group       | click  | Detail               |
               | Period      | period datepicker | input  | {today-30} ~ {blank} |
               | Office      | select            | select | All                  |
          And the user click 'General Ledger Report' 'Print' button
          Then the 'General Ledger Report' (Detail) should show without any errors
          And the 'Period' on 'General Ledger Report' (Detail) should be '{today-30}' ~ '[Last Record]'
          And the 'General Ledger Report' (Detail) should show with freights
          When the user closes current tab

          #? KNOWN ISSUE Ticket# GFACCT-1898
          # When the user enter 'General Ledger Report' info
          #      | field       | attribute         | action | data              |
          #      | Report Type | radio group       | click  | Detail            |
          #      | Period      | period datepicker | input  | {blank} ~ {today} |
          #      | Office      | select            | select | All               |
          # And the user click 'General Ledger Report' 'Print' button
          # Then the 'General Ledger Report' (Detail) should show without any errors
          # And the 'Period' on 'General Ledger Report' (Summary) should be '[First Record]' ~ '{today}'
          # And the 'General Ledger Report' (Detail) should show with freights
          # When the user closes current tab

          #? KNOWN ISSUE Ticket# GFACCT-1898
          # When the user enter 'General Ledger Report' info
          #      | field       | attribute         | action | data              |
          #      | Report Type | radio group       | click  | Detail            |
          #      | Period      | period datepicker | input  | {blank} ~ {blank} |
          #      | Office      | select            | select | All               |
          # And the user click 'General Ledger Report' 'Print' button
          # Then the 'General Ledger Report' (Detail) should show without any errors
          # And the 'Period' on 'General Ledger Report' (Detail) should be '[First Record]' ~ '[Last Record]'
          # And the 'General Ledger Report' (Detail) should show with freights
