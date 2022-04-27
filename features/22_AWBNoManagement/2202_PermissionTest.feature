@OLC
Feature: [AWB No Management] Permission Test for Acceptance Test GQT_130

  Scenario: Enable "Navigator Setting - AWB No.Management" then user can see 'AWB No. Management' under 'Settings' navigator
    Given the user is a 'Super Admin'
    And the user is on 'Permission Management' page
    And settings in 'Permission Management' page are as listed below
      | User       | Navigator Setting - AWB No. Management |
      | gm_lcl lee | Allow                                  |
    Given the user is a 'General Manager'
    And the user is on 'Dashboard' page
    When the user expand the navigator 'Settings'
    Then the user can see 'AWB No. Management' on the navigator

  Scenario: Disable "Navigator Setting - AWB No.Management" then user can NOT see 'AWB No. Management' under 'Settings' navigator
    Given the user is a 'Super Admin'
    And the user is on 'Permission Management' page
    And settings in 'Permission Management' page are as listed below
      | User       | Navigator Setting - AWB No. Management |
      | gm_lcl lee | Deny                                   |
    Given the user is a 'General Manager'
    And the user is on 'Dashboard' page
    When the user expand the navigator 'Settings'
    Then the user can NOT see 'AWB No. Management' on the navigator

  Scenario: Enable "Navigator Mawb No. Stock List" then user can see 'MAWB Stock List' under 'Air Export' navigator
    Given the user is a 'Super Admin'
    And the user is on 'Permission Management' page
    And settings in 'Permission Management' page are as listed below
      | User       | Navigator Mawb No. Stock List |
      | gm_lcl lee | Allow                         |
    Given the user is a 'General Manager'
    And the user is on 'Dashboard' page
    When the user expand the navigator 'Air Export'
    Then the user can see 'MAWB Stock List' on the navigator

  Scenario: Disable "Navigator Mawb No. Stock List" then user can NOT see 'MAWB Stock List' under 'Air Export' navigator
    Given the user is a 'Super Admin'
    And the user is on 'Permission Management' page
    And settings in 'Permission Management' page are as listed below
      | User       | Navigator Mawb No. Stock List |
      | gm_lcl lee | Deny                          |
    Given the user is a 'General Manager'
    And the user is on 'Dashboard' page
    When the user expand the navigator 'Air Export'
    Then the user can NOT see 'MAWB Stock List' on the navigator

  Scenario: Enable "MAWB No Stock List View" then user can view this page
    Given the user is a 'Super Admin'
    And the user is on 'Permission Management' page
    And settings in 'Permission Management' page are as listed below
      | User       | MAWB No Stock List View |
      | gm_lcl lee | Allow                   |
    Given the user is a 'General Manager'
    And the user is on 'MAWB Stock List' page
    Then the user can see 'MAWB Stock List' page

  Scenario: Disable "MAWB No Stock List View" then user can NOT view this page
    Given the user is a 'Super Admin'
    And the user is on 'Permission Management' page
    And settings in 'Permission Management' page are as listed below
      | User       | MAWB No Stock List View |
      | gm_lcl lee | Deny                    |
    Given the user is a 'General Manager'
    And the user is on 'MAWB Stock List' page
    Then the user can NOT see 'MAWB Stock List' page

  Scenario: Enable "MAWB No Stock List Edit" then user can edit "MAWB STOCK LIST"
    Given the user is a 'Super Admin'
    And the user is on 'Permission Management' page
    And settings in 'Permission Management' page are as listed below
      | User       | MAWB No Stock List Edit | MAWB No Stock List View |
      | gm_lcl lee | Allow                   | Allow                   |
    Given the user is a 'General Manager'
    And the user is on 'MAWB Stock List' page
    Then the checkbox and remark field for stock(1) in 'MAWB Stock List' is 'Enable'

  Scenario: Disable "MAWB No Stock List Edit" then user can NOT edit "MAWB STOCK LIST"
    Given the user is a 'Super Admin'
    And the user is on 'Permission Management' page
    And settings in 'Permission Management' page are as listed below
      | User       | MAWB No Stock List Edit | MAWB No Stock List View |
      | gm_lcl lee | Deny                    | Allow                   |
    Given the user is a 'General Manager'
    And the user is on 'MAWB Stock List' page
    Then the checkbox and remark field for stock(1) in 'MAWB Stock List' is 'Disable'

  Scenario: Enable "Setting Code View" then user can see 'AWB No. Management' page
    Given the user is a 'Super Admin'
    And the user is on 'Permission Management' page
    And settings in 'Permission Management' page are as listed below
      | User       | Setting Code View |
      | gm_lcl lee | Allow             |
    Given the user is a 'General Manager'
    And the user is on 'AWB No. Management' page
    Then the user can see 'AWB No. Management' page

  Scenario: Disable "Setting Code View" then user can NOT see 'AWB No. Management' page
    Given the user is a 'Super Admin'
    And the user is on 'Permission Management' page
    And settings in 'Permission Management' page are as listed below
      | User       | Setting Code View |
      | gm_lcl lee | Deny              |
    Given the user is a 'General Manager'
    And the user is on 'AWB No. Management' page
    Then the user can NOT see 'AWB No. Management' page

  Scenario: Enable "Setting Code Edit" then the user can create/edit 'AWB No. Management' page
    Given the user is a 'Super Admin'
    And the user is on 'Permission Management' page
    And settings in 'Permission Management' page are as listed below
      | User       | Setting Code Edit | Setting Code View |
      | gm_lcl lee | Allow             | Allow             |
    Given the user is a 'General Manager'
    And the user is on 'AWB No. Management' page
    When the user add AWB No. range in 'AWB No. Management'
      | Carrier | Prefix | Begin No. | End No. | Remark |
      | AIR9191 | 911    | 0000000   | 0000001 | ABC    |
    Then 'AWB No. range' should be saved correctly
    When the user edits AWB No. range(AIR9191)
      | Carrier | Prefix | Begin No. | End No. | Remark |
      | AIR9191 | 911    | 0000001   | 0000010 | CBA    |
    Then 'AWB No. range' should be saved correctly
    And AWB No. range should NOT be existed
      | Carrier | Prefix | Begin No. | End No. | Remark |
      | AIR9191 | 911    | 0000000   | 0000001 | ABC    |
