# int
# float

# IEEE-754
# - 1985

# bool
# and - muszą oba być True
# or - jedno z nich musi być True


# None
# str



def add(a, b):
    if type(a) not in (int, float):
        raise TypeError('A może być tylko int lub float')

    if type(b) not in (int, float):
        raise TypeError('B może być tylko int lub float')

    return a + b

add(1, 2)        # 3
add(1.0, 2.0)    # 3.0
add(True, True)  # 2