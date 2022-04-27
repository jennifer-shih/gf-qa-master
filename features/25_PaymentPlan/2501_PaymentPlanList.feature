@OLC
Feature: [Payment Plan] Payment Plan List for GQT_142

  Background: Permission setting, Company setting, Feature and Approval setting
    Given the user is a 'Super Admin'
    And the user is on 'Permission Management' page
    And settings in 'Permission Management' page are as listed below
      | User        | Payment Plan List Export Excel | Navigator Accounting Payment Plan | Navigator Accounting Payment Plan Excel | Navigator Accounting Payment Plan List | Payment Plan Entry Delete | Payment Plan Entry Edit | Payment Plan Entry View All | Payment Plan Excel Upload File | Payment Plan Excel View | Payment Plan List View All | Invoice Make/Receive Payment Button Visible | Payment Plan Entry View Self |
      | acc_lcl lee | Allow                          | Allow                             | Allow                                   | Allow                                  | Allow                     | Allow                   | Allow                       | Allow                          | Allow                   | Allow                      | Allow                                       | Allow                        |
    And the user is on 'Company Management' page
    And settings in 'Company Management' page are as listed below
      | field                     | attribute   | action | data          |
      | Enable Payment Plan       | checkbox    | tick   | {on}          |
      | Payment Plan Display Mode | radio group | click  | Freight Based |
    And the user is on 'Feature and Approval' page
    And there are departments configured for 'Payment Plan' Approver in 'QD' office


  Scenario: The user can browse to payment plan list by navigator
    Given the user is a 'Accounting' in 'QD' office
    When the user browse to 'Payment Plan List' page by navigator
    Then 'Payment Plan List' page will show


  Scenario: The user switches off all config then only the checkbox will show
    Given the user is a 'Accounting' in 'QD' office
    And the user is on 'Payment Plan List' page
    When the user switches 'Column Config' in 'Payment Plan List'
      | column config           | switch |
      | Approval Status         | {off}  |
      | Payment Plan No.        | {off}  |
      | Plan Type               | {off}  |
      | Party                   | {off}  |
      | Post Date               | {off}  |
      | File No.                | {off}  |
      | MB/L No.                | {off}  |
      | HB/L No.                | {off}  |
      | ETA                     | {off}  |
      | ETD                     | {off}  |
      | Amount                  | {off}  |
      | Amount (Receivable)     | {off}  |
      | Amount (Payable)        | {off}  |
      | Paid Amount             | {off}  |
      | Paid Amount (Collected) | {off}  |
      | Paid Amount (Paid Out)  | {off}  |
      | Balance                 | {off}  |
      | Last Paid Date          | {off}  |
      | Invoice No.             | {off}  |
      | Booking No.             | {off}  |
      | Flight No.              | {off}  |
      | Reconciliation No.      | {off}  |
      | Customer Reference No.  | {off}  |
      | Office                  | {off}  |
      | Issued by               | {off}  |
      | Vessel                  | {off}  |
      | Voyage                  | {off}  |
      | Operation               | {off}  |
      | Sales                   | {off}  |
      | Issued                  | {off}  |
      | E-Invoice No.           | {off}  |
      | Status                  | {off}  |
    Then the table column should be the same as above setting in 'Payment Plan List'
    And there is Check All checkbox in 'Payment Plan List'


  Scenario: The user switches on all config then columns should show
    Given the user is a 'Accounting' in 'QD' office
    And the user is on 'Payment Plan List' page
    When the user switches 'Column Config' in 'Payment Plan List'
      | column config           | switch |
      | Approval Status         | {on}   |
      | Payment Plan No.        | {on}   |
      | Plan Type               | {on}   |
      | Party                   | {on}   |
      | Post Date               | {on}   |
      | File No.                | {on}   |
      | MB/L No.                | {on}   |
      | HB/L No.                | {on}   |
      | ETA                     | {on}   |
      | ETD                     | {on}   |
      | Amount                  | {on}   |
      | Amount (Receivable)     | {on}   |
      | Amount (Payable)        | {on}   |
      | Paid Amount             | {on}   |
      | Paid Amount (Collected) | {on}   |
      | Paid Amount (Paid Out)  | {on}   |
      | Balance                 | {on}   |
      | Last Paid Date          | {on}   |
      | Invoice No.             | {on}   |
      | Booking No.             | {on}   |
      | Flight No.              | {on}   |
      | Reconciliation No.      | {on}   |
      | Customer Reference No.  | {on}   |
      | Office                  | {on}   |
      | Issued by               | {on}   |
      | Vessel                  | {on}   |
      | Voyage                  | {on}   |
      | Operation               | {on}   |
      | Sales                   | {on}   |
      | Issued                  | {on}   |
      | E-Invoice No.           | {on}   |
      | Status                  | {on}   |
    Then the table column should be the same as above setting in 'Payment Plan List'
    And there is Check All checkbox in 'Payment Plan List'


  Scenario Outline: Check table sorting by ASC/DESC
    Given the user is a 'Accounting' in 'QD' office
    And the user is on 'Payment Plan List' page
    When the user set record quantity for 1 page to 10 in 'Payment Plan List'
    And the user switches 'Column Config' in 'Payment Plan List'
      | column config    | switch |
      | Payment Plan No. | {on}   |
      | Plan Type        | {on}   |
      | Party            | {on}   |
      | Post Date        | {on}   |
      | Office           | {on}   |
      | Issued by        | {on}   |
      | Issued           | {on}   |
    And the user order column '<column name>' by ASC order in 'Payment Plan List'
    Then column '<column name>' should be sorted by ASC in 'Payment Plan List'
    When the user order column '<column name>' by DESC order in 'Payment Plan List'
    Then column '<column name>' should be sorted by DESC in 'Payment Plan List'
    Examples: <column name>
      | column name      |
      | Payment Plan No. |
      | Plan Type        |
      | Party            |
      | Post Date        |
      | Office           |
      | Issued by        |
      | Issued           |


  Scenario Outline: Check first column has been change when sorting grid (for covering 'Check grid ordering by ASC/DESC')
    Given the user is a 'Accounting' in 'QD' office
    And the user is on 'Payment Plan List' page
    When the user switches 'Column Config' in 'Payment Plan List'
      | column config    | switch |
      | Payment Plan No. | {on}   |
      | Plan Type        | {on}   |
      | Party            | {on}   |
      | Post Date        | {on}   |
      | Office           | {on}   |
      | Issued by        | {on}   |
      | Issued           | {on}   |
    When the user order column '<column name>' by ASC order in 'Payment Plan List'
    And column 1 of '<column name>' is 'A'
    And the user order column '<column name>' by DESC order in 'Payment Plan List'
    And column 1 of '<column name>' is 'B'
    Then 'A' should NOT be 'B'
    Examples: <column name>
      | column name      |
      | Payment Plan No. |
      | Plan Type        |
      | Party            |
      | Post Date        |
      | Office           |
      | Issued by        |
      | Issued           |


  Scenario: Column Config reordering is no problem
    Given the user is a 'Accounting' in 'QD' office
    And the user is on 'Payment Plan List' page
    When the user switches 'Column Config' in 'Payment Plan List'
      | column config    | switch |
      | Payment Plan No. | {on}   |
      | Party            | {on}   |
      | Post Date        | {on}   |
    And the user put 'Party' under 'Freeze Column Divider' in table column config in 'Payment Plan List'
    And the user put 'Post Date' on 'Freeze Column Divider' in table column config in 'Payment Plan List'
    And the user put 'Payment Plan No.' on 'Post Date' in table column config in 'Payment Plan List'
    Then the position of columns should match config in 'Payment Plan List'
    And 'Party' is under 'Freeze Column Divider' in table column config in 'Payment Plan List'
    And 'Post Date' is on 'Freeze Column Divider' in table column config in 'Payment Plan List'
    And 'Payment Plan No.' is on 'Post Date' in table column config in 'Payment Plan List'


  Scenario: Search filter can be pinned and other list view pages will be pinned
    Given the user is a 'Accounting' in 'QD' office
    And the user is on 'Payment Plan List' page
    When the user open and pin the filter in 'Payment Plan List' page
    And the user refresh browser
    Then the filter bar should show in 'Payment Plan List' page
    Given the user is on 'Trade Partner List' page
    Then the filter bar should show in 'Trade Partner List' page


  Scenario: Search filter can be Unpinned and other list view pages will be Unpinned
    Given the user is a 'Accounting' in 'QD' office
    And the user is on 'Payment Plan List' page
    When the user open and unpin the filter in 'Payment Plan List' page
    And the user refresh browser
    Then the filter bar should NOT show in 'Payment Plan List' page
    Given the user is on 'Trade Partner List' page
    Then the filter bar should NOT show in 'Trade Partner List' page


  Scenario: Unchek all excel column config and download excel, only show 'No' column in file
    Given the user is a 'Accounting' in 'QD' office
    And the user is on 'Payment Plan List' page
    When the user set record quantity for 1 page to 10 in 'Payment Plan List'
    And the user search for the following info in 'Payment Plan List' page
      | field     | attribute         | action | data                 |
      | Post Date | period datepicker | input  | {today-30} ~ {today} |
    And the user switches 'Excel Column Config' and download excel in 'Payment Plan List'
      | column config           | switch |
      | Approval Status         | {off}  |
      | Payment Plan No.        | {off}  |
      | Plan Type               | {off}  |
      | Party                   | {off}  |
      | Post Date               | {off}  |
      | File No.                | {off}  |
      | MB/L No.                | {off}  |
      | HB/L No.                | {off}  |
      | ETA                     | {off}  |
      | ETD                     | {off}  |
      | Amount                  | {off}  |
      | Amount (Receivable)     | {off}  |
      | Amount (Payable)        | {off}  |
      | Paid Amount             | {off}  |
      | Paid Amount (Collected) | {off}  |
      | Paid Amount (Paid Out)  | {off}  |
      | Balance                 | {off}  |
      | Last Paid Date          | {off}  |
      | Invoice No.             | {off}  |
      | Booking No.             | {off}  |
      | Flight No.              | {off}  |
      | Reconciliation No.      | {off}  |
      | Customer Reference No.  | {off}  |
      | Office                  | {off}  |
      | Issued by               | {off}  |
      | Vessel                  | {off}  |
      | Voyage                  | {off}  |
      | Operation               | {off}  |
      | Sales                   | {off}  |
      | Issued                  | {off}  |
      | E-Invoice No.           | {off}  |
      | Status                  | {off}  |
    Then the 'Payment Plan List' excel file should be saved in download folder (120 sec)
    And the columns in 'Payment Plan List Excel' should be the same as above 'Excel Column Config'
    And the columns in 'Payment Plan List' excel should only show 'No'
    And the 'Excel Column Config' match above settings in 'Payment Plan List'


  Scenario: Randomly enable "Excel Column Config" can save correctly
    Given the user is a 'Accounting' in 'QD' office
    And the user is on 'Payment Plan List' page
    When the user randomly enables 6 'Excel Column Config' in 'Payment Plan List'
    Then the 'Excel Column Config' match above settings in 'Payment Plan List'


  Scenario: "Copy List View Setting" can copy "Column Config" and the downloaded excel is matched
    Given the user is a 'Accounting' in 'QD' office
    And the user is on 'Payment Plan List' page
    When the user set record quantity for 1 page to 10 in 'Payment Plan List'
    And the user search for the following info in 'Payment Plan List' page
      | field     | attribute         | action | data                 |
      | Post Date | period datepicker | input  | {today-30} ~ {today} |
    And the user switches 'Column Config' in 'Payment Plan List'
      | column config           | switch |
      | Approval Status         | {on}   |
      | Payment Plan No.        | {on}   |
      | Plan Type               | {on}   |
      | Party                   | {on}   |
      | Post Date               | {on}   |
      | File No.                | {on}   |
      | MB/L No.                | {on}   |
      | HB/L No.                | {on}   |
      | ETA                     | {on}   |
      | ETD                     | {on}   |
      | Amount                  | {on}   |
      | Amount (Receivable)     | {on}   |
      | Amount (Payable)        | {on}   |
      | Paid Amount             | {on}   |
      | Paid Amount (Collected) | {on}   |
      | Paid Amount (Paid Out)  | {on}   |
      | Balance                 | {on}   |
      | Last Paid Date          | {on}   |
      | Invoice No.             | {on}   |
      | Booking No.             | {on}   |
      | Flight No.              | {on}   |
      | Reconciliation No.      | {on}   |
      | Customer Reference No.  | {on}   |
      | Office                  | {on}   |
      | Issued by               | {on}   |
      | Vessel                  | {on}   |
      | Voyage                  | {on}   |
      | Operation               | {on}   |
      | Sales                   | {on}   |
      | Issued                  | {on}   |
      | E-Invoice No.           | {on}   |
      | Status                  | {on}   |
    And the user switches 'Excel Column Config' and save in 'Payment Plan List'
      | column config           | switch |
      | Approval Status         | {off}  |
      | Payment Plan No.        | {off}  |
      | Plan Type               | {off}  |
      | Party                   | {off}  |
      | Post Date               | {off}  |
      | File No.                | {off}  |
      | MB/L No.                | {off}  |
      | HB/L No.                | {off}  |
      | ETA                     | {off}  |
      | ETD                     | {off}  |
      | Amount                  | {off}  |
      | Amount (Receivable)     | {off}  |
      | Amount (Payable)        | {off}  |
      | Paid Amount             | {off}  |
      | Paid Amount (Collected) | {off}  |
      | Paid Amount (Paid Out)  | {off}  |
      | Balance                 | {off}  |
      | Last Paid Date          | {off}  |
      | Invoice No.             | {off}  |
      | Booking No.             | {off}  |
      | Flight No.              | {off}  |
      | Reconciliation No.      | {off}  |
      | Customer Reference No.  | {off}  |
      | Office                  | {off}  |
      | Issued by               | {off}  |
      | Vessel                  | {off}  |
      | Voyage                  | {off}  |
      | Operation               | {off}  |
      | Sales                   | {off}  |
      | Issued                  | {off}  |
      | E-Invoice No.           | {off}  |
      | Status                  | {off}  |
    And the user copy 'Column Config' to 'Excel Column Config' in 'Payment Plan List' and download excel
    Then the 'Payment Plan List' excel file should be saved in download folder (120 sec)
    And the columns in 'Payment Plan List Excel' should be the same as above 'Excel Column Config'
    And the 'Excel Column Config' match above settings in 'Payment Plan List'
    Then the values in 'Payment Plan List' excel should be the same as those in webpage


  Scenario: Pagination is no problem
    Given the user is a 'Accounting' in 'QD' office
    And the user is on 'Payment Plan List' page
    When the user switches 'Column Config' in 'Payment Plan List'
      | column config           | switch |
      | Approval Status         | {on}   |
      | Payment Plan No.        | {on}   |
      | Plan Type               | {on}   |
      | Party                   | {on}   |
      | Post Date               | {on}   |
      | File No.                | {on}   |
      | MB/L No.                | {on}   |
      | HB/L No.                | {on}   |
      | ETA                     | {on}   |
      | ETD                     | {on}   |
      | Amount                  | {on}   |
      | Amount (Receivable)     | {on}   |
      | Amount (Payable)        | {on}   |
      | Paid Amount             | {on}   |
      | Paid Amount (Collected) | {on}   |
      | Paid Amount (Paid Out)  | {on}   |
      | Balance                 | {on}   |
      | Last Paid Date          | {on}   |
      | Invoice No.             | {on}   |
      | Booking No.             | {on}   |
      | Flight No.              | {on}   |
      | Reconciliation No.      | {on}   |
      | Customer Reference No.  | {on}   |
      | Office                  | {on}   |
      | Issued by               | {on}   |
      | Vessel                  | {on}   |
      | Voyage                  | {on}   |
      | Operation               | {on}   |
      | Sales                   | {on}   |
      | Issued                  | {on}   |
      | E-Invoice No.           | {on}   |
      | Status                  | {on}   |
    When the user set record quantity for 1 page to 10 in 'Payment Plan List'
    Then 10 record shows in table and page description is correctly in 'Payment Plan List' (5 sec)
    When the user set record quantity for 1 page to 15 in 'Payment Plan List'
    Then 15 record shows in table and page description is correctly in 'Payment Plan List' (5 sec)
    When the user set record quantity for 1 page to 25 in 'Payment Plan List'
    Then 25 record shows in table and page description is correctly in 'Payment Plan List' (10 sec)
    When the user set record quantity for 1 page to 50 in 'Payment Plan List'
    Then 50 record shows in table and page description is correctly in 'Payment Plan List' (20 sec)
    When the user set record quantity for 1 page to 100 in 'Payment Plan List'
    Then 100 record shows in table and page description is correctly in 'Payment Plan List' (30 sec)
    When the user set record quantity for 1 page to 200 in 'Payment Plan List'
    Then 200 record shows in table and page description is correctly in 'Payment Plan List' (60 sec)


  Scenario: Deny permission 'Payment Plan Entry View'
    Given the user is a 'Super Admin'
    And the user is on 'Permission Management' page
    And settings in 'Permission Management' page are as listed below
      | User        | Payment Plan Entry View All | Payment Plan Entry View Self |
      | acc_lcl lee | Deny                        | Deny                         |
    Given the user is a 'Accounting' in 'QD' office
    And the user is on 'Payment Plan List' page
    When the user switches 'Column Config' in 'Payment Plan List'
      | column config    | switch |
      | Approval Status  | {on}   |
      | Payment Plan No. | {on}   |
    And the user go to entry view of payment plan (2)
    Then the user can NOT see the entry view of payment plan


  Scenario: Deny permisson 'Payment Plan Entry Delete'
    Given the user is a 'Super Admin'
    And the user is on 'Permission Management' page
    And settings in 'Permission Management' page are as listed below
      | User        | Payment Plan Entry Delete |
      | acc_lcl lee | Deny                      |
    Given the user is a 'Accounting' in 'QD' office
    And the user is on 'Payment Plan List' page
    When the user click payment plan (2)
    Then the user can NOT see the 'Delete' button in 'Payment Plan List'


  Scenario: Deny permission 'Invoice Make/Receive Payment Button Visible'
    Given the user is a 'Super Admin'
    And the user is on 'Permission Management' page
    And settings in 'Permission Management' page are as listed below
      | User        | Invoice Make/Receive Payment Button Visible |
      | acc_lcl lee | Deny                                        |
    Given the user is a 'Accounting' in 'QD' office
    And the user is on 'Payment Plan List' page
    When the user click payment plan (2)
    Then the user can NOT see the 'Make / Receive Paymen' button in 'Payment Plan List'


  Scenario: Deny Permission 'Payment Plan List Export Excel'
    Given the user is a 'Super Admin'
    And the user is on 'Permission Management' page
    And settings in 'Permission Management' page are as listed below
      | User        | Payment Plan List Export Excel |
      | acc_lcl lee | Deny                           |
    Given the user is a 'Accounting' in 'QD' office
    And the user is on 'Payment Plan List' page
    When the user click payment plan (2)
    Then the user can NOT see the 'Excel' button in 'Payment Plan List'
