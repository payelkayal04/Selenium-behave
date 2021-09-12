Feature: OrangeHRM Logo

  Scenario: Logo presence on OrangeHRM home page
    Given I launch chrome browser
    When I open orangeHRM home page
    Then verify that the logo present on page
    And close browser


