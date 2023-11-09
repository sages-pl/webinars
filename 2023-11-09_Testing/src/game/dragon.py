from random import randint
from typing import ClassVar
from game.drop import Drop
from game.position import Position
from game.status import Status
from game.utils import when


class Dragon(Position):
    name: str
    health = property()
    _health_current: int

    DAMAGE_MAX: ClassVar[int] = 20
    DAMAGE_MIN: ClassVar[int] = 5
    GOLD_MAX: ClassVar[int] = 100
    GOLD_MIN: ClassVar[int] = 1
    HEALTH_MAX: ClassVar[int] = 100
    HEALTH_MIN: ClassVar[int] = 50
    TEXTURE_ALIVE: ClassVar[str] = 'img/dragon/alive.png'
    TEXTURE_DEAD: ClassVar[str] = 'img/dragon/dead.png'

    class IsDead(Exception):
        pass

    def __init__(self, name: str, /,  # noqa
                 *, position_x: int = 0, position_y: int = 0) -> None:
        self.name = name
        self.status = Status.ALIVE
        self.texture = self.TEXTURE_ALIVE
        self.health = randint(self.HEALTH_MIN, self.HEALTH_MAX)  # noqa
        self.gold = randint(self.GOLD_MIN, self.GOLD_MAX)
        self.position_set(x=position_x, y=position_y)

    @when('is_alive')
    def make_damage(self) -> int:
        return randint(self.DAMAGE_MIN, self.DAMAGE_MAX)

    @health.getter
    def health(self):
        return self._health_current

    @health.setter
    def health(self, value):
        self._health_current = value
        if self.is_alive():
            self.status = Status.ALIVE
            self.texture = self.TEXTURE_ALIVE
        else:
            self.status = Status.DEAD
            self.texture = self.TEXTURE_DEAD
            raise self.IsDead

    @when('is_alive')
    def take_damage(self, damage, /) -> None:
        self.health -= damage  # noqa

    @when('is_dead')
    def get_drop(self) -> Drop:
        gold, self.gold = self.gold, 0
        return Drop(gold=gold, position=self.position_get())

    def is_dead(self):
        return self.health <= 0  # noqa

    def is_alive(self):
        return not self.is_dead()
