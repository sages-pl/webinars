from behave import *


@step("Health is between {low:d} and {high:d}")
def step_impl(context, low, high):
    assert context.dragon.health >= low
    assert context.dragon.health <= high
