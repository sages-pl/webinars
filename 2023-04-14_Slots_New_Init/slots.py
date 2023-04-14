# Slots
# Dataclass
# NamedTuple
# New + Init
from dataclasses import dataclass
from itertools import starmap
from typing import NamedTuple

DATA = [
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
    (4.9, 3.0, 1.4, 0.2, 'setosa'),
    (4.9, 2.5, 4.5, 1.7, 'virginica'),
    (7.1, 3.0, 5.9, 2.1, 'virginica'),
    (4.6, 3.4, 1.4, 0.3, 'setosa'),
    (5.4, 3.9, 1.7, 0.4, 'setosa'),
    (5.7, 2.8, 4.5, 1.3, 'versicolor'),
    (5.0, 3.6, 1.4, 0.3, 'setosa'),
    (5.5, 2.3, 4.0, 1.3, 'versicolor'),
    (6.5, 3.0, 5.8, 2.2, 'virginica'),
    (6.5, 2.8, 4.6, 1.5, 'versicolor'),
    (6.3, 3.3, 6.0, 2.5, 'virginica'),
    (6.9, 3.1, 4.9, 1.5, 'versicolor'),
    (4.6, 3.1, 1.5, 0.2, 'setosa'),
]


@dataclass(slots=True, frozen=True)
class Iris:
    sl: float
    sw: float
    pl: float
    pw: float
    species: str


result = starmap(Iris, DATA[1:])






# Użycie slots blokuje stworzenie __dict__ oraz __weakref__
# Tworzy specjalne miejsca w klasie do przechowywania wartości


>>> class User:
...     __slots__ = ('firstname', 'lastname')
...
... class Admin(User):
...     pass
...
>>>
>>> mark = User()
>>> mark.firstname = 'Mark'
>>> mark.lastname = 'Watney'
>>> mark.age = 40
AttributeError: 'User' object has no attribute 'age'

>>>
>>>
>>> melissa = Admin()
>>> melissa.firstname = 'Melissa'
>>> melissa.lastname = 'Lewis'
>>> melissa.age = 44
>>>
>>> vars(mark)
TypeError: vars() argument must have __dict__ attribute

>>> vars(melissa)
{'age': 44}
>>>
>>> melissa.age
44
>>> melissa.firstname
'Melissa'
>>> melissa.lastname
'Lewis'
>>>
>>> vars(Admin)
mappingproxy({'__module__': '__main__',
              '__dict__': <attribute '__dict__' of 'Admin' objects>,
              '__weakref__': <attribute '__weakref__' of 'Admin' objects>,
              '__doc__': None})
>>>
>>> vars(User)
mappingproxy({'__module__': '__main__',
              '__slots__': ('firstname', 'lastname'),
              'firstname': <member 'firstname' of 'User' objects>,
              'lastname': <member 'lastname' of 'User' objects>,
              '__doc__': None})



>>> class User:
...     __slots__ = ('firstname', 'lastname')
...
>>> class Admin(User):
...     __slots__ = ('age',)
...
>>>
>>> melissa = Admin()
>>> melissa.firstname = 'Melissa'
>>> melissa.lastname = 'Lewis'
>>> melissa.age = 44
>>>
>>> melissa.salary = 10_000
AttributeError: 'Admin' object has no attribute 'salary'

>>>
>>>
>>> vars(User)
mappingproxy({'__module__': '__main__',
              '__slots__': ('firstname', 'lastname'),
              'firstname': <member 'firstname' of 'User' objects>,
              'lastname': <member 'lastname' of 'User' objects>,
              '__doc__': None})
>>>
>>> vars(Admin)
mappingproxy({'__module__': '__main__',
              '__slots__': ('age',),
              'age': <member 'age' of 'Admin' objects>,
              '__doc__': None})


>>> melissa.__slots__
('age',)
>>>
>>> melissa.__class__.mro()
[__main__.Admin, __main__.User, object]
>>>
>>> result = [x.__slots__ for x in melissa.__class__.mro() if hasattr(x, '__slots__')]
>>> result
[('age',), ('firstname', 'lastname')]






>>> result = starmap(Iris, DATA[1:])
>>> data = list(result)
>>>
>>> data[0]
Iris(sl=5.8, sw=2.7, pl=5.1, pw=1.9, species='virginica')
>>>
>>>
>>> vars(data[0])
TypeError: vars() argument must have __dict__ attribute

>>>
>>> from dataclasses import astuple, asdict
>>>
>>> asdict(data[0])
{'sl': 5.8, 'sw': 2.7, 'pl': 5.1, 'pw': 1.9, 'species': 'virginica'}
>>>
>>> astuple(data[0])
(5.8, 2.7, 5.1, 1.9, 'virginica')




def hello(user):
    print(f'Hello {user[0]} {user[1]}')


mark = ('Mark', 'Watney')
hello(mark)
# Hello Mark Watney

mark = ['Mark', 'Watney']
hello(mark)
# Hello Mark Watney

mark = {'Mark', 'Watney'}
hello(mark)
# TypeError: 'set' object is not subscriptable



def hello(user: tuple):
    print(f'Hello {user[0]} {user[1]}')

mark = ('Mark', 'Watney')
hello(mark)
# Hello Mark Watney

mark = {'Mark', 'Watney'}
hello(mark)  # Expected type 'tuple', got 'set[str]' instead







def hello(user: tuple):
    print(f'Hello {user[0]} {user[1]}')


mark = ('Mark', 'Watney')
hello(mark)
# Hello Mark Watney


mark = ('Mark', 'Watney', 'mwatney@nasa.gov', 40, 185.5, 75.5)
hello(mark)
# Hello Mark Watney


