# Dragon
* https://python3.info/dragon/polish/about.html

## Setup

```pycon
>>> from random import seed; seed(0)
>>> from main import Dragon

```

## Nazwa smoka

* Smok przy tworzeniu ma nazwę
* Smok przy tworzeniu podnosi błąd jeżeli nie ma nazwy

Stwórz smoka o nazwie "Wawelski":

```pycon
>>> dragon = Dragon('Wawelski')

```

Stworzenie smoka bez nazwy podnosi błąd:

```pycon
>>> Dragon()
Traceback (most recent call last):
TypeError: Dragon.__init__() missing 1 required positional argument: 'name'

>>> Dragon('')
Traceback (most recent call last):
TypeError: Name cannot be empty

```

## Punkty życia

* Smok przy tworzeniu ma losowe punkty życia z zakresu 50 do 100


Smok przy tworzeniu ma losowe punkty życia:

```pycon
>>> dragon.health
74

```


## Pozycja

* Smok przy tworzeniu zajmuje domyślną pozycję x=0 y=0
* Smok przy tworzeniu może mieć ustawioną dowolną pozycję

Uwaga: Górny lewy róg ekranu to punkt x=0 y=0

Ustaw inicjalną pozycję smoka na x=50, y=100

```pycon
>>> dragon = Dragon('Wawelski', position_x=50, position_y=100)

```
