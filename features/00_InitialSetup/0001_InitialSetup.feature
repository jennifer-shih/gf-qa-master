Feature: [InitialSetup] Initial Setup

    Reset user's DB and do some basic settings

    Background: Log in GoFreight with Super Admin
        Given the user is a 'Super Admin'

    @SFI
    Scenario: Reset DB to SFI's latest one
        Given the user is on 'Reset Backups DB' page
        When the user resets DB to SFI's latest one
        Then the reset DB process will be done for a time

    @LOHAN
    Scenario: Reset DB to LOHAN's 2020/11/01
        Given the user is on 'Reset Backups DB' page
        When the user resets DB to __qa-auto-test / lohan-20201101-migrated-backup.sql.gz
        Then the reset DB process will be done for a time

    @OLC
    Scenario: Reset DB to OLC's latest one
        Given the user is on 'Reset Backups DB' page
        When the user resets DB to OLC's latest one
        Then the reset DB process will be done for a time

    @OLC_TPE
    Scenario: Reset DB to OLC
        Given the user is on 'Reset Backups DB' page
        When the user resets DB to __internal-test / olc-20211012-tpetest
        Then the reset DB process will be done for a time

    @MASCOT
    Scenario: Reset DB to Mascot's latest one
        Given the user is on 'Reset Backups DB' page
        When the user resets DB to Mascot's latest one
        Then the reset DB process will be done for a time

    @Tracking
    Scenario: Reset DB to UCM's latest one
        Given the user is on 'Reset Backups DB' page
        When the user resets DB to UCM's latest one by Jenkins
        Then the reset DB process will be done for a time

    @SFI @LOHAN @OLC @OLC_TPE @MASCOT
    Scenario: Set Super User language
        Given the user is on 'Profile' page
        When the user set language to 'English'
        And the user refresh browser
        Then GoFreight should show with English

    @SFI @LOHAN @OLC
    Scenario: Set 'Office Entry'
        Given the user is on 'Office Management' page
        When the user go to 'Office Entry' page
        And the user input 'Office Entry' fields and save it
            | field                      | attribute       | action   | data           |
            | SCAC                       | input           | input    | EGLV           |
            | Enable Email Function      | checkbox        | tick     | {on}           |
            | SMTP Host                  | input           | input    | smtp.gmail.com |
            | SMTP Port                  | input           | input    | 587            |
            | Security Protocol          | select          | select   | TLS            |
            | IP Network                 | input           | clear    |                |
            | Default Language           | select          | select   | English        |
            | Add Company Logo           | add file button | add file | {companyLogo}  |
            | Allow Duplicate HBL/MBL No | checkbox        | tick     | {on}           |
        Then 'Office Entry' settings are correct

    @OLC_TPE
    Scenario: Set 'Office Entry'
        Given the user is on 'Office Management' page
        And settings in 'TPE' 'Office Entry' page are as listed below
            | field                                  | attribute       | action   | data           |
            | SCAC                                   | input           | input    | EGLV           |
            | Enable Email Function                  | checkbox        | tick     | {on}           |
            | SMTP Host                              | input           | input    | smtp.gmail.com |
            | SMTP Port                              | input           | input    | 587            |
            | Security Protocol                      | select          | select   | TLS            |
            | IP Network                             | input           | clear    |                |
            | Default Language                       | select          | select   | English        |
            | Date Format                            | input           | input    | %Y-%m-%d       |
            | Package Label Date Format (Form)       | input           | input    | %Y-%m-%d       |
            | Local Statement Date Format            | input           | input    | %Y-%m-%d       |
            | Human Date Format                      | input           | input    | %Y-%m-%d       |
            | Human Date Format With Full Month Name | input           | input    | %Y-%m-%d       |
            | Add Company Logo                       | add file button | add file | {companyLogo}  |
        And the user is on 'Office Management' page
        When the user go to 'Office Entry' page
        And the user input 'Office Entry' fields and save it
            | field                 | attribute       | action   | data           |
            | SCAC                  | input           | input    | EGLV           |
            | Enable Email Function | checkbox        | tick     | {on}           |
            | SMTP Host             | input           | input    | smtp.gmail.com |
            | SMTP Port             | input           | input    | 587            |
            | Security Protocol     | select          | select   | TLS            |
            | IP Network            | input           | clear    |                |
            | Default Language      | select          | select   | English        |
            | Add Company Logo      | add file button | add file | {companyLogo}  |
        Then 'Office Entry' settings are correct

    @SFI @LOHAN @OLC @OLC_TPE @MASCOT
    Scenario: Set 'Company Management'
        Given the user is on 'Company Management' page
        When the user input 'Company Management' fields and save it
            | field                            | attribute | action | data  |
            | Enable Warehouse                 | checkbox  | tick   | {on}  |
            | Enable Warehouse App             | checkbox  | tick   | {on}  |
            | Enable Quotation                 | checkbox  | tick   | {on}  |
            | Container Ordering Ocean Import  | checkbox  | tick   | {off} |
            | Container Ordering Ocean Export  | checkbox  | tick   | {off} |
            | Container Ordering Truck         | checkbox  | tick   | {off} |
            | Container Ordering Misc          | checkbox  | tick   | {off} |
            | Container Ordering Ocean Booking | checkbox  | tick   | {off} |
        Then 'Company Management' settings are correct
