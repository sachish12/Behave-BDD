Feature: Pointz Login

  Scenario: Login to Pointz with valid parameters
    Given I launch Chrome browser
    When I open Pointz Homepage
    And Enter username "test1234@gmail.com" and password "PasswordTest123"
    And click on login button
    Then Uses/r must successfully login to the Dashboard page