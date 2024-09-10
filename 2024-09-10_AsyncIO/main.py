import asyncio


def run():
    return 1

type(run())
# <class 'int'>

#%%

def run():
    yield 1

type(run())
# <class 'generator'>


#%%

async def run():
    return 1

type(run())
# <class 'coroutine'>


#%%

async def run():
    yield 1


type(run())
# <class 'async_generator'>



#%%
from asyncio import sleep
from random import seed, randint
seed(0)

async def db_execute(sql):
    await sleep(randint(0,5))


# async def a():
#     print('a before 1')
#     print('a before 2')
#     print('a before 3')
#     await db_execute('...')
#     print('a after 1')
#     print('a after 2')
#     print('a after 3')
#     await db_execute('...')
#     print('a end 1')
#     print('a end 2')
#     print('a end 3')
#     return 'a'

# async def b():
#     print('b before 1')
#     print('b before 2')
#     print('b before 3')
#     await db_execute('...')
#     print('b after 1')
#     print('b after 2')
#     print('b after 3')
#     await db_execute('...')
#     print('b end 1')
#     print('b end 2')
#     print('b end 3')
#     return 'b'

# async def c():
#     print('c before 1')
#     print('c before 2')
#     print('c before 3')
#     await db_execute('...')
#     print('c after 1')
#     print('c after 2')
#     print('c after 3')
#     await db_execute('...')
#     print('c end 1')
#     print('c end 2')
#     print('c end 3')
#     return 'c'

async def main():
    return await asyncio.gather(a(), b(), c())

result = asyncio.run(main())
