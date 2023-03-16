# int
# -5 do 256

# float

# IEEE-754
# - 1985

# bool
# and - muszą oba być True
# or - jedno z nich musi być True

# None

imie = 'Mark'
nazwisko = 'Watney'
wiek = None

# str


%history
print('PyDev console: using IPython 8.7.0\n')
import sys
sys.tracebacklimit = 0
sys.path.extend(['/Users/matt/Developer/sages-webinar'])
GROSZ = 1
ZLOTY = 100 * GROSZ
cukierek = 10 * GROSZ
guma = 20 * GROSZ
suma = cukierek + guma
suma / ZLOTY
cukierek
guma
bool()
int()
float()
True
False
False is None
id(False)
id(None)
hex(id(None))
class User:
    pass
mark = User()
mark
id(mark)
hex(id(mark))
login = 'mwatney'
password = 'Ares3'
admin_login = 'mwatney'
admin_password = 'Ares3'
login = input('Podaj login: ')
password = input('Podaj hasło: ')
login == admin_login
password == admin_password
login == admin_login and password == admin_password
False and True
1 & 1
1 & 0
0 & 0
True & True
True & False
True and False
True or False
x = Ture
x = True
y = True
x and y
y = False
x and y
x or y
True + True
type(True)
bool.mro()
def add(a, b):
    if not isinstance(a, int|float):
        raise TypeError('A może być tylko int lub float')
    if not isinstance(b, int|float):
        raise TypeError('B może być tylko int lub float')
    return a + b
add(1, 2)
add(1.0, 2.0)
add('1', '2')
add(1, '2')
add(True, True)
add(True, False)
isinstance(1, int)
isinstance(1, flaot)
isinstance(1, float)
isinstance(1, bool)
isinstance(True, bool)
isinstance(True, float)
isinstance(True, int)
bool.mro()
def add(a, b):
    if type(a) not in (int, float):
        raise TypeError('A może być tylko int lub float')
    if type(b) not in (int, float):
        raise TypeError('B może być tylko int lub float')
    return a + b
add(1, 2)
add(True, True)
True
id(True)
id(True)
id(True)
id(True)
id(True)
type(int)
type(int)
type(int)
id(int)
id(int)
id(int)
id(int)
id(float)
id(float)
id(float)
id(bool)
id(bool)
id(bool)
x = True
x == True
x is True
id(x)
id(True)
x.__eq__(True)
%%timeit -r 1000 -n 1000
x is True
%%timeit -r 1000 -n 1000
x == True
id(1)
id(Ture)
id(True)
x = None
x == None
x is None
x = 1
x == 1
x is 1
x = 256
x == 256
x is 256
x = 257
x == 257
x is 257
x = -5
x == -5
x is -5
x is -6
x = -6
x == -6
x is -6
x = 1
id(x)
x += 2
id(x)
x -= 2
id(x)
id('Mark')
id('Mark')
id('Mark')
id('Mark')
x = 'Mark'
id('Mark')
id('Mark')
id('Mark')
del x
id('Mark')
id('Mark')
id('Mark')
x = 'Mark'
x is 'Mark'
x == 'Mark'
def echo(text: str):
    print(text)
x = echo('hello')
type(x)
type(x).mro()
text = 'a'
text = 'hello'
for letter in text:
    print(letter)
