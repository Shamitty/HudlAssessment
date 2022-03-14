Feature: HudlProject
    # @hudlLogin
    # Scenario: Login to hudl with user credentials
    #     Given I have navigated to Hudl
    #     When I click the login button
    #     When I enter my userlogin into the username field
    #     When I enter my userpassword into the password field
    #     When I click the sign in button
    #     Then I will see the Hudl sign screen with "Coach S" logged in

    @hudlFailedLogin
    Scenario: Login to hudl with the wrong credentials
        Given I have navigated to Hudl
        When I click the login button
        When I enter my userlogin into the username field
        When I enter the wrong userpassword "WrongPassword" into the password field
        When I click the sign in button
        Then I will see a login failure warning "We didn't recognize that email and/or password. Need help?"