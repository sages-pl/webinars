from unittest import TestCase
from random import randint
from unittest.mock import patch


class Dragon:
    def __init__(self, name, /, *, position_x=0, position_y=0):
        if name == '':
            raise TypeError('Name cannot be empty')
        self.name = name
        self.health = randint(50, 100)
        self.position_x = position_x
        self.position_y = position_y


class NameTest(TestCase):
    def test_name_positional(self):
        dragon = Dragon('Name')
        self.assertEqual(dragon.name, 'Name')

    def test_name_keyword(self):
        with self.assertRaises(TypeError):
            Dragon(name='Name')  # noqa

    def test_name_default(self):
        with self.assertRaises(TypeError):
            Dragon()  # noqa

    def test_name_empty(self):
        with self.assertRaises(TypeError):
            Dragon('')


class HealthTest(TestCase):
    def test_health_default_between(self):
        dragon = Dragon('Name')
        self.assertGreaterEqual(dragon.health, 50)
        self.assertLessEqual(dragon.health, 100)

    def test_health_default_bruteforce(self):
        for i in range(10_000):
            dragon = Dragon('Name')
            self.assertGreaterEqual(dragon.health, 50)
            self.assertLessEqual(dragon.health, 100)

    def test_health_default_range(self):
        dragon = Dragon('Name')
        self.assertIn(dragon.health, range(50, 101))

    @patch('main.randint', return_value=74)
    def test_health_default_path(self, randint):
        dragon = Dragon('Name')
        self.assertEqual(dragon.health, 74)


class PositionTest(TestCase):
    def test_position_default(self):
        dragon = Dragon('Name')
        self.assertEqual(dragon.position_x, 0)
        self.assertEqual(dragon.position_y, 0)

    def test_position_positional(self):
        with self.assertRaises(TypeError):
            Dragon('Name', 1, 2)

    def test_position_keyword(self):
        dragon = Dragon('Name', position_x=1, position_y=2)
        self.assertEqual(dragon.position_x, 1)
        self.assertEqual(dragon.position_y, 2)

