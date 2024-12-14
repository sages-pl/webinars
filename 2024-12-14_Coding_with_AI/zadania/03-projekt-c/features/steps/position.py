from behave import *

from main import Dragon


@step("Position x is {x:d}")
def step_impl(context, x: int):
    assert context.dragon.position_x == x


@step("Position y is {y:d}")
def step_impl(context, y: int):
    assert context.dragon.position_y == y


@when('Dragon is created with name "{name}" and position x={x:d} y={y:d}')
def step_impl(context, name: str, x: int, y: int):
    context.dragon = Dragon(name, position_x=x, position_y=y)
    assert context.dragon.name == name
    assert context.dragon.position_x == x
    assert context.dragon.position_y == y
