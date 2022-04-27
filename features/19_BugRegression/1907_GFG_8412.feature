Feature: [Bug Regression] GFG_8412

    [FCC] [ELI] On invoice entry, 若 Freight item 必填欄位為空時, Save 時直接 ignore 空白的 Freight items
    https://hardcoretech.atlassian.net/browse/GFG-8412

    Scenario: Creating an Invoice (A/R) and add some empty freights, system should ignore empty freights when the user click save button
        Given DB is resets to __internal-test / generic-db-by-office-20201213.sql.gz
        And the user is a 'Super Admin'
        And the user has a OI MBL with 0 HBL as 'A' with only required fields filled
        When the user create an AR and add some empty freight items
        Then the AR should save successfully and ignore empty freight items
