from unittest import TestCase
from game.dragon import Dragon
from game.status import Status


class InitTest(TestCase):
    def setUp(self) -> None:
        self.dragon = Dragon('Wawelski', position_x=10, position_y=20)

    def test_init_name_positional(self):
        dragon = Dragon('Wawelski')
        self.assertEqual(dragon.name, 'Wawelski')

    def test_init_name_keyword(self):
        with self.assertRaises(TypeError):
            Dragon(name='Wawelski')  # noqa

    def test_init_position_default(self):
        dragon = Dragon('Wawelski')
        self.assertEqual(dragon._position.x, 0)
        self.assertEqual(dragon._position.y, 0)

    def test_init_position_keyword(self):
        dragon = Dragon('Wawelski', position_x=1, position_y=2)
        self.assertEqual(dragon._position.x, 1)
        self.assertEqual(dragon._position.y, 2)

    def test_init_position_positional(self):
        with self.assertRaises(TypeError):
            Dragon('Wawelski', 1, position_y=2)  # noqa
        with self.assertRaises(TypeError):
            Dragon('Wawelski', 1, 2)  # noqa

    def test_init_health(self):
        self.assertIn(self.dragon.health, range(50, 101))

    def test_init_texture(self):
        self.assertEqual(self.dragon.texture, 'img/dragon/alive.png')

    def test_init_status(self):
        self.assertEqual(self.dragon.status, Status.ALIVE)


class DamageTest(TestCase):
    def setUp(self) -> None:
        self.dragon = Dragon('Wawelski', position_x=10, position_y=20)

    def test_damage_make(self):
        dmg = self.dragon.make_damage()  # noqa
        self.assertIn(dmg, range(5, 21))

    def test_damage_take_keyword(self):
        with self.assertRaises(TypeError):
            self.dragon.take_damage(damage=1)  # noqa

    def test_damage_take_health_positive(self):
        self.dragon.health = 3
        self.dragon.take_damage(2)
        self.assertEqual(self.dragon.health, 1)

    def test_damage_take_health_zero(self):
        self.dragon.health = 2
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.take_damage(2)

    def test_damage_take_health_negative(self):
        self.dragon.health = 1
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.take_damage(2)


class StatusTest(TestCase):
    def setUp(self) -> None:
        self.dragon = Dragon('Wawelski', position_x=10, position_y=20)

    def test_status_health_positive(self):
        self.dragon.health = 1
        self.assertEqual(self.dragon.status, Status.ALIVE)

    def test_status_health_zero(self):
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.health = 0
        self.assertEqual(self.dragon.status, Status.DEAD)

    def test_status_health_negative(self):
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.health = -1
        self.assertEqual(self.dragon.status, Status.DEAD)


class TextureTest(TestCase):
    def setUp(self) -> None:
        self.dragon = Dragon('Wawelski', position_x=10, position_y=20)

    def test_texture_health_positive(self):
        self.dragon.health = 1
        self.assertEqual(self.dragon.texture, 'img/dragon/alive.png')

    def test_texture_health_zero(self):
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.health = 0
        self.assertEqual(self.dragon.texture, 'img/dragon/dead.png')

    def test_texture_health_negative(self):
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.health = -1
        self.assertEqual(self.dragon.texture, 'img/dragon/dead.png')


class HealthTest(TestCase):
    def setUp(self) -> None:
        self.dragon = Dragon('Wawelski', position_x=10, position_y=20)

    def test_health_isalive_positive(self):
        self.dragon.health = 1
        self.assertTrue(self.dragon.is_alive())

    def test_health_isalive_zero(self):
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.health = 0
        self.assertFalse(self.dragon.is_alive())

    def test_health_isalive_negative(self):
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.health = -1
        self.assertFalse(self.dragon.is_alive())

    def test_health_isdead_positive(self):
        self.dragon.health = 1
        self.assertFalse(self.dragon.is_dead())

    def test_health_isdead_zero(self):
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.health = 0
        self.assertTrue(self.dragon.is_dead())

    def test_health_isdead_negative(self):
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.health = -1
        self.assertTrue(self.dragon.is_dead())
