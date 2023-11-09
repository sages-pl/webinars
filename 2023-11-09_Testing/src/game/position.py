from typing import NamedTuple


class Point(NamedTuple):
    x: int = 0
    y: int = 0

    def __str__(self):
        return f'({self.x}, {self.y})'


class Position:
    _position: Point

    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.position_set(x=x, y=y)

    def position_get(self) -> Point:
        return self._position

    def position_set(self, *, x: int, y: int) -> None:
        self._position = Point(x, y)

    def position_change(self, *,
                        left: int = 0, right: int = 0,
                        up: int = 0, down: int = 0
                        ) -> None:
        current_x, current_y = self.position_get()
        new_x = current_x + right - left
        new_y = current_y + down - up
        self.position_set(x=new_x, y=new_y)
