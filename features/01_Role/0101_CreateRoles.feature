Feature: [Role] Create Roles

    Add roles

    Background: Log in GoFreight with Super Admin
        Given the user is a 'Super Admin'

    Scenario Outline: Create user
        Given the user is on 'Create User' page
        When the user input user profile and create it
            | field               | attribute          | action |
            | User ID             | input              | input  |
            | Password            | input              | input  |
            | Confirm Password    | input              | input  |
            | First Name          | input              | input  |
            | Last Name           | input              | input  |
            | Office              | multi autocomplete | input  |
            | Role                | popup select       | select |
            | E-mail              | input              | input  |
            | Allow Remote Access | checkbox           | tick   |
        Then new user should be created successfully
        @SFI
        Examples: <user id>
            | user id    | password | confirm password | first name | last name | office | role               | e-mail               | allow remote access |
            | op_joey    | 123456   | 123456           | op_joey    | lee       | LAX    | Operation          | edajoey@gofreight.co | {on}                |
            | opm_joey   | 123456   | 123456           | opm_joey   | lee       | LAX    | Operation_Manager  | edajoey@gofreight.co | {on}                |
            | acc_joey   | 123456   | 123456           | acc_joey   | lee       | LAX    | Accounting         | edajoey@gofreight.co | {on}                |
            | am_joey    | 123456   | 123456           | am_joey    | lee       | LAX    | Accounting_Manager | edajoey@gofreight.co | {on}                |
            | sales_joey | 123456   | 123456           | sales_joey | lee       | LAX    | Sales              | edajoey@gofreight.co | {on}                |
            | gm_joey    | 123456   | 123456           | gm_joey    | lee       | LAX    | General_Manager    | edajoey@gofreight.co | {on}                |

        @LOHAN
        Examples: <user id>
            | user id    | password | confirm password | first name | last name | office         | role               | e-mail               | allow remote access |
            | op_joey    | 123456   | 123456           | op_joey    | lee       | SZX;NGB;HQ;FBA | Operation          | edajoey@gofreight.co | {on}                |
            | opm_joey   | 123456   | 123456           | opm_joey   | lee       | SZX;NGB;HQ;FBA | Operation_Manager  | edajoey@gofreight.co | {on}                |
            | acc_joey   | 123456   | 123456           | acc_joey   | lee       | SZX;NGB;HQ;FBA | Accounting         | edajoey@gofreight.co | {on}                |
            | am_joey    | 123456   | 123456           | am_joey    | lee       | SZX;NGB;HQ;FBA | Accounting_Manager | edajoey@gofreight.co | {on}                |
            | sales_joey | 123456   | 123456           | sales_joey | lee       | SZX;NGB;HQ;FBA | Sales              | edajoey@gofreight.co | {on}                |
            | gm_joey    | 123456   | 123456           | gm_joey    | lee       | SZX;NGB;HQ;FBA | General_Manager    | edajoey@gofreight.co | {on}                |

        @OLC
        Examples: <user id>
            | user id   | password | confirm password | first name | last name | office | role               | e-mail               | allow remote access |
            | op_lcl    | 123456   | 123456           | op_lcl     | lee       | 拼箱部 | Operation          | edajoey@gofreight.co | {on}                |
            | op_tpe    | 123456   | 123456           | op_tpe     | lee       | TPE    | Operation          | edajoey@gofreight.co | {on}                |
            | opm_lcl   | 123456   | 123456           | opm_lcl    | lee       | 拼箱部 | Operation_Manager  | edajoey@gofreight.co | {on}                |
            | acc_lcl   | 123456   | 123456           | acc_lcl    | lee       | 拼箱部 | Accounting         | edajoey@gofreight.co | {on}                |
            | am_lcl    | 123456   | 123456           | am_lcl     | lee       | 拼箱部 | Accounting_Manager | edajoey@gofreight.co | {on}                |
            | sales_lcl | 123456   | 123456           | sales_lcl  | lee       | 拼箱部 | Sales              | edajoey@gofreight.co | {on}                |
            | gm_lcl    | 123456   | 123456           | gm_lcl     | lee       | 拼箱部 | General_Manager    | edajoey@gofreight.co | {on}                |

        @OLC_TPE
        Examples: <user id>
            | user id   | password | confirm password | first name | last name | office | role               | e-mail               | allow remote access |
            | op_lcl    | 123456   | 123456           | op_lcl     | lee       | 拼箱部 | Operation          | edajoey@gofreight.co | {on}                |
            | opm_lcl   | 123456   | 123456           | opm_lcl    | lee       | 拼箱部 | Operation_Manager  | edajoey@gofreight.co | {on}                |
            | acc_lcl   | 123456   | 123456           | acc_lcl    | lee       | 拼箱部 | Accounting         | edajoey@gofreight.co | {on}                |
            | acc_tpe   | 123456   | 123456           | acc_tpe    | lee       | 拼箱部 | Accounting         | edajoey@gofreight.co | {on}                |
            | am_lcl    | 123456   | 123456           | am_lcl     | lee       | 拼箱部 | Accounting_Manager | edajoey@gofreight.co | {on}                |
            | sales_lcl | 123456   | 123456           | sales_lcl  | lee       | 拼箱部 | Sales              | edajoey@gofreight.co | {on}                |
            | gm_lcl    | 123456   | 123456           | gm_lcl     | lee       | 拼箱部 | General_Manager    | edajoey@gofreight.co | {on}                |
            | op_tpe    | 123456   | 123456           | op_tpe     | lee       | TLG    | Operation          | edajoey@gofreight.co | {on}                |
            | sales_tpe | 123456   | 123456           | sales_tpe  | lee       | TLG    | Sales              | edajoey@gofreight.co | {on}                |

        @MASCOT
        Examples: <user_id>
            | user id    | password | confirm password | first name | last name | office | role               | e-mail               | allow remote access |
            | op_joey    | 123456   | 123456           | op_joey    | lee       | LA     | Operation          | edajoey@gofreight.co | {on}                |
            | opm_joey   | 123456   | 123456           | opm_joey   | lee       | LA     | Operation_Manager  | edajoey@gofreight.co | {on}                |
            | acc_joey   | 123456   | 123456           | acc_joey   | lee       | LA     | Accounting         | edajoey@gofreight.co | {on}                |
            | am_joey    | 123456   | 123456           | am_joey    | lee       | LA     | Accounting_Manager | edajoey@gofreight.co | {on}                |
            | sales_joey | 123456   | 123456           | sales_joey | lee       | LA     | Sales              | edajoey@gofreight.co | {on}                |
            | sm_joey    | 123456   | 123456           | sm_joey    | lee       | LA     | Sales_Manager      | edajoey@gofreight.co | {on}                |
            | gm_joey    | 123456   | 123456           | gm_joey    | lee       | LA     | General_Manager    | edajoey@gofreight.co | {on}                |

    @SFI @LOHAN @OLC @OLC_TPE @MASCOT
    Scenario: After creating users, disable 'Upsell' feature by Patch DB - 'patch_upsell_read_all_feeds'
        Given the user is on 'Patch DB' page
        When the user clicks 'Apply' button for 'patch_upsell_read_all_feeds' on 'Patch DB' page
        Then the success msg 'News Feeds All Read' will show on 'Console' block in '60' sec
