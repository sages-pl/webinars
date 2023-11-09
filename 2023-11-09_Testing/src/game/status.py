from enum import Enum
from typing import ClassVar


class Status(Enum):
    ALIVE: ClassVar[str] = 'alive'
    DEAD: ClassVar[str] = 'dead'
