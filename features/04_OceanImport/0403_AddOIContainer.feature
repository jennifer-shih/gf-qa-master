Feature: [OceanImport] Add OI Container

    the operator can add a container to the MB/L and HB/L which has been created

    Background: Log in GoFreight with Operator
        Given the user is a 'Operator'


    Scenario Outline: The user should see some default vaule on Container page
        Given the user has a OI MBL with 1 HBL as 'A' with only required fields filled
        When the user click 'Container & Item' tab of OI
        Then PKG Unit = '<unit>'
        And Weight Unit = 'KG'
        And Measurement Unit = 'CBM'

        @SFI @LOHAN
        Examples:
            | unit      |
            | CARTON(S) |
        @OLC
        Examples:
            | unit    |
            | CARTONS |


    @SFI @LOHAN @OLC
    Scenario: KG => LB and CBM => CFT converter are correct
        Given the user has a OI MBL with 1 HBL as 'A' with only required fields filled
        When the user click 'Container & Item' tab of OI
        And the user click 'Add' for OI MBL Container List
        And the user enters datas to OI container(1)
            | field           | attribute | action | data     |
            | Weight KG       | input     | input  | 1234.11  |
            | Measurement CBM | input     | input  | 4321.333 |
        And the user click save button
        Then weight unit converter should caculate with 1 KG = 2.20462262 LB
        And measurement unit converter should caculate with 1 CBM = 35.31466672 CFT


    @SFI @LOHAN @OLC
    Scenario: The user can add a new container for MB/L
        Given the user has a OI MBL with 1 HBL as 'A' with only required fields filled
        When the user click 'Container & Item' tab of OI
        And the user click 'Add' for OI MBL Container List
        And the user click 'More' button of OI MBL container(1)
        And the user enters datas to OI container(1)
            | field              | attribute  | action        | data                       |
            | Container No.      | input      | input         | {randomContainerNo}        |
            | TP/SZ              | select     | random select |                            |
            | Seal No.           | input      | input         | SN{randN(6)}               |
            | LFD                | datepicker | input         | {today+2}                  |
            | FDD                | datepicker | input         | {today+11}                 |
            | PKG                | input      | input         | {randN(3)}                 |
            | Weight KG          | input      | input         | {randN(3)}                 |
            | Measurement CBM    | input      | input         | {randN(3)}                 |
            | Seal No. 2         | input      | input         | SN2{randN(6)}              |
            | Pick No.           | input      | input         | PN{randN(6)}               |
            | CPRS No.           | input      | input         | CPRS{randN(6)}             |
            | CNRU No.           | input      | input         | CNRU{randN(6)}             |
            | D.G                | select     | random select |                            |
            | Storage Start Date | datepicker | input         | {today+15}                 |
            | Storage End Date   | datepicker | input         | {today+16}                 |
            | Rail Start         | datepicker | input         | {today+30}                 |
            | Appt.              | datepicker | input         | {today+12}                 |
            | Pick Up            | datepicker | input         | {today+12}                 |
            | Gate Out           | datepicker | input         | {today+14}                 |
            | F.Dest ETA         | datepicker | input         | {today+4}                  |
            | ETA Door           | datepicker | input         | {today+17}                 |
            | ATA Door           | datepicker | input         | {today+13}                 |
            | Empty Return       | datepicker | input         | {today+26}                 |
            | Remark             | input      | input         | This is a container remark |
        And the user click save button
        And the user refresh browser
        Then the container should be created


    @SFI @LOHAN @OLC
    Scenario: Enable 'Total' of MB/L then the user can manually input total PKG, Weight, Measurement
        Given the user has a OI MBL with 1 HBL as 'A' with only required fields filled
        When the user click 'Container & Item' tab of OI
        And the user enable 'Input total number' of MBL
        And the user input total PKG, Weight, Measurement
            | PKG | Weight | Measurement |
            | 10  | 20.22  | 33.333      |
        And the user click save button
        And the user refresh browser
        Then Total PKG, Weight, Measurement should be
            | PKG | Weight | Measurement |
            | 10  | 20.22  | 33.333      |


    @SFI @LOHAN @OLC
    Scenario: The user can add a new commodity for HB/L
        Given the user has a OI MBL with 1 HBL as 'A' with only required fields filled
        When the user click 'Container & Item' tab of OI
        And the user click 'New' button for HBL Commodity
        And the user add a new commodity #1
            | field                 | attribute | action | data              |
            | Commodity Description | input     | input  | {randomCommodity} |
            | HTS Code              | input     | input  | HTS{randN(4)}     |
        And the user click save button
        And the user refresh browser
        Then the commodity should be created
