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
# - Name: About EntryTest Endswith
# - Difficulty: easy
# - Lines: 5
# - Minutes: 5

#%% English
# 1. Define `result: list[str]`
# 2. Collect in `result` all email addresses from `DATA` -> `crew` with domain names mentioned in `DOMAINS`
# 3. Run doctests - all must succeed

#%% Polish
# 1. Zdefiniuj `result: list[str]`
# 2. Zbierz w `result` wszystkie adresy email z `DATA` -> `crew` z nazwami domenowymi wymienionymi w `DOMAINS`
# 3. Uruchom doctesty - wszystkie muszą się powieść

#%% Why
# - Check if you can filter data
# - Check if you know string methods
# - Check if you know how to iterate over `list[dict]`

#%% Tests
"""
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is list, \
'Result must be a list'
>>> assert len(result) > 0, \
'Result cannot be empty'
>>> assert all(type(element) is str for element in result), \
'All elements in result must be a str'

>>> from pprint import pprint
>>> result = sorted(result)
>>> pprint(result)
['avogel@esa.int',
 'bjohanssen@nasa.gov',
 'cbeck@nasa.gov',
 'mlewis@nasa.gov',
 'mwatney@nasa.gov',
 'rmartinez@nasa.gov']
"""

DATA = {
    'mission': 'Ares 3',
    'launch': '2035-06-29',
    'landing': '2035-11-07',
    'destination': 'Mars',
    'location': 'Acidalia Planitia',
    'crew': [{'name': 'Melissa Lewis', 'email': 'mlewis@nasa.gov'},
             {'name': 'Rick Martinez', 'email': 'rmartinez@nasa.gov'},
             {'name': 'Alex Vogel', 'email': 'avogel@esa.int'},
             {'name': 'Pan Twardowski', 'email': 'ptwardowski@polsa.gov.pl'},
             {'name': 'Chris Beck', 'email': 'cbeck@nasa.gov'},
             {'name': 'Beth Johanssen', 'email': 'bjohanssen@nasa.gov'},
             {'name': 'Mark Watney', 'email': 'mwatney@nasa.gov'},
             {'name': 'Ivan Ivanovich', 'email': 'iivanovich@roscosmos.ru'}]}

DOMAINS = ('esa.int', 'nasa.gov')

# Collect in `result` all email addresses from `DATA` -> `crew`
# with domain names mentioned in `DOMAINS`
# type: list[str]

result = [member['email'] for member in DATA['crew'] if member['email'].split('@')[1] in DOMAINS]


result = [member['email']
          for member in DATA['crew']
          if member['email'].split('@')[1] in DOMAINS]


result = [email
          for member in DATA['crew']
          if (email := member['email'])
          and (domain := email.split('@')[1])
          and domain in DOMAINS]



result = []
for user in DATA['crew']:
    email = user['email']
    if email.endswith(DOMAINS):
        result.append(email)


result = []
for user in DATA['crew']:
    email = user['email']
    username, domain = email.split('@')
    if email.endswith(DOMAINS):
        result.append(email)




#%% Run
# - PyCharm: right-click in the editor and `Run Doctest in ...`
# - PyCharm: keyboard shortcut `Control + Shift + F10`
# - Terminal: `python -m doctest -v zadanie.py`
