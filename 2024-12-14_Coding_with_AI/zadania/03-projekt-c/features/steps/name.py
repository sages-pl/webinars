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
