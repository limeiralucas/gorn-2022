from behave import given, then, when
from behave.runner import Context


@given('a customer account with email {email}')
def customer_email(context: Context, email: str):
    context.user_email = email


@when('I request for recommended offers')
def make_request(context: Context):
    email = context.user_email
    response = context.client.get(f'/v1/offers/{email}')
    context.response_data = response.json()


@then('I receive multiple recommendations')
def assert_recommendations(context: Context):
    response_data = context.response_data
    recommendations = response_data['recommendations']

    assert len(recommendations) >= 2
