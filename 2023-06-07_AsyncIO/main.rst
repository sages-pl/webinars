https://github.com/sages-pl/webinars/
https://github.com/sages-pl/webinars/blob/main/2023-06-07_AsyncIO/main.py
https://www.youtube.com/playlist?list=PLhNSoGM2ik6SIkVGXWBwerucXjgP1rHmB


Zwykła funkcja produkuje zwykły obiekt
>>> def run():
...     return 'hello'
...
>>>
>>> type( run() )
<class 'str'>


>>> def run():
...     yield 'hello'
...
>>> type( run() )
<class 'generator'>


>>> async def run():
...     return 'hello'
...
>>> type( run() )
<class 'coroutine'>


>>> async def run():
...     yield 'hello'
...
>>> type( run() )
<class 'async_generator'>



>>> def run():
...     return 1
...
>>>
>>> run()
1

>>> def run():
...     return 1
...     return 2
...
>>>
>>> run()
1

>>> def run():
...     return 1, 2
...
>>> run()
(1, 2)


>>> def run():
...     yield 1
...
>>>
>>> run()
<generator object run at 0x10fdd3740>
>>>
>>> result = run()
>>>
>>> next(result)
1
>>> next(result)
StopIteration

>>> def run():
...     yield 1
...     yield 2
...
>>>
>>> result = run()
>>>
>>> next(result)
1
>>> next(result)
2
>>> next(result)
StopIteration


%%


>>> DATA = [
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
... ]
>>> 
>>> def get_values_for_species(data, species):
...     result = []
...     for *features, label in data:
...         if label == species:
...             result.append(features)            
...     return result

>>> get_values_for_species(DATA, 'setosa')
[[5.1, 3.5, 1.4, 0.2], [4.7, 3.2, 1.3, 0.2]]
>>> 
>>> 
>>> def get_values_for_species(data, species):
...     for *features, label in data:
...         if label == species:
...             yield features
...             
>>> result = get_values_for_species(DATA, 'setosa')
>>> list(result)
[[5.1, 3.5, 1.4, 0.2], [4.7, 3.2, 1.3, 0.2]]
>>> 
>>> result = get_values_for_species(DATA, 'setosa')
>>> 
>>> next(result)
[5.1, 3.5, 1.4, 0.2]
>>> next(result)
[4.7, 3.2, 1.3, 0.2]
>>> next(result)
StopIteration

>>> 
>>> for result in get_values_for_species(DATA, 'setosa'):
...     print(result)
...     
[5.1, 3.5, 1.4, 0.2]
[4.7, 3.2, 1.3, 0.2]
>>> 
>>> 
>>> 
>>> result = get_values_for_species(DATA, 'setosa')
>>> 
>>> next(result)
[5.1, 3.5, 1.4, 0.2]
>>> 
>>> print('hello')
hello
>>> 
>>> def add(a, b):
...     return a + b
...     
>>> add(1,2)
3
>>> 
>>> next(result)
[4.7, 3.2, 1.3, 0.2]


>>> def get_values_for_species(data, species):
...     for *features, label in data:
...         if label == species:
...             yield features
...
>>> get_values_for_species(DATA, 'setosa')
<generator object get_values_for_species at 0x110075460>

#%%



>>> def work(data):
...     print(f'Processing {data=}')
...
>>> work(1)
Processing data=1
>>>
>>> work('one')
Processing data='one'
>>>
>>> work([1,2,3])
Processing data=[1, 2, 3]


>>> def worker():
...     while True:
...         data = yield
...         print(f'Processing {data=}')
...
>>>
>>>
>>> todo = worker()
>>> todo.send(None)
>>>
>>> todo.send(1)
Processing data=1
>>>
>>> todo.send('one')
Processing data='one'
>>>
>>> todo.send([1,2,3])
Processing data=[1, 2, 3]
>>>
>>>
>>> todo.throw(TimeoutError)
TimeoutError
>>>
>>> todo.throw(RuntimeError)
RuntimeError
>>>
>>> todo.close()

#%%

>>> def run():
...     for x in [1,2,3]:
...         yield x
...     for x in [10,20,30]:
...         yield x
...
>>>
>>> result = run()
>>>
>>> next(result)
1
>>> next(result)
2
>>> next(result)
3
>>> next(result)
10
>>> next(result)
20
>>> next(result)
30
>>> next(result)
StopIteration



>>> def worker1():
...     for x in [1,2,3]:
...         yield x
...
>>> def worker2():
...     for x in [10,20,30]:
...         yield x
...
>>>
>>> def run():
...     return worker1()
...
>>>
>>> result = run()
>>>
>>> next(result)
1
>>> next(result)
2
>>> next(result)
3
>>> next(result)
StopIteration


>>> def run():
...     return worker1(), worker2()
...
>>>
>>> result = run()
>>>
>>> next(result)
TypeError: 'tuple' object is not an iterator

>>>
>>> result
(<generator object worker1 at 0x10fdfba00>, <generator object worker2 at 0x10ff9dcc0>)
>>>
>>> next(result[0])
1
>>> next(result[0])
2
>>> next(result[0])
3
>>> next(result[0])
StopIteration

>>>
>>> next(result[1])
10
>>> next(result[1])
20
>>> next(result[1])
30
>>> next(result[1])
StopIteration



>>> def run():
...     yield worker1()
...     yield worker2()
...
>>>
>>> result = run()
>>>
>>> next(result)
<generator object worker1 at 0x10fdfba00>
>>>
>>> result
<generator object run at 0x10fdfbe80>
>>>
>>> x = next(result)
>>> next(x)
10
>>> next(x)
20
>>> next(x)
30
>>>
>>> next(x)
StopIteration


