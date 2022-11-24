from dataclasses import dataclass, KW_ONLY, field
from datetime import date, timedelta, datetime, timezone


@dataclass
class Mission:
    year: int
    name: str


@dataclass(frozen=True)
class Astronaut:
    firstname: str
    lastname: str
    _: KW_ONLY
    born: date
    job: str = 'astronaut'
    agency: str = field(default='NASA', metadata={'choices': ['NASA', 'ESA']})
    age: int | None = None
    height: int | float | None = field(default=None, metadata={'unit': 'cm', 'min': 156, 'max': 210})
    weight: int | float | None = field(default=None, metadata={'unit': 'kg', 'min': 50, 'max': 90})
    groups: list[str] = field(default_factory=lambda: ['astronauts', 'managers'])
    friends: dict[str,str] = field(default_factory=dict)
    assignments: list[str] | None = field(default=None, metadata={'choices': ['Apollo18', 'Ares3', 'STS-136']})
    missions: list[Mission] = field(default_factory=list)
    experience: timedelta = timedelta(hours=0)
    account_last_login: datetime | None = None
    account_created: datetime = datetime.now(tz=timezone.utc)
    AGE_MIN: int = field(default=30, init=False, repr=False)
    AGE_MAX: int = field(default=50, init=False, repr=False)