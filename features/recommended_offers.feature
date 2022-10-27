Feature: Get Recommended Offers for a Customer

    Scenario: Customer with recommended offers
        Given a customer account with email "goldridge0@thetimes.co.uk"
        When I request for recommended offers
        Then I receive the following offers
            | id | name   | price  |
            | 8  | Brass  | 721.23 |
            | 25 | Rubber | 871.24 |

    Scenario: Customer with zero recommended offers
        Given a customer account with email "zero_offer_customer@imgur.com"
        When I request for recommended offers
            And there's no recommendations for this customer
        Then I receive the following offers
            | id | name       | price  |
            | 0  | Decoration | 2000.0 |
            | 0  | Grill      | 1300.0 |
