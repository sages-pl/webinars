from unittest import TestCase
from random import randint
from unittest.mock import patch


class Dragon:
    def __init__(self, name, /):
        if name == '':
            raise TypeError('Name cannot be empty')
        self.name = name
        self.health = randint(50, 100)


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
