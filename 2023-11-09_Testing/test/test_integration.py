"""
>>> from random import seed; seed(0)
>>> import sys; sys.tracebacklimit = 0
>>> from game.dragon import Dragon

Stwórz smoka w pozycji x=50, y=120 i nazwij go "Wawelski"
>>> dragon = Dragon('Wawelski', position_x=50, position_y=120)

Ustaw nową pozycję na x=10, y=20
>>> dragon.position_set(x=10, y=20)

Przesuń smoka w lewo o 10 i w dół o 20
>>> dragon.position_change(left=10, down=20)

Przesuń smoka w lewo o 10 i w prawo o 15
>>> dragon.position_change(left=10, right=15)

Przesuń smoka w prawo o 15 i w górę o 5
>>> dragon.position_change(right=15, up=5)

Przesuń smoka w dół o 5
>>> dragon.position_change(down=5)

Smok zadaje obrażenia
>>> dmg = dragon.make_damage()

>>> try:
...     dragon.take_damage(10)  # Zadaj 10 obrażeń smokowi
...     dragon.take_damage(5)  # Zadaj 5 obrażeń smokowi
...     dragon.take_damage(3)  # Zadaj 3 obrażeń smokowi
...     dragon.take_damage(2)  # Zadaj 2 obrażeń smokowi
...     dragon.take_damage(15)  # Zadaj 15 obrażeń smokowi
...     dragon.take_damage(25)  # Zadaj 25 obrażeń smokowi
...     dragon.take_damage(75)  # Zadaj 75 obrażeń smokowi
... except dragon.IsDead:
...     drop = dragon.get_drop()
...     print(f'{dragon.name} is dead')
...     print(f'Gold: {drop.gold}')
...     print(f'Position: {drop.position}')
Wawelski is dead
Gold: 98
Position: (20, 40)

Smok powinien zginąć na pozycji: x=20, y=40
"""
