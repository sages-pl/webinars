# new vs init
#


class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname




class User:
    def __init__(self):
        print('init')

>>> mark = User()
init







class User:
    def __new__(cls, *args, **kwargs):
        print('new')

    def __init__(self):
        print('init')

>>> mark = User()
new




>>> class User:
...     def __new__(cls, *args, **kwargs):
...         print('new')
...         instance = object.__new__(cls)
...         return instance
...
...     def __init__(self):
...         print('init')
...
>>>
>>> mark = User()
new
init




>>> class User:
...     def __new__(cls, *args, **kwargs):
...         print('new - before')
...         instance = object.__new__(cls)
...         print('new - after')
...         return instance
...
...     def __init__(self):
...         print('init')
...
>>>
>>> mark = User()
new - before
new - after
init




>>> import logging
... from datetime import datetime
... from uuid import uuid4
...
... class User:
...     def __new__(cls, *args, **kwargs):
...         print('new - before')
...         instance = object.__new__(cls)
...         instance._log = logging.getLogger('myapp.User')
...         instance._since = datetime.now()
...         instance._uuid = str(uuid4().hex)
...         print('new - after')
...         return instance
...
...     def __init__(self):
...         print('init')
...
>>>
>>> mark = User()
new - before
new - after
init


>>> mark._since
datetime.datetime(2023, 4, 14, 11, 8, 31, 135925)
>>> mark._uuid
'e319743ac87442219f62282be2620640'
>>> mark._log
<Logger myapp.User (INFO)>
>>>
>>> vars(mark)
{'_log': <Logger myapp.User (INFO)>,
 '_since': datetime.datetime(2023, 4, 14, 11, 8, 31, 135925),
 '_uuid': 'e319743ac87442219f62282be2620640'}






def new(cls, *args, **kwargs):
    instance = object.__new__(cls)
    instance._log = logging.getLogger(f'myapp.{cls.__name__}')
    instance._since = datetime.now()
    instance._uuid = str(uuid4().hex)
    return instance



class User:
    pass

class Admin:
    pass



>>> class User:
...     pass
...
... class Admin:
...     pass
...
>>>
>>> mark = User()
>>> vars(mark)
{}
>>>
>>> melissa = Admin()
>>> vars(melissa)
{}
>>>
>>>
>>> def new(cls, *args, **kwargs):
...     instance = object.__new__(cls)
...     instance._log = logging.getLogger(f'myapp.{cls.__name__}')
...     instance._since = datetime.now()
...     instance._uuid = str(uuid4().hex)
...     return instance
...
>>>
>>> User.__new__ = new
>>>
>>> mark = User()
>>> vars(mark)
{'_log': <Logger myapp.User (INFO)>,
 '_since': datetime.datetime(2023, 4, 14, 11, 11, 5, 943673),
 '_uuid': 'c00f897cefc84592af2c5d2a5292d061'}


>>> melissa = Admin()
>>> vars(melissa)
{}
>>>
>>> Admin.__new__ = new
>>>
>>> melissa = Admin()
>>> vars(melissa)
{'_log': <Logger myapp.Admin (INFO)>,
 '_since': datetime.datetime(2023, 4, 14, 11, 11, 47, 457042),
 '_uuid': '8b8bf44021e844c49e3e21b2823abdc3'}


>>> mark._log.error('Something wrong')
"2023-04-14", "11:12:54", "ERROR", "Something wrong"




>>> class User:
...     def __new__(cls, *args, **kwargs):
...         print('new - before')
...         instance = int(1)
...         print('new - after')
...         return instance
...
...     def __init__(self):
...         print('init')
...
>>>
>>> mark = User()
new - before
new - after
>>>
>>> mark
1





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

@dataclass
class Setosa:
    sl: float
    sw: float
    pl: float
    pw: float

@dataclass
class Virginica:
    sl: float
    sw: float
    pl: float
    pw: float

@dataclass
class Versicolor:
    sl: float
    sw: float
    pl: float
    pw: float


class Iris:
    def __new__(cls, *args):
        *values, species = args
        match species:
            case 'setosa': cls = Setosa
            case 'virginica': cls = Virginica
            case 'versicolor': cls = Versicolor
        return cls(*values)


result = starmap(Iris, DATA[1:])
data = list(result)

