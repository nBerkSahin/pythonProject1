

  Feature: test 1

    Scenario: 1

      Given I navigate to login page
      When I enter username as "34007"
      And I enter password as "123456h.P,?"
      And I click login button
      Then I check my login
