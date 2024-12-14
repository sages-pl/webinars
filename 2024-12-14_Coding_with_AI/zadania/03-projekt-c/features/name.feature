Feature: Dragon's creation

Scenario: Create Dragon with name
    Given Dragon does not exist
     When Dragon is created with name "Wawelski"
     Then Dragon exists
      And Name is "Wawelski"
