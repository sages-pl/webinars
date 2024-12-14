from behave import *
from main import Dragon


@given("Dragon does not exist")
def step_impl(context):
    assert 'dragon' not in context


@when('Dragon is created with name "{name}"')
def step_impl(context, name: str):
    context.dragon = Dragon(name)


@then("Dragon exists")
def step_impl(context):
    assert 'dragon' in context


@step('Name is "{name}"')
def step_impl(context, name: str):
    assert context.dragon.name == name


@when("Dragon is created without name")
def step_impl(context):
    try:
        context.dragon = Dragon('')
    except TypeError as err:
        context.error = err


@then("Raise an error with message")
def step_impl(context):
    assert 'error' in context
    assert str(context.error) == 'Name cannot be empty'
