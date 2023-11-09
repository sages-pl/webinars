"""
Docstring do modułu

https://podcasts.apple.com/us/podcast/core-py/id1712665877
https://open.spotify.com/episode/6K9BLLnjuYQZAeejeseY3c

https://python3.info
"""

name = 'Mark Watney'
"""
Imię naszego bohatera
"""

def add(a, b):
    """
    Docstring do funkcji

    >>> add(1, 2)
    3

    >>> add(1.0, 2.0)
    3.0

    >>> add('a', 'b')  # doctest: +SKIP
    'ab'

    >>> add(0.1, 0.2)
    0.30000000000000004

    >>> add(0.1, 0.2)  # doctest: +ELLIPSIS
    0.3000...

    >>> data = {'a', 'b', 'c'}
    >>> isinstance(data, set)
    True
    >>> sorted(data)
    ['a', 'b', 'c']

    >>> data = {'a', 'b', 'c'}
    >>> assert isinstance(data, set)
    >>> assert 'a' in data
    >>> assert 'b' in data
    >>> assert 'c' in data

    >>> data = {
    ...     'firstname': 'Mark',
    ...     'lastname': 'Watney',
    ... }
    >>> data  # doctest: +NORMALIZE_WHITESPACE
    {'firstname': 'Mark',
     'lastname': 'Watney'}

    >>> from pprint import pprint

    >>> data = {
    ...     'firstname': 'Mark',
    ...     'lastname': 'Watney',
    ... }
    >>> pprint(data, width=30, sort_dicts=False)
    {'firstname': 'Mark',
     'lastname': 'Watney'}

    >>> add("It is ", "Monty Python")
    'It is Monty Python'

    >>> add("It's ", "Monty Python")
    "It's Monty Python"
    """
    return a + b


class User:
    """
    Docstring do funkcji
    """

    def login(self):
        """
        Docstring do metody
        """
