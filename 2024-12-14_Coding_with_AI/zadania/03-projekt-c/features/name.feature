Feature: Dragon's creation

Scenario: Create Dragon with name
    Given Dragon does not exist
     When Dragon is created with name "Wawelski"
     Then Dragon exists
      And Name is "Wawelski"

Scenario: Create Dragon without name (raise an error)
    Given Dragon does not exist
     When Dragon is created without name
     Then Raise an error with message
