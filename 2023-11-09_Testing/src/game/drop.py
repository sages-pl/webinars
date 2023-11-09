from typing import NamedTuple
from game.position import Point


class Drop(NamedTuple):
    gold: int
    position: Point
