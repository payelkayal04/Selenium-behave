Feature: OrangeHRM Login

  Scenario: Login to OrangeHRM with valid parameters
    Given I launch chrome browser
    When I open orangeHRM home page
    And Enter username "admin" and password "admin123"
    And I click on login button
    Then user must successfully login to the dashboard page
