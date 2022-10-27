from behave import given, then, when
from behave.runner import Context

from features.util import assert_table_equals_list


@given('a customer account with email "{email}"')
def customer_email(context: Context, email: str):
    context.user_email = email


@when('I request for recommended offers')
def make_request(context: Context):
    email = context.user_email
    response = context.client.get(f'/v1/offers/{email}')
    context.offers = response.json()


@then('I receive the following offers')
def assert_recommendations(context: Context):
    assert_table_equals_list(context.table, context.offers)
