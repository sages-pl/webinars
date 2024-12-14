Feature: Dragon's health

Scenario: Create Dragon has random health points
    Given Dragon does not exist
     When Dragon is created with name "Wawelski"
     Then Dragon exists
      And Health is between 50 and 100
