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
# - Name: About EntryTest ToListDict
# - Difficulty: easy
# - Lines: 2
# - Minutes: 5

#%% English
# 1. Define `result: list[dict]`:
# 2. Convert `DATA` from `list[tuple]` to `list[dict]`
#    - key - name from the header
#    - value - numerical value or species name
# 3. Run doctests - all must succeed

#%% Polish
# 1. Zdefiniuj `result: list[dict]`:
# 2. Przekonwertuj `DATA` z `list[tuple]` do `list[dict]`
#    - klucz - nazwa z nagłówka
#    - wartość - wartość numeryczna lub nazwa gatunku
# 3. Uruchom doctesty - wszystkie muszą się powieść

#%% Why
# - Convert data from `list[tuple]` to `list[dict]`
# - `list[tuple]` is used to represent CSV data
# - `list[tuple]` is used to represent database rows
# - `list[dict]` is used to represent JSON data
# - CSV is the most popular format in data science

#%% Tests
"""
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> result = list(result)
>>> assert type(result) is list, \
'Result must be a list'
>>> assert len(result) > 0, \
'Result cannot be empty'
>>> assert all(type(element) is dict for element in result), \
'All elements in result must be a dict'

>>> from pprint import pprint
>>> pprint(result, sort_dicts=False)
[{'sepal_length': 5.8,
  'sepal_width': 2.7,
  'petal_length': 5.1,
  'petal_width': 1.9,
  'species': 'virginica'},
 {'sepal_length': 5.1,
  'sepal_width': 3.5,
  'petal_length': 1.4,
  'petal_width': 0.2,
  'species': 'setosa'},
 {'sepal_length': 5.7,
  'sepal_width': 2.8,
  'petal_length': 4.1,
  'petal_width': 1.3,
  'species': 'versicolor'},
 {'sepal_length': 6.3,
  'sepal_width': 2.9,
  'petal_length': 5.6,
  'petal_width': 1.8,
  'species': 'virginica'},
 {'sepal_length': 6.4,
  'sepal_width': 3.2,
  'petal_length': 4.5,
  'petal_width': 1.5,
  'species': 'versicolor'},
 {'sepal_length': 4.7,
  'sepal_width': 3.2,
  'petal_length': 1.3,
  'petal_width': 0.2,
  'species': 'setosa'}]
"""

DATA = [
    ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]


# Convert `DATA` from `list[tuple]` to `list[dict]`
# - key - name from the header
# - value - numerical value or species name
# type: list[dict[str,float|str]]
result = ...


#%% Run
# - PyCharm: right-click in the editor and `Run Doctest in ...`
# - PyCharm: keyboard shortcut `Control + Shift + F10`
# - Terminal: `python -m doctest -v zadanie.py`

