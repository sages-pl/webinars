# Zasady S.O.L.I.D. i dobre praktyki programowania obiektowego w Python
from abc import ABCMeta, abstractmethod, ABC, abstractproperty


# SOLID
# SRP - Single Responsibility Principle
# OCP - Open/Close Principle
# LSP - Liskov Substitution Principle
# ISP - Interface Segregation Principle
# DIP - Dependency Inversion Principle

# OOP
# - abstrakcja
# - polimorfizm (structural Polimorfizm, explicit polimorfizm)
# - enkapsulacja
# - dziedziczenie

# Abstrakcja
# - otworzeniu socketu do serwera SMTPs
# - negocjacji certyfikatu TLS
# - rozpoczęciu sesji
# - mimetype encoding wartości, które chcemy przesłać
# - wysłaniu FROM
# - wysłaniu RCPT
# - wysłaniu CC
# - wysłaniu BCC
# - wysłaniu SUBJECT
# - wysłaniu BODY
# - zakończenie sesji
# - zamknięcie socket


class Email:
    def __init__(self, from_, rcpt, cc=None, bcc=None, subject=None, body=None):
        self.from_ = from_
        self.rcpt = rcpt
        self.cc = cc
        self.bcc = bcc
        self.subject = subject
        self.body = body

    def send(self):
        self._socket_open()
        self._tls_cert()
        self._session_start()
        ...


email = Email(from_=..., rcpt=..., subject=..., body=...)
email.send()





class UIElement(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def render(self):
        pass


class Button(UIElement):
    def render(self):
        print(f'Rendering button {self.name}')


class TextInput(UIElement):
    def render(self):
        print(f'Rendering text input {self.name}')



def render(component: list[UIElement]):
    for element in component:
        element.render()


# Jeżeli chodzi jak kaczka
# i kwacze jak kaczka
# to prawdopodobnie jest to kaczka

# Jeżeli ma metodę render
# (i ma atrybut name)
# to prawdopodobnie jest to element


# Component
login_window = [
    TextInput('username'),      # element
    TextInput('password'),      # element
    Button('submit'),           # element
]


render(login_window)

#%% Patterny dziedziczenia

# No inheritance
class Vehicle:
    pass

class Car:
    pass

# Single inheritance
class Vehicle:
    pass

class Car(Vehicle):
    pass


# Muli-level inheritance
class Vehicle:
    pass

class VehicleWithWindows(Vehicle):
    pass

class Car(VehicleWithWindows):
    pass


# Multiple inheritance
class Vehicle:
    pass

class HasWindows:
    pass

class HasRadio:
    pass

class HasEngine:
    pass

class Car(Vehicle, HasEngine, HasRadio, HasWindows):
    pass


# Agregacja
class Engine:
    pass

class Windows:
    pass

class Radio:
    pass


class Car:
    parts = [Engine, Windows, Radio]


# Kompozycja
class Engine:
    def start(self): ...
    def stop(self): ...

class Windows:
    def open(self): ...
    def close(self): ...

class Radio:
    def switch_on(self): ...
    def switch_off(self): ...


class Car:
    engine: Engine
    radio: Radio | None
    windows: Windows | None

    def __init__(self, engine=Engine(), radio=None, windows=Windows()):
        self.engine = engine
        self.radio = radio
        self.windows = windows

    def window_open(self):
        if self.windows:
            return self.windows.open()
        else:
            raise NotImplementedError

    def window_close(self):
        if self.windows:
            return self.windows.close()
        else:
            raise NotImplementedError

    def engine_start(self):
        return self.engine.start()

    def engine_stop(self):
        return self.engine.stop()

    def radio_switchon(self):
        if self.radio:
            return self.radio.switch_on()
        else:
            raise NotImplementedError

    def radio_switchoff(self):
        if self.radio:
            return self.radio.switch_off()
        else:
            raise NotImplementedError



class MyRadio(Radio):
    def switch_on(self):
        print('switching on')

    def switch_off(self):
        print('switching off')



maluch = Car(radio=MyRadio())
maluch.window_open()
maluch.window_close()
maluch.engine_start()
maluch.engine_stop()
maluch.radio_switchon()


data = {'firstname': 'Mark', 'lastname': 'Watney'}





class Vehicle:
    pass

class HasEngine:  # EngineMixin
    def engine_stop(self): ...
    def engine_start(self): ...

class HasPassenger:  # PassengerMixin
    def passenger_load(): ...
    def passenger_unload(): ...

class HasWindows:
    def window_open(self): ...
    def window_close(self): ...



class Car(Vehicle, HasEngine, HasWindows, HasPassenger):
    pass

class Truck(Vehicle, HasEngine, HasWindows):
    pass

class Motorcycle(Vehicle, HasEngine, HasPassenger):
    pass



#%% Enkapsulacja
# - property()
# - refleksja: setattr, getattr, hasattr, delattr
# - deskryptory


# Python way
class Point:
    x: int
    y: int


pt = Point()
pt.x = 1
pt.y = 2
print(pt.x, pt.y)


# Java Way
class Point:
    x: int
    y: int

    def set_x(self, value):
        self.x = value

    def get_x(self):
        return self.x

    def set_y(self, value):
        self.y = value

    def get_y(self):
        return self.y


pt = Point()
pt.set_x(1)
pt.set_y(2)
print(pt.get_x(), pt.get_y())


# True Encapsulation
class Point:
    x: int
    y: int

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return self.x, self.y


pt = Point()
pt.set_coordinates(1, 2)
print(pt.get_coordinates())


##

# Python way
class Point:
    x = property()
    y = property()

    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError
        self._x = value

    @x.getter
    def x(self):
        return self._x

    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError
        self._y = value

    @y.getter
    def y(self):
        return self._y


# Bez modyfikacji kodu użytkownika
pt = Point()
pt.x = 1
pt.y = 2
print(pt.x, pt.y)


# Java Way
class Point:
    x: int
    y: int

    def set_x(self, value):
        if value < 0:
            raise ValueError
        self.x = value

    def get_x(self):
        return self.x

    def set_y(self, value):
        if value < 0:
            raise ValueError
        self.y = value

    def get_y(self):
        return self.y


pt = Point()
pt.set_x(1)
pt.set_y(2)
print(pt.get_x(), pt.get_y())


# True Encapsulation
class Point:
    x: int
    y: int

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return self.x, self.y


pt = Point()
pt.set_coordinates(1, 2)
print(pt.get_coordinates())


#%% SOLID

#%% SRP - Single Responsibility Principle

#%% ISP - Interface Segregation Principle
class Message:
    sender: str
    rcpt: str
    subject: str
    body: str
    attachment: str
    urgency: str
    channel: str


class MyMessage(Message):
    ...

#
class SMS:
    sender: str
    rcpt: str
    body: str

class Email:
    sender: str
    rcpt: str
    subject: str
    body: str
    attachment: str

class Chat:
    body: str
    sender: str
    urgency: str
    channel: str


class MyMessage(SMS):
    ...


#%%
from typing import Protocol, runtime_checkable

# open -> Context Manager
with open('myfile.txt') as file:
    file.read()


# składnia with
with <CONTEXT_MANAGER> as <VAR>:
    <VAR>.<METHOD>()



class ContextManager(Protocol):
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_val, exc_tb): ...

