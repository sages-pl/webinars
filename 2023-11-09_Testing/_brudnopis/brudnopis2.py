"""
Moduł z sumowaniem dwóch liczb
"""

def add(a: int, b: int) -> int:
    """
    Funkcja sumuje dwie liczby

    :param a: [int] liczba a
    :param b: [int] liczba b
    :return: [int] suma dwóch liczb
    """
    return a + b


add(1, 2)
add('1', '2')



def status(wiek: int) -> str:
    """
    >>> status(-5) # ???
    >>> status(150) # ???
    >>> status(18) # ???

    >>> status(10)
    'junior'

    >>> status(25)
    'młody dorosły'

    >>> status(40)
    'dorosły'

    >>> status(70)
    'senior'
    """
    if wiek < 18:
        return 'junior'
    elif wiek < 30:
        return 'młody dorosły'
    elif wiek < 65:
        return 'dorosły'
    else:
        return 'senior'
