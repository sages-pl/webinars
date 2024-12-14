from behave import *


@given("Dragon does not exist")
def step_impl(context):
    assert 'dragon' not in context


@then("Dragon exists")
def step_impl(context):
    assert 'dragon' in context