>>> data
[Virginica(sl=5.8, sw=2.7, pl=5.1, pw=1.9),
 Setosa(sl=5.1, sw=3.5, pl=1.4, pw=0.2),
 Versicolor(sl=5.7, sw=2.8, pl=4.1, pw=1.3),
 Virginica(sl=6.3, sw=2.9, pl=5.6, pw=1.8),
 Versicolor(sl=6.4, sw=3.2, pl=4.5, pw=1.5),
 Setosa(sl=4.7, sw=3.2, pl=1.3, pw=0.2),
 Versicolor(sl=7.0, sw=3.2, pl=4.7, pw=1.4),
 Virginica(sl=7.6, sw=3.0, pl=6.6, pw=2.1),
 Setosa(sl=4.9, sw=3.0, pl=1.4, pw=0.2),
 Virginica(sl=4.9, sw=2.5, pl=4.5, pw=1.7),
 Virginica(sl=7.1, sw=3.0, pl=5.9, pw=2.1),
 Setosa(sl=4.6, sw=3.4, pl=1.4, pw=0.3),
 Setosa(sl=5.4, sw=3.9, pl=1.7, pw=0.4),
 Versicolor(sl=5.7, sw=2.8, pl=4.5, pw=1.3),
 Setosa(sl=5.0, sw=3.6, pl=1.4, pw=0.3),
 Versicolor(sl=5.5, sw=2.3, pl=4.0, pw=1.3),
 Virginica(sl=6.5, sw=3.0, pl=5.8, pw=2.2),
 Versicolor(sl=6.5, sw=2.8, pl=4.6, pw=1.5),
 Virginica(sl=6.3, sw=3.3, pl=6.0, pw=2.5),
 Versicolor(sl=6.9, sw=3.1, pl=4.9, pw=1.5),
 Setosa(sl=4.6, sw=3.1, pl=1.5, pw=0.2)]



#%%



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

@dataclass
class Setosa:
    sl: float
    sw: float
    pl: float
    pw: float

@dataclass
class Virginica:
    sl: float
    sw: float
    pl: float
    pw: float

@dataclass
class Versicolor:
    sl: float
    sw: float
    pl: float
    pw: float


class Iris:
    def __new__(cls, *args):
        *values, species = args
        clsname = species.capitalize()
        cls = globals()[clsname]
        return cls(*values)


result = starmap(Iris, DATA[1:])
data = list(result)

>>> data
[Virginica(sl=5.8, sw=2.7, pl=5.1, pw=1.9),
 Setosa(sl=5.1, sw=3.5, pl=1.4, pw=0.2),
 Versicolor(sl=5.7, sw=2.8, pl=4.1, pw=1.3),
 Virginica(sl=6.3, sw=2.9, pl=5.6, pw=1.8),
 Versicolor(sl=6.4, sw=3.2, pl=4.5, pw=1.5),
 Setosa(sl=4.7, sw=3.2, pl=1.3, pw=0.2),
 Versicolor(sl=7.0, sw=3.2, pl=4.7, pw=1.4),
 Virginica(sl=7.6, sw=3.0, pl=6.6, pw=2.1),
 Setosa(sl=4.9, sw=3.0, pl=1.4, pw=0.2),
 Virginica(sl=4.9, sw=2.5, pl=4.5, pw=1.7),
 Virginica(sl=7.1, sw=3.0, pl=5.9, pw=2.1),
 Setosa(sl=4.6, sw=3.4, pl=1.4, pw=0.3),
 Setosa(sl=5.4, sw=3.9, pl=1.7, pw=0.4),
 Versicolor(sl=5.7, sw=2.8, pl=4.5, pw=1.3),
 Setosa(sl=5.0, sw=3.6, pl=1.4, pw=0.3),
 Versicolor(sl=5.5, sw=2.3, pl=4.0, pw=1.3),
 Virginica(sl=6.5, sw=3.0, pl=5.8, pw=2.2),
 Versicolor(sl=6.5, sw=2.8, pl=4.6, pw=1.5),
 Virginica(sl=6.3, sw=3.3, pl=6.0, pw=2.5),
 Versicolor(sl=6.9, sw=3.1, pl=4.9, pw=1.5),
 Setosa(sl=4.6, sw=3.1, pl=1.5, pw=0.2)]

#%%



DATA = """root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
nobody:x:99:99:Nobody:/:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
watney:x:1000:1000:Mark Watney:/home/watney:/bin/bash
lewis:x:1001:1001:Melissa Lewis:/home/lewis:/bin/bash
martinez:x:1002:1002:Rick Martinez:/home/martinez:/bin/bash"""

@dataclass
class SystemAccount:  # uid < 1000
    username: str
    uid: int


@dataclass
class UserAccount:
    username: str
    uid: int


class Record(NamedTuple):
    username: str
    password: str
    uid: int
    gid: int
    gecos: str
    home: str
    shell: str


class Account:
    def __new__(cls, line: str):
        record = Record(*line.strip().split(':'))
        username = record.username
        uid = int(record.uid)
        if uid < 1000:
            return SystemAccount(username, uid)
        else:
            return UserAccount(username, uid)


result = map(Account, DATA.splitlines())
data = list(result)

>>> data
[SystemAccount(username='root', uid=0),
 SystemAccount(username='bin', uid=1),
 SystemAccount(username='daemon', uid=2),
 SystemAccount(username='adm', uid=3),
 SystemAccount(username='shutdown', uid=6),
 SystemAccount(username='halt', uid=7),
 SystemAccount(username='nobody', uid=99),
 SystemAccount(username='sshd', uid=74),
 UserAccount(username='watney', uid=1000),
 UserAccount(username='lewis', uid=1001),
 UserAccount(username='martinez', uid=1002)]
