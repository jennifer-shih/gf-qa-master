Feature: [Truck] Check Doc Center

  Background: Log in GoFreight with Operator
    Given the user is a 'Operator'
    And the download file folder is 'tk'


  Scenario Outline: The user can print Pickup / Delivery Order and save in local
    Given the user has a TK MBL as 'A' with only required fields filled
    When the user click 'Doc Center' tab of Truck
    And the user click 'Tools' -> 'Pickup / Delivery Order'
    And the user switch to 'Pickup / Delivery Order' window
    And the user click 'Download PDF' button
    Then TK <doc> file should be saved in download folder (30 sec)
    When the user switch to main window
    Then <doc> should shows up on 'Document List'

    @SFI @LOHAN
    Examples:
      | doc                     |
      | PICKUP & DELIVERY ORDER |
    @OLC
    Examples:
      | doc                   |
      | Pickup Delivery Order |