DOMAINS = ('nasa.gov', 'esa.int')
email = 'mwatney@nasa.gov'
WHITELIST = ('nasa.gov', 'esa.int')
email = 'mwatney@nasa.gov'
email[-8:]
email[-8:] in WHITELIST
email = 'mwatney@nasa.gov.pl'
email[-8:] in WHITELIST
WHITELIST[0] in email
WHITELIST[1] in email
email.endswith(WHITELIST)
email = 'mwatney@nasa.gov'
email.endswith(WHITELIST)
line = '1969-07-21T02:56:15.123 [WARNING] First step on the Moon'
line.split()
line.split?
help(line.split)
line = '1969-07-21T02:56:15.123 [WARNING] First step on the Moon'
line.split()
line.split?
line = '1969-07-21T02:56:15.123 [WARNING] First step on the Moon'
line.split(maxsplit=2)
dt, lvl, msg = line.split(maxsplit=2)
dt
lvl
msg
dt.split('T')
from datetime import datetime
datetime.fromisoformat(dt)
dt = datetime.fromisoformat(dt)
lvl
lvl.removeprefix('[')
lvl.removeprefix('[').removesuffix(']')
lvl.replace('[', '')
lvl.replace('[', '').replace(']', '')
lvl.strip('[]')
lvl = lvl.strip('[]')
dt
lvl
msg
msg.upper()
msg
msg.lower9)
msg.lower()
msg.title()
msg.capitalize()
line = '1969-07-21T02:56:15.123 [WARNING] First step on the Moon\n'
line = '1969-07-21T02:56:15.123 [WARNING] First step on the Moon \n'
line
print(line)
line.strip()
line
line[0:10]
line[11:18]
line[11:19]
line[:19]
line[11:]
line[11:30:2]
line[11::2]
line[::2]
line[::-1]
line[::-2]
line[::-3]
name = 'Mark Watney'
print(f'Imię i nazwisko: {name}')
print(f'Imię i nazwisko: {name:.^50}')
print(f'Imię i nazwisko: {name:.<50}')
print(f'Imię i nazwisko: {name:.>50}')
x = '-'
x * 50
def print_title(text):
    print('-' * len(text))
    print(text)
    print('-' * len(text))
print_title('Witaj świecie')
print_title('Witaj świecie jak się masz?')
def print_title(text, witdth=50):
    print('-' * width)
    print(f'{text: ^50}')
    print('-' * width)
print_title('hello world')
def print_title(text, width=50):
    print('-' * width)
    print(f'{text: ^50}')
    print('-' * width)
print_title('hello world')
print_title('hello world', width=20)
def print_title(text, width=50):
    print('-' * width)
    print(f'{text: ^{width}}')
    print('-' * width)
print_title('hello world', width=20)
print_title('hello world', width=50)
def print_title(text, width=50, align='^', fill=' '):
    print('-' * width)
    print(f'{text:{fill}{align}{width}}')
    print('-' * width)
def print_title(text, width=50, align='^', fill=' '):
    print('-' * width)
    print(f'{text:{fill}{align}{width}}')
    print('-' * width)
print_title('hello world', width=50, align='>', fill='.')
print_title('hello world', width=50, align='<', fill='.')
def print_title(text, width=50, align='^', fill=' '):
    print('-' * width)
    print(f'{text: {align}{width}}')
    print('-' * width)
print_title('hello world', width=50, align='<', fill='.')
print_title('hello world', width=50, align='>', fill='.')
print_title('hello world', width=50, align='^', fill='.')
f'Hello {name}'
b'Hello World'
f'Hello {name}'
b'Hello World'
u'Hello World'
r'Hello World'
'Hello {name}'
text = 'hello'
text = b'hello'
text
text = b'cześć'
ord('A')
ord('B')
ord('a')
chr(98)
2 ** 7
2 ** 8
text = 'cześć'
text
text = u'cześć'
text = 'cześć'
text.encode('iso-8859-02')
text.encode('iso-8859-2')
text = 'cześć'
text.encode('iso-8859-2')
text.encode('windows-1250')
text.encode('cp1250')
text.encode('utf-8')
text.encode('utf-16')
text.encode('utf-32')
2 ** 32
print('\U0001F606')
print('\U0001F610')
from urllib.request import urlopen
result = urlopen('https://python.astrotech.io')
html = result.read()
html
type(html)
html.decode('utf-8')
html = html.decode('utf-8')
html
path = '/home/mwatney/myfile.txt'
path = '/Users/mwatney/myfile.txt'
path = 'C:\Usersmwatney/myfile.txt'
path = 'C:\Users\mwatney\myfile.txt'
path = 'C:\\Users\\mwatney\\myfile.txt'
'\U0001F680'
import string
string.hexdigits
path = 'c:/Users/mwatney/myfile.txt'
path = 'C:\Users\mwatney\myfile.txt'
path = r'C:\Users\mwatney\myfile.txt'
path
path = r'C:\Users\mwatney\myfile.txt'
print('hello world')
print('hello\tworld')
print('hello\nworld')
print('hello\\nworld')
print(r'hello\nworld')
path = r'C:\Users\mwatney\myfile.txt'
path = 'C:\\Users\mwatney\myfile.txt'
path = 'C:\\Users\urszula\myfile.txt'
path = r'C:\\Users\urszula\myfile.txt'
text = u'cześć'
text = b'hello'
text = f'hello {name}'
text
text = r'hello {name}'
text
text = r'hello \n {name}'
text
%history