Feature: Signup

  Scenario: Signup on Pointzi home page
    Given Launch chrome browser
    When Open Pointzi home page
    And Click on register button
    And Enter email "test1234@gmail.com", password "PasswordTest123" and confirm password "PasswordTest123"
    And Click on next button
    And Select the role and No of app users
    And Click on next button 2
    And Enter firstname "Sachish", lastname "Maharjan", companyname "Pointz", phone number "123456789" and tick on accept agreement policy
    And Click on Sign up button
    Then User must sucessfully login to the Dashboard page

