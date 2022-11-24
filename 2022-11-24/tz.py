from dataclasses import dataclass
from datetime import datetime
from zoneinfo import ZoneInfo


class Timezone:
    def __init__(self, name):
        self.timezone = ZoneInfo(name)

    def __get__(self, parent, *args):
        utc = parent.utc.replace(tzinfo=ZoneInfo('UTC'))
        return utc.astimezone(self.timezone)

    def __set__(self, parent, new_datetime):
        local_time = new_datetime.replace(tzinfo=self.timezone)
        parent.utc = local_time.astimezone(ZoneInfo('UTC'))


@dataclass
class Time:
    utc = datetime.now(tz=ZoneInfo('UTC'))
    warsaw = Timezone('Europe/Warsaw')
    eastern = Timezone('America/New_York')
    pacific = Timezone('America/Los_Angeles')


t = Time()

# Gagarin's launch to space
t.utc = datetime(1961, 4, 12, 6, 7)

print(t.utc)
# 1961-04-12 06:07:00
print(t.warsaw)
# 1961-04-12 07:07:00+01:00
print(t.eastern)
# 1961-04-12 01:07:00-05:00
print(t.pacific)
# 1961-04-11 22:07:00-08:00


# Armstrong's first Lunar step
t.warsaw = datetime(1969, 7, 21, 3, 56, 15)

print(t.utc)
# 1969-07-21 02:56:15+00:00
print(t.warsaw)
# 1969-07-21 03:56:15+01:00
print(t.eastern)
# 1969-07-20 22:56:15-04:00
print(t.pacific)
# 1969-07-20 19:56:15-07:00