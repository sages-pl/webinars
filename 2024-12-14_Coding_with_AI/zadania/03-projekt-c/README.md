# Dragon
* https://python3.info/dragon/polish/about.html

## Setup

```pycon
>>> from main import Dragon

```

## Tworzenie smoka

* Smok przy tworzeniu ma nazwę
* Smok przy tworzeniu podnosi błąd jeżeli nie ma nazwy

Stwórz smoka o nazwie "Wawelski":

```pycon
>>> dragon = Dragon('Wawelski')

```

Stworzenie smoka bez nazwy podnosi błąd:

```pycon
>>> dragon = Dragon()
Traceback (most recent call last):
TypeError: Dragon.__init__() missing 1 required positional argument: 'name'

>>> dragon = Dragon('')
Traceback (most recent call last):
TypeError: Name cannot be empty

```