# Protokoły strukturalne
# Protokoły explicit

class MyFile:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        print(f'Reading {self.filename}')

    def __enter__(self):
        print('Opening file')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Closing file')


with MyFile('myfile.txt') as file:
    file.read()



class MyClass:
    def write(self): ...

print('hello', file=MyClass())



@runtime_checkable
class Message(Protocol):
    def send(self, body: str) -> None: ...
    def receive(self) -> str: ...


class Email:
    def send(self, body: int) -> None: ...
    def receive(self) -> str: ...


def send(msg: Message):
    msg.send('hello')


msg: Message = Email()
send(msg)


>>>
... @runtime_checkable
... class Message(Protocol):
    ...     def send(self, body: str) -> None: ...
...     def receive(self) -> str: ...
...
...
... class Email:
    ...     def send(self, body: int) -> None: ...
...
>>>
>>>
>>> isinstance(Email, Message)


#%% DIP - Dependency Inversion Principle


# cache_protocol.py
class Cache(Protocol):
    def set(self, key: str, value: str) -> None: ...
    def get(self, key: str) -> str: ...
    def clear(self) -> None: ...


# cache_impl.py
class DatabaseCache:
    def set(self, key: str, value: str) -> None: ...
    def get(self, key: str) -> str: ...
    def clear(self) -> None: ...

class FilesystemCache:
    def set(self, key: str, value: str) -> None: ...
    def get(self, key: str) -> str: ...
    def clear(self) -> None: ...

class InMemoryCache:
    def set(self, key: str, value: str) -> None: ...
    def get(self, key: str) -> str: ...
    def clear(self) -> None: ...


# settings.py
from cache_protocol import Cache
from cache_impl import DatabaseCache, FilesystemCache, InMemoryCache

default_cache: Cache = InMemoryCache



# myfile.py
from settings import default_cache


mycache: Cache = default_cache()
mycache.set('firstname', 'Mark')
mycache.set('lastname', 'Watney')
mycache.get('firstname')
mycache.get('lastname')
mycache.clear()



# OCP - Open/Close Principle

class Document(ABC):
    filename: str

    @abstractproperty
    def EXTENSIONS(self) -> list[str]: ...

    @abstractmethod
    def display(self):
        raise NotImplementedError

    def __init__(self, filename: str):
        self.filename = filename

    def __new__(cls, filename: str):
        name, extension = filename.split('.')
        plugins = cls.__subclasses__()
        for plugin in plugins:
            if extension in plugin.EXTENSIONS:
                instance = object.__new__(plugin)
                instance.__init__(filename)
                return instance
        else:
            raise NotImplementedError(f'No Plugin for {extension} filetype')


class PDF(Document):
    EXTENSIONS = ['pdf']

    def display(self):
        print('Displaying PDF document')


class Word(Document):
    EXTENSIONS = ['doc', 'docx']

    def display(self):
        print('Displaying Word document')


class PlainText(Document):
    EXTENSIONS = ['txt']

    def display(self):
        print('Displaying Text document')
