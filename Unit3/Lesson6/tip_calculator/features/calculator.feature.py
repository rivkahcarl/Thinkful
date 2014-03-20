Feature: Confirming that the tip calculator form displays

    Scenario: check that the form displays
        When I go to the tip calculator
        Then I should see the calculator form

    Scenario: check that the form submits successfully
        When I go to the tip calculator
        And I submit the form with a valid total and tip percentage
        Then I should see the results page

    Scenario: check that the calculator calculates accurately
        When you enter a meal cost of $50 
        And a 20% tip 
        Then your code correctly computes displays $10 as the tip amount. 
