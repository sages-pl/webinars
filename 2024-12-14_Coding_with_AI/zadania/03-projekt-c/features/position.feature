Feature: Dragon's position

Scenario: Create Dragon with default position
    Given Dragon does not exist
     When Dragon is created with name "Wawelski"
     Then Dragon exists
      And Position x is 0
      And Position y is 0

Scenario: Create Dragon with initial position
    Given Dragon does not exist
     When Dragon is created with name "Wawelski" and position x=50 y=100
     Then Dragon exists
      And Position x is 50
      And Position y is 100