mark = ('Mark',)
hello(mark)
# IndexError: tuple index out of range




def hello(user: tuple[str,str]):
    print(f'Hello {user[0]} {user[1]}')


mark = ('Mark', 'Watney')
hello(mark)
# Hello Mark Watney


mark = ('Mark', 'Watney', 'mwatney@nasa.gov', 40, 185.5, 75.5)  # Expected type 'tuple[str, str]', got 'tuple[str, str, str, int, float, float]' instead
hello(mark)
# Hello Mark Watney


mark = ('Mark',)  # Expected type 'tuple[str, str]', got 'tuple[str]' instead
hello(mark)
# IndexError: tuple index out of range




def hello(user: tuple[str,str]):
    print(f'Hello {user[0]} {user[1]}')


mark = ('Mark', 'Watney')
hello(mark)
# Hello Mark Watney


numbers = (1, 2)
hello(numbers)  #
# Hello 1 2







class User(NamedTuple):
    firstname: str
    lastname: str


def hello(user: User):
    print(f'Hello {user[0]} {user[1]}')


mark = User('Mark', 'Watney')
hello(mark)
# Hello Mark Watney

mark = User(firstname='Mark', lastname='Watney')
hello(mark)
# Hello Mark Watney




class User(NamedTuple):
    firstname: str
    lastname: str


def hello(user: User):
    print(f'Hello {user.firstname} {user.lastname}')


mark = User('Mark', 'Watney')
hello(mark)
# Hello Mark Watney

mark = User(firstname='Mark', lastname='Watney')
hello(mark)
# Hello Mark Watney



class User(NamedTuple):
    firstname: str
    lastname: str

>>> mark = User(firstname='Mark', lastname='Watney')
>>>
>>>
>>> isinstance(mark, tuple)
True
>>>
>>> mark[0]
'Mark'
>>> mark[1]
'Watney'
>>>
>>> for field in mark:
...     print(field)
...
Mark
Watney




DATA = [
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
    (4.9, 3.0, 1.4, 0.2, 'setosa'),
    (4.9, 2.5, 4.5, 1.7, 'virginica'),
    (7.1, 3.0, 5.9, 2.1, 'virginica'),
    (4.6, 3.4, 1.4, 0.3, 'setosa'),
    (5.4, 3.9, 1.7, 0.4, 'setosa'),
    (5.7, 2.8, 4.5, 1.3, 'versicolor'),
    (5.0, 3.6, 1.4, 0.3, 'setosa'),
    (5.5, 2.3, 4.0, 1.3, 'versicolor'),
    (6.5, 3.0, 5.8, 2.2, 'virginica'),
    (6.5, 2.8, 4.6, 1.5, 'versicolor'),
    (6.3, 3.3, 6.0, 2.5, 'virginica'),
    (6.9, 3.1, 4.9, 1.5, 'versicolor'),
    (4.6, 3.1, 1.5, 0.2, 'setosa'),
]


class Iris(NamedTuple):
    sl: float
    sw: float
    pl: float
    pw: float
    species: str

>>> result = starmap(Iris, DATA[1:])
>>> data = list(result)

>>> data
[Iris(sl=5.8, sw=2.7, pl=5.1, pw=1.9, species='virginica'),
 Iris(sl=5.1, sw=3.5, pl=1.4, pw=0.2, species='setosa'),
 Iris(sl=5.7, sw=2.8, pl=4.1, pw=1.3, species='versicolor'),
 Iris(sl=6.3, sw=2.9, pl=5.6, pw=1.8, species='virginica'),
 Iris(sl=6.4, sw=3.2, pl=4.5, pw=1.5, species='versicolor'),
 Iris(sl=4.7, sw=3.2, pl=1.3, pw=0.2, species='setosa'),
 Iris(sl=7.0, sw=3.2, pl=4.7, pw=1.4, species='versicolor'),
 Iris(sl=7.6, sw=3.0, pl=6.6, pw=2.1, species='virginica'),
 Iris(sl=4.9, sw=3.0, pl=1.4, pw=0.2, species='setosa'),
 Iris(sl=4.9, sw=2.5, pl=4.5, pw=1.7, species='virginica'),
 Iris(sl=7.1, sw=3.0, pl=5.9, pw=2.1, species='virginica'),
 Iris(sl=4.6, sw=3.4, pl=1.4, pw=0.3, species='setosa'),
 Iris(sl=5.4, sw=3.9, pl=1.7, pw=0.4, species='setosa'),
 Iris(sl=5.7, sw=2.8, pl=4.5, pw=1.3, species='versicolor'),
 Iris(sl=5.0, sw=3.6, pl=1.4, pw=0.3, species='setosa'),
 Iris(sl=5.5, sw=2.3, pl=4.0, pw=1.3, species='versicolor'),
 Iris(sl=6.5, sw=3.0, pl=5.8, pw=2.2, species='virginica'),
 Iris(sl=6.5, sw=2.8, pl=4.6, pw=1.5, species='versicolor'),
 Iris(sl=6.3, sw=3.3, pl=6.0, pw=2.5, species='virginica'),
 Iris(sl=6.9, sw=3.1, pl=4.9, pw=1.5, species='versicolor'),
 Iris(sl=4.6, sw=3.1, pl=1.5, pw=0.2, species='setosa')]

>>> data[0]
Iris(sl=5.8, sw=2.7, pl=5.1, pw=1.9, species='virginica')
>>>
>>> data[0].sl
5.8
>>> data[0].species
'virginica'
>>>
>>> print(data[0])
Iris(sl=5.8, sw=2.7, pl=5.1, pw=1.9, species='virginica')
>>>
>>> tuple(data[0])
(5.8, 2.7, 5.1, 1.9, 'virginica')




