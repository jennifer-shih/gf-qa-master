@Tracking
Feature: [GQT-325] Enable GoFreight Tracking

  Prepare environments
  https://hardcoretech.atlassian.net/browse/GQT-325


  Scenario: Enable GoFreight Tracking
    # Step 2
    Given the user is a 'Super Admin'
    And the user is on 'Company Management' page
    And settings in 'Company Management' page are as listed below
      | field                               | attribute | action | data |
      | Login                               | checkbox  | tick   | {on} |
      | Auto Create User                    | checkbox  | tick   | {on} |
      | Enable Tracking User Management     | checkbox  | tick   | {on} |
      | Enable Edi                          | checkbox  | tick   | {on} |
      | Enable Email Notification           | checkbox  | tick   | {on} |
      | Show tracking user email preference | checkbox  | tick   | {on} |
    When the user expand the navigator 'Settings'
    Then the user can see 'Tracking User Management' on the navigator

  Scenario: Create OPM User
    # Step 3
    Given the user is a 'Super Admin'
    And the user is on 'Create User' page
    When the user input user profile and create it
      | field            | attribute          | action | data                         |
      | User ID          | input              | input  | opm_ada                      |
      | Password         | input              | input  | 123456                       |
      | Confirm Password | input              | input  | 123456                       |
      | First Name       | input              | input  | opm_ada                      |
      | Office           | multi autocomplete | input  | UNITED CARGO MANAGEMENT INC. |
      | Role             | popup select       | select | Operation_Manager            |
      | E-mail           | input              | input  | emily.wu@gofreight.co        |
    Then new user should be created successfully

  Scenario: Enable OPM User's All Email Notifications
    # Step 4
    Given the user is on 'Profile' page
    When the user log in with opm_ada and 123456
    And the user set email notifiction settings as listed below
      | field                 | attribute | action | data |
      | In Gate               | checkbox  | tick   | {on} |
      | Rail                  | checkbox  | tick   | {on} |
      | Vessel Departure      | checkbox  | tick   | {on} |
      | Outgate               | checkbox  | tick   | {on} |
      | Vessel Arrival        | checkbox  | tick   | {on} |
      | Unloaded from Vessel  | checkbox  | tick   | {on} |
      | ETD Updated           | checkbox  | tick   | {on} |
      | ETA Updated           | checkbox  | tick   | {on} |
      | New Document Uploaded | checkbox  | tick   | {on} |
      | Shipment Report       | checkbox  | tick   | {on} |
      | Detention Report      | checkbox  | tick   | {on} |
      | Suspicious Report     | checkbox  | tick   | {on} |
    Then user settings are correct

  Scenario: Create Tracking Users
    # Step 5, 6
    Given the user is on 'Create Tracking User' page
    When the user input tracking user profile and create it
      | field            | attribute          | action | data                  |
      | User ID          | input              | input  | tk_cust               |
      | Password         | input              | input  | 123456                |
      | Confirm Password | input              | input  | 123456                |
      | First Name       | input              | input  | tk_cust               |
      | E-mail           | input              | input  | emily.wu@gofreight.co |
      | Trade Partner    | multi autocomplete | input  | HYOSUNG USA INC       |
      | Role             | select             | select | Customer              |
    Then new tracking user should be created successfully

    Given the user is on 'Create Tracking User' page
    When the user input tracking user profile and create it
      | field            | attribute          | action | data                  |
      | User ID          | input              | input  | tk_shipper            |
      | Password         | input              | input  | 123456                |
      | Confirm Password | input              | input  | 123456                |
      | First Name       | input              | input  | tk_shipper            |
      | E-mail           | input              | input  | emily.wu@gofreight.co |
      | Trade Partner    | multi autocomplete | input  | HYOSUNG USA INC       |
      | Role             | select             | select | Shipper               |
    Then new tracking user should be created successfully

    Given the user is on 'Create Tracking User' page
    When the user input tracking user profile and create it
      | field            | attribute          | action | data                  |
      | User ID          | input              | input  | tk_consignee          |
      | Password         | input              | input  | 123456                |
      | Confirm Password | input              | input  | 123456                |
      | First Name       | input              | input  | tk_consignee          |
      | E-mail           | input              | input  | emily.wu@gofreight.co |
      | Trade Partner    | multi autocomplete | input  | HYOSUNG USA INC       |
      | Role             | select             | select | Consignee             |
    Then new tracking user should be created successfully

    Given the user is on 'Create Tracking User' page
    When the user input tracking user profile and create it
      | field            | attribute          | action | data                  |
      | User ID          | input              | input  | tk_oversea_agent      |
      | Password         | input              | input  | 123456                |
      | Confirm Password | input              | input  | 123456                |
      | First Name       | input              | input  | tk_oversea_agent      |
      | E-mail           | input              | input  | emily.wu@gofreight.co |
      | Trade Partner    | multi autocomplete | input  | HYOSUNG USA INC       |
      | Role             | select             | select | Oversea Agent         |
    Then new tracking user should be created successfully
