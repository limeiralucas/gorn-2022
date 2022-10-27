Feature: Get Recommended Offers for a Customer

    Scenario: Customer with recommended offers
        Given a customer account with email "goldridge0@thetimes.co.uk"
        When I request for recommended offers
        Then I receive the following offers
            | id | name   | price  |
            | 8  | Brass  | 721.23 |
            | 25 | Rubber | 871.24 |

    Scenario: Customer with zero recommended offers
        Given a customer account with email "athraves7@imgur.com"
        When I request for recommended offers
        Then I receive the default recommendation
