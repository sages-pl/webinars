from game.dragon import Dragon


dragon = Dragon('Wawelski', position_x=50, position_y=120)
dragon.position_set(x=10, y=20)
dragon.position_change(left=10, down=20)
dragon.position_change(left=10, right=15)
dragon.position_change(right=15, up=5)
dragon.position_change(down=5)
dmg = dragon.make_damage()

try:
    dragon.take_damage(10)
    dragon.take_damage(5)
    dragon.take_damage(3)
    dragon.take_damage(2)
    dragon.take_damage(15)
    dragon.take_damage(25)
    dragon.take_damage(75)
except dragon.IsDead:
    drop = dragon.get_drop()
    print(f'{dragon.name} is dead')
    print(f'Gold: {drop.gold}')
    print(f'Position: {drop.position}')
