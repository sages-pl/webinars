#%% License
# - Copyright 2024, Matt Harasymczuk <matt@python3.info>
# - This code can be used only for learning by humans
# - This code cannot be used for teaching others
# - This code cannot be used for teaching LLMs and AI algorithms
# - This code cannot be used in commercial or proprietary products
# - This code cannot be distributed in any form
# - This code cannot be changed in any form outside of training course
# - This code cannot have its license changed
# - If you use this code in your product, you must open-source it under GPLv2
# - Exception can be granted only by the author

#%% About
# - Name: About EntryTest ListDict
# - Difficulty: hard
# - Lines: 15
# - Minutes: 13

#%% English
# 1. Define `result: list[dict]`, where each dict has keys:
#    - ip: str
#    - hosts: list[str]
# 2. Iterate over lines in `DATA` skipping comments (`#`) and empty lines
# 3. Extract from each line: `ip` and `hosts`
# 4. Add `ip` and `hosts` to `result` as a dict, example:
#    {'ip': '10.13.37.1', 'hosts': ['nasa.gov', 'esa.int']}
# 5. Each line must be a separate dict
# 6. Mind, that for 127.0.0.1 there will be two separate entries
# 7. Run doctests - all must succeed

#%% Polish
# 1. Zdefiniuj `result: list[dict]`, gdzie każdy dict ma klucze:
#    - ip: str
#    - hosts: list[str]
# 2. Iteruj po liniach w `DATA` pomijając komentarze (`#`) i puste linie
# 3. Wyciągnij z każdej linii: `ip` i `hosts`
# 4. Dodaj `ip` i `hosts` do `result` jako słownik, przykład:
#    {'ip': '10.13.37.1', 'hosts': ['nasa.gov', 'esa.int']}
# 5. Każda linia ma być osobnym słownikiem
# 6. Zwróć uwagę, że dla 127.0.0.1 będą dwa osobne wiersze
# 7. Uruchom doctesty - wszystkie muszą się powieść

#%% Why
# - Check if you know how to parse files
# - Check if you can filter strings
# - Check if you know string methods
# - Check if you know how to iterate over `list[dict]`

#%% Tests
"""
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> result = list(result)
>>> assert len(result) > 0, \
'Result cannot be empty'
>>> assert type(result) is list, \
'Variable `result` has invalid type, should be list'
>>> assert all(type(x) is dict for x in result), \
'All keys in `result` should be dict'

>>> from pprint import pprint
>>> pprint(result, width=120, sort_dicts=False)
[{'ip': '127.0.0.1', 'hosts': ['localhost']},
 {'ip': '127.0.0.1', 'hosts': ['astromatt']},
 {'ip': '10.13.37.1', 'hosts': ['nasa.gov', 'esa.int']},
 {'ip': '255.255.255.255', 'hosts': ['broadcasthost']},
 {'ip': '::1', 'hosts': ['localhost']}]
"""

DATA = """##
# `/etc/hosts` structure:
#    - ip: internet protocol address (IPv4 or IPv6)
#    - hosts: host names
 ##

127.0.0.1       localhost
127.0.0.1       astromatt
10.13.37.1      nasa.gov esa.int
255.255.255.255 broadcasthost
::1             localhost"""

# Skip comments (`#`) and empty lines
# Extract from each line: `ip` and `hosts`
# Add `ip` and `hosts` to `result` as a dict, example:
# {'ip': '10.13.37.1', 'hosts': ['nasa.gov', 'esa.int']}
# Each line must be a separate dict
# Mind, that for 127.0.0.1 there will be two separate entries
# type: list[dict]
result = ...


#%% Run
# - PyCharm: right-click in the editor and `Run Doctest in ...`
# - PyCharm: keyboard shortcut `Control + Shift + F10`
# - Terminal: `python -m doctest -v zadanie.py`
