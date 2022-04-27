Feature: [Login] Login

    log in in differnet situation

    # @SFI @LOHAN @OLC
    # Scenario Outline: Login failed
    #     Given the user is on 'Login' page
    #      When the user log in with <username> and <password>
    #      Then login failed message should show
    # Examples: username / password
    #           | username      | password      |
    #           | {randomNo(5)} | {randomNo(5)} |
    #           | gm_joey       | 1             |
    #           | gm_joey       | {randomNo(5)} |

    Scenario Outline: Login passed
        Given the user is on 'Login' page
        When the user log in with <username> and <password>
        Then 'Dashboard' page should show

        @SFI @LOHAN
        Examples: username / password
            | username | password |
            | gm_joey  | 123456   |

        @OLC
        Examples: username / password
            | username | password |
            | gm_acc   | 123456   |
