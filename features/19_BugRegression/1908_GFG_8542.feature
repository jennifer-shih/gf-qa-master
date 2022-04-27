Feature: [Bug Regression] GFG_8412

    [FCC] After copy Booking (already linked to MBL), the booking entry page should show normally
    https://hardcoretech.atlassian.net/browse/GFG-8542

    Scenario: After copy Booking (already linked to MBL), the booking entry page should show normally
        Given DB is resets to __internal-test / generic-db-by-office-20201213.sql.gz
        And the user is a 'Super Admin'
        And the user has a OE Shipment with one HBL(HACO-8412)
        And the user is at HBL(HACO-8412) Booking entry
        When the user click booking Tools => Copy => OK
        Then the copy booking should show normally
        And the copy booking can be saved successfully
