Feature: [Accounting] Accounting Report With Large Period

  Reports without start date / end date should print without errors
  (these test case need high level fms)

  @SFI @LOHAN @OLC
  Scenario: Trail Balance without 'start date' should be OK
    Given the user is a 'General Manager'
    And the user is on 'Trial Balance' page
    When the user enter 'Trial Balance' info
      | field  | attribute         | action | data              |
      | Period | period datepicker | input  | {blank} ~ {today} |
      | Office | select            | select | All               |
    And the user click 'Trial Balance' 'Print' button
    Then the 'Trial Balance Print' should show without any errors
    And the 'Period' on 'Trial Balance Print' should be '[First Record]' to '{today}'

  @SFI @LOHAN @OLC
  Scenario: Trail Balance without 'end date' should be OK
    Given the user is a 'General Manager'
    And the user is on 'Trial Balance' page
    Given the user is on 'Trial Balance' page
    When the user enter 'Trial Balance' info
      | field  | attribute         | action | data                 |
      | Period | period datepicker | input  | {today-30} ~ {blank} |
      | Office | select            | select | All                  |

    And the user click 'Trial Balance' 'Print' button
    Then the 'Trial Balance Print' should show without any errors
    And the 'Period' on 'Trial Balance Print' should be '{today-30}' to '[Last Record]'

  @SFI @LOHAN @OLC
  Scenario: Trail Balance without 'start date' and 'end date' should be OK
    Given the user is a 'General Manager'
    And the user is on 'Trial Balance' page
    When the user enter 'Trial Balance' info
      | field  | attribute         | action | data              |
      | Period | period datepicker | input  | {blank} ~ {blank} |
      | Office | select            | select | All               |
    And the user click 'Trial Balance' 'Print' button
    Then the 'Trial Balance Print' should show without any errors
    And the 'Period' on 'Trial Balance Print' should be '[First Record]' to '[Last Record]'