>>> def run():
...     yield from worker1()
...     yield from worker2()
...
>>>
>>> result = run()
>>>
>>> next(result)
1
>>> next(result)
2
>>> next(result)
3
>>> next(result)
10
>>> next(result)
20
>>> next(result)
30
>>> next(result)
StopIteration



>>> def run():
...     return [1, 2, 3]
...
>>> run()
[1, 2, 3]
>>>
>>>
>>> def run():
...     yield [1, 2, 3]
...
>>>
>>> run()
<generator object run at 0x10fdfbe80>
>>>
>>> result = run()
>>> next(result)
[1, 2, 3]
>>>
>>> next(result)
StopIteration

>>>
>>>
>>> def run():
...     yield from [1, 2, 3]
...
>>> run()
<generator object run at 0x10fdfbe80>
>>>
>>> result = run()
>>> next(result)
1
>>> next(result)
2
>>> next(result)
3
>>> next(result)
StopIteration



>>> def run():
...     return 1
...
>>>
>>> type( run() )
<class 'int'>

>>> def run():
...     yield 1
...
>>> type( run() )
<class 'generator'>

>>> async def run():
...     return 1
...
>>> type( run() )
<class 'coroutine'>

>>> async def run():
...     yield 1
...
>>> type( run() )
<class 'async_generator'>





from

>>> from threading import Lock
>>>
>>>
>>> mylock = Lock()
>>>
>>>
>>> mylock.acquire()
True
>>> print('...')
...
>>> print('...')
...
>>> print('...')
...
>>> print('...')
...
>>> mylock.release()


>>> mylock.acquire()
True
>>> try:
...     print('...')
...     print('...')
...     print('...')
...     print('...')
... finally:
...     mylock.release()


>>> with mylock:
...     print('...')
...     print('...')
...     print('...')
...     print('...')




aw
*aws


class MyClass:
    def __await__(self):
        ...

aw = MyClass()
aws = MyClass(), MyClass(), MyClass()



async def run():
    return 1



>>> import asyncio
>>>
>>> async def hello():
...     print('hello')
...
>>>
>>> asyncio.run( hello )
ValueError: a coroutine was expected, got <function hello at 0x1100d9c60>

>>>
>>> asyncio.run( hello() )
hello




>>> async def a():
...     print('a')
...
>>> async def b():
...     print('b')
...
>>>
>>> async def main():
...     await asyncio.gather(
...         a(),
...         b(),
...     )
...
>>>
>>> asyncio.run( main() )
a
b
>>>
>>> asyncio.gather( a(), b() )
<_GatheringFuture pending>
>>>
>>> await asyncio.gather( a(), b() )
a
b
a
b
[None, None]


>>> res = await asyncio.gather( a(), b() )
a
b
>>> res
[None, None]



>>> async def a():
...     return 'a'
...
>>> async def b():
...     return 'b'
...
>>>
>>> asyncio.gather( a(), b() )
<_GatheringFuture pending>
>>>
>>> result = await asyncio.gather( a(), b() )
>>>
>>> result
['a', 'b']



>>> async def run():
...     return 1
...


>>> def run():
...     return await 1
SyntaxError: 'await' outside async function


>>> async def run():
...     return await 1

from time import sleep


def db_execute(SQL):
    sleep(5.0)



def get_user():
    print('a1')
    print('a2')
    print('a3')
    user = db_execute('SELECT * FROM user WHERE id=1')
    print('a4')
    print('a5')
    print('a6')
    orders = db_execute('SELECT * FROM orders WHERE user_id=1')
    print('a7')
    print('a8')
    print('a9')


def get_contact():
    print('b1')
    print('b2')
    print('b3')
    contact = db_execute('SELECT * FROM contacts WHERE lastname="Watney"')
    print('b4')
    print('b5')
    print('b6')
    address = db_execute('SELECT * FROM addresses WHERE lastname="Watney"')
    print('b7')
    print('b8')
    print('b9')





# from time import sleep
from asyncio import sleep

# psycopg
# asyncpg


async def db_execute(SQL):
    await sleep(5.0)


async def get_user():
    print('a1')
    print('a2')
    print('a3')
    user = await db_execute('SELECT * FROM user WHERE id=1')
    print('a4')
    print('a5')
    print('a6')
    orders = await db_execute('SELECT * FROM orders WHERE user_id=1')
    print('a7')
    print('a8')
    print('a9')


async def get_contact():
    print('b1')
    print('b2')
    print('b3')
    contact = await db_execute('SELECT * FROM contacts WHERE lastname="Watney"')
    print('b4')
    print('b5')
    print('b6')
    address = await db_execute('SELECT * FROM addresses WHERE lastname="Watney"')
    print('b7')
    print('b8')
    print('b9')


#%%




class MyClass:
    def __enter__(self):
    def __exit__(self, exc_type, exc_val, exc_tb):


with MyClass():



class MyClass:
    def __aenter__(self):
    def __aexit__(self, exc_type, exc_val, exc_tb):


async with MyClass()



class MyClass:
    def __iter__(self):
    def __next__(self):


for x in MyClass():
    ...


class MyClass:
    def __aiter__(self):
    def __anext__(self):

async for x in MyClass():
    ...



import asyncio
import httpx

DATA = [
     'https://python3.info/_static/iris.csv',
     'https://python3.info/_static/iris-clean.csv',
     'https://python3.info/_static/iris-dirty.csv',
]


async def fetch(url: str) -> httpx.Response:
    async with httpx.AsyncClient() as ac:
        return await ac.get(url)


async def get_data(url: str) -> str:
    resp = await fetch(url)
    return resp.text


async def main():
    todo = [get_data(x) for x in DATA]
    return await asyncio.gather(*todo)

result = asyncio.run(main())
