Feature: Choose a menu.
  As a user I should be able to choose menu.

  Scenario: order menu
    Given that i am already on menu page
    When i click on some dishes 
    Then add more quantity of dishes 
    Then i should be able to proceed and it should move me to checkout page