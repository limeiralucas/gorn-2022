Feature: Get Recommended Offers for a Customer

    Scenario: Customer with recommended offers
        Given a customer account with email "goldridge0@thetimes.co.uk"
        When I request for recommended offers
        Then I receive multiple recommendations

    Scenario: Customer with zero recommended offers
        Given a customer account with email "athraves7@imgur.com"
        When I request for recommended offers
        Then I receive the default recommendation
