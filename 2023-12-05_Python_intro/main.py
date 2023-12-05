from base64 import b64encode, b64decode
from hashlib import sha512


b64encode(b'hello')
# b'aGVsbG8='

b64decode(b'aGVsbG8=')
# b'hello'

sha512(b'hello').hexdigest()
# '9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72323c3d99ba5c11d7c7acc6e14b8c5da0c4663475c2e5c3adef46f73bcdec043'


sha512(b'hello@facebook.com').hexdigest()

# rainbow tables
# solenie haseł
# komputery kwantowe

# passkey
# regresja liniowa



# przypisanie
# porównanie
# powtarzanie


a = 1

if a > 1:
    ...

while a != 1:
    ...



2 - 1
# 1

2 + (-1)
# 1

2 * 3
# 6

2 + 2 + 2
# 6

# +


data = 1
data = 1.5
data = True
data = False
data = None
data = 'hello'
data = [1, 2.5, True, None, 'hello']
data = (1, 2.5, True, None, 'hello')
data = {1, 2.5, True, None, 'hello'}
data = {
    'firstname': 'Mark',
    'lastname': 'Watney',
    'birthday': '1969-07-21',
}
for key in data.keys():
    ...
for values in data.values():
    ...
for key, value in data.items():
    ...
def add(a,b):
    return a + b
add(1,2)
3
add(a=1, b=2)
3
if 'firstname' in data:
    print('jest')
else:
    print('brak')

jest
class User:
    firstname: str
    lastname: str

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def say_hello(self):
        return 'hello'

mark = User('Mark', 'Watney')
melissa = User('Melissa', 'Lewis')
vars(mark)
{'firstname': 'Mark', 'lastname': 'Watney'}
vars(melissa)
{'firstname': 'Melissa', 'lastname': 'Lewis'}
mark.say_hello()
'hello'
