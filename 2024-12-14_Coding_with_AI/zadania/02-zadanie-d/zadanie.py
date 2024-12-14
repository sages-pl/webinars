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

result = []
for line in DATA.splitlines():
    line = line.strip()

    if not line or line.startswith('#'):
        continue

    records = line.split()
    ip = records[0]
    hosts = records[1:]
    result.append({'ip': ip, 'hosts': hosts})


result = []
for line in DATA.splitlines():
    line = line.strip()

    if len(line) == 0:
        continue
    if line.isspace():
        continue
    if line.startswith('#'):
        continue

    ip, *hosts = line.split()
    result.append({'ip': ip, 'hosts': hosts})



result = []
for line in DATA.splitlines():
    if line and not (line[0] == '#' or line[1] == '#'):
        ip, *hosts = line.split()
        result.append({'ip': ip, 'hosts': hosts})




def valid_line(line):
    return line and not (line[0] == '#' or line[1] == '#')


result = []
for line in DATA.splitlines():
    if valid_line(line):
        ip, *hosts = line.split()
        result.append({'ip': ip, 'hosts': hosts})




def valid_line_empty_string():
    assert not valid_line("")

def valid_line_comment():
    assert not valid_line("# This is a comment")

def valid_line_whitespace():
    assert not valid_line("   ")

def valid_line_valid_ip():
    assert valid_line("127.0.0.1 localhost")

def valid_line_valid_ipv6():
    assert valid_line("::1 localhost")

def valid_line_invalid_ip():
    assert not valid_line("999.999.999.999 invalidhost")

def valid_line_mixed_content():
    assert valid_line("10.13.37.1 nasa.gov esa.int")


# złożoność obliczeniowa
# - ile kroków ma algorytm
# - tracimy na: for, while, nested loop

# złożoność pamięciowa
# - ile ramu potrzebuje nasz algorytm
# - tracimy na: =, :=, .copy()

# złożoność cyklomatyczna
# - na ile gałęzi rozwidla się nasz kod
# - tracimy na: if, elif, else, match, case

# złożoność kognitywna
# - jak trudno jest zrozumieć kod
# - tracimy na: not, and, or, xor, &, |, ~, ^, <<, >>, <<=, >>=, &=, |=, ~=, ^=, @, @=, %, %=

def status(age: int):
    if age < 18:
        return 'junior'
    elif age < 30:
        return 'young'
    elif age < 65:
        return 'adult'
    else:
        return 'senior'


def test_a():
    assert status(10) == 'junior'

def test_b():
    assert status(80) == 'senior'

def test_c():
    assert status(40) == 'adult'

def test_d():
    assert status(20) == 'young'


status(18)
status(30)
status(65)

status(-1)
status(0)
status(133)
status(999)



#%% Run
# - PyCharm: right-click in the editor and `Run Doctest in ...`
# - PyCharm: keyboard shortcut `Control + Shift + F10`
# - Terminal: `python -m doctest -v zadanie.py`
